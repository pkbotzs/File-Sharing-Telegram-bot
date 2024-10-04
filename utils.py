#anshvachhani
from shortzy import Shortzy  # Import your link shortening class



async def short_link(link):
    if not SHORTNER_MODE:  # Skip shortening if mode is off
        return link

    # Ensure API key and base URL are available
    api_key = SHORTNER_API
    base_site = SHORTNER_URL

    if not (api_key and base_site):
        return link  # Return original link if API key or URL is missing

    shortzy = Shortzy(api_key, base_site)  # Initialize shortener
    short_link = await shortzy.convert(link)  # Shorten the link

    return short_link
