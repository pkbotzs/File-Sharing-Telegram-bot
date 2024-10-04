#anshvachhani
from shortzy import Shortzy


SHORTNER_MODE = True 
SHORTNER_URL = "https://modijiurl.com"
SHORTNER_API = "6a0a4f826e12f701a433063ebbe730caa1c29c38"

async def short_link(link):
    if not SHORTNER_MODE:
        return link

  
    api_key = SHORTNER_API
    base_site = SHORTNER_URL

    if not (api_key and base_site):
        return link

    shortzy = Shortzy(api_key, base_site)
    short_link = await shortzy.convert(link)  

    return short_link
