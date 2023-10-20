# --coding:utf-8--
import pytest

from aomaker.base.base_testcase import BaseTestcase
from aomaker import aomaker

import apis

test_data_file_path = "data/api_data/case_data.yaml"


@pytest.mark.usefixtures("clear_resource")
class TestCase(BaseTestcase):
    @pytest.mark.case
    @pytest.mark.parametrize("test_data", aomaker.data_maker(test_data_file_path, "case", "crate_case"))
    def test_create_case(self, test_data):
        res = apis.case_obj.create_case(test_data)
        self.assert_eq(res['code'], 0)
