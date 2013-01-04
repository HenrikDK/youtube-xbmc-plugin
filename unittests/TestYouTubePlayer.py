# -*- coding: utf-8 -*-
import nose
import BaseTestCase
from mock import Mock, patch
import sys
from YouTubePlayer import YouTubePlayer


class TestYouTubePlayer(BaseTestCase.BaseTestCase):

    def test__getVideoLinks_should_return_empty_dictionary_on_missing_map(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"status":303, "content": ""}
        sys.modules["__main__"].common.parseDOM.return_value = []

        player = YouTubePlayer()
        (result, status) = player.extractVideoLinksFromYoutube({},{"videoid":"123"})

        assert (result == {})

    def test_playVideo_should_call_getVideoObject(self):
        player = YouTubePlayer()
        player.buildVideoObject = Mock(return_value=[{"apierror": "some error"}, 303])

        player.playVideo()

        player.buildVideoObject.assert_called_with({})

    def test_playVideo_should_log_and_fail_gracefully_on_apierror(self):
        player = YouTubePlayer()
        player.buildVideoObject = Mock()
        player.buildVideoObject.return_value = [{"apierror": "some error"}, 303]

        result = player.playVideo()

        assert(result == False)
        sys.modules["__main__" ].common.log.assert_called_with("construct video url failed contents of video item {'apierror': 'some error'}")

    def test_playVideo_should_call_xbmc_setResolvedUrl(self):
        sys.modules["__main__"].settings.getSetting.return_value = "0"
        player = YouTubePlayer()
        player.addSubtitles = Mock()
        player.buildVideoObject = Mock()
        player.buildVideoObject.return_value = ({"Title": "someTitle", "videoid": "some_id", "thumbnail": "someThumbnail", "video_url": "someUrl"}, 200)
        sys.argv = ["test1", "1", "test2"]

        player.playVideo({"videoid": "some_id"})

        assert(sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_count > 0)

    def test_playVideo_should_call_addSubtitles(self):
        video = {"Title": "someTitle", "videoid": "some_id", "thumbnail": "someThumbnail", "video_url": "someUrl"}
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.argv = ["test1", "1", "test2"]
        player = YouTubePlayer()
        player.buildVideoObject = Mock()
        player.buildVideoObject.return_value = (video, 200)

        player.playVideo({"videoid": "some_id"})

        sys.modules["__main__"].subtitles.addSubtitles.assert_called_with(video)

    def test_playVideo_should_call_remove_from_watch_later_if_viewing_video_from_watch_later_queue(self):
        player = YouTubePlayer()
        sys.modules["__main__"].settings.getSetting.return_value = "0"
        sys.argv = ["test1", "1", "test2"]
        player.buildVideoObject = Mock()
        player.buildVideoObject.return_value = ({"Title": "someTitle", "videoid": "some_id", "thumbnail": "someThumbnail", "video_url": "someUrl"}, 200)
        player.addSubtitles = Mock()
        call_params = {"videoid": "some_id", "watch_later": "true", "playlist": "playlist_id", "playlist_entry_id": "entry_id"}

        player.playVideo(call_params)

        sys.modules["__main__"].core.remove_from_watch_later.assert_called_with(call_params)

    def test_playVideo_should_update_locally_stored_watched_status(self):
        sys.modules["__main__"].settings.getSetting.return_value = "0"
        sys.argv = ["test1", "1", "test2"]
        player = YouTubePlayer()
        player.buildVideoObject = Mock()
        player.buildVideoObject.return_value = ({"Title": "someTitle", "videoid": "some_id", "thumbnail": "someThumbnail", "video_url": "someUrl"}, 200)
        player.addSubtitles = Mock()

        player.playVideo({"videoid": "some_id"})
        sys.modules["__main__"].storage.storeValue.assert_called_with("vidstatus-some_id", "7" )

    def test_getInfo_should_use_cache_when_possible(self):
        sys.modules["__main__"].cache.get.return_value = '["something"]'
        player = YouTubePlayer()

        player.getInfo({"videoid": "some_id"})

        sys.modules["__main__"].cache.get.assert_called_with("videoidcachesome_id")

    def test_getInfo_should_call_fetchPage_with_correct_url(self):
        sys.modules["__main__"].cache.get.return_value = {}
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 303, "content": "something"}
        player = YouTubePlayer()

        player.getInfo({"videoid": "some_id"})

        sys.modules["__main__"].core._fetchPage.assert_called_with({"api": "true", "link": player.urls["video_info"] % ("some_id")})

    def test_getInfo_should_call_core_getVideoInfo_to_parse_youtube_xml(self):
        sys.modules["__main__"].cache.get.return_value = {}
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "something"}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id"}]
        player = YouTubePlayer()

        player.getInfo({"videoid": "some_id"})

        sys.modules["__main__"].core.getVideoInfo.assert_called_with("something", {"videoid": "some_id"})

    def test_getInfo_should_fail_correctly_if_api_is_unavailable(self):
        sys.modules["__main__"].cache.get.return_value = {}
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "something"}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        sys.modules["__main__"].language.return_value = "some_string"
        player = YouTubePlayer()

        (video, status) = player.getInfo({"videoid": "some_id"})

        sys.modules["__main__"].common.log.assert_called_with("- Couldn't parse API output, YouTube doesn't seem to know this video id?")
        sys.modules["__main__"].language.assert_called_with(30608)
        assert(video["apierror"] == "some_string")

    def test_getInfo_should_save_video_info_in_cache(self):
        sys.modules["__main__"].cache.get.return_value = {}
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": "something"}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id"}]
        player = YouTubePlayer()

        player.getInfo({"videoid": "some_id"})

        sys.modules["__main__"].cache.set.assert_called_with('videoidcachesome_id', "{'videoid': 'some_id'}")

    def test_selectVideoQuality_should_prefer_h264_over_vp8_for_720p_as_appletv2_cant_handle_vp8_properly(self):
        sys.modules["__main__"].settings.getSetting.return_value = "2"
        player = YouTubePlayer()

        url = player.selectVideoQuality({},{22: "h264", 45: "vp8"})

        print "url: " + repr(url)
        assert(url == "h264 | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_prefer_1080p_if_asked_to(self):
        sys.modules["__main__"].settings.getSetting.return_value = "2"
        player = YouTubePlayer()

        url = player.selectVideoQuality({"quality": "1080p"},{37: "1080p", 22: "720p", 35: "SD"})

        assert(url == "1080p | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_prefer_720p_if_asked_to(self):
        sys.modules["__main__"].settings.getSetting.return_value = "2"
        player = YouTubePlayer()

        url = player.selectVideoQuality({"quality": "720p"},{37: "1080p", 22: "720p", 35: "SD"})

        assert(url == "720p | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_prefer_SD_if_asked_to(self):
        sys.modules["__main__"].settings.getSetting.return_value = "2"
        player = YouTubePlayer()

        url = player.selectVideoQuality({"quality": "SD"},{37: "1080p", 22: "720p", 35: "SD"})

        assert(url == "SD | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_choose_highest_sd_quality_if_only_multiple_sd_qualities_are_available(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        player = YouTubePlayer()

        url = player.selectVideoQuality({},{5: "1", 33: "2", 18: "3", 26: "4", 43: "5", 34: "6", 78: "7", 44: "8", 59: "9", 35: "10"})

        assert(url == "10 | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_prefer_1080p_if_user_has_selected_that_option(self):
        sys.modules["__main__"].settings.getSetting.return_value = "3"
        player = YouTubePlayer()

        url = player.selectVideoQuality({},{35: "SD", 22: "720p", 37: "1080p"})

        assert(url == "1080p | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_limit_to_720p_if_user_has_selected_that_option(self):
        sys.modules["__main__"].settings.getSetting.return_value = "2"
        player = YouTubePlayer()

        url = player.selectVideoQuality({},{35: "SD", 22: "720p", 37: "1080p"})

        assert(url == "720p | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_limit_to_sd_if_user_has_selected_that_option(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        player = YouTubePlayer()

        url = player.selectVideoQuality({},{35: "SD", 22: "720p", 37: "1080p"})

        assert(url == "SD | Mozilla/5.0 (MOCK)")

    def test_selectVideoQuality_should_call_userSelectsVideoQuality_if_user_selected_that_option(self):
        sys.modules["__main__"].settings.getSetting.return_value = "0"
        player = YouTubePlayer()
        player.userSelectsVideoQuality = Mock()

        player.selectVideoQuality({},{35: "SD", 22: "720p", 37: "1080p"})

        player.userSelectsVideoQuality.assert_called_with({}, {35: 'SD', 37: '1080p', 22: '720p'})

    def test_selectVideoQuality_should_add_user_agent_when_not_called_by_download_function(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        player = YouTubePlayer()

        url = player.selectVideoQuality({},{35: "SD", 22: "720p", 37: "1080p"})

        assert(url.find("| Mozilla/5.0 (MOCK)") > 0)

    def test_selectVideoQuality_should_not_add_user_agent_when_called_by_download_function(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        player = YouTubePlayer()

        url = player.selectVideoQuality({"action": "download"},{35: "SD", 22: "720p", 37: "1080p"})

        assert(url.find("| Mozilla/5.0 (MOCK)") < 0)

    def test_userSelectsVideoQuality_should_append_list_of_known_qualities(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].xbmcgui.Dialog().select.return_value = -1
        sys.modules["__main__"].language.return_value = ""
        player = YouTubePlayer()

        url = player.userSelectsVideoQuality({}, {35: u"SD", 22: u"720p", 37: u"1080p", 35: u"480p", 18: u"380p", 34: u"360p", 5: u"240p", 17: u"144p"})
        print repr(url)

        sys.modules["__main__"].xbmcgui.Dialog().select.assert_any_call("", [u"1080p", u"720p", u"480p", u"380p", u"360p", u"240p", u"144p"])

    def test_userSelectsVideoQuality_should_prefer_h264_over_vp8_as_appletv2_cant_handle_vp8_properly(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].xbmcgui.Dialog().select.return_value = 0
        sys.modules["__main__"].language.return_value = ""
        player = YouTubePlayer()

        url = player.userSelectsVideoQuality({}, {22: "h264", 45: "vp8"})

        assert(url == "h264")

    def test_userSelectsVideoQuality_should_select_proper_quality_based_on_user_input(self):
        player = YouTubePlayer()
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].xbmcgui.Dialog().select.return_value = 0
        sys.modules["__main__"].language.return_value = ""
        sys.modules["__main__"].common.makeUTF8.return_value = "bla"

        url = player.userSelectsVideoQuality({}, {35: u"SD", 22: u"720p", 37: u"1080p"})

        sys.modules["__main__"].xbmcgui.Dialog().select.assert_called_with("", [u"1080p", u"720p", u"480p"])
        assert(url == "1080p")

    def test_userSelectsVideoQuality_should_call_xbmc_dialog_select_to_ask_for_user_input(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].xbmcgui.Dialog().select.return_value = -1
        sys.modules["__main__"].language.return_value = ""
        player = YouTubePlayer()

        url = player.userSelectsVideoQuality({}, {35: "SD", 22: "720p", 37: "1080p"})

        print repr(url)

        assert(sys.modules["__main__"].xbmcgui.Dialog().select.call_count > 0)

    def test_buildVideoObject_should_get_video_information_from_getInfo(self):
        sys.modules["__main__"].settings.getSetting.return_value = ""
        player = YouTubePlayer()
        player.getInfo = Mock()
        player.getInfo.return_value = ({}, 303)
        player.extractVideoLinksFromYoutube = Mock()
        player.extractVideoLinksFromYoutube.return_value = ({}, {})

        player.buildVideoObject({})

        player.getInfo.assert_called_with({})

    def test_buildVideoObject_should_use_local_file_for_playback_if_found(self):
        sys.modules["__main__"].subtitles.getLocalFileSource.return_value = "somePath/someTitle.mp4"
        params = {"videoid": "some_id"}
        player = YouTubePlayer()
        player.getInfo = Mock()
        video = {"videoid": "some_id", "Title": "someTitle"}
        player.getInfo.return_value = (video, 200)

        (video, status) = player.buildVideoObject(params)

        assert(video["video_url"] == "somePath/someTitle.mp4")

    def test_buildVideoObject_should_not_scrape_webpage_if_local_file_is_found(self):
        sys.modules["__main__"].subtitles.getLocalFileSource.return_value = "somePath/someTitle.mp4"
        params = {"videoid": "some_id"}
        player = YouTubePlayer()
        player.getInfo = Mock()
        player.extractVideoLinksFromYoutube = Mock()
        video = {"videoid": "some_id", "Title": "someTitle"}
        player.getInfo.return_value = (video, 200)

        player.buildVideoObject(params)

        assert(player.extractVideoLinksFromYoutube.call_count == 0)

    def test_buildVideoObject_should_check_for_local_file_before_scraping(self):
        sys.modules["__main__"].subtitles.getLocalFileSource.return_value = "somePath/someTitle.mp4"
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        params = {"videoid": "some_id"}
        player = YouTubePlayer()
        player.getInfo = Mock()
        video = {"videoid": "some_id", "Title": "someTitle"}
        player.getInfo.return_value = (video, 200)

        (video, status) = player.buildVideoObject(params)

        sys.modules["__main__"].subtitles.getLocalFileSource.assert_called_with(params, video)

    def test_buildVideoObject_should_call_getVideoLinks_if_local_file_not_found(self):
        sys.modules["__main__"].subtitles.getLocalFileSource.return_value = ""
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        params = {"videoid": "some_id"}
        player = YouTubePlayer()
        player.getInfo = Mock()
        player.extractVideoLinksFromYoutube = Mock()
        player.extractVideoLinksFromYoutube.return_value = ({}, {})
        video = {"videoid": "some_id", "Title": "someTitle"}
        player.getInfo.return_value = (video, 200)

        player.buildVideoObject(params)

        player.extractVideoLinksFromYoutube.assert_any_call(video, params)

    def test_buildVideoObject_should_call_selectVideoQuality_if_local_file_not_found_and_remote_links_found(self):
        sys.modules["__main__"].subtitles.getLocalFileSource.return_value = ""
        params = {"videoid": "some_id"}
        video = {"videoid": "some_id", "Title": "someTitle"}

        player = YouTubePlayer()
        player.getInfo = Mock()
        player.getInfo.return_value = (video, 200)

        player.extractVideoLinksFromYoutube = Mock()
        player.extractVideoLinksFromYoutube.return_value = ({22: "720p"}, {})
        player.selectVideoQuality = Mock()

        player.buildVideoObject(params)

        player.selectVideoQuality.assert_called_with(params,{22: "720p"})

    def test_buildVideoObject_should_use_pre_defined_error_messages_on_missing_url(self):
        sys.modules["__main__"].settings.getSetting.return_value = ""
        player = YouTubePlayer()
        player.getInfo = Mock()
        player.getInfo.return_value = ({}, 303)
        player.getLocalFileSource = Mock(return_value="")
        player.extractVideoLinksFromYoutube = Mock(return_value = ({}, {}))

        player.buildVideoObject({})

        player.getInfo.assert_called_with({})
        sys.modules["__main__"].language.assert_called_with(30618)

    def test_buildVideoLinks_should_try_scraping_first(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"status":303, "content": ""}
        sys.modules["__main__"].common.parseDOM.return_value = []

        player = YouTubePlayer()
        player.extractVideoLinksFromYoutube({},{"videoid":"123"})

        sys.modules["__main__"].core._fetchPage.assert_any_call({"link":player.urls["video_stream"] % "123", "login":"true"})

    def ttest_getVideoLinks_should_fall_back_to_embed(self):

        assert(False)

    def ttest_getVideoLinks_should_get_error_message_from_embed(self):
        assert(False)

    def test_getVideoLinks_should_parse_main_video_structure_on_webpage_correctly(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": self.readTestInput("normal-video-page-bQbbtnTz1KE.html", False)}
        sys.modules["__main__"].common.parseDOM.return_value = []
        player = YouTubePlayer()
        sys.modules["__main__"].core._findErrors.return_value = "mock error"

        result = player.extractVideoLinksFromYoutube({}, {"videoid": "some_id"})

        print repr(result)

        assert(result[0].has_key(35))

    def test_getVideoLinks_should_parse_rtmpe_video_structure_on_webpage_correctly(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": self.readTestInput("rtmpe-video-page-8wxOVn99FTE.html", False)}
        player = YouTubePlayer()
        sys.modules["__main__"].core._findErrors.return_value = "mock error"
        sys.modules["__main__"].common.parseDOM.return_value = []

        result = player.extractVideoLinksFromYoutube({}, {"videoid": "some_id"})

        print repr(result)

        assert(result[0].has_key(36))

    def test_getVideoLinks_should_parse_live_video_structure_on_webpage_correctly(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"status": 200, "content": self.readTestInput("live-video-page-e93MaEwrsfc.html", False)}
        sys.modules["__main__"].common.parseDOM.return_value = []
        player = YouTubePlayer()
        sys.modules["__main__"].core._findErrors.return_value = "mock error"

        result = player.extractVideoLinksFromYoutube({}, {"videoid": "some_id"})

        print repr(result)

        assert(result[0].has_key(35))



if __name__ == '__main__':
    nose.runmodule()
