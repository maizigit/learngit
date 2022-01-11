import requests
import pytest
from excel_driver.yaml_read import load_yaml
from conf.conf import c
class TestApi:
    @pytest.mark.parametrize('apiinfo',load_yaml('../Data/api_baidu.yaml'))
    def test_baidu(self,apiinfo):
        url = apiinfo['request']['url']
        headers=apiinfo['request']['headers']
        rep = requests.get(url=url,headers=headers)
        print(rep.status_code)






if __name__ == '__main__':
    pytest.main(['-vs','test_api.py'])

