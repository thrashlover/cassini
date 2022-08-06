import openpyxl
import pytest
from selenium.common import TimeoutException

from selenium_task.pages.yahoo_page import Yahoo
from contextlib import nullcontext as does_not_raise


class TestYahooCassini:
    wb = openpyxl.load_workbook(r'Credentials.xlsx')
    sheet = wb.active
    test_data = {
        "username_param__1": [sheet['A2'].value, sheet['B2'].value],
        "username_param__2": pytest.param([sheet['A3'].value, sheet['B3'].value], marks=pytest.mark.xfail(
            reason="Wrong login username"))
    }

    @pytest.mark.parametrize("test_data", test_data.values(), ids=list(test_data.keys()))
    def test(self, browser, test_data):
        yahoo_page = Yahoo(browser)
        yahoo_page.go_to_url()
        yahoo_page.login(test_data)
        yahoo_page.click_finances()
        yahoo_page.hover_market_data_and_click_calendar()
        yahoo_page.click_next_button()
        yahoo_page.assert_values_for_the_day()


'''Alternative approach'''


# class TestYahooCassini:
#     wb = openpyxl.load_workbook(r'Credentials.xlsx')
#     sheet = wb.active
#     testdata = [
#         (sheet['A2'].value, sheet['B2'].value, does_not_raise()),
#         (sheet['A3'].value, sheet['B3'].value, pytest.raises(TimeoutException))
#     ]
#
#     def scenario(self, browser, user, password):
#         yahoo_page = Yahoo(browser)
#         yahoo_page.go_to_url()
#         yahoo_page.login(user, password)
#         yahoo_page.click_finances()
#         yahoo_page.hover_market_data_and_click_calendar()
#         yahoo_page.click_next_button()
#         yahoo_page.assert_values_for_the_day()
#
#     @pytest.mark.parametrize('user, password, expectation', testdata)
#     def test(self, browser, user, password, expectation):
#         with expectation:
#             assert self.scenario(browser, user, password) is None
