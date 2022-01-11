import os

import  pytest
if __name__ == '__main__':
    # 生成测试数据
    pytest.main(['-s','-v','./testcase/test_dome.py','--alluredir','./allure-results'])
    # 生成测试报告
    os.system('allure generate ./allure-results -o ./reports -c')