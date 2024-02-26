import openai

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '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'
openai.api_key = api_key

# Get user input
user_input = input("Enter your prompt: ")

# Define the completion parameters
completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
        )
# Print the API response
print("Response from ChatGPT:")
print(completion['choices'][0]['message']['content'])

