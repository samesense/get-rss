import get_rss


def test_nature():
    url = "https://www.nature.com/cgt/"
    rss_url = "https://www.nature.com/cgt.rss"
    model = "meta-llama/Llama-3.3-70B-Instruct"
    cand_url = get_rss.get_rss(url, model)
    assert cand_url == rss_url
