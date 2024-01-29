from Portfolio_front_end.pages.main_page import MainPage

link = "https://ibench.net/"


class TestPositive:
    def test_check_header_elements(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_verify_header_elements()
        page.should_be_header_elements_clickable_and_enabled()
        page.should_be_header_elements_have_correct_size_and_color()
        page.check_fail_status()

    def test_header_elements_follow_to_right_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.go_to_hireteam_page()
        page.should_be_hireteam_page()
        page.go_to_main_page()
        page.should_be_main_page()
        page.go_to_hiredevelopers_page()
        page.should_be_hiredevelopers_page()
        page.go_to_main_page()
        page.should_be_main_page()
        page.go_to_blog_page()
        page.should_be_blog_page()
        page.go_to_main_page()
        page.should_be_main_page()
        page.go_to_register_page()
        page.should_be_register_page()
        page.go_to_main_page()
        page.should_be_main_page()
        page.go_to_login_page()
        page.should_be_login_page()
        page.go_to_main_page()
        page.should_be_main_page()
        page.check_fail_status()

    def test_check_text_headings(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_correct_heading_text()
        page.check_fail_status()

    def test_check_animation_elements(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_animation_elements()
        page.should_be_correct_width_height_in_animation_elements()
        page.check_fail_status()

    def test_check_dropdown_project_type(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_dropdown_menu_poject_type_in_main_page()
        page.should_be_choose_mobile_app_value_in_list_of_the_popular_teams()
        page.should_be_choose_landing_pages_value_in_list_of_the_popular_teams()
        page.should_be_choose_company_website_value_in_list_of_the_popular_teams()
        page.should_be_choose_e_commerce_value_in_list_of_the_popular_teams()
        page.should_be_choose_web_app_value_in_list_of_the_popular_teams()
        page.check_fail_status()

    def test_check_video(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_video()
        page.check_fail_status()

    def test_check_need_new_team_block(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_need_new_team_block_1()
        page.should_be_need_new_team_block_2()
        page.should_be_need_new_team_block_3()
        page.check_fail_status()

    def test_check_sterling_law_banner(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_sterling_low_banner_open()
        page.should_be_main_page()
        page.check_fail_status()

    def test_check_download_checklist_banner(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        page.should_be_download_checklist_banner()
        page.check_fail_status()
