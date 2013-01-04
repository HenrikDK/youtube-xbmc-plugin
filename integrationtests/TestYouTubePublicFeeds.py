import BaseTestCase
import nose


class TestYouTubePublicFeedsScraper(BaseTestCase.BaseTestCase):
    def test_plugin_should_list_categories_folder_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_categories", "path": "/root/explore/categories", "folder": "true"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_folder_list()
        self.assert_directory_item_urls_contain("category")

    def test_plugin_should_list_category_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_category", "path": "/root/explore/categories", "category": "Comedy"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_category_video_list_page_2_correctly(self):
        self.navigation.listMenu({"feed": "feed_category", "path": "/root/explore/categories", "category": "Comedy", "page": "1"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_live_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_live", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_thumbnails()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_most_viewed_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_viewed", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_most_linked_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_linked", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(20)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_most_recent_videos_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_recent", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_most_responded_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_responded", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_most_share_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_shared", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_top_featured_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_featured", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(20)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_trending_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_trending", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_top_favorited_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_favorites", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_top_rated_video_list_correctly(self):
        self.navigation.listMenu({"feed": "feed_rated", "path": "/root/explore/movies"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_search_video_list_correctly(self):
        self.navigation.listMenu({"feed": "search", "search": "Star Craft 2", "path": "/root/favorites"})

        self.assert_directory_count_greater_than_or_equals(30)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_related_video_list_correctly(self):
        self.navigation.listMenu({"feed": "related", "videoid": "byv-wpqDydI", "path": "/root/favorites"})

        self.assert_directory_count_greater_than_or_equals(20)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

if __name__ == "__main__":
    nose.runmodule()
