import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/danielamitay/api/app-stores'

mcp = FastMCP('app-stores')

@mcp.tool()
def user_reviews(store: Annotated[str, Field(description='The app store that you would like to retrieve results from (apple or google)')],
                 id: Annotated[str, Field(description='The identifier for the application you would like to retrieve reviews for')],
                 language: Annotated[Union[str, None], Field(description='The two-letter code for the language you want results in (ISO-639-1). Optional')] = None) -> dict: 
    '''Fetch the most recent user reviews for a given application'''
    url = 'https://app-stores.p.rapidapi.com/reviews'
    headers = {'x-rapidapi-host': 'app-stores.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'store': store,
        'id': id,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def app_details(store: Annotated[str, Field(description='The app store that you would like to retrieve results from (apple or google)')],
                id: Annotated[str, Field(description='The identifier for the application you would like to retrieve results for')],
                language: Annotated[Union[str, None], Field(description='The two-letter code for the language you want results in (ISO-639-1). Optional')] = None) -> dict: 
    '''Fetch app store details for a given application'''
    url = 'https://app-stores.p.rapidapi.com/details'
    headers = {'x-rapidapi-host': 'app-stores.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'store': store,
        'id': id,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def app_search(store: Annotated[str, Field(description='The app store that you would like to retrieve reviews from (apple or google)')],
               term: Annotated[str, Field(description='The search term you would like to retrieve app results for')],
               language: Annotated[Union[str, None], Field(description='The two-letter code for the language you want results in (ISO-639-1). Optional')] = None) -> dict: 
    '''Fetch the list of search results for a given term'''
    url = 'https://app-stores.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'app-stores.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'store': store,
        'term': term,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete(store: Annotated[str, Field(description='The app store that you would like to retrieve reviews from (apple or google)')],
                 term: Annotated[str, Field(description='The search term you would like to retrieve autocomplete results for')],
                 language: Annotated[Union[str, None], Field(description='The two-letter code for the language you want results in (ISO-639-1). Optional')] = None) -> dict: 
    '''Fetch a list of autocomplete terms for a given search term'''
    url = 'https://app-stores.p.rapidapi.com/autocomplete'
    headers = {'x-rapidapi-host': 'app-stores.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'store': store,
        'term': term,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
