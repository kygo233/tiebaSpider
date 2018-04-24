
import queue
import threading
import time
from bs4 import BeautifulSoup 
import urllib.request
import re  
import multiprocessing
from multiprocessing import Pool
from time import sleep
    
def getMemberList_PAGE(pagenum):
    url_Member  = "http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%D0%DE%B3%B5tv"
    url_Member1 = "http://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%D0%DE%B3%B5tv&pn=pagenum"
    url_grxx = "http://www.baidu.com/p/username/detail"
    list2 = []
    url = url_Member1.replace("pagenum", str(pagenum));
    page = urllib.request.urlopen(url);
    html = page.read().decode('GBK');
    soup = BeautifulSoup(html, "lxml");
    tag_a = soup.select(".user_name")
    for tag in tag_a :
        list2.append(tag.get("title"))
    list_name=list(set(list2)) 
    print("Page "+str(pagenum)+":"+list_name)   
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

   

if __name__ == "__main__":
    results = []
    
    pool = multiprocessing.Pool(processes=10)
    for page in range(1,10):
        results.append(pool.apply_async(getMemberList_PAGE,(page,))) 
    pool.close()
    pool.join()
    
#     print (results[0].get()) 
#     result2 = []
#     pool2 = multiprocessing.Pool(processes=10) 
#     for num in range(0,len(results)):
#         if results[num]._success:
#             print ( results[num]._success) 
            
         
#         for n in results[num] : 
#             result2.append(pool2.apply_async(gettbname,(n,))) 
#     pool2.close()
#     pool2.join()
#     print (result2) 