import pandas as pd
import requests
import openai
openai.api_key
# Read the CSV file

def generate_answer(message):
    try:

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
        )

    # completion = openai.Completion.create(
    # model="text-davinci-003",
    # prompt=message,
    # max_tokens=100,
    # temperature=0,
    # n=1,

    
    # stop = None
    # )
        print(completion)
        #return completion.choices[0].message['content']
    except:
        print("error in message generation")


data = pd.read_csv('cosmetics.csv')

# Separate cosmetics and ingredients
cosmetics = data['Cosmetics'].tolist()
ingredients = data['Ingredients'].tolist()

# Define your OpenAI GPT-3 API credentials
openai.api_key = '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'
username = 'rakesh9985'

# Loop through each cosmetic and ask the ChatGPT API about the ingredients
for cosmetic, ingredient_list in zip(cosmetics, ingredients):
    # Connect to the ChatGPT API
    endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
    

    # Ask if the ingredients are harmful
    prompt = f"I have a cosmetic product called '{cosmetic}' with ingredients: {ingredient_list}. Are these ingredients harmful?"
    """data = {
        'prompt': prompt,
        'max_tokens': 100
    }"""

    # Make the request to ChatGPT API
    response=generate_answer(prompt)
    #response = requests.post(endpoint, headers=headers, json=data)
    
    """if response.status_code == 200:
        answer = response.json()['choices'][0]['text'].strip()
        print(f"Q: {prompt}\nA: {answer}\n")
    else:
        print("Failed to get a response from the ChatGPT API.")
"""
    print(response)
