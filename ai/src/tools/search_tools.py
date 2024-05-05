import json
import os
import requests
from langchain.tools import tool


class SearchTools:

    @tool("Search the internet")
    def search_internet(query):
        """
        Useful to search the internet for information about a given topic,
        including results relevant to specific travel dates.

        Args:
            query (str): The search query string to find relevant results.

        Returns:
            str: Relevant search results in a formatted string.
        """
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)

        # Check if there's an 'organic' key in the response
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-----------------"
                    ]))
                except KeyError:
                    continue

            return '\n'.join(string)
