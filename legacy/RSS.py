import feedparser
import schedule
import json

def Load(Case):
    if Case == "Notice" :
        with open("./Notice_recent.json", 'r') as f:
            rss = json.load(f)
            #rss = json.dumps(rss, ensure_ascii=False)
    
    elif Case == "Free" :
        with open("./Free_recent.json", 'r') as f:
            rss = json.load(f)
            #rss = json.dumps(rss, ensure_ascii=False)
    
    elif Case == "Employment" :
        with open("./Employment_recent.json", 'r') as f:
            rss = json.load(f)
            #rss = json.dumps(rss, ensure_ascii=False)
    
    else:
        with open("./Contest_recent.json", 'r') as f:
            rss = json.load(f)
            #rss = json.dumps(rss, ensure_ascii=False)
    
    f.close()
    
    return rss

def Save(Case):
    if Case == "Notice" :
        Notice_rss = feedparser.parse("https://cse.pusan.ac.kr/bbs/cse/2605/rssList.do?row=50")
        with open("./Notice_recent.json", 'w') as f:
            f.write(json.dumps(Notice_rss, ensure_ascii=False))
    
    elif Case == "Free" :
        Free_rss = feedparser.parse("https://cse.pusan.ac.kr/bbs/cse/2618/rssList.do?row=50")
        with open("./Free_recent.json", 'w') as f:
            f.write(json.dumps(Free_rss, ensure_ascii=False))
    
    elif Case == "Employment" :
        Employment_rss = feedparser.parse("https://cse.pusan.ac.kr/bbs/cse/2616/rssList.do?row=50")
        with open("./Employment_recent.json", 'w') as f:
            f.write(json.dumps(Employment_rss, ensure_ascii=False))
            
    
    else:
        Contest_rss = feedparser.parse("https://cse.pusan.ac.kr/bbs/cse/12278/rssList.do?row=50")
        with open("./Contest_recent.json", 'w') as f:
            f.write(json.dumps(Contest_rss, ensure_ascii=False))
    
    f.close()
    

try:
    Save("Notice")
    Save("Free")
    Save("Employment")
    Save("Contest")
    
    Notice_rss = Load("Notice")
    Free_rss = Load("Free")
    Employment_rss = Load("Employment")
    Contest_rss = Load("Contest")

except:
    Notice_rss = Load("Notice")
    Free_rss = Load("Free")
    Employment_rss = Load("Employment")
    Contest_rss = Load("Contest")
    
Notice_present_state = Notice_rss["entries"][0]
Free_present_state = Free_rss["entries"][0]
Employment_present_state = Employment_rss["entries"][0]
Contest_presnet_state = Contest_rss["entries"][0]

def Notice():
    print("공지사항")
    global Notice_present_state
    try:
       Save("Notice")
    except:
        pass
    Notice_new_rss = Load("Notice")
    Notice_new_state = Notice_new_rss["entries"][0]
    if Notice_present_state != Notice_new_state:
        date = f'{Notice_new_state.published_parsed.tm_year}-{Notice_new_state.published_parsed.tm_mon}-{Notice_new_state.published_parsed.tm_mday}'
        print("공지사항\n")
        print(f'{date}\n{Notice_new_state.title}\n{Notice_new_state.link}')
        Notice_present_state = Notice_new_state
            
def Free():
    print("자유\n")
    global Free_present_state
    try:
       Save("Free")
    except:
        pass
    Free_new_rss = Load("Free")
    Free_new_state = Free_new_rss["entries"][0]
    if Free_present_state != Free_new_state:
        date = f'{Free_new_state.published_parsed.tm_year}-{Free_new_state.published_parsed.tm_mon}-{Free_new_state.published_parsed.tm_mday}'
        print("자유 게시판\n")
        print(f'{date}\n{Free_new_state.title}\n{Free_new_state.link}')
        Free_present_state = Free_new_state
        
def Employoment():
    print("채용\n")
    global Employment_present_state
    try:
       Save("Employment")
    except:
        pass
    Employment_new_rss = Load("Employment")
    Employment_new_state = Employment_new_rss["entries"][0]
    if Employment_present_state != Employment_new_state:
        date = f'{Employment_new_state.published_parsed.tm_year}-{Employment_new_state.published_parsed.tm_mon}-{Employment_new_state.published_parsed.tm_mday}'
        print("채용 게시판\ n")
        print(f'{date}\n{Employment_new_state.title}\n{Employment_new_state.link}')
        Employment_present_state = Employment_new_state
        
def Contest():
    print("경진대회\n")
    global Contest_present_state
    try:
       Save("Contest")
    except:
        pass
    Contest_new_rss = Load("Contest")
    Contest_new_state = Contest_new_rss["entries"][0]
    if Contest_presnet_state != Contest_new_state:
        date = f'{Contest_new_state.published_parsed.tm_year}-{Contest_new_state.published_parsed.tm_mon}-{Contest_new_state.published_parsed.tm_mday}'
        print("경진대회 게시판\n")
        print(f'{date}\n{Contest_new_state.title}\n{Contest_new_state.link}')
        Contest_present_state = Contest_new_state
        
schedule.every(10).seconds.do(Contest)
schedule.every(15).seconds.do(Employoment)
schedule.every(20).seconds.do(Free)
schedule.every(25).seconds.do(Notice)

while True:
    schedule.run_pending()
