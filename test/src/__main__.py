
from bs4 import BeautifulSoup 
import urllib.request
import re  
import multiprocessing
import time    
def getMemberList_PAGE(pagenum):
    url_Member1 = "http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%D0%DE%B3%B5tv&pn=pagenum"
    list2 = []
    url = url_Member1.replace("pagenum", str(pagenum));
    page = urllib.request.urlopen(url);
    html = page.read().decode('GBK');
    soup = BeautifulSoup(html, "lxml");
    tag_a = soup.select(".user_name")
    for tag in tag_a :
        list2.append(tag.get("title"))
    list_name=list(set(list2)) 
    return  list_name 

def gettbname(username):
    url_gz = "http://www.baidu.com/p/username?from=tieba"
    page = urllib.request.urlopen(url_gz.replace("username", username))  
    html = page.read().decode("UTF-8")
    html=html.replace('\\x22',"'")
    html=BeautifulSoup(html, "lxml") ;
    pattern = re.compile(r'target=_blank title=\'(.*?)\'>')
    list1=pattern.findall(html.prettify())
    return list1         

def counttb(list1):
    counts = { }           
    for x in list1:    
        print(x)                  
        for tb in x:
            if  tb in counts:
                counts[tb] += 1
            else:
                counts[tb] = 1
    return counts 

def counttb_Pool(tblist):
    counts = { }           
    for x in tblist: 
        tb_list=x.get()   
        for tb in tb_list:
            if  tb in counts:
                counts[tb] += 1
            else:
                counts[tb] = 1
    return counts 

 
if __name__ == "__main__":
    t1 = time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1)))
    result = []
    pool = multiprocessing.Pool(processes=20)
    for page in range(1,100):
        time.sleep(0.1)
        result.append(pool.apply_async(getMemberList_PAGE,(page,))) 
    pool.close()
    pool.join()
    print("Name got!")
    result2 = []
    pool2 = multiprocessing.Pool(processes=24) 
    for list_name in result:
        list_name1 = list_name.get()
        for n in list_name1 : 
            time.sleep(0.1)
            result2.append(pool2.apply_async(gettbname,(n,))) 
    pool2.close()
    pool2.join()
    print("Begin counting!")
    print(len(result2))
    print(counttb_Pool(result2))
    t2 = time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t2)))
    print(t2-t1)
#     for tb_name in result2:
#         tb_name1 = tb_name.get()
#         print(tb_name1)
        