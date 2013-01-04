import BaseTestCase
import nose

class TestYouTubeShowsScraper(BaseTestCase.BaseTestCase):

    def test_plugin_should_scrape_trailers_top_100_playlist_and_video_list(self):
        self.navigation.listMenu({"scraper": "trailers", "path": "/root/explore/trailers"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_thumbnails()
        self.assert_directory_should_have_next_folder()

if __name__ == "__main__":
    nose.runmodule()
