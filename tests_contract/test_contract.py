# -*- coding: utf-8 -*-
from fixture.variables import Profinity
from contract_lib import Contact, connection


def test_of_add_new_valid_contact(app):
    """
    Validation of add correct new contact with full data
    """

    app.contact.create(Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                       middle_name=Profinity.correct_data, nickname=Profinity.correct_data,
                       title=Profinity.correct_data, company_name=Profinity.correct_data,
                       address_name=Profinity.correct_data, work=Profinity.correct_phone_number,
                       fax=Profinity.correct_phone_number, home=Profinity.correct_phone_number,
                       mobile=Profinity.correct_phone_number, email1=Profinity.correct_email,
                       email2=Profinity.correct_email, email3=Profinity.correct_email, homepage=Profinity.correct_data,
                       add_year=True, address=Profinity.correct_data, phone=Profinity.correct_data,
                       notes=Profinity.correct_data))
    app.contact.delete_contract()


def test_of_add_new_valid_contact_name_only(app):
    """
    Validation of add correct new contact with only full name
    """

    app.contact.create((Contact(first_name=Profinity.correct_data, last_name=Profinity.correct_data,
                        middle_name=Profinity.correct_data, nickname=Profinity.correct_data)))
    app.contact.delete_contract()


def test_of_delete_contract(app):
    """
    Validation of  delete contract
    """

    app.contact.validation_of_contact_exist()
    app.contact.delete_contract()


def test_of_edit_contract(app):
    """
    Validation of edit contract
    """

    app.contact.validation_of_contact_exist()
    app.contact.edit_contract((Contact(first_name=Profinity.long_word_20, last_name=Profinity.long_word_20,
                                        middle_name=Profinity.long_word_20, nickname=Profinity.long_word_20)))
    app.contact.delete_contract()