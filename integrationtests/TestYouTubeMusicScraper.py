import BaseTestCase
import nose


class TestYouTubeMusicScraper(BaseTestCase.BaseTestCase):

    def test_plugin_should_scrape_youtube_top_100_video_list_correctly(self):
        self.navigation.listMenu({"scraper": "music_top100", "path": "/root/explore/music/top100"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_thumbnails()

if __name__ == "__main__":
    nose.runmodule()
