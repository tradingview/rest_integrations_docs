import os
from bs4 import BeautifulSoup



def finder():
    names = os.listdir(os.getcwd())
    if 'build' in names:
        for root, dirs, files in os.walk(os.getcwd() + '/build/html', topdown=False):
            for name in files:
                if name.endswith('.html'):
                    print(os.path.join(root, name))
                    f = open(os.path.join(root, name), 'r+')
                    my_str = f.read()
                    f.seek(0)
                    my_str = build_ref(my_str)
                    f.write(my_str)
            for _ in dirs:
                continue


def build_ref(str_html):
    local_html = str_html
    soup = BeautifulSoup(local_html, 'lxml')
    arr = soup.find_all("a")
    for tag in arr:
        str_tag = str(tag)
        if ("class=\"reference external\"" in str_tag
                and check_list(str_tag)
                and str_tag.find("nofollow", 0, len(str_tag)) == -1):
            old_tag = str_tag
            tag['rel'] = 'nofollow'
            local_html = local_html.replace(old_tag, str(tag))
    return local_html


find_list = ["tradingview.com"]  # add site who ignored nofollow


def check_list(str_tag):
    for site_name in find_list:
        if str_tag.find(site_name, 0, len(str_tag)) != -1:
            return False
    return True


if __name__ == '__main__':
    finder()
