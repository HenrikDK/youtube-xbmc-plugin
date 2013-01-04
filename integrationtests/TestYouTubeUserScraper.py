import BaseTestCase
import nose
import sys


class TestYouTubeUserScraper(BaseTestCase.BaseTestCase):
    def test_plugin_should_scrape_liked_videos_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"scraper": "liked_videos", 'login': 'true', "path": "/root/liked_videos"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

if __name__ == "__main__":
    nose.runmodule()
