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


# url = "https://www.nature.com/cgt/"
# url = "https://www.mdpi.com/journal/genes"
# url = "https://www.science.org/journal/stm"
# url = "https://www.cell.com/cell-systems/home"
# url = "https://www.sciencedirect.com/journal/cell-reports"
# model_id = "meta-llama/Llama-3.3-70B-Instruct"
#
# model = HfApiModel(model_id=model_id, token="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")
# agent = CodeAgent(tools=[], model=model, add_base_tools=True)
#
# agent.run(
#     "Could you give me the 118th number in the Fibonacci sequence?",
# )

# model = LiteLLMModel(model_id="ollama_chat/llama3.2", api_key="ollama")
# m = "describeai/gemini-small"
# m = "meta-llama/Llama-3.3-70B-Instruct"
# m = "microsoft/phi-4"


def get_rss(url: str, model: str):
    model = HfApiModel(model_id=model)
    agent = CodeAgent(
        tools=[download_website, url_exists],
        model=model,
        additional_authorized_imports=["bs4", "requests", "playwright", "urllib"],
    )
    o = agent.run(
        f"Get the url of the rss url for the journal hosted at '{url}'. Only give me the rss url. Use download_website to get the html of the journal website. Use url_exists to test the rss url before giving it to me. Try looking at all urls provided in the html, and check to see if they mention rss."
    )
    # You might need to look in data-react-helmet elements.
    # print("debug", o)
    # print(dir(o))
    # print(o.content)
    return o.content


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
    print(rss_url)


if __name__ == "__main__":
    main()
