import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def ddg_search(query, num=10):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        results = []
        matches = re.findall(r'<a class="result__url" href="([^"]+)".*?<h2 class="result__title">.*?<a[^>]*>(.*?)</a>.*?<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL)
        if not matches:
            titles = re.findall(r'<h2 class="result__title">\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
            snippets = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL)
            for i in range(min(len(titles), len(snippets))):
                link, title = titles[i]
                snippet = snippets[i]
                title = re.sub(r'<[^>]+>', '', title).strip()
                snippet = re.sub(r'<[^>]+>', '', snippet).strip()
                results.append((title, snippet, link))
        else:
            for link, title, snippet in matches:
                title = re.sub(r'<[^>]+>', '', title).strip()
                snippet = re.sub(r'<[^>]+>', '', snippet).strip()
                results.append((title, snippet, link))
        return results[:num]
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

queries = [
    "mạng xã hội việt nam nóng nhất hôm nay",
    "threads việt nam tranh cãi hot",
    "facebook việt nam xu hướng bão lũ sao kê",
    "tiktok việt nam trend nóng",
    "tin nóng mạng xã hội việt nam"
]

with open("d:/Antigravity+Codex/Hop_Den_Tri_Thuc/.system_generated/search_out.txt", "w", encoding="utf-8") as out:
    for q in queries:
        out.write(f"\n==================== {q} ====================\n")
        res = ddg_search(q, 5)
        for title, snippet, link in res:
            out.write(f"TITLE: {title}\nSNIP: {snippet}\nLINK: {link}\n---\n")

print("Done writing to search_out.txt")
