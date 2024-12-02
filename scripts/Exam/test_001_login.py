import requests
import pytest
BASE_URL = "http://ihrm2-test.itheima.net"
class TestLoginAPI:
    @pytest.mark.smoke
    def test_login_success(self):
        url = f"BASE_URL/api/sys/login"
        HEADERS = {'Content-Type': 'application/json;charset=utf-8'}
        VALID_PAYLOAD = {"mobile": "13800000002", "password": "123456"}
        response = requests.post(url,json=VALID_PAYLOAD,headers=HEADERS)
        assert response.status_code == 200
        response_data=response.json()
        assert response_data['success'] is True
        assert response_data['code'] == 10000
        assert response_data['message'] == '操作成功'
        assert "data" in response_data


