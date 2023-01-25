import feedparser
import json

Notice_rss = feedparser.parse("https://cse.pusan.ac.kr/bbs/cse/2605/rssList.do?row=50")

with open("Notice_recent.json", "w") as f:
    f.write(json.dumps(Notice_rss, ensure_ascii=False))
    
with open("./Notice_recent.json", 'r') as f:
    json_data = json.load(f)
    #json_data = json.dumps(json_data, ensure_ascii=False)
    
print(json_data["entries"][0])
