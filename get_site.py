from playwright.sync_api import sync_playwright

# custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36"
# custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"
#
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4; rv:118.0) Gecko/20100101 Firefox/118.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36 Edg/117.0.2045.60",
# ]
#
# custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.6; rv:129.0) Gecko/20100101 Firefox/129.0"


def get_html(url: str) -> str:
    with sync_playwright() as p:
        # Launch a headless browser
        # browser = p.chromium.launch(headless=True)
        browser = p.firefox.launch(headless=True)
        context = browser.new_context(user_agent=custom_user_agent)
        page = context.new_page()
        page.set_default_timeout(60000)  # Set timeout to 60 seconds

        # Open the website
        page.goto(url)

        # Wait for the JavaScript to finish loading (if necessary)
        # page.wait_for_load_state("networkidle")

        # Get the HTML content
        html = page.content()

        # Close the browser
        browser.close()

    return html
