import sys
import time
import inspect


class MockYouTubeDepends:
    common = ""

    def mock(self):
        from mock import Mock
        sys.path.append(u"../plugin/")

        #Setup default test various values
        sys.modules[u"__main__"].plugin = u"YouTube - Unittest"
        sys.modules[u"__main__"].dbg = True
        try:
            plat = platform.uname()
        except:
            plat = ('', '', '', '', '', '')

        if plat[0] == u"FreeBSD" and False:
            sys.modules[u"__main__"].dbglevel = 5
        else:
            sys.modules[u"__main__"].dbglevel = 3

        sys.modules[u"__main__"].login = ""
        sys.modules[u"__main__"].language = Mock()
        sys.modules[u"__main__"].opener = Mock()
        sys.modules[u"__main__"].cookiejar = Mock()

        import YouTubeUtils
        sys.modules[u"__main__"].utils = Mock(spec=YouTubeUtils.YouTubeUtils)
        sys.modules[u"__main__"].utils.INVALID_CHARS = u"\\/:*?\"<>|"

        sys.modules[u"__main__"].common = Mock()
        sys.modules[u"__main__"].common.log.side_effect = self.log
        sys.modules[u"__main__"].common.USERAGENT = u"Mozilla/5.0 (MOCK)"

        sys.modules[u"__main__"].cache = Mock()

        import YouTubeStorage
        sys.modules[u"__main__"].storage = Mock(spec=YouTubeStorage.YouTubeStorage)
        import YouTubePluginSettings
        sys.modules[u"__main__"].pluginsettings = Mock(spec=YouTubePluginSettings.YouTubePluginSettings)
        import YouTubeCore
        sys.modules[u"__main__"].core = Mock(spec=YouTubeCore.YouTubeCore)
        import YouTubeLogin
        sys.modules[u"__main__"].login = Mock(spec=YouTubeLogin.YouTubeLogin)
        import YouTubeFeeds
        sys.modules[u"__main__"].feeds = Mock(spec=YouTubeFeeds.YouTubeFeeds)
        import YouTubeSubtitleControl
        sys.modules[u"__main__"].subtitles = Mock(spec=YouTubeSubtitleControl.YouTubeSubtitleControl)
        import YouTubePlayer
        sys.modules[u"__main__"].player = Mock(spec=YouTubePlayer.YouTubePlayer)
        sys.modules[u"__main__"].downloader = Mock()
        import YouTubeScraper
        sys.modules[u"__main__"].scraper = Mock(spec=YouTubeScraper.YouTubeScraper)
        import YouTubePlaylistControl
        sys.modules[u"__main__"].playlist = Mock(spec=YouTubePlaylistControl.YouTubePlaylistControl)
        import YouTubeNavigation
        sys.modules[u"__main__"].navigation = Mock(spec=YouTubeNavigation.YouTubeNavigation)

    def mockXBMC(self):
        from mock import Mock
        sys.path.append(u"../xbmc-mocks/")
        import xbmc
        import xbmcaddon
        import xbmcgui
        import xbmcplugin
        import xbmcvfs

        #Setup basic xbmc dependencies
        sys.modules[u"__main__"].xbmc = Mock(spec=xbmc)
        sys.modules[u"__main__"].xbmc.translatePath = Mock()
        sys.modules[u"__main__"].xbmc.translatePath.return_value = u"testing"
        sys.modules[u"__main__"].xbmc.getSkinDir = Mock()
        sys.modules[u"__main__"].xbmc.getSkinDir.return_value = u"testSkinPath"
        sys.modules[u"__main__"].xbmc.getInfoLabel.return_value = u"some_info_label"
        sys.modules[u"__main__"].xbmcaddon = Mock(spec=xbmcaddon)
        sys.modules[u"__main__"].xbmcgui = Mock(spec=xbmcgui)
        sys.modules[u"__main__"].xbmcgui.WindowXMLDialog.return_value = u"testWindowXML"

        sys.modules[u"__main__"].xbmcplugin = Mock(spec=xbmcplugin)
        sys.modules[u"__main__"].xbmcvfs = Mock(spec=xbmcvfs)
        sys.modules[u"__main__"].settings = Mock(spec=xbmcaddon.Addon())
        sys.modules[u"__main__"].settings.getAddonInfo.return_value = u"somepath"

        sys.modules[u"DialogDownloadProgress"] = __import__(u"mock")
        sys.modules[u"DialogDownloadProgress"].DownloadProgress = Mock()

    def log(self, description, level=0):
        if sys.modules[u"__main__"].dbg and sys.modules[u"__main__"].dbglevel > level:
            try:
                print u"%s [%s] %s : '%s'" % (time.strftime(u"%H:%M:%S"), u"YouTube IntegrationTest", inspect.stack()[3][3], description.decode(u"utf-8", u"ignore"))
            except:
                print u"%s [%s] %s : '%s'" % (time.strftime(u"%H:%M:%S"), u"YouTube IntegrationTest", inspect.stack()[3][3], description)
