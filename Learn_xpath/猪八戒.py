import requests
from lxml import etree      #安装 lxml 模块：pip install lxml
import csv

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
url = 'https://www.zbj.com/search/f/?kw=saas'
resp = requests.get(url,headers=headers)
html_text = resp.text
resp.close()

#构造xpath 对象
html = etree.HTML(html_text)    # etree.HTML() 解析HTML源代码，  etree.XML() 解析XML源代码  etree.parse() 解析页面文件
#开始获取数据
# div_list = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div') #通过绝对路径的方式获取 数据集
div_list = html.xpath('//div[@class="new-service-wrap"]/div')    #获取到包含想要提取数据的列表  //:代表更节点的所有后代，@属性="属性值"
f = open('zbj.csv',mode='a',encoding='utf8')
csv_w = csv.writer(f)
for div in div_list:
    company_nane = div.xpath('.//a[@class="service-bottom-wrap j_ocpc"]/div[1]/p/text()')[1].strip('\n\n')    #./ :代表当前路径  ,通过 text() 获取标签中的文本内容
    company_addr = div.xpath('.//a[@class="service-bottom-wrap j_ocpc"]/div[1]/div/span/text()')[0]   #./ :代表当前路径
    company_img = div.xpath('.//a[@class="service-top-wrap j_ocpc"]//div[@class="carousel-wrap"]/div[1]/img/@data-original')[0]  #通过 @属性获取属性值
    title = 'saas'.join(div.xpath('.//a[@class="service-top-wrap j_ocpc"]//div[@class="service-title"]/p/text()'))
    price = div.xpath('.//a[@class="service-top-wrap j_ocpc"]//span[@class="price"]/text()')[0]
    info_list = [title,price,company_nane,company_addr,company_img]
    csv_w.writerow(info_list)
f.close()
print('Over!!!!')

