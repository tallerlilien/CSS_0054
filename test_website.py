import pytest

def test_html_title():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<title>Feladat 0054</title>' in content, "A címsor nem tartalmazza a 'Feladat 0054' szót!"

def test_html_structure():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<div class="container">' in content, "A body elem nem tartalmazza a div.container elemet!"
        assert '<div class="left-background">' in content, "A container nem tartalmazza a left-background div-et!"
        assert '<div class="content">' in content, "A container nem tartalmazza a content div-et!"
        assert '<div class="right-background">' in content, "A container nem tartalmazza a right-background div-et!"

def test_css_container_style():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '.container {' in content, "Nincs .container osztály a CSS-ben!"
        assert 'display: flex;' in content, "A .container osztály nem tartalmaz 'display: flex' tulajdonságot!"
        assert 'width: 80%;' in content, "A .container osztály nem tartalmaz 80%-os szélességet!"

def test_css_background_style():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '.left-background {' in content, "Nincs .left-background osztály a CSS-ben!"
        assert 'background-image: url("bal_hatterkep.png");' in content, "A .left-background osztály nem tartalmazza a bal_hatterkep.png képet!"
        assert '.right-background {' in content, "Nincs .right-background osztály a CSS-ben!"
        assert 'background-image: url("jobb_hatterkep.png");' in content, "A .right-background osztály nem tartalmazza a jobb_hatterkep.png képet!"

def test_css_content_style():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '.content {' in content, "Nincs .content osztály a CSS-ben!"
        assert 'text-align: center;' in content, "A .content osztály nem tartalmazza a 'text-align: center' tulajdonságot!"
        assert 'flex: 1;' in content, "A .content osztály nem tartalmazza a 'flex: 1' tulajdonságot!"