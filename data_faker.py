import os
import tempfile
from faker import Faker
from faker.providers import BaseProvider
from mimesis import Person
from mimesis.locales import Locale
from mimesis import Text
from mimesis.enums import Gender
import factory
from factory import Factory, Faker
from hypothesis import given, strategies as st

data_page_form_example = "https://testpages.eviltester.com/styled/basic-html-form-test.html"

fake = Faker("ru_RU")


def generate_test_data_faker():
    return {
        "name": fake.name(),
        "pass": fake.password(),
        "text": fake.passport_full(),
    }


def generate_test_data_mimesis():
    chel = Person(Locale.RU)
    return {
        "name": chel.full_name(),
        "password": chel.password(),
        "text": chel.political_views(),
    }


class User:
    def __init__(self, name, email, address, password, phone_number):
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.password = password


class UserFactory(factory.Factory):
    class Meta:
        model = User
    person = Person(Locale.EN)
    name = factory.LazyAttribute(lambda _: person.name())
    email = factory.LazyAttribute(lambda _: person.email())
    address = factory.LazyAttribute(lambda _: person.address())
    phone_number = factory.LazyAttribute(lambda _: person.phone_number())
    password = factory.LazyAttribute(lambda _: person.password())


@st.composite
def generate_test_data_hypothesis(draw):
    name = draw(st.text())
    email = draw(st.emails())
    password = draw(st.text())
    text = draw(st.text())
    return {
        "name": name,
        "email": email,
        "password": password,
        "text": text
    }


def file_content_strategy(draw):
    return draw(st.text(min_size=1, max_size=1000))
