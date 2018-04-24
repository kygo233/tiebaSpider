from bs4 import BeautifulSoup 
import urllib.request
import re  

url_Member  = "http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%D0%DE%B3%B5tv";
url_Member1 = "http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%D0%DE%B3%B5tv&pn=pagenum";
url_gz = "http://www.baidu.com/p/username?from=tieba";
url_grxx = "http://www.baidu.com/p/username/detail";

def getHtml(url,charset):  
    page = urllib.request.urlopen(url)  
    html = page.read().decode(charset)
    return BeautifulSoup(html, "lxml") ;

def getHtml2(url):  
    page = urllib.request.urlopen(url)  
    html = page.read().decode("UTF-8")
    html=html.replace('\\x22',"'")
    return BeautifulSoup(html, "lxml") ;
def getPagenum():
    html = getHtml(url_Member,'GBK')
    pattern = re.compile(r'共(.*?)页')
    list1=pattern.findall(html.prettify())
    return list1
#获取用户名


def getMemberList():
    list1 =getPagenum();
    pagenum=int(list1[0]);
    list2 = []
    for page in range(0,pagenum):
        print("第"+str(page)+"页")
        soup = getHtml(url_Member1.replace("pagenum", str(page)),'GBK')
        tag_a = soup.select(".user_name")
        for tag in tag_a :
            list2.append(tag.get("title"))
    return list(set(list2))

def getgrxxUrl(username):   
    return url_grxx.replace("username", username) ;

def getgzUrl(username):   
    return url_gz.replace("username", username) ;

def getgrxx(username):
    grxx={'用户名':'','性别':'','生日':'','血型':'','出生地':'','居住地':''}
    grxx['用户名']=username;
    tag=getHtml(getgrxxUrl(username),'UTF-8').select(".userdetail-profile-basic")
    key=tag[0].select(".profile-attr")
    value=tag[0].select(".profile-cnt")
    for i in range(len(key)):
        grxx[key[i].get_text()]=value[i].get_text()

def counttb(list1):
    counts = { }          #字典
    for x in list1:    
        print(x)                  #time_zones 为列表
        for tb in x:
            if  tb in counts:
                counts[tb] += 1
            else:
                counts[tb] = 1
    return counts  
    
list_tieba=[]
nameList=getMemberList()
print(nameList)
for i in range(len(nameList)):
    html=getHtml2(getgzUrl(nameList[i]))
    pattern = re.compile(r'target=_blank title=\'(.*?)\'>')
    list1=pattern.findall(html.prettify())
    list_tieba.append(list1)
tb=counttb(list_tieba)
print(counttb(list_tieba))      
f =open("C:/Users/ys/Desktop/tb.txt", 'w') 
f.write(str(tb))
f.close() 

 
 
# nameList=getMemberList(url_Member)
# for i in range(len(nameList)):
#     grxx={'用户名':'','性别':'','生日':'','血型':'','出生地':'','居住地':''}
#     grxx['用户名']=nameList[i];
#     tag=getHtml(getgrxxUrl(nameList[i]),'UTF-8').select(".userdetail-profile-basic")
#     key=tag[0].select(".profile-attr")
#     value=tag[0].select(".profile-cnt")
#     for i in range(len(key)):
#         grxx[key[i].get_text()]=value[i].get_text()
#     print(grxx) 