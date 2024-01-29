import time
from .base_page import BasePage
from Portfolio_front_end.src.locators import HireTeamPageLocators
from Portfolio_front_end.src.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class HireTeamPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(HireTeamPage, self).__init__(*args, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------
    # POSITIVE TESTS METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def should_be_header_elements_have_correct_size_and_color(self):
        self.print_method_name()
        self.check_element_size(MainPageLocators.HEADER_LOGO, "HEADER_LOGO", 244, 58)
        self.check_element_size(MainPageLocators.DEVTEAMS_BTN, "DEVTEAMS_BTN", 160, 32)
        self.check_element_size(MainPageLocators.HIRETEAM_BTN, "HIRETEAM_BTN", 133, 32)
        self.check_element_size(MainPageLocators.HIREDEV_BTN, "HIREDEV_BTN", 133, 32)
        self.check_element_size(MainPageLocators.BLOG_BTN, "BLOG_BTN", 72, 32)
        self.check_element_size(MainPageLocators.REGISTER_BTN, "REGISTER_BTN", 120, 50)
        self.check_element_size(MainPageLocators.LOGIN_BTN, "LOGIN_BTN", 120, 50)
        element = self.find_elem(MainPageLocators.DEVTEAMS_BTN)
        print(element.value_of_css_property("background-color"))
        element = self.find_elem(MainPageLocators.HIRETEAM_BTN)
        print(element.value_of_css_property("background-color"))
        self.is_css_property_value_have_correct_value(
            MainPageLocators.DEVTEAMS_BTN,
            "DEVTEAMS_BTN",
            "background-color",
            "rgba(247, 247, 247, 1)",
        )
        self.is_css_property_value_have_correct_value(
            MainPageLocators.HIRETEAM_BTN,
            "HIRETEAM_BTN",
            "background-color",
            "rgba(250, 199, 1, 1)",
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
        self.browser.find_element(*MainPageLocators.DEVTEAMS_BTN).click()
        # Back page MainPage
        # return MainPage(browser=self.browser, url=self.browser.current_url)

    def go_to_hireteam_page(self):
        self.print_method_name()
        self.browser.get(self.url)
        # Back page Hireteam
        # return HireteamPage(browser=self.browser, url=self.browser.current_url)

    def should_be_correct_heading_text(self):
        self.print_method_name()
        self.is_element_or_text_present(HireTeamPageLocators.HEADING, "Development team\nrequest form")

    def should_be_animation_elements(self):
        self.print_method_name()
        self.is_element_animating(HireTeamPageLocators.ANIMATION_ELEM, "ANIMATION_ELEM")

    def should_be_correct_width_height_in_animation_elements(self):
        self.print_method_name()
        self.check_element_size(HireTeamPageLocators.ANIMATION_ELEM, "ANIMATION_ELEM", 450, 337.5)

    def should_be_step_1_request_form(self):
        self.print_method_name()
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 1 of 5")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_1,
            "FORM_INDICATOR_1",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_2,
            "FORM_INDICATOR_2",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_3,
            "FORM_INDICATOR_3",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_4,
            "FORM_INDICATOR_4",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_5,
            "FORM_INDICATOR_5",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_element_clickable(HireTeamPageLocators.INPUT_NAME_FORM, "INPUT_NAME_FORM")
        self.is_element_enabled(HireTeamPageLocators.INPUT_NAME_FORM, "INPUT_NAME_FORM")
        self.is_element_clickable(HireTeamPageLocators.INPUT_EMAIL_FORM, "INPUT_EMAIL_FORM")
        self.is_element_enabled(HireTeamPageLocators.INPUT_EMAIL_FORM, "INPUT_EMAIL_FORM")
        self.is_element_present(HireTeamPageLocators.CHECKBOX_TRUE, "CHECKBOX_TRUE")
        self.is_element_or_text_present(HireTeamPageLocators.PRIVACY_POLICE, "Privacy Policy")
        self.is_element_clickable(HireTeamPageLocators.PRIVACY_POLICE, "PRIVACY_POLICE")
        self.is_element_or_text_present(HireTeamPageLocators.NEXT_STEP_BTN, "Next step")
        self.is_element_clickable(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "-webkit-appearance",
            "button",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )

    def should_be_fill_correctly_step_1(self):
        self.print_method_name()
        self.is_element_send_keys(HireTeamPageLocators.INPUT_NAME_FORM, "INPUT_NAME_FORM", Keys.ENTER)
        self.is_element_or_text_present(HireTeamPageLocators.VALIDATION_MESSAGE_1, "is required")
        self.is_element_send_keys(HireTeamPageLocators.INPUT_EMAIL_FORM, "INPUT_EMAIL_FORM", Keys.ENTER)
        self.is_element_or_text_present(HireTeamPageLocators.VALIDATION_MESSAGE_2, "is required")
        self.is_element_send_keys(HireTeamPageLocators.INPUT_EMAIL_FORM, "INPUT_EMAIL_FORM", "uncorrect email")
        self.is_element_or_text_present(
            HireTeamPageLocators.VALIDATION_MESSAGE_2,
            "is not a valid email",
        )

        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            Keys.CONTROL + "a",
        )
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            Keys.DELETE,
        )
        random_name = self.generate_random_string(8)
        self.is_element_send_keys(HireTeamPageLocators.INPUT_NAME_FORM, "INPUT_NAME_FORM", random_name)
        self.is_element_present(HireTeamPageLocators.VALIDATION_STATUS_OK_1, "VALIDATION_STATUS_OK_1")
        random_email = self.generate_random_email()
        self.is_element_send_keys(HireTeamPageLocators.INPUT_EMAIL_FORM, "INPUT_EMAIL_FORM", random_email)
        self.is_element_present(HireTeamPageLocators.VALIDATION_STATUS_OK_2, "VALIDATION_STATUS_OK_2")
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 2 of 5")

    def should_be_step_2_request_form(self):
        self.print_method_name()
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 2 of 5")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_1,
            "FORM_INDICATOR_1",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_2,
            "FORM_INDICATOR_2",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_3,
            "FORM_INDICATOR_3",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_4,
            "FORM_INDICATOR_4",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_5,
            "FORM_INDICATOR_5",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_element_enabled(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM")
        self.is_element_clickable(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM")
        self.is_property_have_correct_value(
            HireTeamPageLocators.INPUT_FORM,
            "INPUT_FORM",
            "role",
            "listbox",
        )
        self.is_element_clickable(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.is_element_enabled(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.is_property_have_correct_value(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON", "type", "button")
        self.is_element_or_text_present(HireTeamPageLocators.POPULAR_SEARCHES_TEXT, "Popular searches:")
        self.is_element_clickable(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.is_element_enabled(HireTeamPageLocators.FIRST_BTN, "BLOCKCHAINS_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.FIRST_BTN, "Blockchains")

        self.is_element_clickable(HireTeamPageLocators.SECOND_BTN, "SECOND_BTN")
        self.is_element_enabled(HireTeamPageLocators.SECOND_BTN, "SECOND_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.SECOND_BTN, "Mobile application")

        self.is_element_clickable(HireTeamPageLocators.THIRD_BTN, "THIRD_BTN")
        self.is_element_enabled(HireTeamPageLocators.THIRD_BTN, "THIRD_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.THIRD_BTN, "Web Development")

        self.is_element_or_text_present(HireTeamPageLocators.NEXT_STEP_BTN, "Next step")
        self.is_element_clickable(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_enabled(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "-webkit-appearance",
            "button",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )

    def should_be_fill_correctly_step_2(self):
        self.print_method_name()
        self.element_click(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.element_click(HireTeamPageLocators.PRODUCT_TYPE_ART, "PRODUCT_TYPE_ART")
        self.element_click(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.element_click(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.INPUT_ELEMENT_1, "Art ×")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.INPUT_ELEMENT_1,
            "INPUT_ELEMENT_1",
            "background-color",
            "rgba(152, 73, 234, 1)",
        )
        self.is_element_or_text_present(HireTeamPageLocators.INPUT_ELEMENT_2, "Blockchains ×")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.INPUT_ELEMENT_2,
            "INPUT_ELEMENT_2",
            "background-color",
            "rgba(152, 73, 234, 1)",
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 3 of 5")

    def should_be_step_3_request_form(self):
        self.print_method_name()
        self.is_element_or_text_present(HireTeamPageLocators.STEP_3_HEADING, "What skills\nare you looking for?")
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 3 of 5")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_1,
            "FORM_INDICATOR_1",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_2,
            "FORM_INDICATOR_2",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_3,
            "FORM_INDICATOR_3",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_4,
            "FORM_INDICATOR_4",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_5,
            "FORM_INDICATOR_5",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_element_enabled(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM")
        self.is_element_clickable(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM")
        self.is_property_have_correct_value(
            HireTeamPageLocators.INPUT_FORM,
            "INPUT_FORM",
            "role",
            "listbox",
        )
        self.is_element_clickable(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.is_element_enabled(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.is_property_have_correct_value(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON", "type", "button")
        self.is_element_or_text_present(HireTeamPageLocators.POPULAR_SEARCHES_TEXT, "Popular searches:")
        self.is_element_clickable(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.is_element_enabled(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.FIRST_BTN, "React.js")

        self.is_element_clickable(HireTeamPageLocators.SECOND_BTN, "SECOND_BTN")
        self.is_element_enabled(HireTeamPageLocators.SECOND_BTN, "SECOND_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.SECOND_BTN, "Angular")

        self.is_element_clickable(HireTeamPageLocators.THIRD_BTN, "THIRD_BTN")
        self.is_element_enabled(HireTeamPageLocators.THIRD_BTN, "THIRD_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.THIRD_BTN, "Node.js")

        self.is_element_or_text_present(HireTeamPageLocators.NEXT_STEP_BTN, "Next step")
        self.is_element_clickable(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_enabled(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "-webkit-appearance",
            "button",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )

    def should_be_fill_correctly_step_3(self):
        self.print_method_name()
        self.element_click(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.element_click(HireTeamPageLocators.SKILL_ACTION_SCRIPT, "SKILL_ACTION_SCRIPT")
        self.element_click(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.element_click(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.INPUT_ELEMENT_1, "ActionScript ×")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.INPUT_ELEMENT_1,
            "INPUT_ELEMENT_1",
            "background-color",
            "rgba(152, 73, 234, 1)",
        )
        self.is_element_or_text_present(HireTeamPageLocators.INPUT_ELEMENT_2, "React.js ×")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.INPUT_ELEMENT_2,
            "INPUT_ELEMENT_2",
            "background-color",
            "rgba(152, 73, 234, 1)",
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 4 of 5")

    def should_be_step_4_request_form(self):
        self.print_method_name()
        self.is_element_or_text_present(HireTeamPageLocators.STEP_4_HEADING, "What is your\nplanned monthly budget?")
        self.is_element_or_text_present(
            HireTeamPageLocators.STEP_4_TEXT,
            "Specify your monthly budget for this project.",
        )
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 4 of 5")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_1,
            "FORM_INDICATOR_1",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_2,
            "FORM_INDICATOR_2",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_3,
            "FORM_INDICATOR_3",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_4,
            "FORM_INDICATOR_4",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_5,
            "FORM_INDICATOR_5",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.is_element_clickable(HireTeamPageLocators.RADIO_BUTTON_1, "RADIO_BUTTON_1")
        self.is_element_clickable(HireTeamPageLocators.RADIO_BUTTON_2, "RADIO_BUTTON_2")
        self.is_element_clickable(HireTeamPageLocators.RADIO_BUTTON_3, "RADIO_BUTTON_3")
        self.is_element_enabled(HireTeamPageLocators.RADIO_BUTTON_1, "RADIO_BUTTON_1")
        self.is_element_enabled(HireTeamPageLocators.RADIO_BUTTON_2, "RADIO_BUTTON_2")
        self.is_element_enabled(HireTeamPageLocators.RADIO_BUTTON_3, "RADIO_BUTTON_3")
        self.check_element_size(HireTeamPageLocators.RADIO_BUTTON_1, "RADIO_BUTTON_1", 18, 18)
        self.check_element_size(HireTeamPageLocators.RADIO_BUTTON_2, "RADIO_BUTTON_2", 18, 18)
        self.check_element_size(HireTeamPageLocators.RADIO_BUTTON_3, "RADIO_BUTTON_3", 18, 18)
        self.is_element_or_text_present(HireTeamPageLocators.LESS_5000_TEXT, "Less than $5,000")
        self.is_element_or_text_present(HireTeamPageLocators.UP_TO_10000_TEXT, "Up to $10,000")
        self.is_element_or_text_present(HireTeamPageLocators.UP_TO_20000_TEXT, "Up to $20,000")
        self.is_element_or_text_present(HireTeamPageLocators.ONE_DEVELOPER_TEXT, "1 developer")
        self.is_element_or_text_present(HireTeamPageLocators.TWO_THREE_DEVELOPERS_TEXT, "2-3 developers")
        self.is_element_or_text_present(
            HireTeamPageLocators.TWO_DEVELOPERS_AND_UX_TEXT,
            "2 developers + UX/UI designer and QA engineer",
        )
        self.is_element_clickable(HireTeamPageLocators.TEXTAREA, "TEXTAREA")
        self.is_element_enabled(HireTeamPageLocators.TEXTAREA, "TEXTAREA")
        self.is_property_have_correct_value(
            HireTeamPageLocators.TEXTAREA,
            "TEXTAREA",
            "placeholder",
            "For example: A cross-functional team (developers, designers, project managers)",
        )
        self.is_element_or_text_present(HireTeamPageLocators.NEXT_STEP_BTN, "Next step")
        self.is_element_clickable(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_enabled(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "-webkit-appearance",
            "button",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )

    def should_be_fill_correctly_step_4(self):
        self.print_method_name()
        self.element_click(HireTeamPageLocators.RADIO_BUTTON_1, "RADIO_BUTTON_1")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_1,
            "RADIO_BUTTON_1",
            "border-color",
            "rgb(152, 73, 234)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_2,
            "RADIO_BUTTON_2",
            "border-color",
            "rgb(151, 151, 151)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_3,
            "RADIO_BUTTON_3",
            "border-color",
            "rgb(151, 151, 151)",
        )
        self.element_click(HireTeamPageLocators.RADIO_BUTTON_2, "RADIO_BUTTON_2")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_1,
            "RADIO_BUTTON_1",
            "border-color",
            "rgb(151, 151, 151)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_2,
            "RADIO_BUTTON_2",
            "border-color",
            "rgb(152, 73, 234)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_3,
            "RADIO_BUTTON_3",
            "border-color",
            "rgb(151, 151, 151)",
        )
        self.element_click(HireTeamPageLocators.RADIO_BUTTON_3, "RADIO_BUTTON_3")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_1,
            "RADIO_BUTTON_1",
            "border-color",
            "rgb(151, 151, 151)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_2,
            "RADIO_BUTTON_2",
            "border-color",
            "rgb(151, 151, 151)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.RADIO_BUTTON_3,
            "RADIO_BUTTON_3",
            "border-color",
            "rgb(152, 73, 234)",
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.VALIDATION_MESSAGE_STEP_4, "is required")
        random_text = self.generate_random_sentence(10)
        self.is_element_send_keys(HireTeamPageLocators.TEXTAREA, "TEXTAREA", random_text)
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.VALIDATION_STATUS_OK_STEP_4,
            "VALIDATION_STATUS_OK_STEP_4",
            "background",
            'rgba(0, 0, 0, 0) url("https://ibench.net/static/media/check.58f633ee.svg") no-repeat scroll 0% 0% / 34px 25px padding-box border-box',
        )
        self.check_element_size(
            HireTeamPageLocators.VALIDATION_STATUS_OK_STEP_4,
            "VALIDATION_STATUS_OK_STEP_4",
            34,
            25,
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 5 of 5")

    def should_be_step_5_request_form(self):
        self.print_method_name()
        self.is_element_or_text_present(HireTeamPageLocators.STEP, "Step 5 of 5")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_1,
            "FORM_INDICATOR_1",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_2,
            "FORM_INDICATOR_2",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_3,
            "FORM_INDICATOR_3",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_4,
            "FORM_INDICATOR_4",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.FORM_INDICATOR_5,
            "FORM_INDICATOR_5",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_element_clickable(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM")
        self.is_element_enabled(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM")
        self.is_property_have_correct_value(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM", "role", "listbox")
        self.is_property_have_correct_value(
            HireTeamPageLocators.INPUT_FORM,
            "INPUT_FORM",
            "placeholder",
            "How long do you need the developer?",
        )
        self.is_property_have_correct_value(HireTeamPageLocators.INPUT_FORM, "INPUT_FORM", "size", 36)
        self.is_element_clickable(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.is_element_enabled(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.is_property_have_correct_value(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON", "type", "button")
        self.is_element_or_text_present(HireTeamPageLocators.POPULAR_SEARCHES_TEXT, "Popular searches:")
        self.is_element_clickable(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.is_element_enabled(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.FIRST_BTN, "1 month")

        self.is_element_clickable(HireTeamPageLocators.SECOND_BTN, "SECOND_BTN")
        self.is_element_enabled(HireTeamPageLocators.SECOND_BTN, "SECOND_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.SECOND_BTN, "2 month")

        self.is_element_clickable(HireTeamPageLocators.THIRD_BTN, "THIRD_BTN")
        self.is_element_enabled(HireTeamPageLocators.THIRD_BTN, "THIRD_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.THIRD_BTN, "3 month")

        self.is_element_clickable(HireTeamPageLocators.TEXTAREA, "TEXTAREA")
        self.is_element_enabled(HireTeamPageLocators.TEXTAREA, "TEXTAREA")
        self.is_property_have_correct_value(
            HireTeamPageLocators.TEXTAREA,
            "TEXTAREA",
            "placeholder",
            "Do you have product specifications ready?",
        )
        self.is_element_or_text_present(HireTeamPageLocators.NEXT_STEP_BTN, "Next step")
        self.is_element_clickable(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_enabled(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "-webkit-appearance",
            "button",
        )
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.NEXT_STEP_BTN,
            "NEXT_STEP_BTN",
            "background-color",
            "rgba(66, 133, 244, 1)",
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.VALIDATION_MESSAGE_STEP_4, "is required")
        random_text = self.generate_random_sentence(10)
        self.is_element_send_keys(HireTeamPageLocators.TEXTAREA, "TEXTAREA", random_text)
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.VALIDATION_STATUS_OK_STEP_4,
            "VALIDATION_STATUS_OK_STEP_4",
            "background",
            'rgba(0, 0, 0, 0) url("https://ibench.net/static/media/check.58f633ee.svg") no-repeat scroll 0% 0% / 34px 25px padding-box border-box',
        )
        self.check_element_size(
            HireTeamPageLocators.VALIDATION_STATUS_OK_STEP_4,
            "VALIDATION_STATUS_OK_STEP_4",
            34,
            25,
        )

    def should_be_fill_correctly_step_5(self):
        self.print_method_name()
        self.element_click(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.element_click(HireTeamPageLocators.ONE_MONTH_CHOICE, "ONE_MONTH_CHOICE")
        self.element_click(HireTeamPageLocators.SELECT_BUTTON, "SELECT_BUTTON")
        self.is_element_or_text_present(HireTeamPageLocators.INPUT_ELEMENT_1, "1 month ×")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.INPUT_ELEMENT_1,
            "INPUT_ELEMENT_1",
            "background-color",
            "rgba(152, 73, 234, 1)",
        )
        self.element_click(HireTeamPageLocators.SECOND_BTN, "SECOND_BTN")
        self.is_element_or_text_present(HireTeamPageLocators.INPUT_ELEMENT_1, "2 month ×")
        self.is_css_property_value_have_correct_value(
            HireTeamPageLocators.INPUT_ELEMENT_1,
            "INPUT_ELEMENT_1",
            "background-color",
            "rgba(152, 73, 234, 1)",
        )

        self.is_element_clickable(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_enabled(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")

    def go_to_step_2_hireteam_page(self):
        self.print_method_name()
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_NAME_FORM,
            "INPUT_NAME_FORM",
            Faker().name(),
        )
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            Faker().email(),
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")

    def go_to_step_3_hireteam_page(self):
        self.print_method_name()
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_NAME_FORM,
            "INPUT_NAME_FORM",
            Faker().name(),
        )
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            Faker().email(),
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.element_click(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")

    def go_to_step_4_hireteam_page(self):
        self.print_method_name()
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_NAME_FORM,
            "INPUT_NAME_FORM",
            Faker().name(),
        )
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            Faker().email(),
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.element_click(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.element_click(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")

    def go_to_step_5_hireteam_page(self):
        self.print_method_name()
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_NAME_FORM,
            "INPUT_NAME_FORM",
            Faker().name(),
        )
        self.is_element_send_keys(
            HireTeamPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            Faker().email(),
        )
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.element_click(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.element_click(HireTeamPageLocators.FIRST_BTN, "FIRST_BTN")
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.element_click(HireTeamPageLocators.RADIO_BUTTON_1, "RADIO_BUTTON_1")
        self.is_element_send_keys(HireTeamPageLocators.TEXTAREA, "TEXTAREA", Faker().text())
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")

    # ------------------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTS METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def cant_go_to_next_step_with_incorrect_data(
            self,
            input_form_1_status,
            input_form_1_locator,
            input_form_1_send_data,
            input_form_2_status,
            input_form_2_locator,
            input_form_2_send_data,
            check_filter,
            privacy_status,
            budget_plan,
            textarea_status,
            textarea_text,
            locator_validation_message,
            text_validation_message,
            next_step_locator,
    ):
        self.print_method_name()
        if input_form_1_status == "Input_form_1_ON":
            self.is_element_send_keys(
                input_form_1_locator,
                "INPUT_FORM_1",
                input_form_1_send_data,
            )
        else:
            pass
        if check_filter == "Check_filter_ON":
            time.sleep(1)
            self.is_element_or_text_present(HireTeamPageLocators.NO_RESULTS_TEXT, "The filter returned no results")
            if self.is_property_present(
                    HireTeamPageLocators.INPUT_FORM,
                    "INPUT_FORM",
                    "placeholder",
            ):
                print("\033[92mPass:\033[0m It is impossible send to input form  incorrect data")
                # return True
            else:
                print("\033[91mFail:\033[0m It is possible send to input form incorrect data")
                self.print_problem("Method_if_not_and_else")
        else:
            pass

        if input_form_2_status == "Input_form_2_ON":
            self.is_element_send_keys(
                input_form_2_locator,
                "INPUT_FORM_2",
                input_form_2_send_data,
            )
        else:
            pass

        if privacy_status == "Privacy_OFF":
            self.empty_privacy_policy()
        else:
            pass
        if budget_plan == "Budget_ON":
            self.element_click(HireTeamPageLocators.RADIO_BUTTON_1, "RADIO_BUTTON_1")
        else:
            pass
        if textarea_status == "Textarea_ON":
            self.is_element_send_keys(HireTeamPageLocators.TEXTAREA, "TEXTAREA", textarea_text)
        else:
            pass
        self.element_click(HireTeamPageLocators.NEXT_STEP_BTN, "NEXT_STEP_BTN")
        self.is_element_or_text_present(locator_validation_message, text_validation_message)
        wait = WebDriverWait(self.browser, 3)
        try:
            wait.until(EC.presence_of_element_located(next_step_locator))
            print("\033[91mFail:\033[0m It is possible - go to the next step with incorrect data")
            self.print_problem("Method_if_not_and_else")
        except Exception:
            print("\033[92mPass:\033[0m It is impossible - go to the next step with incorrect data")
            return True

    def empty_privacy_policy(self):
        self.print_method_name()
        self.element_click(HireTeamPageLocators.CHECKBOX_BTN, "CHECKBOX_BTN")
        self.is_element_present(HireTeamPageLocators.CHECKBOX_FALSE, "CHECKBOX_FALSE")
        self.element_click(HireTeamPageLocators.FORM_INDICATOR_1, "FORM_INDICATOR_1")
        self.is_element_or_text_present(HireTeamPageLocators.VALIDATION_MESSAGE_MUST_BE_ACCEPTED, "must be accepted")
