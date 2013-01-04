# -*- coding: utf-8 -*-
import BaseTestCase
import nose
import sys
import os
from mock import Mock


class TestYouTubeDownloader(BaseTestCase.BaseTestCase):

    def test_plugin_should_download_standard_videos(self):
        sys.modules["__main__"].xbmcvfs.rename.side_effect = os.rename
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].downloader._getNextItemFromQueue = Mock()
        (video, status) = sys.modules["__main__"].player.buildVideoObject({"action": "download", "videoid": "54VJWHL2K3I"})
        video["download_path"] = "./tmp/"
        video["url"] = video["video_url"]
        sys.modules["__main__"].downloader._getNextItemFromQueue.side_effect = [("Roll a D6-[54VJWHL2K3I].mp4", video), {}]

        self.navigation.executeAction({"action": "download", "videoid": "54VJWHL2K3I", "async": "false"})
        assert(os.path.exists('./tmp/Roll a D6-[54VJWHL2K3I].mp4'))
        assert(os.path.getsize('./tmp/Roll a D6-[54VJWHL2K3I].mp4') > 100)

    def ttest_plugin_should_download_with_subtitles_when_available(self):
        sys.modules["__main__"].xbmcvfs.rename.side_effect = os.rename
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings.xml")
        sys.modules["__main__"].downloader._getNextItemFromQueue = Mock()
        (video, status) = sys.modules["__main__"].player.buildVideoObject({"action": "download", "videoid": "bUcszN8jRB8"})
        video["download_path"] = "./tmp/"
        video["url"] = video["video_url"]
        sys.modules["__main__"].downloader._getNextItemFromQueue.side_effect = [("Morning Dew — a bad lip reading of Bruno Mars, feat. Lady Gaga and Jay-Z-[bUcszN8jRB8].mp4", video), {}]

        self.navigation.executeAction({"action": "download", "videoid": "bUcszN8jRB8", "async": "false"})

        assert(os.path.exists('./tmp/Morning Dew — a bad lip reading of Bruno Mars, feat. Lady Gaga and Jay-Z-[bUcszN8jRB8].mp4'))
        assert(os.path.exists('./tmp/Morning Dew  a bad lip reading of Bruno Mars, feat. Lady Gaga and Jay-Z-[bUcszN8jRB8].ssa'))
        assert(os.path.getsize('./tmp/Morning Dew — a bad lip reading of Bruno Mars, feat. Lady Gaga and Jay-Z-[bUcszN8jRB8].mp4') > 100)
        assert(os.path.getsize('./tmp/Morning Dew  a bad lip reading of Bruno Mars, feat. Lady Gaga and Jay-Z-[bUcszN8jRB8].ssa') > 100)

if __name__ == "__main__":
    nose.runmodule()
