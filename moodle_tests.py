import unittest
import moodle_methods as methods
import moodle_locators as locators


class MoodleAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_a_log_in_log_out():
        methods.setUp()
        methods.log_in()
        methods.log_out()
        # methods.tearDown()

    @staticmethod
    def test_b_create_new_user():
        methods.setUp()
        methods.log_in()
        methods.create_new_user()
        methods.logger()
        methods.check_user_created()
        methods.log_out()
        methods.log_in(locators.username, locators.password)
        methods.check_logged_in_with_new_cred()
        methods.log_out()
        methods.log_in()
        methods.delete_new_user()
        methods.log_out()
        methods.tearDown()


