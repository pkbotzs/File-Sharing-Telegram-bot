from shortzy import Shortzy

# Configuration variables
SHORTNER_MODE = True  # Set to True to enable link shortening
SHORTNER_URL = "https://modijiurl.com"  # Base URL for the shortening service
SHORTNER_API = "6a0a4f826e12f701a433063ebbe730caa1c29c38"  # Your API key

async def short_link(link):
    # If shortening is disabled, return the original link
    if not SHORTNER_MODE:
        return link

    api_key = SHORTNER_API  # Set your API key
    base_site = SHORTNER_URL  # Set your base site URL

    # Check if the API key and base URL are defined
    if not (api_key and base_site):
        return link  # Return original link if either is missing

    # Initialize the Shortzy object
    shortzy = Shortzy(api_key, base_site)

    try:
        # Attempt to shorten the link asynchronously
        short_link = await shortzy.convert(link)  
        return short_link  # Return the shortened link
    except Exception as e:
        print(f"Error shortening link: {e}")  # Log any errors
        return link  # Return the original link on error
