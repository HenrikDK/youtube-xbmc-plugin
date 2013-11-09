# -*- coding: utf-8 -*-
import BaseTestCase
import nose
import sys
from mock import Mock


class TestYouTubePlayer(BaseTestCase.BaseTestCase):

    def test_plugin_should_play_standard_videos(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]

        self.navigation.executeAction({"action": "play_video", "videoid": "54VJWHL2K3I"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)

    def test_plugin_should_play_standard_videos_flashvars_fallback(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]

        self.navigation.executeAction({"action": "play_video", "videoid": "54VJWHL2K3I", "use_flashvars": "true"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)

    def test_plugin_should_play_standard_videos_embed_fallback(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]

        self.navigation.executeAction({"action": "play_video", "videoid": "54VJWHL2K3I", "embed": "true"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)

    def test_plugin_should_play_live_vidoes(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]

        self.navigation.executeAction({"action": "play_video", "videoid": "RcRdNkUhK8M"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)

    def test_plugin_should_warn_on_restricted_videos_if_no_credentials(self):
        sys.modules["__main__"].settings.load_strings("./resources/settings.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]
        sys.modules["__main__"].utils.showMessage = Mock()
        self.navigation.executeAction({"action": "play_video", "videoid": "Vzue74y7A84"})

        args = sys.modules["__main__"].utils.showMessage.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr(args[0][0][1] == "Playback requires valid YouTube account")

        assert(args[0][0][1] == "Playback requires valid YouTube account")

    def test_plugin_should_play_age_restricted_videos_if_user_provides_credentials(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]

        self.navigation.executeAction({"action": "play_video", "videoid": "Vzue74y7A84"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)

    def test_plugin_should_play_rtmpe_vidoes(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]

        self.navigation.executeAction({"action": "play_video", "videoid": "8wxOVn99FTE"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)

    def test_plugin_should_play_videos_with_subtitles_when_available(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].settings.setSetting("lang_code", "1")
        import os
        sys.modules["__main__"].xbmcvfs.exists.side_effect = os.path.exists
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]
        self.navigation.executeAction({"action": "play_video", "videoid": "bUcszN8jRB8"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        args2 = sys.modules["__main__"].xbmc.Player().setSubtitles.call_args_list

        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print "Args2: " + repr(args2)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)
        print repr(args2[0][0][0] == u"./tmp/Morning Dew  a bad lip reading of Bruno Mars, feat. Lady Gaga and Jay-Z-[bUcszN8jRB8]-EN.ssa")

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)
        assert(args2[0][0][0] == u"./tmp/Morning Dew  a bad lip reading of Bruno Mars, feat. Lady Gaga and Jay-Z-[bUcszN8jRB8]-EN.ssa")

    def test_plugin_should_play_videos_with_subtitles_and_annotation_when_available(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].settings.setSetting("lang_code", "1")
        import os
        sys.modules["__main__"].xbmcvfs.exists.side_effect = os.path.exists
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]

        self.navigation.executeAction({"action": "play_video", "videoid": "YcQfiYUXrtI"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        args2 = sys.modules["__main__"].xbmc.Player().setSubtitles.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print "Args2: " + repr(args2)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)
        print repr(args2[0][0][0] == './tmp/Kicked Your Monkey  A Bad Lip Reading of Gotye\'s Somebody That I Used To Know-[YcQfiYUXrtI]-EN.ssa')

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)
        assert(args2[0][0][0] == './tmp/Kicked Your Monkey  A Bad Lip Reading of Gotye\'s Somebody That I Used To Know-[YcQfiYUXrtI]-EN.ssa')

    def test_plugin_should_play_video_with_subtitle_other_than_english(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].settings.setSetting("lang_code", "2")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]
        import os
        sys.modules["__main__"].xbmcvfs.exists.side_effect = os.path.exists

        self.navigation.executeAction({"action": "play_video", "videoid": "4Z9WVZddH9w"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        args2 = sys.modules["__main__"].xbmc.Player().setSubtitles.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print "Args2: " + repr(args2)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)
        print repr(args2[0][0][0] == u"./tmp/ZEITGEIST MOVING FORWARD  OFFICIAL RELEASE  2011-[4Z9WVZddH9w]-ES.ssa")

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)
        assert(args2[0][0][0] == u"./tmp/ZEITGEIST MOVING FORWARD  OFFICIAL RELEASE  2011-[4Z9WVZddH9w]-ES.ssa")

    def ttest_plugin_should_play_geolocked_videos(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].cache.getMulti.return_value = ["7"]
        import os
        sys.modules["__main__"].xbmcvfs.exists.side_effect = os.path.exists

        self.navigation.executeAction({"action": "play_video", "videoid": "ha_NOX_-Aeg"})

        args = sys.modules["__main__"].xbmcplugin.setResolvedUrl.call_args_list
        print "url: " + repr(sys.modules["__main__"].xbmcgui.ListItem.call_args_list)
        print "Args: " + repr(args)
        print repr("listitem" in args[0][1])
        print repr(args[0][1]["handle"] == -1)
        print repr(args[0][1]["succeeded"] == True)

        assert("listitem" in args[0][1])
        assert(args[0][1]["handle"] == -1)
        assert(args[0][1]["succeeded"] == True)

if __name__ == "__main__":
    nose.runmodule()
