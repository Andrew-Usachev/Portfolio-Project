from .base_page import BasePage
from Portfolio_front_end.src.locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
import requests
import os


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------
    # POSITIVE TESTS METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def should_be_verify_header_elements(self):
        self.print_method_name()
        self.is_element_present(MainPageLocators.HEADER_LOGO, "Header logo")
        self.is_element_or_text_present(
            MainPageLocators.DEVTEAMS_BTN, "Development teams"
        )
        self.is_element_or_text_present(MainPageLocators.HIRETEAM_BTN, "Hire team")
        self.is_element_or_text_present(MainPageLocators.HIREDEV_BTN, "Hire developers")
        self.is_element_or_text_present(MainPageLocators.BLOG_BTN, "Blog")
        self.is_element_or_text_present(MainPageLocators.REGISTER_BTN, "Register")
        self.is_element_or_text_present(MainPageLocators.LOGIN_BTN, "Log in")

    def should_be_header_elements_clickable_and_enabled(self):
        self.print_method_name()
        self.is_element_clickable(MainPageLocators.HEADER_LOGO, "HEADER_LOGO")
        self.is_element_enabled(MainPageLocators.HEADER_LOGO, "HEADER_LOGO")
        self.is_element_clickable(MainPageLocators.DEVTEAMS_BTN, "DEVTEAMS_BTN")
        self.is_element_enabled(MainPageLocators.DEVTEAMS_BTN, "DEVTEAMS_BTN")
        self.is_element_clickable(MainPageLocators.HIRETEAM_BTN, "HIRETEAM_BTN")
        self.is_element_enabled(MainPageLocators.HIRETEAM_BTN, "HIRETEAM_BTN")
        self.is_element_clickable(MainPageLocators.HIREDEV_BTN, "HIREDEV_BTN")
        self.is_element_enabled(MainPageLocators.HIREDEV_BTN, "HIREDEV_BTN")
        self.is_element_clickable(MainPageLocators.BLOG_BTN, "BLOG_BTN")
        self.is_element_enabled(MainPageLocators.BLOG_BTN, "BLOG_BTN")
        self.is_element_clickable(MainPageLocators.REGISTER_BTN, "REGISTER_BTN")
        self.is_element_enabled(MainPageLocators.REGISTER_BTN, "REGISTER_BTN")
        self.is_element_clickable(MainPageLocators.LOGIN_BTN, "LOGIN_BTN")
        self.is_element_enabled(MainPageLocators.LOGIN_BTN, "LOGIN_BTN")

    def should_be_header_elements_have_correct_size_and_color(self):
        self.print_method_name()
        self.check_element_size(MainPageLocators.HEADER_LOGO, "HEADER_LOGO", 244, 58)
        self.check_element_size(MainPageLocators.DEVTEAMS_BTN, "DEVTEAMS_BTN", 160, 32)
        self.check_element_size(MainPageLocators.HIRETEAM_BTN, "HIRETEAM_BTN", 133, 32)
        self.check_element_size(MainPageLocators.HIREDEV_BTN, "HIREDEV_BTN", 133, 32)
        self.check_element_size(MainPageLocators.BLOG_BTN, "BLOG_BTN", 72, 32)
        self.check_element_size(MainPageLocators.REGISTER_BTN, "REGISTER_BTN", 120, 50)
        self.check_element_size(MainPageLocators.LOGIN_BTN, "LOGIN_BTN", 120, 50)
        self.is_css_property_value_have_correct_value(
            MainPageLocators.DEVTEAMS_BTN,
            "DEVTEAMS_BTN",
            "background-color",
            "rgba(250, 199, 1, 1)",
        )
        self.is_css_property_value_have_correct_value(
            MainPageLocators.HIRETEAM_BTN,
            "HIRETEAM_BTN",
            "background-color",
            "rgba(247, 247, 247, 1)",
        )
        self.is_css_property_value_have_correct_value(
            MainPageLocators.HIREDEV_BTN,
            "HIREDEV_BTN",
            "background-color",
            "rgba(247, 247, 247, 1)",
        )
        self.is_css_property_value_have_correct_value(
            MainPageLocators.BLOG_BTN,
            "BLOG_BTN",
            "background-color",
            "rgba(247, 247, 247, 1)",
        )
        self.is_css_property_value_have_correct_value(
            MainPageLocators.REGISTER_BTN,
            "REGISTER_BTN",
            "background-color",
            "rgba(197, 74, 232, 1)",
        )
        self.is_css_property_value_have_correct_value(
            MainPageLocators.LOGIN_BTN,
            "LOGIN_BTN",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )

    def go_to_main_page(self):
        self.print_method_name()
        self.browser.get(self.url)
        # Back page MainPage
        # return MainPage(browser=self.browser, url=self.browser.current_url)

    def go_to_hireteam_page(self):
        self.print_method_name()
        self.browser.find_element(*MainPageLocators.HIRETEAM_BTN).click()
        # Back page Hireteam
        # return HireteamPage(browser=self.browser, url=self.browser.current_url)

    def go_to_hiredevelopers_page(self):
        self.print_method_name()
        self.browser.find_element(*MainPageLocators.HIREDEV_BTN).click()
        # Back page Hiredevelopers
        # return HiredevelopersPage(browser=self.browser, url=self.browser.current_url)

    def go_to_blog_page(self):
        self.print_method_name()
        self.browser.find_element(*MainPageLocators.BLOG_BTN).click()
        # Back page Blog
        # return BlogPage(browser=self.browser, url=self.browser.current_url)

    def go_to_register_page(self):
        self.print_method_name()
        self.browser.find_element(*MainPageLocators.REGISTER_BTN).click()
        # Back page Register
        # return RegisterPage(browser=self.browser, url=self.browser.current_url)

    def go_to_login_page(self):
        self.print_method_name()
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()
        # Back page Login
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_correct_heading_text(self):
        self.print_method_name()
        self.is_element_or_text_present(
            MainPageLocators.HEADING_1, "Select a development team for your project"
        )
        self.is_element_or_text_present(
            MainPageLocators.HEADING_2, "Popular\ndevelopment teams"
        )
        self.is_element_or_text_present(
            MainPageLocators.HEADING_3,
            "We understand\nhow to select a development team",
        )

    def should_be_animation_elements(self):
        self.print_method_name()
        self.is_element_animating(MainPageLocators.ANIMATION_ELEM_1, "ANIMATION_ELEM_1")
        self.is_element_animating(MainPageLocators.ANIMATION_ELEM_2, "ANIMATION_ELEM_2")

    def should_be_correct_width_height_in_animation_elements(self):
        self.print_method_name()
        self.check_element_size(
            MainPageLocators.ANIMATION_ELEM_1, "ANIMATION_ELEM_1", 420, 420
        )
        self.check_element_size(
            MainPageLocators.ANIMATION_ELEM_2, "ANIMATION_ELEM_2", 420, 315
        )

    def should_be_dropdown_menu_poject_type_in_main_page(self):
        self.print_method_name()
        self.is_element_or_text_present(MainPageLocators.PROJECT_TYPE, "Project type")
        self.is_element_present(
            MainPageLocators.DROPDOWN_PROJECT_TYPE, "DROPDOWN_PROJECT_TYPE"
        )
        self.is_attribute_present(
            MainPageLocators.DROPDOWN_PROJECT_TYPE, "DROPDOWN_PROJECT_TYPE", "value"
        )
        self.check_element_size(
            MainPageLocators.DROPDOWN_PROJECT_TYPE, "DROPDOWN_PROJECT_TYPE", 220, 40
        )
        self.is_css_property_value_have_correct_value(
            MainPageLocators.DROPDOWN_PROJECT_TYPE,
            "DROPDOWN_PROJECT_TYPE",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )

    def should_be_choose_mobile_app_value_in_list_of_the_popular_teams(self):
        self.print_method_name()
        self.select_element_by_value(
            MainPageLocators.DROPDOWN_PROJECT_TYPE,
            "DROPDOWN_PROJECT_TYPE",
            "1",
            "MOBILE APP",
        )

        if self.is_element_or_text_present(
                MainPageLocators.LIST_OF_THE_POPULAR_TEAMS_TEXT,
                "List of the Popular, Mobile app development teams",
        ):
            print(
                "\033[92mPass:\033[0m Chosen element 'Mobile app' in dropdown menu contain equal element 'Mobile app' in List of the Popular development teams"
            )
        else:
            print(
                "\033[91mFail:\033[0m Chosen element 'Mobile app' in dropdown menu not contain equal element 'Mobile app' in List of the Popular development teams",
            )

    def should_be_choose_landing_pages_value_in_list_of_the_popular_teams(self):
        self.print_method_name()
        self.select_element_by_value(
            MainPageLocators.DROPDOWN_PROJECT_TYPE,
            "DROPDOWN_PROJECT_TYPE",
            "2",
            "LANDING PAGES",
        )
        if self.is_element_or_text_present(
                MainPageLocators.LIST_OF_THE_POPULAR_TEAMS_TEXT,
                "List of the Popular, Landing pages development teams",
        ):
            print(
                "\033[92mPass:\033[0m Chosen element 'Landing pages' in dropdown menu contain equal element 'Landing pages' in List of the Popular development teams"
            )
        else:
            print(
                "\033[91mFail:\033[0m Chosen element 'Landing pages' in dropdown menu not contain equal element 'Landing pages' in List of the Popular development teams",
            )

    def should_be_choose_company_website_value_in_list_of_the_popular_teams(self):
        self.print_method_name()
        self.select_element_by_value(
            MainPageLocators.DROPDOWN_PROJECT_TYPE,
            "DROPDOWN_PROJECT_TYPE",
            "3",
            "COMPANY WEBSITE",
        )
        if self.is_element_or_text_present(
                MainPageLocators.LIST_OF_THE_POPULAR_TEAMS_TEXT,
                "List of the Popular, Company website development teams",
        ):
            print(
                "\033[92mPass:\033[0m Chosen element 'Company website' in dropdown menu contain equal element 'Company website' in List of the Popular development teams"
            )
        else:
            print(
                "\033[91mFail:\033[0m Chosen element 'Company website' in dropdown menu not contain equal element 'Company website' in List of the Popular development teams",
            )

    def should_be_choose_e_commerce_value_in_list_of_the_popular_teams(self):
        self.print_method_name()
        self.select_element_by_value(
            MainPageLocators.DROPDOWN_PROJECT_TYPE,
            "DROPDOWN_PROJECT_TYPE",
            "4",
            "E-COMMERCE",
        )
        if self.is_element_or_text_present(
                MainPageLocators.LIST_OF_THE_POPULAR_TEAMS_TEXT,
                "List of the Popular, E-commerce development teams",
        ):
            print(
                "\033[92mPass:\033[0m Chosen element 'E-commerce' in dropdown menu contain equal element 'E-commerce' in List of the Popular development teams"
            )
        else:
            print(
                "\033[91mFail:\033[0m Chosen element 'E-commerce' in dropdown menu not contain equal element 'E-commerce' in List of the Popular development teams",
            )

    def should_be_choose_web_app_value_in_list_of_the_popular_teams(self):
        self.print_method_name()
        self.select_element_by_value(
            MainPageLocators.DROPDOWN_PROJECT_TYPE,
            "DROPDOWN_PROJECT_TYPE",
            "5",
            "WEB APP",
        )
        if self.is_element_or_text_present(
                MainPageLocators.LIST_OF_THE_POPULAR_TEAMS_TEXT,
                "List of the Popular, Web app development teams",
        ):
            print(
                "\033[92mPass:\033[0m Chosen element 'Web app' in dropdown menu contain equal element 'Web app' in List of the Popular development teams"
            )
        else:
            print(
                "\033[91mFail:\033[0m Chosen element 'Web app' in dropdown menu not contain equal element 'Web app' in List of the Popular development teams",
            )

    def should_be_video(self):
        self.print_method_name()
        try:
            iframe_locator = (By.CSS_SELECTOR, "iframe[src*='youtube.com']")
            iframe = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(iframe_locator)
            )
            self.browser.switch_to.frame(iframe)
        except Exception:
            print(
                "\033[91mFail:\033[0m Сan't switch to iframe",
                "Error is:",
                sys.exc_info()[0],
            )

        self.is_element_video(MainPageLocators.VIDEO_ELEMENT, "VIDEO ELEMENT")
        self.check_element_size(
            MainPageLocators.VIDEO_ELEMENT, "VIDEO ELEMENT", 1099, 618
        )
        self.is_video_muted(MainPageLocators.VIDEO_ELEMENT, "VIDEO ELEMENT")
        self.is_video_duratation(MainPageLocators.VIDEO_ELEMENT, "VIDEO ELEMENT")
        self.browser.switch_to.default_content()

    def should_be_need_new_team_block_1(self):
        self.print_method_name()
        self.is_element_clickable(
            MainPageLocators.NEED_NEW_TEAM_BTN_1, "NEED_NEW_TEAM_BTN_1"
        )
        self.is_element_enabled(
            MainPageLocators.NEED_NEW_TEAM_BTN_1, "NEED_NEW_TEAM_BTN_1"
        )
        self.check_element_size(
            MainPageLocators.NEED_NEW_TEAM_BTN_1, "NEED_NEW_TEAM_BTN_1", 257, 58
        )
        self.is_element_or_text_present(
            MainPageLocators.DESCRIBE_YOUR_PROJECT_TEXT_1,
            "If you don't have time, describe your project to us, and we will select several teams suitable for your project.",
        )

    def should_be_need_new_team_block_2(self):
        self.print_method_name()
        self.is_element_clickable(
            MainPageLocators.NEED_NEW_TEAM_BTN_2, "NEED_NEW_TEAM_BTN_2"
        )
        self.is_element_enabled(
            MainPageLocators.NEED_NEW_TEAM_BTN_2, "NEED_NEW_TEAM_BTN_2"
        )
        self.check_element_size(
            MainPageLocators.NEED_NEW_TEAM_BTN_2, "NEED_NEW_TEAM_BTN_2", 257, 58
        )
        self.is_element_or_text_present(
            MainPageLocators.DESCRIBE_YOUR_PROJECT_TEXT_2,
            "If you don't have time, describe your project to us, and we will select several teams suitable for your project.",
        )

    def should_be_need_new_team_block_3(self):
        self.print_method_name()
        self.is_element_clickable(
            MainPageLocators.NEED_NEW_TEAM_BTN_3, "NEED_NEW_TEAM_BTN_3"
        )
        self.is_element_enabled(
            MainPageLocators.NEED_NEW_TEAM_BTN_3, "NEED_NEW_TEAM_BTN_3"
        )
        self.check_element_size(
            MainPageLocators.NEED_NEW_TEAM_BTN_3, "NEED_NEW_TEAM_BTN_3", 257, 58
        )
        self.is_element_or_text_present(
            MainPageLocators.DESCRIBE_YOUR_PROJECT_TEXT_3,
            "If you don't have time, describe your project to us, and we will select several teams suitable for your project.",
        )

    def should_be_sterling_low_banner_open(self):
        self.print_method_name()
        self.is_element_clickable(
            MainPageLocators.STERLING_LAW_BANNER, "STERLING_LOW_BANNER"
        )
        self.is_element_enabled(
            MainPageLocators.STERLING_LAW_BANNER, "STERLING_LOW_BANNER"
        )
        self.check_element_size(
            MainPageLocators.STERLING_LAW_BANNER, "STERLING_LOW_BANNER", 360, 360
        )
        if self.element_click(
                MainPageLocators.STERLING_LAW_BANNER,
                "STERLING_LOW_BANNER",
        ):
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.number_of_windows_to_be(2))
            self.browser.switch_to.window(self.browser.window_handles[1])
            print(f"\033[92mPass:\033[0m Sterling Law page is open")
            self.check_url("https://sterling-law.co.uk/")
            self.check_title("Law Firm London | Sterling Law | London Solicitors")
            self.check_API_status_code(200)
            print(f"\033[92mPass:\033[0m Sterling Law page is working")

            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])
            WebDriverWait(self.browser, 10)

        else:
            print(f"\033[91mFail:\033[0m Sterling Law page is not open")

    def should_be_download_checklist_banner(self):
        self.print_method_name()
        self.is_element_clickable(
            MainPageLocators.DOWNLOAD_CHECKLIST_BANNER, "DOWNLOAD_CHECKLIST_BANNER"
        )
        self.is_element_enabled(
            MainPageLocators.DOWNLOAD_CHECKLIST_BANNER, "DOWNLOAD_CHECKLIST_BANNER"
        )
        self.check_element_size(
            MainPageLocators.DOWNLOAD_CHECKLIST_BANNER,
            "DOWNLOAD_CHECKLIST_BANNER",
            706,
            360,
        )
        try:
            element = self.browser.find_element(
                *MainPageLocators.DOWNLOAD_CHECKLIST_BANNER
            )
            file_url = element.get_attribute("href")
            response = requests.get(file_url)
            if response.status_code == 200:
                folder_path = "download_files"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                file_path = os.path.join(folder_path, "ibench_teams_checklist.pdf")
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print("File saved correctly in the 'download_files' folder")
                return True
            else:
                print("File not saved")
                self.print_problem("Block_if")
        except Exception:
            self.print_problem("Block_try")
