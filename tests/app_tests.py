# -*- coding: utf-8 -*-

from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    #确认返回了 404 Not Found 相应
    resp = app.request("/")
    print assert_response(resp, status="404")

    #GET
    resp = app.request("/hello")
    assert_response(resp)
    # assert_response(resp, status="200")

    #POST
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")

    data = {'name': "Zed", 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")
