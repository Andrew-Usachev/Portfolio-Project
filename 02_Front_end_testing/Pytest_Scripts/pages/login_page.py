from .base_page import BasePage
from Portfolio_front_end.src.locators import LoginPageLocators
from Portfolio_front_end.src.locators import MainPageLocators
from Portfolio_front_end.src.locators import HireTeamPageLocators
from Portfolio_front_end.src.locators import PersonalPageLocators
from Portfolio_front_end.src.locators import password
from Portfolio_front_end.src.locators import get_email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------
    # POSITIVE TESTS METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def should_be_verify_header_elements(self):
        self.print_method_name()
        self.is_element_present(MainPageLocators.HEADER_LOGO, "HEADER_LOGO")
        self.is_element_or_text_present(MainPageLocators.REGISTER_BTN, "Register")
        self.is_element_or_text_present(MainPageLocators.LOGIN_BTN, "Log in")

    def should_be_header_elements_clickable_and_enabled(self):
        self.print_method_name()
        self.is_element_clickable(MainPageLocators.HEADER_LOGO, "HEADER_LOGO")
        self.is_element_enabled(MainPageLocators.HEADER_LOGO, "HEADER_LOGO")
        self.is_element_clickable(MainPageLocators.REGISTER_BTN, "REGISTER_BTN")
        self.is_element_enabled(MainPageLocators.REGISTER_BTN, "REGISTER_BTN")
        self.is_element_clickable(MainPageLocators.LOGIN_BTN, "LOGIN_BTN")
        self.is_element_enabled(MainPageLocators.LOGIN_BTN, "LOGIN_BTN")

    def should_be_header_elements_have_correct_size_and_color(self):
        self.print_method_name()
        self.check_element_size(MainPageLocators.HEADER_LOGO, "HEADER_LOGO", 244, 73)
        self.check_element_size(MainPageLocators.REGISTER_BTN, "REGISTER_BTN", 120, 50)
        self.check_element_size(MainPageLocators.LOGIN_BTN, "LOGIN_BTN", 120, 50)
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
        self.browser.find_element(*LoginPageLocators.HOME_BTN).click()
        # Back page MainPage
        # return MainPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_page_body_elements(self):
        self.print_method_name()
        self.is_element_clickable(LoginPageLocators.HOME_BTN, "HOME_BTN")
        self.is_element_enabled(LoginPageLocators.HOME_BTN, "HOME_BTN")
        self.is_element_or_text_present(LoginPageLocators.HOME_BTN, "Home")
        self.is_element_or_text_present(LoginPageLocators.LOGIN_LEFT_TEXT, "Log in")
        self.is_element_or_text_present(LoginPageLocators.LOGIN_HEDING, "Log in")
        self.is_element_or_text_present(
            LoginPageLocators.AMAZING_DEVELOPERS_TEXT,
            "amazing developer's for startups",
        )
        self.is_element_or_text_present(LoginPageLocators.EMAIL_TEXT, "email")
        self.is_element_clickable(
            LoginPageLocators.INPUT_EMAIL_FORM, "INPUT_EMAIL_FORM"
        )
        self.is_element_enabled(LoginPageLocators.INPUT_EMAIL_FORM, "INPUT_EMAIL_FORM")
        self.is_element_or_text_present(
            LoginPageLocators.EXAMPLE_MAIL_TEXT, "for example: user@company.com"
        )
        self.is_element_or_text_present(LoginPageLocators.PASSWORD_TEXT, "password")
        self.is_element_clickable(
            LoginPageLocators.INPUT_PASSWORD_FORM, "INPUT_PASSWORD_FORM"
        )
        self.is_element_enabled(
            LoginPageLocators.INPUT_PASSWORD_FORM, "INPUT_PASSWORD_FORM"
        )
        self.is_element_or_text_present(
            LoginPageLocators.EXAMPLE_PASSWORD_TEXT, "for example: iddqd$!@#$"
        )
        self.is_element_or_text_present(
            LoginPageLocators.RECOVERY_PASSWORD_BTN, "Recovery password"
        )
        self.is_element_clickable(
            LoginPageLocators.RECOVERY_PASSWORD_BTN, "RECOVERY_PASSWORD_BTN"
        )
        self.is_element_enabled(
            LoginPageLocators.RECOVERY_PASSWORD_BTN, "RECOVERY_PASSWORD_BTN"
        )
        self.is_element_or_text_present(
            LoginPageLocators.LOGIN_BTN_LOGIN_PAGE, "Log in"
        )
        self.is_element_clickable(
            LoginPageLocators.LOGIN_BTN_LOGIN_PAGE, "LOGIN_BTN_LOGIN_PAGE"
        )
        self.is_element_enabled(
            LoginPageLocators.LOGIN_BTN_LOGIN_PAGE, "LOGIN_BTN_LOGIN_PAGE"
        )
        self.check_element_size(
            LoginPageLocators.LOGIN_BTN_LOGIN_PAGE, "LOGIN_BTN", 145, 57
        )
        self.is_css_property_value_have_correct_value(
            LoginPageLocators.LOGIN_BTN_LOGIN_PAGE,
            "LOGIN_BTN",
            "background-color",
            "rgba(255, 199, 0, 1)",
        )
        self.is_element_or_text_present(
            LoginPageLocators.REGISTER_BTN_LOGIN_PAGE, "Register"
        )
        self.is_element_clickable(
            LoginPageLocators.REGISTER_BTN_LOGIN_PAGE, "REGISTER_BTN_LOGIN_PAGE"
        )
        self.is_element_enabled(
            LoginPageLocators.REGISTER_BTN_LOGIN_PAGE, "REGISTER_BTN_LOGIN_PAGE"
        )

    def go_to_recovery_password_page(self):
        self.print_method_name()
        self.element_click(
            LoginPageLocators.RECOVERY_PASSWORD_BTN, "RECOVERY_PASSWORD_BTN"
        )
        # Back page RecoverPasswordPage
        # return RecoverPasswordPage(browser=self.browser, url=self.browser.current_url)

    def go_to_register_page_from_login_page(self):
        self.print_method_name()
        self.element_click(
            LoginPageLocators.REGISTER_BTN_LOGIN_PAGE, "REGISTER_BTN_LOGIN_PAGE"
        )
        # Back page RegisterPage
        # return RegisterPage(browser=self.browser, url=self.browser.current_url)

    def should_be_correct_user_logged_in(self):
        self.print_method_name()
        self.is_element_send_keys(
            LoginPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            get_email,
        )
        self.is_element_present(
            HireTeamPageLocators.VALIDATION_STATUS_OK_1, "VALIDATION_STATUS_OK_1"
        )
        self.check_element_size(
            HireTeamPageLocators.VALIDATION_STATUS_OK_1,
            "VALIDATION_STATUS_OK_1",
            34,
            25,
        )
        self.is_element_send_keys(
            LoginPageLocators.INPUT_PASSWORD_FORM,
            "INPUT_PASSWORD_FORM",
            password,
        )
        self.is_element_present(
            HireTeamPageLocators.VALIDATION_STATUS_OK_2, "VALIDATION_STATUS_OK_2"
        )
        self.check_element_size(
            HireTeamPageLocators.VALIDATION_STATUS_OK_2,
            "VALIDATION_STATUS_OK_2",
            34,
            25,
        )
        self.element_click(
            LoginPageLocators.LOGIN_BTN_LOGIN_PAGE, "LOGIN_BTN_LOGIN_PAGE"
        )
        wait = WebDriverWait(self.browser, 3)
        try:
            wait.until(EC.url_to_be(PersonalPageLocators.PERSONAL_PAGE_LINK))
            print(
                "\033[92mPass:\033[0m Login is successful. User is logged in with correct email and password"
            )
            return True
        except Exception:
            print(
                "\033[91mFail:\033[0m Login is not successful. User is not logged in with correct email and password"
            )
            self.print_problem("Method_if_not_and_else")

    # ------------------------------------------------------------------------------------------------------------------
    # NEGATIVE TEST METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def cant_go_to_personal_page_with_incorrect_data(
            self,
            input_email_form_send_data,
            validation_message_1_status,
            text_validation_message_1,
            input_password_form_send_data,
            validation_message_2_status,
            text_validation_message_2,
            validation_message_3_status,
            text_validation_message_3
    ):
        self.print_method_name()

        self.is_element_send_keys(
            LoginPageLocators.INPUT_EMAIL_FORM,
            "INPUT_EMAIL_FORM",
            input_email_form_send_data,
        )

        self.is_element_send_keys(
            LoginPageLocators.INPUT_PASSWORD_FORM,
            "INPUT_PASSWORD_FORM",
            input_password_form_send_data,
        )
        self.element_click(
            LoginPageLocators.LOGIN_BTN_LOGIN_PAGE, "LOGIN_BTN_LOGIN_PAGE"
        )
        if validation_message_1_status == "validation_message_1_ON":
            self.is_element_or_text_present(
                LoginPageLocators.VALIDATION_MESSAGE_1_LOGIN_PAGE, text_validation_message_1
            )
        else:
            pass
        if validation_message_2_status == "validation_message_2_ON":
            self.is_element_or_text_present(
                LoginPageLocators.VALIDATION_MESSAGE_2_LOGIN_PAGE, text_validation_message_2
            )
        else:
            pass
        if validation_message_3_status == "validation_message_3_ON":
            self.is_element_or_text_present(
                LoginPageLocators.VALIDATION_MESSAGE_3_LOGIN_PAGE, text_validation_message_3
            )
        else:
            pass

        wait = WebDriverWait(self.browser, 3)
        try:
            wait.until(EC.url_to_be(PersonalPageLocators.PERSONAL_PAGE_LINK))
            print("\033[91mFail:\033[0m It is possible - login with incorrect data")
            self.print_problem("Method_if_not_and_else")
        except Exception:
            print("\033[92mPass:\033[0m It is impossible - login with incorrect data")
            return True
