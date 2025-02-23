import click
import requests
from smolagents import CodeAgent, HfApiModel, tool

import get_site


@tool
def download_website(url: str) -> str:
    """
    This is a tool that returns the html of the site at the url.

    Args:
        url: The url of the website to download.

    Returns:
        str: HTML from the url
    """
    return get_site.get_html(url)


@tool
def url_exists(url: str) -> bool:
    """
    This is a tool to check if a URL exists by sending a HEAD request.

    Args:
        url: The URL to check.
        timeout: Timeout in seconds for the request.

    Returns:
        bool: True if the URL exists, False otherwise.
    """
    timeout = 2
    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)
        # Check if the HTTP status code indicates success (2xx or 3xx)
        return response.status_code < 400
    except requests.RequestException:
        # Any exception (e.g., connection error, timeout) means the URL doesn't exist
        return False


def get_rss(url: str, model: str):
    model = HfApiModel(model_id=model)
    agent = CodeAgent(
        tools=[download_website, url_exists],
        model=model,
        additional_authorized_imports=["bs4", "requests", "playwright", "urllib"],
    )
    o = agent.run(
        f"Get the url of the rss feed for the journal hosted at '{url}'. Only give me the rss url. Use download_website to get the html of the journal hosted at '{url}'. Use url_exists to test the rss url before giving it to me. If you get stuck, try looking at all urls provided in the journal html, and check to see if they mention rss. Some rss urls are presented relative to the base domain, so try adding the journal domain prefix when an rss url does not contain http or https. There is no need to visit the rss url. Do not give me a rss url that does not pass the url_exists check."
    )
    try:
        res = o.content
    except:
        res = o
    return res


@click.command()
@click.argument("url")
@click.option(
    "--model",
    "-m",
    default="meta-llama/Llama-3.3-70B-Instruct",
    help="Model to use for RSS detection. Default: meta-llama/Llama-3.3-70B-Instruct",
)
def main(url: str, model: str):
    rss_url = get_rss(url, model)
    print(f"rss-url: {rss_url}")


if __name__ == "__main__":
    main()
