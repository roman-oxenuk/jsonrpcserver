"""response_test.py"""
# pylint: disable=missing-docstring,line-too-long

import os
import sys
import nose
import json

sys.path.append(os.path.dirname(__file__)+'/../jsonrpcserver')
import rpc

def test_result():
    nose.tools.assert_equal(
        '{"jsonrpc": "2.0", "result": {"name": "Joe"}, "id": 1}',
        json.dumps(rpc.result(1, {'name': 'Joe'}))
    )

def test_error():
    nose.tools.assert_equal(
        '{"jsonrpc": "2.0", "error": {"code": -32000, "message": "There was an error"}, "id": 1}',
        json.dumps(rpc.error(1, -32000, 'There was an error'))
    )