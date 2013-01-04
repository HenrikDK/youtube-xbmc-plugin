import BaseTestCase
import nose
import time
import sys
from mock import Mock


class TestYouTubeUserActions(BaseTestCase.BaseTestCase):
    def test_plugin_should_add_favorite(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "favorites", "login": "true", "path": "/root/favorites"})
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        for arg in args:
            print repr(arg[1]["url"].find("f21TjSzgxjM") > -1)
            if arg[1]["url"].find("f21TjSzgxjM") > -1:
                result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/favorites?start-index=1&max-results=50", "auth": "true", "api": "true"})
                items = sys.modules["__main__"].core.getVideoInfo(result["content"])
                for item in items:
                    if item["videoid"] == "f21TjSzgxjM":
                        self.navigation.executeAction({"action": "remove_favorite", "editid": item["editid"]})

        self.navigation.executeAction({"action": "add_favorite", "videoid": "f21TjSzgxjM"})
        self.navigation.listMenu({"user_feed": "favorites", "login": "true", "path": "/root/favorites"})
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        result = False
        for arg in args:
            print repr(arg[1]["url"].find("f21TjSzgxjM") > -1)
            if arg[1]["url"].find("f21TjSzgxjM") > -1:
                result = True
        assert(result)

    def test_plugin_should_remove_favorite(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "favorites", "login": "true", "path": "/root/favorites"})
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        result = False
        for arg in args:
            #print repr(arg[1]["url"].find("7eiD38Av8fQ") > -1)
            if arg[1]["url"].find("7eiD38Av8fQ") > -1:
                result = True
        if not result:
            self.navigation.executeAction({"action": "add_favorite", "videoid": "7eiD38Av8fQ"})

        result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/favorites?start-index=1&max-results=50", "auth": "true", "api": "true"})
        items = sys.modules["__main__"].core.getVideoInfo(result["content"])
        editid = False
        for item in items:
            if item["videoid"] == "7eiD38Av8fQ":
                editid = item["editid"]

        if editid:
            self.navigation.executeAction({"action": "remove_favorite", "editid": editid})
            self.navigation.listMenu({"user_feed": "favorites", "login": "true", "path": "/root/favorites"})
            args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
            print repr(args)
            for arg in args:
                assert(arg[1]["url"].find("7eiD38Av8fQ") == -1)
        else:
            assert(False)

    def ttest_plugin_should_add_subscription(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        #self.navigation.executeAction({"action": "add_subscription", "channel": "chuggaaconroy"})
        self.navigation.listMenu({"user_feed": "subscriptions", 'login': 'true', "path": "/root/subscriptions/something/smokey"})
        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        print repr(args)
        assert(False)

    def ttest_plugin_should_remove_subscription(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        self.navigation.executeAction({"action": "remove_subscription", "editid": "8wxOVn99FTE"})
        assert(False)

    def ttest_plugin_should_add_contact(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        self.navigation.executeAction({"action": "add_contact", "contact": "chuggaaconroy"})

        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in-10-perpage.xml")

        self.navigation.listMenu({"user_feed": "contacts", 'login': 'true', "path": "/root/contacts/smokey", "folder": "true"})

        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        print repr(args)
        assert(False)

    def ttest_plugin_should_remove_contact(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        self.navigation.executeAction({"action": "remove_contact", "contact": "chuggaaconroy"})
        assert(False)

    def ttest_plugin_should_add_to_playlist(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/playlists?v=2.1&start-index=1&max-results=50", "auth": "true"})
        items = sys.modules["__main__"].core.getFolderInfo(result["content"])

        playlistid = False
        for item in items:
            print repr(item)
            if item["Title"] == "1":
                playlistid = item["editid"]

        if playlistid:
            self.navigation.executeAction({"action": "add_to_playlist", "videoid": "8wxOVn99FTE", "playlist": playlistid})
            assert(False)
        else:
            assert(False)

    def ttest_plugin_should_remove_from_playlist(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/playlists?v=2.1&start-index=1&max-results=50", "auth": "true"})
        items = sys.modules["__main__"].core.getFolderInfo(result["content"])

        playlistid = False
        for item in items:
            print repr(item)
            if item["Title"] == "1":
                playlistid = item["editid"]

        result = sys.modules["__main__"].core._fetchPage({'link': 'http://gdata.youtube.com/feeds/api/playlists/' + playlistid + '?v=2.1&start-index=1&max-results=50', 'auth': 'true'})

        items = sys.modules["__main__"].core.getVideoInfo(result["content"])

        playlist_entry_id = False
        for item in items:
            print repr(item)
            if item["Title"] == "1":
                playlist_entry_id = item["playlist_entry_id"]

        if playlistid and playlist_entry_id:
            self.navigation.executeAction({"action": "remove_from_playlist", "playlist_entry_id": playlist_entry_id, "playlist": playlistid})
            assert(False)
        else:
            assert(False)

    def test_plugin_should_add_playlist(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        sys.modules["__main__"].xbmc.Keyboard().isConfirmed.return_value = True
        sys.modules["__main__"].common.getUserInput = Mock()
        sys.modules["__main__"].common.getUserInput.return_value = "testlist"

        result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/playlists?v=2.1&start-index=1&max-results=50", "auth": "true"})
        items = sys.modules["__main__"].core.getFolderInfo(result["content"])

        for item in items:
            if item["Title"] == "testlist":
                print "Deleting stale playlist with editid: %s" % item["editid"]
                self.navigation.executeAction({"action": "delete_playlist", "playlist": item["editid"]})

        self.navigation.executeAction({"action": "create_playlist", "title": "testlist", "summary": "test"})

        time.sleep(15)
        exists = False
        result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/playlists?v=2.1&start-index=1&max-results=50", "auth": "true"})
        items = sys.modules["__main__"].core.getFolderInfo(result["content"])

        for item in items:
            print repr(item) + " - looking for 'testlist'"
            if item["Title"] == "testlist":
                exists = True
        assert(exists)

    def test_plugin_should_remove_playlist(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].xbmc.Keyboard().isConfirmed.return_value = True
        sys.modules["__main__"].common.getUserInput = Mock()
        sys.modules["__main__"].common.getUserInput.return_value = "testlist"

        exists = False
        result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/playlists?v=2.1&start-index=1&max-results=50", "auth": "true"})
        items = sys.modules["__main__"].core.getFolderInfo(result["content"])

        for item in items:
            if item["Title"] == "testlist":
                print "Playlist 'testlist' exists."
                exists = True
        if not exists:
            print "Playlist does not exist. Creating."
            #self.navigation.executeAction({"action": "create_playlist", "title": "testlist", "summary": "test"})
            self.navigation.executeAction({"action": "create_playlist", "summary": "test"})

        result = sys.modules["__main__"].core._fetchPage({"link": "http://gdata.youtube.com/feeds/api/users/default/playlists?v=2.1&start-index=1&max-results=50", "auth": "true"})
        items = sys.modules["__main__"].core.getFolderInfo(result["content"])
        print repr(items)
        editid = False
        for item in items:
            print repr(item) + " - looking for 'testlist'"
            if item["Title"] == "testlist":
                editid = item["editid"]
                self.navigation.executeAction({"action": "delete_playlist", "playlist": item["editid"]})

        self.navigation.listMenu({"user_feed": "playlists", "login": "true", "path": "/root/playlists", "folder": "true"})

        args = sys.modules["__main__"].xbmcplugin.addDirectoryItem.call_args_list
        result = False
        if editid:
            for arg in args:
                print repr(arg[1]) + " - " + editid
                assert(arg[1]["url"].find(editid) == -1)
        else:
            assert(False)

if __name__ == "__main__":
    nose.runmodule()
