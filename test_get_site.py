import get_site


def test_get_html_sciencedirect():
    url = "https://www.sciencedirect.com/journal/cell-reports"
    html = get_site.get_html(url)
    with open("h.html", "w") as fout:
        print(html, file=fout)
    assert "application/rss+xml" in html


def test_get_html_mdpi():
    url = "https://www.mdpi.com/journal/genes"
    html = get_site.get_html(url)
    with open("h2.html", "w") as fout:
        print(html, file=fout)
    assert "rss/journal/genes" in html
