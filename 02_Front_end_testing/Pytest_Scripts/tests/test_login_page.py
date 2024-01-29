from Portfolio_front_end.pages.login_page import LoginPage
from Portfolio_front_end.pages.main_page import MainPage
import pytest
from faker import Faker

link = "https://ibench.net/login"


class TestPositive:
    # def test_check_header_elements(self, browser):
    #     page = LoginPage(browser, link)
    #     page.open()
    #     page.should_be_login_page()
    #     page.should_be_verify_header_elements()
    #     page.should_be_header_elements_clickable_and_enabled()
    #     page.should_be_header_elements_have_correct_size_and_color()
    #     page.check_fail_status()
    #
    # def test_header_elements_follow_to_right_link(self, browser):
    #     page = LoginPage(browser, link)
    #     main_page_method = MainPage(browser, link)
    #     page.open()
    #     page.should_be_login_page()
    #     main_page_method.go_to_register_page()
    #     page.should_be_register_page()
    #     main_page_method.go_to_login_page()
    #     page.should_be_login_page()
    #     page.go_to_main_page()
    #     page.should_be_main_page()
    #
    # def test_check_login_page_body_elements(self, browser):
    #     page = LoginPage(browser, link)
    #     page.open()
    #     page.should_be_login_page()
    #     page.should_be_login_page_body_elements()
    #     page.check_fail_status()
    #
    # def test_go_to_recover_password_page_from_login_page(self, browser):
    #     page = LoginPage(browser, link)
    #     page.open()
    #     page.should_be_login_page()
    #     page.go_to_recovery_password_page()
    #     page.should_be_recovery_password_page()
    #     page.check_fail_status()
    #
    # def test_go_to_register_page_from_login_page(self, browser):
    #     page = LoginPage(browser, link)
    #     page.open()
    #     page.should_be_login_page()
    #     page.go_to_register_page_from_login_page()
    #     page.should_be_register_page()
    #     page.check_fail_status()

    def test_login_user_with_correct_data(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
        page.should_be_correct_user_logged_in()
        page.should_be_personal_page()
        page.check_fail_status()
#
#
# class TestNegative:
#     @pytest.mark.parametrize(
#         "args",
#         [
#             pytest.param(
#                 (  # Cant go to personal page with empty email and password
#                         "",
#                         "validation_message_1_ON",
#                         "is required",
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="NTTC1",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with empty password
#                         Faker().email(),
#                         "validation_message_1_OFF",
#                         None,
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="NTTC2",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with empty email
#                         "",
#                         "validation_message_1_ON",
#                         "is required",
#                         Faker().random_number(),
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="NTTC3",
#             ),
#         ],
#     )
#     def test_cant_login_with_empty_data(self, browser, args):
#         page = LoginPage(browser, link)
#         page.open()
#         page.should_be_login_page()
#         page.cant_go_to_personal_page_with_incorrect_data(*args)
#         page.check_fail_status()
#
#     @pytest.mark.parametrize(
#         "args",
#         [
#             pytest.param(
#                 (  # Cant go to personal page with incorrect email
#                         "mailmail.com",
#                         "validation_message_1_ON",
#                         "is not a valid email",
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="NTTC4",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with incorrect email
#                         "mail@mailcom",
#                         "validation_message_1_ON",
#                         "is not a valid email",
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="NTTC5",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with correct email and incorrect password
#                         "A.Crok@atlant.com",
#                         "validation_message_1_OFF",
#                         None,
#                         "123456789",
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "Incorrect password.",
#                 ),
#                 id="NTTC6",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with fake email and correct password
#                         Faker().email(),
#                         "validation_message_1_OFF",
#                         None,
#                         "Password1234",
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "User not found.",
#                 ),
#                 id="NTTC7",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with fake email and incorrect password
#                         Faker().email(),
#                         "validation_message_1_OFF",
#                         None,
#                         Faker().random_number(),
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "User not found.",
#                 ),
#                 id="NTTC8",
#             ),
#         ],
#     )
#     def test_cant_login_with_incorrect_data(self, browser, args):
#         page = LoginPage(browser, link)
#         page.open()
#         page.should_be_login_page()
#         page.cant_go_to_personal_page_with_incorrect_data(*args)
#         page.check_fail_status()
#
#
# class TestAdHoc:
#     @pytest.mark.parametrize(
#         "args",
#         [
#             pytest.param(
#                 (  # Cant go to personal page with incorrect email and empty password
#                         ".",
#                         "validation_message_1_ON",
#                         "is not a valid email",
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="ATTC1",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with adhoc email and empty password
#                         "!@#$%^&*()_+",
#                         "validation_message_1_ON",
#                         "is not a valid email",
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="ATTC2",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with correct email and adhoc password
#                         "A.Crok@atlant.com",
#                         "validation_message_1_OFF",
#                         None,
#                         ".",
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "Incorrect password.",
#                 ),
#                 id="ATTC3",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with fake email and adhoc password
#                         Faker().email(),
#                         "validation_message_1_OFF",
#                         None,
#                         Faker().text(),
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "User not found.",
#                 ),
#                 id="ATTC4",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with adhoc email and adhoc password
#                         ".",
#                         "validation_message_1_ON",
#                         "is not a valid email",
#                         ".",
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="ATTC5",
#             ),
#         ],
#     )
#     def test_cant_login_with_adhoc_data(self, browser, args):
#         page = LoginPage(browser, link)
#         page.open()
#         page.should_be_login_page()
#         page.cant_go_to_personal_page_with_incorrect_data(*args)
#         page.check_fail_status()
#
#
# class TestBoundary:
#     @pytest.mark.parametrize(
#         "args",
#         [
#             pytest.param(
#                 (  # Cant go to personal page with one letter email
#                         "A",
#                         "validation_message_1_ON",
#                         "is not a valid email",
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="BTTC1",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with zero letters email
#                         "",
#                         "validation_message_1_ON",
#                         "is required",
#                         "",
#                         "validation_message_2_ON",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="BTTC2",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with one letter password
#                         Faker().email(),
#                         "validation_message_1_OFF",
#                         None,
#                         "1",
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "User not found.",
#                 ),
#                 id="BTTC3",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with zero letters password
#                         Faker().email(),
#                         "validation_message_1_OFF",
#                         None,
#                         "",
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "is required",
#                 ),
#                 id="BTTC4",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with one letter email and incorrect password
#                         "A",
#                         "validation_message_1_OFF",
#                         None,
#                         "1",
#                         "validation_message_2_OFF",
#                         None,
#                         "validation_message_3_ON",
#                         "is not a valid email",
#                 ),
#                 id="BTTC5",
#             ),
#             pytest.param(
#                 (  # Cant go to personal page with zero letters email and incorrect password
#                         "",
#                         "validation_message_1_ON",
#                         "is required",
#                         "",
#                         "validation_message_2_OM",
#                         "is required",
#                         "validation_message_3_OFF",
#                         None,
#                 ),
#                 id="BTTC6",
#             ),
#         ],
#     )
#     def test_cant_login_with_boundary_data(self, browser, args):
#         page = LoginPage(browser, link)
#         page.open()
#         page.should_be_login_page()
#         page.cant_go_to_personal_page_with_incorrect_data(*args)
#         page.check_fail_status()
