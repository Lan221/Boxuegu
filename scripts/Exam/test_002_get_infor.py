import requests
import pytest
BASE_URL = "http://ihrm2-test.itheima.net"
def test_get_users_list_success()
    url = f"{BASE_URL}/api/sys/user?page=1&size=10"
    HEADERS={'Authorization':'Bearer c3627bf5-f816-474f-a78e-4aa1a5fa43'}
    response = requests.get(url,headers=HEADERS)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data.get("success") is True
    assert response_data.get("code") is 10000
    assert response_data.get("message") is "操作成功！"

    data = response.data.get("data")
    assert data is not None
    assert "total" in data
    assert "row" in data

