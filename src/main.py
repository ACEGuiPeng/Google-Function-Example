# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: White Gui
@Date  : 2024/8/28
@Desc :
"""

import functions_framework
import requests
from flask import Request, make_response


@functions_framework.http
def api_proxy(request: Request):
    """
        1 Get target url
        2 Get proxy method
        3 get data body
        4 proxy to target url with params
    :param request:
    :return:
    """
    target_url = request.path.replace("/", "", 1)
    if not target_url.startswith("http"):
        return resp_failure("Target url must start with http")

    method = request.method
    params = request.args.to_dict()
    data = request.data
    headers = dict(request.headers)
    # remove host to avoid 403
    headers.pop("Host", None)

    cookies = request.cookies
    print(
        f"Try to proxy request: {target_url}, method: {method}, params: {params}, data: {data}, headers: {headers},cookies: {cookies}")
    resp = requests.request(method=method, url=target_url, data=data, params=params,
                            headers=headers, cookies=cookies)
    flask_response = make_response(resp.content, resp.status_code)
    print(f"SUCCESS to get proxy request result from server: {target_url},status: {resp.status_code}")
    return flask_response


def resp_failure(reason: str):
    return {"result": "failure", "reason": reason}
