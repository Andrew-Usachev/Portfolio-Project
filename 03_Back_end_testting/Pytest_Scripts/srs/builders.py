'''
This file contains all the builders for the API.
'''
from faker import Faker
import random

fake = Faker()


class LoginBodyBuilder:
    def __init__(self):
        self.test_data = {}

    def with_email(self, email):
        self.test_data['email'] = email
        return self

    def with_password(self, password):
        self.test_data['password'] = password
        return self

    def with_country(self, country):
        self.test_data['country'] = country
        return self

    def with_terms_accepted(self, terms_accepted):
        self.test_data['terms_accepted'] = terms_accepted
        return self

    def with_type(self, type):
        self.test_data['type'] = type
        return self

    def with_company_name(self, company_name):
        self.test_data['company_name'] = company_name
        return self

    def build(self):
        return self.test_data


class LoginUrlBuilder:
    def __init__(self):
        self.test_data = {}

    def with_url(self, url):
        self.test_data = url
        return self

    def build(self):
        return self.test_data


class LoginHeaderBuilder:
    def __init__(self):
        self.test_data = {}

    def with_sec_ch_ua(self, sec_ch_ua):
        self.test_data['sec-ch-ua'] = sec_ch_ua
        return self

    def with_sec_ch_ua_platform(self, sec_ch_ua_platform):
        self.test_data['sec-ch-ua-platform'] = sec_ch_ua_platform
        return self

    def with_sec_ch_ua_mobile(self, sec_ch_ua_mobile):
        self.test_data['sec-ch-ua-mobile'] = sec_ch_ua_mobile
        return self

    def with_user_agent(self, user_agent):
        self.test_data['User-Agent'] = user_agent
        return self

    def with_content_type(self, content_type):
        self.test_data['Content-Type'] = content_type
        return self

    def with_accept(self, accept):
        self.test_data['Accept'] = accept
        return self

    def with_sec_fetch_site(self, sec_fetch_site):
        self.test_data['Sec-Fetch-Site'] = sec_fetch_site
        return self

    def with_sec_fetch_mode(self, sec_fetch_mode):
        self.test_data['Sec-Fetch-Mode'] = sec_fetch_mode
        return self

    def with_sec_fetch_dest(self, sec_fetch_dest):
        self.test_data['Sec-Fetch-Dest'] = sec_fetch_dest
        return self

    def with_host(self, host):
        self.test_data['host'] = host
        return self

    def build(self):
        return self.test_data


class LoginHeaderResponseBuilder:
    def __init__(self):
        self.test_data = {}

    def with_server(self, server):
        self.test_data['Server'] = server
        return self

    def with_date(self, date):
        self.test_data['Date'] = date
        return self

    def with_content_type(self, content_type):
        self.test_data['Content-Type'] = content_type
        return self

    def with_transfer_encoding(self, transfer_encoding):
        self.test_data['Transfer-Encoding'] = transfer_encoding
        return self

    def with_connection(self, connection):
        self.test_data['Connection'] = connection
        return self

    def with_access_control_allow_origin(self, access_control_allow_origin):
        self.test_data['Access-Control-Allow-Origin'] = access_control_allow_origin
        return self

    def with_vary(self, vary):
        self.test_data['Vary'] = vary
        return self

    def with_content_encoding(self, content_encoding):
        self.test_data['Content-Encoding'] = content_encoding
        return self

    def with_x_frame_options(self, x_frame_options):
        self.test_data['X-Frame-Options'] = x_frame_options
        return self

    def with_content_length(self, content_length):
        self.test_data['Content-Length'] = content_length
        return self

    def build(self):
        return self.test_data


class FindContractorsBaseBuilder:

    def __init__(self):
        super().__init__()
        self.test_data = {}
        self.reset()

    def set_contractor_id(self, id=fake.random_int(min=1100, max=1200)):
        self.test_data['Id_Contractors'] = id
        return self

    def set_verified_companies(self, company=random.choice(['All companies', 'Only verified'])):
        self.test_data['Verified_companies'] = company
        return self

    def set_slot_name(self, slot_name=fake.word()):
        self.test_data['Slot_name'] = slot_name
        return self

    def set_developers_location(self, developer_location=random.choice(['Canada', 'United States'])):
        self.test_data['Developers_location'] = developer_location
        return self

    def set_job_title(self, job_title=random.choice(['QA Automation', 'QA Manual'])):
        self.test_data['Job_title'] = job_title
        return self

    def set_maximum_hourly_rate(self, maximum_hourly_rate=fake.random_int(min=10, max=100)):
        self.test_data['Maximum_hourly_rate'] = maximum_hourly_rate
        return self

    def set_position_level(self, position_level=random.choice(['Senior', 'Middle', 'Junior', 'Team Lead'])):
        self.test_data['Position_level'] = position_level
        return self

    def set_experience(self, experience=random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])):
        self.test_data['Experience'] = experience
        return self

    def set_english_level(self, english_level=random.choice(['0 (Begginer)', 'A1 (Elementary)', 'A2 (Pre-Entermediate)',
                                                             'B1 (Entermediate)', 'B2 (Upper Intermediate)',
                                                             'C1 (Advanced)', 'C2 (Proficient)'])):
        self.test_data['English_level'] = english_level
        return self

    def set_skills(self, skills=random.choice(['SQL', 'MySQL', 'MongoDB', 'Git', 'GitHUB'])):
        self.test_data['Skills'] = skills
        return self

    def set_project_description(self, project_description=fake.text()):
        self.test_data['Project_Description'] = project_description
        return self

    def reset(self):
        self.set_contractor_id()
        self.set_verified_companies()
        self.set_slot_name()
        self.set_developers_location()
        self.set_job_title()
        self.set_maximum_hourly_rate()
        self.set_position_level()
        self.set_experience()
        self.set_english_level()
        self.set_skills()
        self.set_project_description()

    def build(self):
        return self.test_data
