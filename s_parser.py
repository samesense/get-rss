from typing import Dict, List

import speedparser


def get_rss_feed_items(url: str) -> List[Dict[str, str]]:
    """
    Fetches the first 10 items from an RSS feed.

    Args:
        url: The URL of the RSS feed.

    Returns:
        list: A list of dictionaries containing title and link of the first 10 items.
    """
    # Parse the RSS feed
    feed = speedparser.parse(url)

    if feed.bozo:
        raise ValueError("Failed to parse RSS feed. Please check the URL.")

    # Extract the first 10 items
    items = []
    for entry in feed.entries[:10]:
        description = entry["summary_detail"]
        print(description)
        items.append(entry)

    return items


rss_url = "https://www.nature.com/cgt.rss"
rss_items = get_rss_feed_items(rss_url)
processed_items = []
for item in rss_items:
    print(list(item.keys()))
    i = 1 / 0
    processed_item = {
        "title": item["title"],
        "link": item["link"],
        "description": item["summary"],
    }
    processed_items.append(processed_item)
print(processed_items)
