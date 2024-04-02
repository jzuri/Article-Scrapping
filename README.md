# Article-Scrapping
Jazmyn Zurita
Project 1 - 3 

## Breakdown:
main.py - holds the base code for the article scrapping
articles_urls.txt - holds urls to be scraped
articles.txt - holds scraped article data

## Instructions:
1. To scrap articles, posts the urls in the article_url.txt file
2. Each article url will need to have its own line
3. Run main.py after url links are entered
4. Scraped articles will be places in the articles.txt file
5. If scraped successfully, "Article scraped" will be printed
6. If scraped unsuccessfully, "Just go ahead and change your major =P" will be printed
7. Idk why i decided to put that print line, just wanted to be funny I guess

# LLM API Breakdown
## Creating a LLM API account
In order to use the Large Language Model (LLM) API, you must create an OpenAI account.

 1. Go to the OpenAI website (https://openai.com) and sign up for an account by using an email and creating a password
 2. Once your account is created, navigate to the API section by clicking on your profile in the top right corner and clicking "API" from the menu dropdown

## Generating an API Key
After creating an account with OpenAI, you can generate an API key to make your requests to the LLM API.

1. In the API section, click on "API Keys" in the left sidebar
2. Click on the "Create API Key" button.
3. Enter a name for your API key and click on "Create API Key"
4. Copy the generated API key and paste it somewhere secure

## How to make an API call
```
import openai
# Note: For this program 'YOUR_API_KEY' should be replaced with your own unique API key!!!

# Set your API key
# Initializing OpenAI library with your API key

api_key = 'YOUR_API_KEY'
openai.api_key = api_key

# Prompt example
ex_prompt = "C's may or may not get degrees???"

# Make an API call to generate text based on the prompt example
result = openai.Completion.create(
    engine = "text-davinci-003",
    ex_prompt = ex_prompt,
    max_tokens = 50
)

# Print the generated text
print(result.choices[0].text.strip())
```






  
