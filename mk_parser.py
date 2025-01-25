from typing import Dict, List

import feedparser
from smolagents import CodeAgent, HfApiModel, tool


# @tool
def get_rss_feed_items(url: str) -> List[Dict[str, str]]:
    """
    Fetches the first 10 items from an RSS feed.

    Args:
        url: The URL of the RSS feed.

    Returns:
        list: A list of dictionaries containing title and link of the first 10 items.
    """
    # Parse the RSS feed
    feed = feedparser.parse(url)

    if feed.bozo:
        raise ValueError("Failed to parse RSS feed. Please check the URL.")

    # Extract the first 10 items
    items = []
    for entry in feed.entries[:10]:
        # description = entry["summary_detail"]
        # description2 = entry["summary"].text
        # print(description2)
        items.append(entry)

    return items


rss_url = "https://www.nature.com/cgt.rss"
rss_items = get_rss_feed_items(rss_url)
processed_items = []
for item in rss_items:
    print(list(item.keys()))
    print(item["content"])
    processed_item = {
        "title": item["title"],
        "link": item["link"],
        "description": item["summary"],
    }
    processed_items.append(processed_item)
# print(processed_items)

# url = "https://www.nature.com/cgt/"
# rss_url = "https://www.nature.com/cgt.rss"
# # model_id = "meta-llama/Llama-3.3-70B-Instruct"
# #
# # model = HfApiModel(model_id=model_id, token="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")
# # agent = CodeAgent(tools=[], model=model, add_base_tools=True)
# #
# # agent.run(
# #     "Could you give me the 118th number in the Fibonacci sequence?",
# # )
#
# # model = LiteLLMModel(model_id="ollama_chat/llama3.2", api_key="ollama")
# m = "meta-llama/Llama-3.3-70B-Instruct"
# model = HfApiModel(model_id=m)
# agent = CodeAgent(
#     tools=[get_rss_feed_items],
#     model=model,
#     additional_authorized_imports=["requests", "bs4"],
# )
# agent.run(
#     f"This is an rss url: {rss_url}. Give me python code that takes results from get_rss_feed_items, and returns a list of dictionaries. Each dictionary will title, link, and description/abstract."
# )
