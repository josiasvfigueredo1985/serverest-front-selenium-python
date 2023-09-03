class metal_archives_page:
    """
    class name - Locates elements whose class name contains the search value
    (compound class names are not permitted)

    css selector - Locates elements matching a CSS selector

    id	- Locates elements whose ID attribute matches the search value

    name - Locates elements whose NAME attribute matches the search value

    link text -	Locates anchor elements whose visible text matches the search value

    partial link text -	Locates anchor elements whose visible text contains the search value.
    If multiple elements are matching, only the first one will be selected.

    tag name - Locates elements whose tag name matches the search value

    xpath -	Locates elements matching an XPath expression"""

    ########################################################################
    # Login Form
    # CSS Locators
    username = "[name=loginUsername]"
    password = "[name=loginPassword]"
    login_button = ".btn_login"
    # Link Text
    register_link = "Register"
    forgot_login_link = "Forgot login?"

    ########################################################################
    # Left Menu Box
    #### XPATH Locators ####
    # BANDS
    bands_alphabetical = "(//div[@id='left_menu_box']//child::ul/child::li/child::a)[1]"
    bands_country = "(//div[@id='left_menu_box']//child::ul/child::li/child::a)[2]"
    bands_genre = "(//div[@id='left_menu_box']//child::ul/child::li/child::a)[3]"
    # LABELS
    # Same approach as the XPATH bellow, "/*" ignore the tag name property
    labels_alphabetical = "(//div[@id='left_menu_box']/*/*/*/*)[1]"

    labels_country = "(//div[@id='left_menu_box']//child::ul/child::li/child::a)[5]"
    #### LINK TEXT Locators ####
    """
    Avoid to use Link Text locators, in this case, to use XPATH would be recommended.
    To use link text safely, be sure that there is only one element found by the text
    on the current page, use this same approach for all locators but id and data-test-id 
    (which is far the most recommended).
    """
    # REVIEWS
    reviews_link_text = "Reviews"

    # R.I.P
    rip_link_text = "R.I.P."

    # RANDOM BAND
    random_band_link_text = "Random Band"

    # USER RANKINGS
    user_rankings_link_text = "User rankings"

    # NEWS ARCHIVE
    news_archive_link_text = "News archive"

    # REPORTS
    reports_link_text = "Reports"

    # CONTRIBUTE/TO DO
    contribute_link_text = "Contribute / To do"

    # Privacy Policy link
    privacy_policy_link_text = "Privacy Policy"

    ########################################################################
    # Search Menu Box
    search_field_id = "searchQueryBox"
    advanced_search_link_text = "Advanced search"
    submit_button_class_name = ".btn_submit"
    select_combobox_name = "type"
    """
    For combobox and list, is recommended to use the locator from the whole element, instead of 
    a single element, that because after find elements inside the parent element is possible to
    interact with it is the same way a real user would do, also avoid to create 
    a single variable to each list option 
    """
    ########################################################################
    # Top Menu Box
    help_link_xpath = "//a[text()='Help']"
    rules_link_xpath = "//a[text()='Rules']"
    store_link_xpath = "//a[text()='Store']"
    forum_link_xpath = "//a[text()='Forum']"
    faq_link_xpath = "//a[text()='FAQ']"
    support_us_link_xpath = "//a[text()='Support Us']"
    addons_help_link_xpath = "//a[text()='Add-ons']"
    """
    Always prefer to use the element tag as identifier, in the case below the tag 'a' from href
    was provided to reach a better performance, that way the XPATH only will search for a single
    element type.
    """
    ########################################################################
    #### Advanced Search  #####
    # Search Bands
    search_bands_tab_css = ".ui-state-default #ui-id-1"
    band_name_css = "#bands #bandName"
    band_genre_css = "#bands #genre"
    country_type_css = "#bands .advancedSearchLeft .multiLink"
    country_selection_css = "#bands #country"
    year_formation_from_css = "#bands #yearCreationFrom"
    year_formation_to_css = "#bands #yearCreationTo"
    band_notes_css = "#bands #bandNotes"

    exact_match_check_css = "#bands #exactMatchBand"
    status_type_css = "#bands #link_status"
    status_selection_css = "#bands #status"
    themes_css = "#bands #themes"
    city_state_prov_css = "#bands #location"
    label_css = "#bands #bandLabelName"
    indie_label_check_css = "#bands #indieLabelBand"

    # Search Albums
    search_albums_tab_css = ".ui-state-default #ui-id-2"

    # Search Songs
    search_songs_tab_css = ".ui-state-default #ui-id-3"

    """
    Nested lookup is useful to identify when you may have the same id for the same field
    on different tabs or pages.
    In this case the id itself helps to identify which tab it belongs.
    In order to work properly, the call of the locators must be hierarchical
    Examples:
        <ol id="vegetables">
            <li class="potatoes">…
            <li class="onions">…
            <li class="tomatoes"><span>Tomato is a Vegetable</span>…
        </ol>
        <ul id="fruits">
            <li class="bananas">…
            <li class="apples">…
            <li class="tomatoes"><span>Tomato is a Fruit</span>…
        </ul>
    This works:
    "#vegetables .potatoes" -> vegetables comes first and then the class potatoes

    This not works:
    ".potatoes #vegetables" -> not following the hierarchy
    or
    "#fruits .potatoes" -> potatoes class is not inside the fruits list

    """
    # Your mappings go here :-)