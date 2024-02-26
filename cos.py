import pandas as pd
import requests

# Read the Excel file
data = pd.read_excel('your_excel_file.xlsx')

# Separate cosmetics and ingredients
cosmetics = data['Cosmetics'].tolist()
ingredients = data['Ingredients'].tolist()

# Loop through each cosmetic and ask the ChatGPT API about the ingredients
for cosmetic, ingredient_list in zip(cosmetics, ingredients):
    # Connect to the ChatGPT API
    endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_KEY'  # Replace with your API key
    }

    # Ask if the ingredients are harmful
    prompt = f"I have a cosmetic product called '{cosmetic}' with ingredients: {ingredient_list}. Are these ingredients harmful?"
    data = {
        'prompt': prompt,
        'max_tokens': 100
    }

    # Make the request to ChatGPT API
    response = requests.post(endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        answer = response.json()['choices'][0]['text'].strip()
        print(f"Q: {prompt}\nA: {answer}\n")
    else:
        print("Failed to get a response from the ChatGPT API.")
