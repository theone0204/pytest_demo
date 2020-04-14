#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time:2020-04-14
import pytest
import requests
import json
from assertpy import assert_that
from tests.contant import HOST


class TestGetUsers:
    def test_get_users(self):
        url = HOST + "/users"
        response = requests.get(url)
        response_josn = json.loads(response.text)
        for item in response_josn:
            assert_that(list(item.keys())).is_equal_to(["username","password"])

    def test_get_users_error_method(self):
        url = HOST + "/users"
        response = requests.post(url)
        assert_that(response.status_code).is_equal_to(405)
