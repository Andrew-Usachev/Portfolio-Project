'''
This file contains the locators for the test data.
'''

from selenium.webdriver.common.by import By
import requests
import json
from faker import Faker
from Portfolio_front_end.src.builders import LoginBodyBuilder

password = 'Password1234'

REGISTER_BODY = LoginBodyBuilder().with_email(Faker().email()).with_password(password).with_country(
    'Canada').with_terms_accepted(1).with_type(2).with_company_name(Faker().company()).build()

response = requests.post("https://ibench.net/api/auth/register", REGISTER_BODY)
response_json = json.loads(response.content)
get_email = response_json['user']['email']


class MainPageLocators:
    HEADER_LOGO = (
        By.CSS_SELECTOR,
        "div#root a > img",
    )
    DEVTEAMS_BTN = (
        By.CSS_SELECTOR,
        "ul[class='Navigation_menu__Xg4DA'] > li:nth-child(1) > a",
    )
    HIRETEAM_BTN = (
        By.CSS_SELECTOR,
        "ul[class='Navigation_menu__Xg4DA'] > li:nth-child(2) > a[href='/team-search']",
    )
    HIREDEV_BTN = (
        By.CSS_SELECTOR,
        "ul[class='Navigation_menu__Xg4DA'] > li:nth-child(3) > a[href='/hire-developers']",
    )
    BLOG_BTN = (
        By.CSS_SELECTOR,
        "ul[class='Navigation_menu__Xg4DA'] > li:nth-child(4) > a[href='https://ibench.net/blog/']",
    )
    REGISTER_BTN = (
        By.CSS_SELECTOR,
        "div[class='Navigation_auth_buttons__29gW3 mobile_hidden']  > a[href='/registration']",
    )
    LOGIN_BTN = (
        By.CSS_SELECTOR,
        "div[class='Navigation_auth_buttons__29gW3 mobile_hidden']  > a:nth-child(2)[href='/login']",
    )

    HEADING_1 = (By.CSS_SELECTOR, "h1.FrontPage_title__2VL4j")
    HEADING_2 = (By.CSS_SELECTOR, "h2.FrontPage_title__2VL4j")
    HEADING_3 = (
        By.CSS_SELECTOR,
        "h2[class='FrontPage_title__2VL4j FrontPage_understand__Kalm-']",
    )

    ANIMATION_ELEM_1 = (
        By.CSS_SELECTOR,
        "div.FrontPage_calculatorWrapper__3czVW > div > div > svg[width='1080']",
    )
    ANIMATION_ELEM_2 = (
        By.CSS_SELECTOR,
        "div.FrontPage_calculatorWrapper__3czVW > div > div > svg[width='800']",
    )

    PROJECT_TYPE = (
        By.CSS_SELECTOR,
        "div.FrontPage_leftColumn__1RvWJ > div.dropdown_id_name_wrapper.FrontPage_select__24Mqv > label",
    )

    DROPDOWN_PROJECT_TYPE = (
        By.CSS_SELECTOR,
        "div.FrontPage_leftColumn__1RvWJ > div.dropdown_id_name_wrapper.FrontPage_select__24Mqv > select",
    )

    LIST_OF_THE_POPULAR_TEAMS_TEXT = (
        By.CSS_SELECTOR,
        "div.FrontPage_list_title__2znwz > h3",
    )

    VIDEO_ELEMENT = (
        By.CSS_SELECTOR,
        "div#player > div > div.html5-video-container > video",
    )

    NEED_NEW_TEAM_BTN_1 = (
        By.CSS_SELECTOR,
        "div:nth-child(1) > div.FrontPage_topForm__1SmZh > div.FrontPage_mobileButtons__gPE5i > a > img[alt='I need a new team']",
    )

    NEED_NEW_TEAM_BTN_2 = (
        By.CSS_SELECTOR,
        "div:nth-child(1) > div.FrontPage_mobileButtons__gPE5i > a[href='/team-search'] > img[alt='I need a new team']",
    )

    NEED_NEW_TEAM_BTN_3 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(4) > div:nth-child(5) > div.FrontPage_mobileButtons__gPE5i > a[href='/team-search'] > img[alt='I need a new team']",
    )

    DESCRIBE_YOUR_PROJECT_TEXT_1 = (
        By.CSS_SELECTOR,
        "div:nth-child(1) > div.FrontPage_topForm__1SmZh > div.FrontPage_describeProject__Fw0E3",
    )

    DESCRIBE_YOUR_PROJECT_TEXT_2 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(1) > div.FrontPage_describeProject__Fw0E3",
    )

    DESCRIBE_YOUR_PROJECT_TEXT_3 = (
        By.CSS_SELECTOR,
        "div:nth-child(5) > div.FrontPage_describeProject__Fw0E3",
    )

    STERLING_LAW_BANNER = (
        By.CSS_SELECTOR,
        "div.FrontPage_bannersBlock__o-BQo > a[href='https://sterling-law.co.uk/'] > img[src='/static/media/banner.df63f069.png']",
    )

    DOWNLOAD_CHECKLIST_BANNER = (
        By.CSS_SELECTOR,
        "a.FrontPage_downloadPDFLink__1CqSg[href]",
    )


class HireTeamPageLocators:
    HEADING = (
        By.CSS_SELECTOR,
        "h1.TeamSearch_desktopTitle__225_G",
    )

    ANIMATION_ELEM = (
        By.CSS_SELECTOR,
        "div.TeamSearch_animationWrapper__2LSdj  > div > svg[width='800']",
    )

    STEP = (By.CSS_SELECTOR, "div#root div.FormIndicator_title__1ouH0")

    FORM_INDICATOR_1 = (
        By.CSS_SELECTOR,
        "div#root div.FormIndicator_indicator__o2nyB > div:nth-child(1)",
    )
    FORM_INDICATOR_2 = (
        By.CSS_SELECTOR,
        "div#root div.FormIndicator_indicator__o2nyB > div:nth-child(2)",
    )
    FORM_INDICATOR_3 = (
        By.CSS_SELECTOR,
        "div#root div.FormIndicator_indicator__o2nyB > div:nth-child(3)",
    )
    FORM_INDICATOR_4 = (
        By.CSS_SELECTOR,
        "div#root div.FormIndicator_indicator__o2nyB > div:nth-child(4)",
    )
    FORM_INDICATOR_5 = (
        By.CSS_SELECTOR,
        "div#root div.FormIndicator_indicator__o2nyB > div:nth-child(5)",
    )
    INPUT_NAME_FORM = (
        By.CSS_SELECTOR,
        "div.form_group.undefined.form_control_2_wrapper > div > input[placeholder='Name']",
    )
    INPUT_EMAIL_FORM = (
        By.CSS_SELECTOR,
        "div.form_group.undefined.form_control_2_wrapper > div > input[placeholder='Work email address']",
    )

    VALIDATION_MESSAGE_1 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(1) > div.validation_message",
    )
    VALIDATION_MESSAGE_2 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(2) > div.validation_message",
    )
    VALIDATION_MESSAGE_3 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(3) > div.validation_message",
    )

    VALIDATION_MESSAGE_MUST_BE_ACCEPTED = (
        By.CSS_SELECTOR,
        "div#root form > div:nth-child(2) > div:nth-child(3) > div",
    )

    VALIDATION_STATUS_OK_1 = (By.CSS_SELECTOR, "div#root div:nth-child(1) > span")
    VALIDATION_STATUS_OK_2 = (By.CSS_SELECTOR, "div#root div:nth-child(2) > span")
    CHECKBOX_TRUE = (
        By.CSS_SELECTOR,
        "div.form_group.undefined.undefined.undefined > label > input[value='true']",
    )
    CHECKBOX_FALSE = (
        By.CSS_SELECTOR,
        "div.form_group.undefined.undefined.undefined > label > input[value='false']",
    )
    CHECKBOX_BTN = (
        By.CSS_SELECTOR,
        "div.form_group.undefined.undefined.undefined > label > input + span",
    )

    PRIVACY_AGREEMENT_TEXT = (By.CSS_SELECTOR, "div#root label")
    PRIVACY_POLICE = (By.CSS_SELECTOR, "div#root label > a[href = '/privacy-policy'] ")
    NEXT_STEP_BTN = (
        By.CSS_SELECTOR,
        "div#root button.TeamSearch_submit__3OjIy.btn_2.btn_purple.mobile_hidden",
    )

    INPUT_FORM = (
        By.CSS_SELECTOR,
        "div#root input",
    )

    SELECT_BUTTON = (By.CSS_SELECTOR, "div#root span.rw-select > button[type='button']")

    POPULAR_SEARCHES_TEXT = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_popular_searches_label__1vjNw",
    )
    FIRST_BTN = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_popular_searches_list__Cbs_t > div:nth-child(1)",
    )
    SECOND_BTN = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_popular_searches_list__Cbs_t > div:nth-child(2)",
    )
    THIRD_BTN = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_popular_searches_list__Cbs_t > div:nth-child(3)",
    )
    PRODUCT_TYPE_ART = (By.XPATH, "//li[contains(text(),'Art')]")
    INPUT_ELEMENT_1 = (By.CSS_SELECTOR, "ul.rw-multiselect-taglist li:nth-child(1)")
    INPUT_ELEMENT_2 = (By.CSS_SELECTOR, "ul.rw-multiselect-taglist li:nth-child(2)")

    STEP_3_HEADING = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_advantages__3g9cB > div",
    )
    SKILL_ACTION_SCRIPT = (By.XPATH, "//li[contains(text(),'ActionScript')]")

    STEP_4_HEADING = (By.CSS_SELECTOR, "div#root div.TeamSearch_budget_question__t1IoD")
    STEP_4_TEXT = (By.CSS_SELECTOR, "div#root div.TeamSearch_budget_tip__1LFGQ")
    UP_TO_10000_TEXT = (By.CSS_SELECTOR, "div#root div:nth-child(2) > label")
    UP_TO_20000_TEXT = (By.CSS_SELECTOR, "div#root div:nth-child(3) > label")
    LESS_5000_TEXT = (By.CSS_SELECTOR, "div#root div:nth-child(1) > label")
    RADIO_BUTTON_1 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(1) > label > input + span.RadioButton_radiomark__1suCw",
    )
    RADIO_BUTTON_2 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(2) > label > input + span.RadioButton_radiomark__1suCw",
    )
    RADIO_BUTTON_3 = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(3) > label > input + span.RadioButton_radiomark__1suCw",
    )
    ONE_DEVELOPER_TEXT = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_monthBudget_wrapper__1aQxW > div:nth-child(1) > div",
    )
    TWO_THREE_DEVELOPERS_TEXT = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_monthBudget_wrapper__1aQxW > div:nth-child(2) > div",
    )
    TWO_DEVELOPERS_AND_UX_TEXT = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_monthBudget_wrapper__1aQxW > div:nth-child(3) > div",
    )
    TEXTAREA = (By.CSS_SELECTOR, "div#root textarea")
    VALIDATION_MESSAGE_4 = (
        By.CSS_SELECTOR,
        "div#root div.form_group.undefined.form_control_2_wrapper > div.validation_message",
    )
    VALIDATION_MESSAGE_STEP_4 = (By.CSS_SELECTOR, "div#root div.validation_message")
    VALIDATION_STATUS_OK_STEP_4 = (
        By.CSS_SELECTOR,
        "div#root div.form_group.undefined.form_control_2_wrapper > span",
    )
    ONE_MONTH_CHOICE = (By.XPATH, "//li[contains(text(),'1 month')]")
    NO_RESULTS_TEXT = (By.CSS_SELECTOR, "div.rw-popup > ul > li")
    REQUEST_SENT_MASSEGE = (
        By.CSS_SELECTOR,
        "div#root div.TeamSearch_response_message__2RXh_",
    )


class LoginPageLocators:
    HOME_BTN = (
        By.CSS_SELECTOR,
        "div#root div.container.App_app_wrapper_content__6P4WE > ul > li:nth-child(1) > a",
    )
    LOGIN_LEFT_TEXT = (
        By.CSS_SELECTOR,
        "div#root div.container.App_app_wrapper_content__6P4WE > ul > li:nth-child(2)",
    )
    LOGIN_HEDING = (By.CSS_SELECTOR, "div#root h1")
    AMAZING_DEVELOPERS_TEXT = (By.CSS_SELECTOR, "div#root h5")
    EMAIL_TEXT = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(1) > div.input_wrapper > label",
    )
    PASSWORD_TEXT = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(2) > div.input_wrapper > label",
    )
    INPUT_EMAIL_FORM = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(1) > div.input_wrapper > label + input",
    )
    INPUT_PASSWORD_FORM = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(2) > div.input_wrapper > label + input",
    )
    EXAMPLE_MAIL_TEXT = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(1) > div.FormControls_input_help__362EO.undefined",
    )
    EXAMPLE_PASSWORD_TEXT = (
        By.CSS_SELECTOR,
        "div#root div:nth-child(2) > div.FormControls_input_help__362EO.undefined",
    )
    RECOVERY_PASSWORD_BTN = (
        By.CSS_SELECTOR,
        "div#root div.Login_recovery_link__1asIj > a",
    )
    LOGIN_BTN_LOGIN_PAGE = (By.CSS_SELECTOR, "div#root button")
    REGISTER_BTN_LOGIN_PAGE = (
        By.CSS_SELECTOR,
        "div#root div.container.App_app_wrapper_content__6P4WE > div > div > a",
    )
    VALIDATION_MESSAGE_1_LOGIN_PAGE = (By.CSS_SELECTOR, "div#root div:nth-child(1) > div.validation_message")
    VALIDATION_MESSAGE_2_LOGIN_PAGE = (By.CSS_SELECTOR, "div#root div:nth-child(2) > div.validation_message")
    VALIDATION_MESSAGE_3_LOGIN_PAGE = (By.CSS_SELECTOR, "div#root div.validation_message")


class BasePageLocators:
    pass


class PersonalPageLocators:
    LOGOUT_BTN = (By.CSS_SELECTOR, "div#root li:nth-child(6) > button")
    PERSONAL_PAGE_LINK = "https://ibench.net/stats"
