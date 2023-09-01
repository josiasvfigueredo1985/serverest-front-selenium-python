from selenium_utils.seleniumutils import utils
from pages.metalarchivespage import metal_archives_page


class main(utils, metal_archives_page):
    Close = utils.Driver

    def click_checkboxes_and_tabs(self):
        """
        Use example for the locators assigned to variables
        """
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
        self.Close.quit()

    def print_all_the_countries_from_combobox(self):
        """
        This approach allows to get elements from an specif list element, using loops to run through the 
        element tree, only recommended if there´s a scenario where the element have no option to get all the elements
        with a single method
        """
        # Click Advanced Search link
        self.click_element(self.By.LINK_TEXT, self.advanced_search_link_text)

        # Get all elements from country combo box
        # countries_elements store all the elements from the list of country
        countries_elements = self.get_multiple_elements(
            self.By.CSS_SELECTOR, self.country_selection_css
        )
        # Now the loop will fetch each element that contains the country info
        for country_elements in countries_elements:
            # country_element stores the specific info inside each country
            country_element = country_elements.find_elements(
                self.By.TAG_NAME, "option")
            for country in country_element:
                print(country.text + "---" + country.get_attribute("value"))
                atr = country.get_attribute("value")
                # Click each country
                self.click_element(self.By.XPATH, f"//option[@value='{atr}']")

        self.Close.quit()

    def get_all_elements_from_combobox_list(self):
        """
        Nested locators are useful to fetch elements and make it unique for interaction
        #bands -> the id from the Search Bands tab, present only for that specific tab
        .countrySelect -> combo box class, is present on the Search Albums tab too
        * used to fetch all the elements that corresponds to the css selector
        In short, using a tab id and the class, the selector becomes unique, then with 
        "*" we can fetch all the data from the combo box class
        """
        # Click Advanced Search link
        self.click_element(self.By.LINK_TEXT, self.advanced_search_link_text)
        # Store all the elements from the combo box class
        # The following locator parameter is informed as string to be easy to understand
        # In a real scenario is recommended assign to a variable
        countries = self.get_multiple_elements(
            self.By.CSS_SELECTOR, "#bands .countrySelect *")
        # loop inside the element list
        for country in countries:
            # Due the use of the nested css selector, we can access the element attribute "text"
            # and all the available attributes
            print(country.text)
            atr = country.get_attribute("value")
            # Click each country
            if (atr):
                self.click_element(self.By.XPATH, f"//option[@value='{atr}']")
        self.Close.quit()


main_instance = main()
# main_instance.click_checkboxes_and_tabs()
# main_instance.print_all_the_countries_from_combobox()
main_instance.get_all_elements_from_combobox_list()
