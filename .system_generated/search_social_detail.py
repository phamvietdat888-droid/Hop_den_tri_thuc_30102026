import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

topics = [
    "tài xế công nghệ tắt app phản đối chiết khấu",
    "dự án lê thanh thản cư dân thanh hà mường thanh",
    "lạm thu đầu năm học 2026 trường học",
    "ngập lụt đà nẵng huế áp thấp nhiệt đới",
    "bẫy nợ mua iphone trả góp giới trẻ"
]

with open("d:/Antigravity+Codex/Hop_Den_Tri_Thuc/.system_generated/social_detail_search.txt", "w", encoding="utf-8") as out:
    for t in topics:
        out.write(f"\n==================== TOPIC: {t} ====================\n")
        q_url = f"https://news.google.com/rss/search?q={urllib.parse.quote(t)}&hl=vi&gl=VN&ceid=VN:vi"
        try:
            req = urllib.request.Request(q_url, headers={'User-Agent': 'Mozilla/5.0'})
            xml = urllib.request.urlopen(req, timeout=10).read()
            root = ET.fromstring(xml)
            for item in root.findall('.//item')[:5]:
                title = item.find('title').text if item.find('title') is not None else ''
                link = item.find('link').text if item.find('link') is not None else ''
                pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ''
                out.write(f"- {title} [{pubDate}]\n  Link: {link}\n")
        except Exception as e:
            out.write(f"Error: {e}\n")

print("Done social detail search")
