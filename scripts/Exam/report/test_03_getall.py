import pytest
import requests
BASE_URL = "http://ihrm2-test.itheima.net/"
@pytest.mark.parametrize(
    "mobile,password,expected_success,expected_code,expected_message",
    [   ("13800000002","123456",True,10000,"操作成功！"),
        ("13800000004","123456",False,10001,"用户名错！"),
        ("13800000002","12348",False,10002,"密码错！"),
    ]
)
def test_loginAPI(mobile,password,expected_success,expected_code,expected_message):
    url = f"{BASE_URL}/api/sys/login"
    headers={"Content-Type": "application/json;charset=utf-8"}
    payload = {"mobile":mobile,"password":password}
    response = requests.post(url,json=payload,headers=headers)
    assert response.status_code == 200,f"the failed, expected 200, the actual {response.status_code}"
    response_data=response.json()
    assert response_data.get("success") == expected_success,f"the failed, expected {expected_success}, the actual {response_data.get("success")}"



