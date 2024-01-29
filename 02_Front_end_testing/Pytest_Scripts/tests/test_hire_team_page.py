import time
from Portfolio_front_end.pages.hire_team_page import HireTeamPage
from Portfolio_front_end.pages.main_page import MainPage
from Portfolio_front_end.pages.main_page import BasePage
from Portfolio_front_end.src.locators import HireTeamPageLocators
import pytest
import random
from faker import Faker
from selenium.webdriver.common.keys import Keys

link = "https://ibench.net/team-search"


class TestPositive:
    def test_check_header_elements(self, browser):
        page = HireTeamPage(browser, link)
        main_page_method = MainPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        main_page_method.should_be_verify_header_elements()
        main_page_method.should_be_header_elements_clickable_and_enabled()
        page.should_be_header_elements_have_correct_size_and_color()
        page.check_fail_status()

    def test_header_elements_follow_to_right_link(self, browser):
        page = HireTeamPage(browser, link)
        main_page_method = MainPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        main_page_method.go_to_hiredevelopers_page()
        page.should_be_hiredevelopers_page()
        page.go_to_hireteam_page()
        page.should_be_hireteam_page()
        page.go_to_main_page()
        page.should_be_main_page()
        page.go_to_hireteam_page()
        page.should_be_hireteam_page()
        main_page_method.go_to_blog_page()
        page.should_be_blog_page()
        page.go_to_hireteam_page()
        page.should_be_hireteam_page()
        main_page_method.go_to_register_page()
        page.should_be_register_page()
        page.go_to_hireteam_page()
        page.should_be_hireteam_page()
        main_page_method.go_to_login_page()
        page.should_be_login_page()
        page.go_to_hireteam_page()
        page.should_be_hireteam_page()
        page.check_fail_status()

    def test_check_text_headings(self, browser):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.should_be_correct_heading_text()
        page.check_fail_status()

    def test_check_animation_elements(self, browser):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.should_be_animation_elements()
        page.should_be_correct_width_height_in_animation_elements()
        page.check_fail_status()

    def test_check_and_fill_out_request_form(self, browser):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.should_be_step_1_request_form()
        page.should_be_fill_correctly_step_1()
        page.should_be_step_2_request_form()
        page.should_be_fill_correctly_step_2()
        page.should_be_step_3_request_form()
        page.should_be_fill_correctly_step_3()
        page.should_be_step_4_request_form()
        page.should_be_fill_correctly_step_4()
        page.should_be_step_5_request_form()
        page.should_be_fill_correctly_step_5()
        page.check_fail_status()


class TestNegative:

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go to step 2 with empty name and privacy ON
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC1",
            ),
            pytest.param(
                (  # Cant go to step 2 with empty name and privacy OFF
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_OFF",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_MUST_BE_ACCEPTED,
                        "must be accepted",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC2",
            ),
            pytest.param(
                (  # Cant go to step 2 with empty email and privacy ON
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC3",
            ),
            pytest.param(
                (  # Cant go step to 2 with empty email and privacy OFF
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_OFF",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC4",
            ),
            pytest.param(
                (  # Cant go to step 2 with privacy OFF
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_OFF",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_MUST_BE_ACCEPTED,
                        "must be accepted",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC5",
            ),
            pytest.param(
                (  # Cant go step to 2 with empty email and name and privacy OFF
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC6",
            ),
        ],
    )
    def test_cant_go_to_step_2_with_empty_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go step 2 with incorrect name
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().random_int(min=1, max=10),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is not a valid name",  # FAIL
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,  # FAIL
                ),
                id="NTTC7",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect name
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        "NaMe!1",
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is not a valid name",  # FAIL
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,  # FAIL
                ),
                id="NTTC8",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().name(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC9",
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().random_int(min=1, max=10),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC10",
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        "mailmail.com",
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC11",
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        "mail@mailcom",
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC12",
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect email and name
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().random_int(min=1, max=10),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().random_int(min=1, max=10),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC13",
            ),
        ],
    )
    def test_cant_go_to_step_2_with_incorrect_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go to step 3 without data
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "must be filled",  # FAIL
                        HireTeamPageLocators.STEP_3_HEADING,
                ),
                id="NTTC14",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant send in step 2 incorrect data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        Faker().name(),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_3_HEADING,
                ),
                id="NTTC15",
            ),
            pytest.param(
                (  # Cant send in step 2 incorrect data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        Faker().random_int(min=1, max=10),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_3_HEADING,
                ),
                id="NTTC16",
            ),
        ],
    )
    def test_cant_go_to_step_3_with_incorrect_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_2_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go to step 4 without data
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "must be filled",  # FAIL
                        HireTeamPageLocators.STEP_4_HEADING,
                ),
                id="NTTC15",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant send in step 3 incorrect data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        Faker().name(),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_4_HEADING,
                ),
                id="NTTC16",
            ),
            pytest.param(
                (  # Cant send in step 3 incorrect data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        Faker().random_int(min=1, max=10),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_4_HEADING,
                ),
                id="NTTC17",
            ),
        ],
    )
    def test_cant_go_to_step_4_with_incorrect_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_3_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go to step 5 without data
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC18"
            ),
            pytest.param(
                (  # Cant go to step 5 with empty budget form
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_ON",
                        Faker().text(),
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC19",
            ),
            pytest.param(
                (  # Cant go to step 5 with empty textarea
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_ON",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="NTTC20",
            ),
        ],
    )
    def test_cant_go_to_step_5_with_empty_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_4_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant send application in step 5 without data
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="NTTC21"
            ),
            pytest.param(
                (  # Cant send application in step 5 with empty input form
                        "Input_form_1_OFF",
                        None,
                        None,
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_ON",
                        Faker().text(),
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is required",  # FAIL
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,  # FAIL
                ),
                id="NTTC22",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it")
            ),
            pytest.param(
                (  # Cant send application in step 5 with empty textarea
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "1 year",
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        Keys.ENTER,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="NTTC23",
            ),
        ],
    )
    def test_cant_send_a_application_in_step_5_with_empty_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_5_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant send application in step 5 incorrect data in input form
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        Faker().text(),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="NTTC24",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it")
            ),
            pytest.param(
                (  # Cant send application in step 5 incorrect data in input form
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        Faker().random_int(min=1, max=10),
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="NTTC25",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it")
            ),
        ],
    )
    def test_cant_send_a_application_in_step_5_with_incorrect_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_5_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()


class TestAdHoc:

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go step 2 with incorrect adhoc name
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        ".",
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is not a valid name",  # FAIL
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,  # FAIL
                ),
                id="ATTC1",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect adhoc name
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        "!@#$%^&*()_+",
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is not a valid name",  # FAIL
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,  # FAIL
                ),
                id="ATTC2",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect adhoc email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        ".",
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="ATTC3",
            ),
            pytest.param(
                (  # Cant go step 2 with incorrect adhoc email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        "!@#$%^&*()_+",
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="ATTC4",
            ),
        ],
    )
    def test_cant_go_to_step_2_with_incorrect_adhoc_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant send in step 2 incorrect adhoc data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        ".",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_3_HEADING,
                ),
                id="ATTC5",
            ),
            pytest.param(
                (  # Cant send in step 2 incorrect adhoc data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "!@#$%^&*()_+",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_3_HEADING,
                ),
                id="ATTC6",
            ),
        ],
    )
    def test_cant_go_to_step_3_with_incorrect_adhoc_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_2_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant send in step 3 incorrect adhoc data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        ",",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_4_HEADING,
                ),
                id="ATTC7",
            ),
            pytest.param(
                (  # Cant send in step 3 incorrect adhoc data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "!@#$%^&*()_+",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_4_HEADING,
                ),
                id="ATTC8",
            ),
        ],
    )
    def test_cant_go_to_step_4_with_incorrect_adhoc_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_3_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant send application in step 5 incorrect adhoc data in input form
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        ".",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="ATTC9",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it")
            ),
            pytest.param(
                (  # Cant send application in step 5 incorrect adhoc data in input form
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "!@#$%^&*()_+",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="ATTC10",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it")
            ),
        ],
    )
    def test_cant_send_a_application_in_step_5_with_incorrect_adhoc_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_5_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()


class TestBoundary:

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go to step 2 with zero letters in name
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        "",
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is not a valid name",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="BTTC1",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant go step 2 with one letter in name
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        "A",
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        Faker().email(),
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_1,
                        "is not a valid name",  # FAIL
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,  # FAIL
                ),
                id="BTTC2",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it"),
            ),
            pytest.param(
                (  # Cant go to step 2 with zero letters email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        "",
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is required",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="BTTC3",
            ),
            pytest.param(
                (  # Cant go step 2 with one letter in email
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_NAME_FORM,
                        Faker().name(),
                        "Input_form_2_ON",
                        HireTeamPageLocators.INPUT_EMAIL_FORM,
                        "A",
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_2,
                        "is not a valid email",
                        HireTeamPageLocators.POPULAR_SEARCHES_TEXT,
                ),
                id="BTTC4",
            ),
        ],
    )
    def test_cant_go_to_step_2_with_boundary_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go to step 3 with zero letters data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_3_HEADING,
                ),
                id="BTTC5",
            ),
            pytest.param(
                (  # Cant go to step 3 with two letters data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "Zz",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_3_HEADING,
                ),
                id="BTTC6",
            ),
        ],
    )
    def test_cant_go_to_step_3_with_boundary_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_2_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant go to step 4 with zero letters data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_4_HEADING,
                ),
                id="BTTC7",
            ),
            pytest.param(
                (  # Cant go to step 4 with two letters data
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "Zz",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.NEXT_STEP_BTN,
                        "Next step",
                        HireTeamPageLocators.STEP_4_HEADING,
                ),
                id="BTTC8",
            ),
        ],
    )
    def test_cant_go_to_step_4_with_boundary_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_3_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()

    @pytest.mark.parametrize(
        "args",
        [
            pytest.param(
                (  # Cant send application in step 5 with zero letters in input form
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_OFF",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="BTTC9",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it")
            ),
            pytest.param(
                (  # Cant send application in step 5 with two letter in input form
                        "Input_form_1_ON",
                        HireTeamPageLocators.INPUT_FORM,
                        "Zz",
                        "Input_form_2_OFF",
                        None,
                        None,
                        "Check_filter_ON",
                        "Privacy_ON",
                        "Budget_OFF",
                        "Textarea_OFF",
                        None,
                        HireTeamPageLocators.VALIDATION_MESSAGE_4,
                        "is required",
                        HireTeamPageLocators.REQUEST_SENT_MASSEGE,
                ),
                id="BTTC10",
                marks=pytest.mark.skip(reason="Skipping this Test Case. Need to fix it")
            ),
        ],
    )
    def test_cant_send_a_application_in_step_5_with_boundary_data(self, browser, args):
        page = HireTeamPage(browser, link)
        page.open()
        page.should_be_hireteam_page()
        page.go_to_step_5_hireteam_page()
        page.cant_go_to_next_step_with_incorrect_data(*args)
        page.check_fail_status()
