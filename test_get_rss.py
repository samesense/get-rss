import get_rss


def test_nature():
    url = "https://www.nature.com/cgt/"
    rss_url = "https://www.nature.com/cgt.rss"
    model = "meta-llama/Llama-3.3-70B-Instruct"
    cand_url = get_rss.get_rss(url, model)
    assert cand_url == rss_url


def test_mdpi():
    url = "https://www.mdpi.com/journal/genes"
    rss_url = "https://www.mdpi.com/rss/journal/genes"
    model = "meta-llama/Llama-3.3-70B-Instruct"
    cand_url = get_rss.get_rss(url, model)
    assert cand_url == rss_url


def sciencedirect():
    url = "https://www.sciencedirect.com/journal/cell-reports"
    rss_url = "https://rss.sciencedirect.com/publication/science/22111247"
    model = "meta-llama/Llama-3.3-70B-Instruct"
    cand_url = get_rss.get_rss(url, model)
    assert cand_url == rss_url
