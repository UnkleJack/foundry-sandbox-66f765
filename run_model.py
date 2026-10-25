from anthropic import AnthropicFoundry
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://unklejackclaude4vscode-resource.services.ai.azure.com/anthropic"
deployment_name = "claude-sonnet-5"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = AnthropicFoundry(
    azure_ad_token_provider=token_provider,
    base_url=endpoint
)

message = client.messages.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=1024,
)

print(message.content)