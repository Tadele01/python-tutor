import requests

def gen_from_urls(urls: tuple) -> tuple:
    for resp in(requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
value = gen_from_urls(urls)
