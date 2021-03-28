import feedparser
import json


def test_func(url):
    one_page_dict = feedparser.parse(url)  # 解析得到的是一个字典
    print(json.dumps(one_page_dict, indent=4, ensure_ascii=False))  # 缩进4空格，中文字符不转义成Unicode
    pass


def main():
    FEED_URL = ['https://news.ycombinator.com/rss', 'http://feeds.bbci.co.uk/news/rss.xml']
    test_func(FEED_URL[0])


if __name__ == '__main__':
    main()
