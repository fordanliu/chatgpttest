import os
import openai

# Load your API key from an environment variable or secret management service
#openai.api_key = os.getenv("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")
openai.api_key = "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"


response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7,
                                    echo=True)

# openai api completions.create -m text-davinci-003 -p "Say this is a test" -t 0 -M 7 --stream
# print(response.choices[0].text)

print(response.choices[0].text)