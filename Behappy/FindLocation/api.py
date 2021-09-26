from urllib.parse import urlencode, unquote, quote_plus
import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree

from requests.sessions import Request


serviceKey="aEwwPiJLOfQLF991Fvvcv6piLOUwnO7uH7qiX6DXVazK8EDb6Yw39Hsq7xA+F4ux1KvKgLNVTx3CP7/IvdpOtQ=="
service = unquote(serviceKey, 'UTF-8')

def showBin():
    data = []
    where =[]

    url = "https://api.odcloud.kr/api/15087773/v1/uddi:6bcb9ebf-d368-4ac8-9382-a9e82437f74d"
    returnType = "XML"
    page = "1"
    perPage = "10"

    queryParams = '?' + urlencode({ quote_plus('serviceKey') : service, quote_plus('page') : page, quote_plus('perPage') : perPage, quote_plus('returnType') : returnType})
    res = requests.get(url + queryParams)


    #url = "https://api.odcloud.kr/api/15087773/v1/uddi:6bcb9ebf-d368-4ac8-9382-a9e82437f74d?page=1&perPage=10&returnType=XML&serviceKey=aEwwPiJLOfQLF991Fvvcv6piLOUwnO7uH7qiX6DXVazK8EDb6Yw39Hsq7xA%2BF4ux1KvKgLNVTx3CP7%2FIvdpOtQ%3D%3D"
    #get = urllib.request.urlopen(url).read().decode('utf-8')
    #res = requests.get(get)
    xml = res.text
    soup = BeautifulSoup(xml,'html.parser')
    # for tag in soup.find_all('수거쓰레기종류'):
    #     data.append(tag.text)
    # for tag in soup.find_all('소재지도로명주소'):
    # #     where.append(tag.text)
    # for tag in soup.find_all():
    #     data.append(tag.text)
    data.append("kim")
    where.append(soup.text)
    res= dict(zip(data,where))
    return res
