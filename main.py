import requests
import json
import os


def print_hi(ide_name):
    print(f'hello, {ide_name}')


def get_from_api():  
    # 通过Elsevier的api获取xml格式的文章信息，订阅用户（学校、研究所等）可以获取全文，非订阅用户可以获取摘要
    # https://doi.org/10.1016/j.rse.2024.114475
    # https://doi.org/10.1016/j.rse.2025.114775
    doi_0 = "10.1016/j.rse.2024.114475"
    doi_1 = "10.1016/j.rse.2025.114775"

    # pass your APIkey and article doi via requests, for example:
    # https://api.elsevier.com/content/article/doi/[DOI]?APIKey=[APIKey]
    elsevier0 = requests.get('https://api.elsevier.com/content/article/doi/10.1016/j.rse.2025.114775?APIKey=273a092e888e19f1cce1a83714a12776')
    data0 = elsevier0.text

    # save the xml to a file article1.xml
    if elsevier0.status_code == 200:
        with open('article1.xml', 'wb') as file:
            file.write(elsevier0.content)
        print('saved successfully')
    else:
        print(f"requests failed with status code: {elsevier0.status_code}")
        
    return elsevier0


if __name__ == '__main__':
    os.chdir("Work/Project/else_api_vs")
    print_hi('vs_code')
    el0 = get_from_api()