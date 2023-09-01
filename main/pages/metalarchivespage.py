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
