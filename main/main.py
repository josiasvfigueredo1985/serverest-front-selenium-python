from selenium_utils.seleniumutils import utils
from pages.metalarchivespage import metal_archives_page


class main(utils, metal_archives_page):
    def click_checkboxes_and_tabs(self):
        # Click Advanced Search link
        self.click_element(self.By.LINK_TEXT, self.advanced_search_link_text)

        # Mark the "Exact match?" checkbox
        self.click_element(self.By.CSS_SELECTOR, self.exact_match_check_css)

        # Mark the "Indie?" checkbox
        self.click_element(self.By.CSS_SELECTOR, self.indie_label_check_css)

        # Click the "Search Albums" tab
        self.click_element(self.By.CSS_SELECTOR, self.search_albums_tab_css)

        # Click the "Search Songs" tab
        self.click_element(self.By.CSS_SELECTOR, self.search_songs_tab_css)
        self.Close()

    def print_all_the_countries_from_combobox(self):
        # Click Advanced Search link
        self.click_element(self.By.LINK_TEXT, self.advanced_search_link_text)

        # Get all elements from country combo box
        countries = self.get_single_element(
            self.By.CSS_SELECTOR, self.country_selection_css
        )
        # Click each country
        for country in countries:
            self.click_element(self.By.XPATH, "//*[text()='" + country + "]")

        self.Close()


main_instance = main()
main_instance.click_checkboxes_and_tabs()
# main_instance.print_all_the_countries_from_combobox()
