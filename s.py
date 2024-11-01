import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/e55398db69ed9e0f5c8fa16cd4b486b7/ai/run/"
headers = {"Authorization": "Bearer 8VI1W4BKlrtng_xTxO1c8jl2pmyL1oEjXH5gXyNF"}

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
];
output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output)