#!/usr/bin/env python

import os
import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

def login():
    ''' Logs in to page setting session cookie and returning session.
    Remember to close session when you're done with it.
    The 'username' and 'password' environment variables must be set
    or exceptions will be thrown. '''

    # raise exception if username environment variable isn't set
    if "username" in os.environ:
        username = os.environ["username"]
    else:
        raise Exception("username environment variable not set")

    # raise exception if passwrd environment variable isn't set
    if "password" in os.environ:
        password = os.environ["password"]
    else:
        raise Exception("password environment variable not set")

    form_data = {
        "amember_login" : username,
        "amember_pass" : password,
        "amember_redirect_url": "https://www.footballguys.com"
    }

    login_url = "https://subscribers.footballguys.com/amember/login.php"
    s = requests.Session()
    r = s.post(login_url, data=form_data, allow_redirects=False)
    r.raise_for_status()
    return s

def retrieve_table(url, class_):
    ''' Logs in and retrieve requested page. Returns a string
    that contains the HTML markup of the table with css class 'class_' '''
    s = login()
    r = s.get(url)
    r.raise_for_status()
    s.close()
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find("table", class_=class_)
    return str(result)

def make_page(env, table):
    ''' Will render the table into the page template'''
    template = env.get_template("page.html")
    return template.render(table=table)

def main():
    env = Environment(loader=FileSystemLoader("templates"))
    #url = 'https://subscribers.footballguys.com/apps/article.php?article=2018-lineup-optimizer-fanduel-week12'
    url = 'https://subscribers.footballguys.com/apps/article.php?article=2018-vegas-value-chart-week12'
    table = retrieve_table(url, "datasmall")
    print(table)
    #page = make_page(table)

if __name__ == '__main__':
    main()
