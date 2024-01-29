'''
This file contains the builder classes for the test data.
'''


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
