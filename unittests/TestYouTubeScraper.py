# -*- coding: utf-8 -*-
import nose
import BaseTestCase
from mock import Mock, patch
import sys
from  YouTubeScraper import YouTubeScraper 

class TestYouTubeScraper(BaseTestCase.BaseTestCase):
    scraper = ""
    
    def setUp(self):
        super(self.__class__,self).setUp()
        sys.modules["__main__"].common.parseDOM.return_value = ["some_string","some_string","some_string"]
        sys.modules["__main__"].core._fetchPage.return_value = {"content":"some_content","status":200}
        sys.modules["__main__"].common.makeAscii.return_value = "some_ascii_string"
        sys.modules["__main__"].common.replaceHTMLCodes.return_value = "some_html_free_string"
        sys.modules["__main__"].utils.extractVID.return_value = ["some_id_1","some_id_2","some_id_3"]
        sys.modules["__main__"].language.return_value = "some_language_string %s"
        sys.modules["__main__"].common.stripTags.return_value = "some_tag_less_string"
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].cache.cacheFunction.return_value = (["some_cached_string"], 200)
        
        self.scraper = YouTubeScraper()
        self.scraper.createUrl = Mock()
        self.scraper.createUrl.return_value = "some_url"

    def test_searchDisco_should_call_createUrl_to_get_seach_url(self):
        
        self.scraper.searchDisco({"search":"some_search"})
        
        self.scraper.createUrl.assert_any_call({"search":"some_search"})

    def test_searchDisco_should_call_fetchPage_to_get_search_result(self):
        
        self.scraper.searchDisco({"search":"some_search"})
                
        sys.modules["__main__"].core._fetchPage.assert_any_call({"link":"some_url"})

    def test_searchDisco_should_call_listPlaylist_to_list_content(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"content":"some_content&v=some_video_id&list=some_mix_list&blablabla","status":200}
        sys.modules["__main__"].feeds.return_value = []

        self.scraper.searchDisco({"search":"some_search"})

        assert(sys.modules["__main__"].core._fetchPage.call_count == 1)
        sys.modules["__main__"].core._fetchPage.assert_any_call({"link":"some_url"})

    def test_searchDisco_should_return_list_of_dictionaries_with_video_information(self):
        sys.modules["__main__"].common.parseDOM.return_value = ["some_id_1,some_id_2,some_id_3"]
        sys.modules["__main__"].core._fetchPage.return_value = {"content":"some_content&v=some_video_id&list=some_mix_list&blablabla","status":200}
        sys.modules["__main__"].feeds.listPlaylist.return_value = [{"videoid":"some_id_1"},{"videoid":"some_id_2"},{"videoid":"some_id_3"}]
        
        result = self.scraper.searchDisco({"search":"some_search"})
        
        assert(result[0]["videoid"] == "some_id_1")
        assert(result[1]["videoid"] == "some_id_2")
        assert(result[2]["videoid"] == "some_id_3")

    def test_scrapeUserLikedVideos_should_call_createUrl_to_get_proper_url(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"content":"some_content_&p=some_playlist&_blabal", "status":200}
        sys.modules["__main__"].common.parseDOM.return_value = ["a=1&list=list1&b=2"]

        self.scraper.scrapeUserLikedVideos({})
        
        self.scraper.createUrl.assert_any_call({})

    def test_scrapeUserLikedVideos_should_call_core_fetchPage_to_get_page_content(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"content":"some_content_&p=some_playlist&_blabal", "status":200}
        sys.modules["__main__"].common.parseDOM.return_value = ["a=1&list=list1&b=2"]
        
        self.scraper.scrapeUserLikedVideos({})
        
        sys.modules["__main__"].core._fetchPage.assert_any_call({"link":"some_url","login":"true"})

    def test_scrapeUserLikedVideos_should_call_parseDOM_to_find_playlist(self):
        sys.modules["__main__"].core._fetchPage.return_value = {"content":"some_content_&p=some_playlist&_blabal", "status":200}
        sys.modules["__main__"].common.parseDOM.return_value = ["a=1&list=list1&b=2"]
        
        self.scraper.scrapeUserLikedVideos({})
        
        assert(sys.modules["__main__"].common.parseDOM.call_count > 0)

    def test_scrapeYouTubeTop100_should_call_createUrl_to_get_proper_url(self):
        self.scraper.scrapeYouTubeTop100({})        
        
        self.scraper.createUrl.assert_any_call({})

    def test_scrapeYouTubeTop100_should_call_fetchPage_to_get_page_content(self):
        self.scraper.scrapeYouTubeTop100({})        
        
        sys.modules["__main__"].core._fetchPage.assert_any_call({"link":"some_url"})
        
    def test_scrapeYouTubeTop100_should_call_parseDOM_to_find_video_elements(self):        
        
        self.scraper.scrapeYouTubeTop100({})        
        
        assert(sys.modules["__main__"].common.parseDOM.call_count > 0)
                
    def test_scrapeYouTubeTop100_should_return_list_of_video_ids(self):
        sys.modules["__main__"].common.parseDOM.return_value = ["some_id_1","some_id_2","some_id_3"]
        
        result , status = self.scraper.scrapeYouTubeTop100({})        
        
        assert(result[0] == "some_id_1")
        assert(result[1] == "some_id_2")
        assert(result[2] == "some_id_3")

    def test_getNewResultsFunction_should_set_proper_params_for_searchDisco_if_scraper_is_search_diso(self):
        params = {"scraper":"search_disco"}
        
        self.scraper.getNewResultsFunction(params)
        
        assert(params["new_results_function"] == self.scraper.searchDisco)

    def test_getNewResultsFunction_should_set_proper_params_for_scrapeUserVideoFeed_if_scraper_is_liked_videos(self):
        params = {"scraper":"liked_videos"}
        
        self.scraper.getNewResultsFunction(params)
        
        assert(params["new_results_function"] == self.scraper.scrapeUserLikedVideos)

    def test_getNewResultsFunction_should_set_proper_params_for_scrapeYouTubeTop100_if_scraper_is_music_top100(self):
        params = {"scraper":"music_top100"}
        
        self.scraper.getNewResultsFunction(params)
        
        assert(params["batch"] == "true")
        assert(params["new_results_function"] == self.scraper.scrapeYouTubeTop100)

    def test_createUrl_should_return_proper_url_for_music_top_100(self):
        self.scraper = YouTubeScraper()
        
        url = self.scraper.createUrl({"scraper":"music_top100"})

        assert(url == self.scraper.urls["disco_main"])

    def test_createUrl_should_return_proper_url_for_search_disco(self):
        self.scraper = YouTubeScraper()
        
        url = self.scraper.createUrl({"scraper":"search_disco", "search":"some_search"})
        
        assert(url == self.scraper.urls["disco_search"] % "some_search")

    def test_paginator_should_call_cache_function_with_pointer_to_new_results_function_if_scraper_is_not_show(self):
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer"})
        
        sys.modules["__main__"].cache.cacheFunction.assert_called_with("some_function_pointer",{"scraper":"some_scraper","new_results_function":"some_function_pointer"})

    def test_paginator_should_call_new_results_function_pointer_if_scraper_is_show_and_show_is_in_params(self):
        self.scraper.scrapeShow = Mock()
        self.scraper.scrapeShow.return_value = (["some_string"],200)
        params = {"scraper":"show","new_results_function":self.scraper.scrapeShow, "show":"some_show"}

        result, status = self.scraper.paginator(params)
        
        sys.modules["__main__"].cache.cacheFunction.assert_called_with(self.scraper.scrapeShow,params)

    def test_paginator_should_return_error_if_no_results_are_found(self):
        sys.modules["__main__"].cache.cacheFunction.return_value = ([],303)
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer"})
        
        assert(status == 303)
        assert(result == [])
        
    def test_paginator_should_not_return_error_when_no_results_are_found_if_scraper_is_youtube_top100(self):
        sys.modules["__main__"].storage.retrieve.return_value = ["some_store_value"]
        sys.modules["__main__"].cache.cacheFunction.return_value = ([],303)
        
        result, status = self.scraper.paginator({"scraper":"music_top100","new_results_function":"some_function_pointer"})
        
        assert(status == 200)
        assert(result == ["some_store_value"])

    def test_paginator_should_call_storage_retrieve_when_no_results_are_found_if_scraper_is_youtube_top100(self):
        sys.modules["__main__"].storage.retrieve.return_value = ["some_store_value"]
        sys.modules["__main__"].cache.cacheFunction.return_value = ([],303)
        
        result, status = self.scraper.paginator({"scraper":"music_top100","new_results_function":"some_function_pointer"})
        
        assert(sys.modules["__main__"].storage.retrieve.call_count > 0)
            
    def test_paginator_should_call_getBatchDetailsThumbnails_if_batch_is_thumbnails(self):
        sys.modules["__main__"].core.getBatchDetailsThumbnails.return_value = ([],200)
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer", "batch":"thumbnails"})
        
        assert(sys.modules["__main__"].core.getBatchDetailsThumbnails.call_count > 0)
        
    def test_paginator_should_call_getBatchDetails_if_batch_is_set_but_not_thumbnails(self):
        sys.modules["__main__"].core.getBatchDetails.return_value = ([],200)
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer", "batch":"true"})
        
        assert(sys.modules["__main__"].core.getBatchDetails.call_count > 0)
        
    def test_paginator_should_call_utils_addNextFolder_if_item_list_is_longer_than_per_page_count(self):
        sys.modules["__main__"].core.getBatchDetails.return_value = ([],200)
        videos = []
        i = 0
        while i < 50:
            videos.append("some_cached_string_" + str(i))
            i += 1
            
        sys.modules["__main__"].cache.cacheFunction.return_value = (videos, 200)
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer", "batch":"true"})
        
        assert(sys.modules["__main__"].utils.addNextFolder.call_count > 0)
        
    def test_paginator_should_store_thumbnail_if_scraper_is_search_disco(self):
        sys.modules["__main__"].cache.cacheFunction.return_value = ([{"thumbnail":"some_cached_string"}], 200)
        
        result, status = self.scraper.paginator({"scraper":"search_disco","new_results_function":"some_function_pointer"})
        
        sys.modules["__main__"].storage.store.assert_called_with({'new_results_function': 'some_function_pointer', 'scraper': 'search_disco'}, 'some_cached_string', 'thumbnail')

    def test_paginator_should_limit_list_length_if_its_longer_than_perpage(self):
        videos = []
        i = 0
        while i < 50:
            videos.append("some_cached_string_" + str(i))
            i += 1
            
        sys.modules["__main__"].cache.cacheFunction.return_value = (videos, 200)
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer"})
        
        assert(len(result) == 15)
        
    def test_paginator_should_not_limit_list_length_if_fetch_all_is_set(self):
        videos = []
        i = 0
        while i < 50:
            videos.append("some_cached_string_" + str(i))
            i += 1
            
        sys.modules["__main__"].cache.cacheFunction.return_value = (videos, 200)
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer","fetch_all":"true"})
        
        assert(len(result) == 50)
    
    def test_paginator_should_begin_list_at_correct_count_if_page_is_set(self):
        videos = []
        i = 0
        while i < 50:
            videos.append("some_cached_string_" + str(i))
            i += 1
            
        sys.modules["__main__"].cache.cacheFunction.return_value = (videos, 200)
        
        result, status = self.scraper.paginator({"scraper":"some_scraper","new_results_function":"some_function_pointer","page":"1"})
        
        assert(result[0] == "some_cached_string_15")
        assert(result[14] == "some_cached_string_29")
            
    def test_scrape_should_call_getNewResultsFunction(self):
        self.scraper.getNewResultsFunction = Mock()
        self.scraper.paginator = Mock()
        
        self.scraper.scrape()
        
        self.scraper.getNewResultsFunction.assert_called_with({})

    def test_scrape_should_call_paginator(self):
        self.scraper.getNewResultsFunction = Mock()
        self.scraper.paginator = Mock()
        
        self.scraper.scrape()
        
        self.scraper.paginator.assert_called_with({})
        
if __name__ == '__main__':
    nose.runmodule()
