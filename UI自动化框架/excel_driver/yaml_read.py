import yaml

# #   封装读取yaml文件类
# class Yamlconf:
#     def __init__(self,file_path):
#         """file_path: yaml文件的路径"""
#         self.file_path = file_path
#     def load_yaml(self):
#         with open(self.file_path,encoding='utf-8')as f:
#             data = yaml.load(stream=f.read(),Loader=yaml.FullLoader)
#             print(data)
#             return data
#
#
# if __name__ == '__main__':
#     y  = Yamlconf('../Data/whitedata1')
#     y.load_yaml()

def load_yaml(path):
    with open(path,encoding='utf-8')as f:
        data =yaml.load(f,Loader=yaml.FullLoader)
        print(data)
        return data



