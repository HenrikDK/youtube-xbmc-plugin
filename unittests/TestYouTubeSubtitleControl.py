# -*- coding: utf-8 -*-
import nose
import BaseTestCase
from YouTubeSubtitleControl import YouTubeSubtitleControl
from mock import Mock, patch
import sys

class TestYouTubePlayer(BaseTestCase.BaseTestCase):

    def test_saveSubtitle_should_call_xbmcvfs_translatePath(self):
        sys.modules["__main__"].xbmc.translatePath.return_value = "tempFilePath"
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"

        subtitles = YouTubeSubtitleControl()
        subtitles.getSubtitleFileName = Mock()

        subtitles.saveSubtitle("my_subtitle_stream", {"Title": "testTitle", "videoid": "someVideoId", "downloadPath": "downloadFilePath"})

        sys.modules["__main__"].xbmc.translatePath.assert_called_with("somepath")

    def test_saveSubtitle_should_call_xbmcvfs_rename(self):
        sys.modules["__main__"].xbmc.translatePath.return_value = "tempFilePath"
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        subtitles = YouTubeSubtitleControl()
        subtitles.getSubtitleFileName = Mock(return_value="testTitle-[someVideoId].ssa")

        subtitles.saveSubtitle("my_subtitle_stream", {"Title": "testTitle", "videoid": "someVideoId", "downloadPath": "downloadFilePath"})

        sys.modules["__main__"].xbmcvfs.rename.assert_called_with("tempFilePath/testTitle-[someVideoId].ssa", "downloadFilePath/testTitle-[someVideoId].ssa")

    def test_saveSubtitle_should_call_openFile_with_correct_params(self):
        sys.modules["__main__"].xbmc.translatePath.return_value = "tempFilePath"
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        subtitles = YouTubeSubtitleControl()
        subtitles.getSubtitleFileName = Mock(return_value="testTitle-[someVideoId].ssa")

        subtitles.saveSubtitle("my_subtitle_stream", {"Title": "testTitle", "videoid": "someVideoId", "downloadPath": "downloadFilePath"})

        sys.modules["__main__"].storage.openFile.assert_called_with("tempFilePath/testTitle-[someVideoId].ssa", "w") # was "wb"

    def test_downloadSubtitle_should_call_transformSubtitleToSSA(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "nothingness"}
        subtitlesettings = ["false", "0", "true"]
        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: subtitlesettings.pop()
        player.transformAnnotationToSSA = Mock()
        player.transformAnnotationToSSA.return_value = ("", "style")

        player.downloadSubtitle()

        player.transformAnnotationToSSA.assert_called_with("nothingness")

    def test_downloadSubtitle_should_call_saveSubtitle(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "nothingness"}
        subtitlesettings = ["false", "0", "true"]
        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: subtitlesettings.pop()
        player.transformAnnotationToSSA = Mock()
        player.transformAnnotationToSSA.return_value = ("something", "style")
        player.saveSubtitle = Mock()

        result = player.downloadSubtitle()

        assert(result == True)
        assert(player.saveSubtitle.called)

    def test_downloadSubtitle_should_call_getSubtitleUrl(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "nothingness"}

        subtitlesettings = ["false", "2", "true"]

        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: subtitlesettings.pop()
        player.transformAnnotationToSSA = Mock()
        player.transformAnnotationToSSA.return_value = ("", "style")
        player.getSubtitleUrl = Mock()
        player.getSubtitleUrl.return_value = ""

        player.downloadSubtitle()

        player.getSubtitleUrl.assert_called_with({})

    def test_downloadSubtitle_should_call_getTranscriptionUrl(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "nothingness"}
        subtitlesettings = ["true", "2", "true"]

        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: subtitlesettings.pop()
        player.transformAnnotationToSSA = Mock()
        player.transformAnnotationToSSA.return_value = ("", "style")
        player.getSubtitleUrl = Mock()
        player.getSubtitleUrl.return_value = ""
        player.getTranscriptionUrl = Mock()
        player.getTranscriptionUrl.return_value = ""

        player.downloadSubtitle()

        player.getTranscriptionUrl.assert_called_with({})

    def test_convertSecondsToTimestamp_should_convert(self):
        player = YouTubeSubtitleControl()

        res = player.convertSecondsToTimestamp(250.43800000000002)
        print repr(res)

        assert(res == "0:04:10.438")

    def test_downloadSubtitle_should_call_transformSubtitleXMLtoSRT(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "nothingness"}

        subtitlesettings = ["true", "2", "true"]

        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: subtitlesettings.pop()
        player.transformAnnotationToSSA = Mock()
        player.transformAnnotationToSSA.return_value = ("", "style")
        player.getSubtitleUrl = Mock()
        player.getSubtitleUrl.return_value = ""
        player.getTranscriptionUrl = Mock()
        player.getTranscriptionUrl.return_value = "something"
        player.transformSubtitleXMLtoSRT = Mock()
        player.transformSubtitleXMLtoSRT.return_value = ""

        player.downloadSubtitle()

        player.transformSubtitleXMLtoSRT.assert_called_with("nothingness")

    def test_downloadSubtitle_should_exit_gracefully_if_subtitles_and_annotations_are_disabled(self):
        player = YouTubeSubtitleControl()

        subtitlessettings = ["false", "0", "false"]

        def popSetting(self, *args, **kwargs):
            val = subtitlessettings.pop()
            return val

        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.side_effect = popSetting

        result = player.downloadSubtitle()

        assert(result == False)

    def test_getSubtitleUrl_should_call_fetchPage_with_correct_url(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 303, "content": ""}

        player.getSubtitleUrl({"videoid": "some_id"})

        sys.modules["__main__"].core._fetchPage.assert_called_with({"link": player.urls["timed_text_index"] % ('some_id')})

    def test_getTranscriptionUrl_should_call_return_correct_url(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 303, "content": ""}
        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        ret = player.getTranscriptionUrl({"videoid": "some_id", "ttsurl": "http://some.url/transcript"})
        print ret
        assert(ret == "http://some.url/transcript&type=trackformat=1&lang=en&kind=asr&name=&v=some_id&tlang=en")

    def test_getSubtitleUrl_should_find_url_with_proper_language_code(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": self.readTestInput("timedtextDirectoryTest.xml", False)}
        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.return_value = "3"
        sys.modules["__main__"].common.parseDOM.side_effect = [["de"], ["german"], ["deutch"]]
        sys.modules["__main__"].core.getVideoIdStatusFromCache = Mock()

        url = player.getSubtitleUrl({"videoid": "some_id"})
        print repr(url)

        assert(url.find("lang=de") > 0)

    def test_getSubtitleUrl_should_fall_back_to_english_if_proper_language_code_is_not_found(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].core._fetchPage = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": self.readTestInput("timedtextDirectoryTest.xml", False)}
        sys.modules["__main__"].core.getVideoIdStatusFromCache = Mock()
        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.return_value = "2"
        sys.modules["__main__"].common.parseDOM.side_effect = [["en"], ["english"], ["english"]]

        url = player.getSubtitleUrl({"videoid": "some_id"})

        assert(url.find("lang=en") > 0)

    def test_transformSubtitleXMLtoSRT_should_parse_youtube_subtitle_xml(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].common.replaceHTMLCodes = Mock()
        sys.modules["__main__"].common.replaceHTMLCodes.side_effect = lambda x: x.encode("ascii", 'ignore')
        sys.modules["__main__"].common.parseDOM.side_effect = [["content"] * 3, ["content"], ["00"], ["10"], ["content1"], ["20"], ["30"], ["content3"], ["40"], ["50"]]

        result = player.transformSubtitleXMLtoSRT(self.readTestInput("subtitleTest.xml", False))

        assert(len(result.split("\r\n")) == 4)

    def test_transformSubtitleXMLtoSRT_should_call_replaceHTMLCodes_for_user_visible_text(self):
        sys.modules["__main__"].common.parseDOM.side_effect = [["content TEXT"] * 2, ["text"], ["14.017"], ["2.07"], ["text"], ["16.087"], ["2.996"]]
        player = YouTubeSubtitleControl()
        player.simpleReplaceHTMLCodes = Mock()
        player.simpleReplaceHTMLCodes.side_effect = lambda x: x.encode("ascii", 'ignore')

        result = player.transformSubtitleXMLtoSRT(self.readTestInput("subtitleTest.xml", False))

        print repr(result)

        assert(player.simpleReplaceHTMLCodes.call_count > 0)

    def test_transformSubtitleXMLtoSRT_should_correctly_find_start_time_for_text_elements(self):
        input = '<?xml version="1.0" encoding="utf-8" ?><transcript>\n\
                <text start="14.017" dur="2.07">first</text>\n\
                <text start="16.087" dur="2.996">second</text>\n\
                </transcript>'
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].common.replaceHTMLCodes = Mock()
        sys.modules["__main__"].common.replaceHTMLCodes.side_effect = lambda x: x.encode("ascii", 'ignore')
        sys.modules["__main__"].common.parseDOM.side_effect = [["content TEXT"] * 2, ["text"], ["14.017"], ["2.07"], ["text"], ["16.087"], ["2.996"]]

        result = player.transformSubtitleXMLtoSRT(input).split("\r\n")

        assert(result[0].find("Marked=0,0:00:14.017") > 0)
        assert(result[1].find("Marked=0,0:00:16.087") > 0)

    def test_transformSubtitleXMLtoSRT_should_correctly_recalculate_duration_time_for_text_elements(self):
        input = '<?xml version="1.0" encoding="utf-8" ?><transcript>\n\
                <text start="14.017" dur="2.07">first</text>\n\
                <text start="16.087" dur="2.996">second</text>\n\
                </transcript>'
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].common.replaceHTMLCodes = Mock()
        sys.modules["__main__"].common.replaceHTMLCodes.side_effect = lambda x: x.encode("ascii", 'ignore')
        sys.modules["__main__"].common.parseDOM.side_effect = [["content TEXT"] * 2, ["text"], ["14.017"], ["2.07"], ["text"], ["16.087"], ["2.996"]]

        result = player.transformSubtitleXMLtoSRT(input).split("\r\n")

        assert(result[0].find("0:00:16.087,Default") > 0)
        assert(result[1].find("0:00:19.083,Default") > 0)

    def test_transformAlpha_should_tranform_transparent(self):
        player = YouTubeSubtitleControl()

        color = player.transformAlpha("0.0")
        print color
        assert(color == "-1")

    def test_transformAlpha_should_tranform_80(self):
        player = YouTubeSubtitleControl()

        color = player.transformAlpha("0.800000011921")
        print color
        assert(color == "34")

    def test_transformColor_should_convert_white(self):
        player = YouTubeSubtitleControl()

        color = player.transformColor("16777215")
        print color
        assert(color == "ffffff")

    def test_transformColor_should_convert_red(self):
        player = YouTubeSubtitleControl()

        color = player.transformColor("13369344")
        print color
        assert(color == "0000cc")

    def test_transformColor_should_convert_blue(self):
        player = YouTubeSubtitleControl()

        color = player.transformColor("9828")
        print color
        assert(color == "642600")

    def test_transformColor_should_convert_0(self):
        player = YouTubeSubtitleControl()

        color = player.transformColor("0")
        print color
        assert(color == "000000")

    def test_transformAnnotationToSSA_should_parse_youtube_annotations_xml(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].common.replaceHTMLCodes = Mock()
        sys.modules["__main__"].common.replaceHTMLCodes.side_effect = lambda x: x.encode("ascii", 'ignore')
        sys.modules["__main__"].common.parseDOM.side_effect = [["content TEXT"], ["TEXT"], ["popup"], ["popup"], ["0:00:06.5", "0:01:06.5"], [0], [0], [0], [0], [["snode"]], ["16777215"], ["26777215"], ["36777215"], ["46777215"]]

        (result, style) = player.transformAnnotationToSSA(self.readTestInput("annotationsTest.xml", False).encode("utf-8"))
        print repr(result)
        assert(len(result.split("\r\n")) == 2)

    def test_transformAnnotationToSSA_should_call_replaceHTMLCodes_for_user_visible_text(self):
        player = YouTubeSubtitleControl()
        sys.modules["__main__"].common.replaceHTMLCodes = Mock()
        sys.modules["__main__"].common.replaceHTMLCodes.side_effect = lambda x: x.encode("ascii", 'ignore')
        sys.modules["__main__"].common.parseDOM.side_effect = [["content TEXT"], ["TEXT"], ["bla"], ["bla2"], []]

        result = player.transformAnnotationToSSA(self.readTestInput("annotationsTest.xml", False).encode("utf-8"))
        print repr(result)

        assert(sys.modules["__main__"].common.replaceHTMLCodes.call_count > 0)

    def test_addSubtitles_should_call_downloadSubtitle(self):
        player = YouTubeSubtitleControl()

        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        sys.modules["__main__"].settings.getSetting = Mock()
        sys.modules["__main__"].settings.getSetting.return_value = "testDownloadPath"
        sys.modules["__main__"].xbmcvfs.exists.return_value = False
        player.downloadSubtitle = Mock()
        player.getSubtitleFileName = Mock(return_value="testTitle-[testid].ssa")
        player.downloadSubtitle.return_value = False

        player.addSubtitles({"videoid": "testid", "Title": "testTitle"})

        player.downloadSubtitle.assert_called_with({"videoid": "testid", "Title": "testTitle"})

    def test_addSubtitles_should_check_if_subtitle_exists_locally_before_calling_downloadSubtitle(self):
        player = YouTubeSubtitleControl()

        settings = [False, True]
        sys.modules["__main__"].settings.getSetting.return_value = "testDownloadPath"
        sys.modules["__main__"].xbmcvfs.exists.side_effect = lambda x: settings.pop()
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        player.downloadSubtitle = Mock()
        player.getSubtitleFileName = Mock(return_value="testTitle-[testid].ssa")
        player.downloadSubtitle.return_value = False

        player.addSubtitles({"videoid": "testid", "Title": "testTitle"})

        sys.modules["__main__"].xbmcvfs.exists.assert_called_with('testDownloadPath/testTitle-[testid].ssa')
        assert(player.downloadSubtitle.call_count == 0)

    def test_addSubtitles_should_call_xbmcs_setSubtitles(self):
        sys.modules["__main__"].settings.getSetting.return_value = "testDownloadPath"
        sys.modules["__main__"].xbmcvfs.exists.return_value = True
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        player = YouTubeSubtitleControl()
        player.getSubtitleFileName = Mock(return_value="testTitle-[testid].ssa")
        player.downloadSubtitle = Mock()
        player.downloadSubtitle.return_value = True

        player.addSubtitles({"videoid": "testid", "Title": "testTitle"})

        sys.modules["__main__"].xbmcvfs.exists.assert_called_with('testDownloadPath/testTitle-[testid].ssa')
        sys.modules["__main__"].xbmc.Player().setSubtitles.assert_called_with('testDownloadPath/testTitle-[testid].ssa')

    def test_addSubtitles_should_sleep_for_1_second_if_player_isnt_ready(self):
        sys.modules["__main__"].settings.getSetting.return_value = "testDownloadPath"
        sys.modules["__main__"].xbmcvfs.exists.return_value = True
        sys.modules["__main__"].xbmc.Player().isPlaying.side_effect = [False, True] 
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        patcher = patch("time.sleep")
        patcher.start()
        sleep = Mock()
        import time
        time.sleep = sleep
        player = YouTubeSubtitleControl()
        player.getSubtitleFileName = Mock(return_value="testTitle-[testid].ssa")
        player.downloadSubtitle = Mock()
        player.downloadSubtitle.return_value = True

        player.addSubtitles({"videoid": "testid", "Title": "testTitle"})

        patcher.stop()
        sleep.assert_any_call(1)

    def test_addSubtitles_should_check_if_subtitle_exists_locally_before_calling_xbmcs_setSubtitles(self):
        player = YouTubeSubtitleControl()
        player.getSubtitleFileName = Mock(return_value="testTitle-[testid].ssa")
        sys.modules["__main__"].settings.getSetting.return_value = "testDownloadPath"
        sys.modules["__main__"].xbmcvfs.exists.return_value = True
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        player.downloadSubtitle = Mock()
        player.downloadSubtitle.return_value = False

        player.addSubtitles({"videoid": "testid", "Title": "testTitle"})

        sys.modules["__main__"].xbmcvfs.exists.assert_called_with('testDownloadPath/testTitle-[testid].ssa')
        assert(player.downloadSubtitle.call_count == 0)
        sys.modules["__main__"].xbmc.Player().setSubtitles.assert_called_with('testDownloadPath/testTitle-[testid].ssa')

    def test_addSubtitles_should_wait_for_playback_to_start_before_adding_subtitle(self):
        player = YouTubeSubtitleControl()
        player.getSubtitleFileName = Mock(return_value="testTitle-[testid].ssa")
        sys.modules["__main__"].settings.getSetting.return_value = "testDownloadPath"
        sys.modules["__main__"].xbmcvfs.exists.return_value = True
        sys.modules["__main__"].common.makeUTF8.return_value = "testTitle"
        player.addSubtitles({"videoid": "testid", "Title": "testTitle"})

        sys.modules["__main__"].xbmc.Player().isPlaying.assert_called_with()
        sys.modules["__main__"].xbmc.Player().setSubtitles.assert_called_with('testDownloadPath/testTitle-[testid].ssa')

if __name__ == '__main__':
    nose.runmodule()
