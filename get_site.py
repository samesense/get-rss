from playwright.sync_api import sync_playwright


def get_html(url: str) -> str:
    custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.6; rv:129.0) Gecko/20100101 Firefox/129.0"
    with sync_playwright() as p:
        # Launch a headless browser
        browser = p.firefox.launch(headless=True)
        context = browser.new_context(user_agent=custom_user_agent)
        page = context.new_page()
        page.set_default_timeout(60000)  # Set timeout to 60 seconds

        page.goto(url)
        html = page.content()
        browser.close()

    return html
