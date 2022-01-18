'''
介绍：
    1、selenium:自动化测试工具，可以调用浏览器，然后像人一样操作浏览器
    2、程序从selenium 中提取网页的各种数据，避免了通过其他方式抓数据时的：数据加解密的过程
    3、selenium环境搭建
        a、pip install selenium -i 清华源
        b、下载浏览器驱动：https://npm.taobao.org/mirrors/chromedriver，查看自己电脑浏览器的版本，下载对应的版本驱动，如果该没有找到对应的版本就向上查找一个最近的版本下载
        c、把解压出来的驱动文件放到python 安装目录的 Scripts文件中
'''

##################################
##测试用 selenium 打开谷歌浏览器##
##################################
from selenium.webdriver import Chrome

web = Chrome()    # 创建一个浏览器对象
web.get("https://www.baidu.com")     # 打开一个网址

print(web.title)   #获取页面title
web_text = web.page_source     #查看selenium加载后的网页代码
print('\n经过浏览器处理好的网页代码如下：\n',web_text)
web.close()    #关闭浏览器




###################################
##  防止被检测 和 浏览器窗口切换 ##
###################################
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By   #selenium 摒弃了之前的find_element_by_xpath()的写法，换成By.XPATH
from selenium.webdriver.common.keys import Keys #引入输入键盘的Keys 包
from selenium.webdriver.chrome.options import Options    #浏览器选项插件
import time
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])  #防止被检测，取消浏览器的 ：Chrome 正受到自动检测软件的控制
options.add_experimental_option('useAutomationExtension', False)    #防止被检测，取消浏览器的 ：Chrome 正受到自动检测软件的控制

web = Chrome(options=options)
web.get("https://www.lagou.com/")
el = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')  #模拟鼠标找到需要点击的按钮
el.click()   #点击鼠标

time.sleep(3)    #为了避免鼠标点击后，页面还未加载出来，先阻塞程序3秒
web.find_element(By.ID,'search_input').send_keys("python",Keys.ENTER)   #在搜索框中输入python 并回车。
time.sleep(5)
div_list = web.find_elements(By.CLASS_NAME,"item__10RTO")     #通过classs属性 来快速查询
for div in div_list:
    job_name = div.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text     #通过插xpath来定位信息，  通过.text 提取文本信息
    public_time = div.find_element(By.XPATH,'./div[1]/div[1]/div[1]/span').text
    price = div.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    company_name = div.find_element(By.XPATH,'./div[1]/div[2]/div[1]/a').text

    div.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').click()   #点击a标签，打开一个新窗口
    time.sleep(3)
    web.switch_to.window(web.window_handles[-1])   #切换到新打开的窗口，请窗口一般都在最后一个，所以切换到[-1]
    try:    #因为有反扒，打开子页面需要登录，如果遇到登录情况，直接退出循环
        job_info = web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text     #抓取子页面的数据
    except:    #如果遇到登录情况，定位失败，直接退出循环
        web.close()   #关闭子窗口
        web.switch_to.window(web.window_handles[0])     #切换到主窗口
        break
    print(company_name,job_name,public_time,price,'\n',job_info,'\n\n\n')
    web.close()
    web.switch_to.window(web.window_handles[0])   #子窗口关闭后，需要再次切换到主窗口
    time.sleep(3)
web.close()



##################################
##页面源代码中遇到Ifram 的视角切换##
##################################
'''
    iframe的用途：在页面中套页面
   遇到网页中有 iframe时，需要先拿到iframe,然后切换到iframe视角，然后才能拿到数据
'''
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

web = Chrome()
web.get('https://91kanju2.com/vod-play/541-2-1.html')
resp = web.find_element(By.XPATH,'//*[@id="player_iframe"]')
web.switch_to.frame(resp)  #切换至iframe视角
tx = web.find_element(By.XPATH,'//*[@id="sub-frame-error-details"]').text
print(tx)
web.switch_to.default_content()    #切换回原页面
web.close()


############################
##无头浏览器+ Select选择器##
############################
'''
    不需要程序展示出浏览器页面，在后台默默运行即可
'''
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options    #浏览器选项插件
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

options = Options()
options.headless=True  # 或者使用 opt.add_argument("--headless")   #配置无头参数
options.add_argument("--disable-gpu")

web = Chrome(options=options)   #把参数加载到浏览器
web.get('https://suijimimashengcheng.bmcx.com/')
select_elm = web.find_element(By.XPATH,'//*[@id="ss_cd"]')  #定位到下拉框
sel = Select(select_elm)     #对元素进行包装，包装成下拉框
#让浏览器进行调整选项
num = str(input('请输入希望生成的密码位数（1-99）：'))
for i in range(len(sel.options)):    #i 就是每一个下拉框选项的索引位置
    '''
        sel.select_by_index()    #根据索引进行选择
        sel.select_by_value()    #根据value进行选择
        sel.select_by_visible_text()   #根据文本进行选择
    '''
    sel.select_by_visible_text(num)   #按照文本进行切换

web.find_element(By.XPATH,'//*[@id="ss_anniu"]').click()
time.sleep(1)
passwd = web.find_element(By.XPATH,'//*[@id="ss_mmscjg"]').get_attribute('value')    #获取标签的属性值
print("passwd:",passwd)
web.close()

