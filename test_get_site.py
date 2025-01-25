import get_site


def test_get_html():
    url = "https://www.sciencedirect.com/journal/cell-reports"
    html = get_site.get_html(url)
    with open("h.html", "w") as fout:
        print(html, file=fout)
    assert "application/rss+xml" in html
