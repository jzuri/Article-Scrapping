"""
Module for interacting with the LLM (Large Language Model) API.
"""

import openai                                            # OpenAI library 

class LLMClient:
    def __init__(self, api_key):                         # Constructor for LLMClient class.
        self.api_key = api_key  
        openai.api_key = api_key                         # Setting the API key for OpenAI library

    def summarized_article(self, result):                # Generate a summarized version of the article using the LLM API.
        summary = ""                                     # Initialize summary to an empty string
        response = openai.ChatCompletion.create(         # Making a request to generate a concise article
            model="gpt-3.5-turbo-0613",                  # Model used for request
            messages=[                                   # Providing a message as input to the model
                {
                    "role": "system",
                    "content": "Result: " + result       # Adding the prompt as content
                }
            ],
            max_tokens=250                               # Limiting the maximum number of tokens (words) in the generated response
        )
