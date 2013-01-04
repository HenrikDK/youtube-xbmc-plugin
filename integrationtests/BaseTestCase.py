import sys
import os
import time
import unittest2
import MockYouTubeDepends
from mock import Mock
MockYouTubeDepends.MockYouTubeDepends().mockXBMC()

sys.path.append('../plugin/')
sys.path.append('../xbmc-mocks/')

if not os.path.exists("tmp"):
    os.mkdir("tmp")
else:
    for old_file in os.listdir("tmp"):
        os.remove("./tmp/" + old_file)


class BaseTestCase(unittest2.TestCase):  #pragma: no cover
    def setUp(self):
        time.sleep(5)
        MockYouTubeDepends.MockYouTubeDepends().mock()
        MockYouTubeDepends.MockYouTubeDepends().mockXBMC()
        self.intializePlugin()

    def intializePlugin(self):
        import cookielib
        import urllib2
        sys.modules["__main__"].cookiejar = cookielib.LWPCookieJar()
        sys.modules["__main__"].opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(sys.modules["__main__"].cookiejar))
        urllib2.install_opener(sys.modules["__main__"].opener)

        sys.argv = ["something", -1, "something_else"]
        import CommonFunctions
        reload(CommonFunctions)
        sys.modules["__main__"].common = CommonFunctions
        sys.modules["__main__"].common.log = sys.modules["__main__"].xbmc.log
        sys.modules["__main__"].settingsDL.load_strings("./resources/settings.xml")
        sys.modules["__main__"].xbmcaddon.Addon.return_value = sys.modules["__main__"].settingsDL
        sys.modules["__main__"].xbmcvfs.exists.return_value = True

        import SimpleDownloader
        sys.modules["__main__"].downloader = SimpleDownloader.SimpleDownloader()
        sys.modules["__main__"].xbmcvfs.exists.return_value = False
        import YouTubePluginSettings
        sys.modules["__main__"].pluginsettings = YouTubePluginSettings.YouTubePluginSettings()
        import YouTubeUtils
        sys.modules["__main__"].utils = YouTubeUtils.YouTubeUtils()
        import YouTubeStorage
        sys.modules["__main__"].storage = YouTubeStorage.YouTubeStorage()
        import YouTubeCore
        sys.modules["__main__"].core = YouTubeCore.YouTubeCore()
        sys.modules["__main__"].core.getVideoIdStatusFromCache = Mock()
        sys.modules["__main__"].core.getVideoIdStatusFromCache.return_value = []
        import YouTubeLogin
        sys.modules["__main__"].login = YouTubeLogin.YouTubeLogin()
        import YouTubeFeeds
        sys.modules["__main__"].feeds = YouTubeFeeds.YouTubeFeeds()
        import YouTubeSubtitleControl
        sys.modules["__main__"].subtitles = YouTubeSubtitleControl.YouTubeSubtitleControl()
        import YouTubePlayer
        sys.modules["__main__"].player = YouTubePlayer.YouTubePlayer()
        import YouTubeScraper
        sys.modules["__main__"].scraper = YouTubeScraper.YouTubeScraper()
        import YouTubePlaylistControl
        sys.modules["__main__"].playlist = YouTubePlaylistControl.YouTubePlaylistControl()
        import YouTubeNavigation
        self.navigation = YouTubeNavigation.YouTubeNavigation()

    def reset_xbmc_mocks(self):
        sys.modules["__main__"].xbmcplugin.addDirectoryItem.reset_mock()
        sys.modules["__main__"].xbmcplugin.reset_mock()
        sys.modules["__main__"].xbmc.PlayList().add.reset_mock()
        sys.modules["__main__"].xbmc.PlayList().reset_mock()
        sys.modules["__main__"].xbmc.reset_mock()
        sys.modules["__main__"].xbmcgui.ListItem.reset_mock()
        sys.modules["__main__"].xbmcgui.reset_mock()

    def assert_directory_count_greater_than_or_equals(self, count):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list

        if len(args) < count:
            print "Directory list length %s is not greater than or equal to expected list lengt %s" % (repr(len(args)), repr(count))
        
        assert(len(args) >= count)
    
    def assert_directory_count_less_than_or_equals(self, count):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        if len(args) > count:
            print "Directory list length %s is not less than or equal to expected list lengt %s" % (repr(len(args)), repr(count))
        
        assert(len(args) <= count)

    def assert_directory_count_equals(self, count):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        if len(args) != count:
            print "Expected directory list length %s does not match actual list lengt %s" % (repr(count), repr(len(args)))
        
        assert(len(args) == count)
    
    def assert_directory_is_a_video_list(self):
        folder_count = 0
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        for call in args:
            if call[1]["isFolder"] == True:
                folder_count += 1
        
        if folder_count > 1:
            print "Directory is not a video list, it contains %s folders (Max 1 allowed)" % folder_count
            print "Directory list: \r\n" + repr(args)

        assert(folder_count <= 1)
        
    def assert_directory_is_a_folder_list(self):
        video_count = 0
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        for call in args:
            if call[1]["isFolder"] == False:
                video_count += 1
        
        if video_count > 0:
            print "Directory is not a folder list, it contains %s videos" % video_count
            print "Directory list: \r\n" + repr(args)
            
        assert(video_count == 0)
            
    def assert_directory_contains_almost_only_unique_video_items(self):
        video_ids = []
        non_unique = []
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        for call in args:
            url = call[1]["url"]
            if url.find("videoid=") > -1:
                video = url[url.find("videoid=") + len("videoid="):]
                if video.find("&") > -1:
                    video = video[:video.find("&")]
                
                if video:
                    if video in video_ids:
                        non_unique.append(video)
                    video_ids.append(video)
        
        if len(non_unique) > 2:
            print "Directory contains three or more duplicate videoids.\r\n Duplicates: %s \r\n Full List: %s" % (repr(non_unique), repr(video_ids)) 
            print "Directory list: \r\n" + repr(args)
            
        assert(len(non_unique) <= 2)
    
    def assert_directory_items_should_have_external_thumbnails(self):
        args = sys.modules["__main__"].xbmcgui.ListItem.call_args_list
        
        missing_thumb_count = 0
        for call in args:
            if call[1]["thumbnailImage"].find("http://") == -1: 
                missing_thumb_count += 1
        
        if missing_thumb_count > 1:
            print "Directory contains more than one item with an invalid thumbnail: " 
            print "List Items: \r\n" + repr(args)
        
        assert(missing_thumb_count <= 1)
    
    def assert_directory_items_should_have_thumbnails(self):
        args = sys.modules["__main__"].xbmcgui.ListItem.call_args_list
        
        missing_thumb_count = 0
        for call in args:
            if len(call[1]["thumbnailImage"]) <= 7: 
                missing_thumb_count += 1
        
        if missing_thumb_count > 1:
            print "Directory contains more than one item with an invalid thumbnail: " 
            print "List Items: \r\n" + repr(args)
        
        assert(missing_thumb_count <= 1)
        
    def assert_directory_items_should_have_poster_thumbnails(self):
        args = sys.modules["__main__"].xbmcgui.ListItem.call_args_list
        
        missing_poster_count = 0
        for call in args:
            if call[1]["thumbnailImage"].find("poster") == -1: 
                missing_poster_count += 1
        
        if missing_poster_count > 1:
            print "Directory contains more than one item with an invalid thumbnail: " 
            print "List Items: \r\n" + repr(args)
        
        assert(missing_poster_count <= 1)
    
    def assert_directory_should_have_next_folder(self):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        next_folder_count = 0
        
        for call in args:
            if call[1]["url"].find("page=") > 0:
                next_folder_count += 1
        
        if next_folder_count != 1:
            print "Expected Directory Listing to contain a next folder but didn't find any:"
            print "List Items: \r\n" + repr(args)
        assert(next_folder_count == 1)
        
    def assert_directory_item_urls_contain(self, param):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        missing_count = 0
        
        for call in args:
            url = call[1]["url"]
            if url.find(param + "=") < 0:
                missing_count += 1
            else:
                value = url[url.find(param + "=") + len(param + "="):]
                if value.find("&") > -1:
                    value = value[:value.find("&")]

                if len(value) == 0:
                    missing_count += 1
        
        if missing_count > 1:
            print 'Expected directory items url\'s to contain the "%s" but more than one item was missing this property' % param
            print "Directory list: \r\n" + repr(args)
            
        assert(missing_count <= 1)

    def assert_directory_item_urls_contain_at_least_one(self, param):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list

        found = False

        for call in args:
            print repr(call)
            url = call[1]["url"]
            if url.find(param) > -1:
                found = True
        
        if not found:
            print 'Couldnt find %s in list of directory item title\'s' % param
            print "Directory list: \r\n" + repr(args)
            
        assert(found == True)

    def assert_directory_item_titles_contain(self, param):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list

        found = False
        
        for call in args:
            title = call[1]["Title"]
            if title.find(param) > -1:
                found = True 
        
        if not found:
            print 'Couldnt find %s in list of directory item title\'s' % param
            print "Directory list: \r\n" + repr(args)
            
        assert(found == True)

    def assert_directory_item_titles_does_not_contain(self, param):
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        
        found = False
        
        for call in args:
            title = call[1]["Title"]
            if title.find(param) > -1:
                found = True 
        
        if found:
            print 'Found %s in list of directory item title\'s' % param
            print "Directory list: \r\n" + repr(args)
            
        assert(found == False)
                
    def assert_playlist_count_greater_than_or_equals(self, count):
        args = sys.modules["__main__"].xbmc.PlayList().add.call_args_list
        
        if len(args) < count:
            print "Playlist list length %s is not greater than or equal to expected list lengt %s" % (repr(len(args)), repr(count))
        
        assert(len(args) >= count)
        
    def assert_playlist_count_less_than_or_equals(self, count):
        args = sys.modules["__main__"].xbmc.PlayList().add.call_args_list
        
        if len(args) > count:
            print "Playlist list length %s is not less than or equal to expected list lengt %s" % (repr(len(args)), repr(count))
        
        assert(len(args) <= count)

    def assert_playlist_count_equals(self, count):
        args = sys.modules["__main__"].xbmc.PlayList().add.call_args_list
        
        if len(args) != count:
            print "Playlist list length %s does not equal expected list lengt %s" % (repr(len(args)), repr(count))
        
        assert(len(args) == count)

    def assert_playlist_contains_only_unique_video_items(self):
        video_ids = []
        non_unique = []
        args = sys.modules["__main__"].xbmc.PlayList().add.call_args_list
        
        for call in args:
            url = call[0][0]
            if url.find("videoid=") > -1:
                video = url[url.find("videoid=") + len("videoid="):]
                if video.find("&") > -1:
                    video = video[:video.find("&")]
                
                if video:
                    if video in video_ids:
                        non_unique.append(video)
                    video_ids.append(video)
        
        if len(non_unique) > 0:
            print "Playlist contains one or more duplicate videoids.\r\n Duplicates: %s \r\n Full List: %s" % (repr(non_unique), repr(video_ids)) 
            print "Playlist: \r\n" + repr(args)
            
        assert(len(non_unique) == 0)
    
    def assert_playlist_videos_contain(self, videoid):
        video_ids = []
        args = sys.modules["__main__"].xbmc.PlayList().add.call_args_list
        
        for call in args:
            url = call[0][0]
            if url.find("videoid=") > -1:
                video = url[url.find("videoid=") + len("videoid="):]
                if video.find("&") > -1:
                    video = video[:video.find("&")]
                
                if video not in video_ids:
                    video_ids.append(video)
        
        print repr(video_ids)
        
        if videoid not in video_ids:
            print 'Expected to find %s in playlist items' % videoid
            print "Playlist items: \r\n" + repr(args)
        
        assert(videoid in video_ids)

    def assert_playlist_videos_does_not_contain(self, videoid):
        video_ids = []
        args = sys.modules["__main__"].xbmc.PlayList().add.call_args_list
        
        for call in args:
            url = call[0][0]
            if url.find("videoid=") > -1:
                video = url[url.find("videoid=") + len("videoid="):]
                if video.find("&") > -1:
                    video = video[:video.find("&")]
                
                if video not in video_ids:
                    video_ids.append(video)
        
        if videoid in video_ids:
            print 'Expected not to find %s in playlist items' % videoid
            print "Playlist items: \r\n" + repr(args)
            
        assert(videoid not in video_ids)
