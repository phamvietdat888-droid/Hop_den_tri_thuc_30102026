import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def search_bing(query):
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'
    })
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        # match items
        items = re.findall(r'<li class="b_algo".*?<h2><a[^>]+href="([^"]+)"[^>]*>(.*?)</a></h2>.*?<p class="b_lineclamp[^"]*"[^>]*>(.*?)</p>', html, re.DOTALL)
        if not items:
            items = re.findall(r'<li class="b_algo".*?<h2><a[^>]+href="([^"]+)"[^>]*>(.*?)</a></h2>.*?(?:<p>(.*?)</p>|<div class="b_caption"><p>(.*?)</p>)', html, re.DOTALL)
            clean_items = []
            for it in items:
                link = it[0]
                title = it[1]
                snippet = it[2] if len(it) > 2 and it[2] else (it[3] if len(it) > 3 else '')
                clean_items.append((link, title, snippet))
            items = clean_items
        
        results = []
        for it in items:
            link = it[0]
            title = re.sub(r'<[^>]+>', '', it[1]).strip()
            snippet = re.sub(r'<[^>]+>', '', it[2]).strip()
            results.append((title, snippet, link))
        return results
    except Exception as e:
        return [('Error', str(e), '')]

queries = [
    "mạng xã hội facebook việt nam xu hướng nóng nhất hôm nay",
    "threads việt nam bài viết thảo luận nhiều nhất",
    "tiktok việt nam trend bùng nổ",
    "vụ việc gây tranh cãi mạng xã hội việt nam",
    "bão lũ sạt lở sao kê mạng xã hội",
    "tin nóng giới trẻ threads facebook việt nam"
]

with open("d:/Antigravity+Codex/Hop_Den_Tri_Thuc/.system_generated/bing_results.txt", "w", encoding="utf-8") as f:
    for q in queries:
        f.write(f"\n==================== QUERY: {q} ====================\n")
        res = search_bing(q)
        for t, s, l in res[:6]:
            f.write(f"TITLE: {t}\nSNIP: {s}\nLINK: {l}\n---\n")

print("Finished search")
