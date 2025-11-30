import asyncio
import os
from agent_framework import ChatAgent, MCPStreamableHTTPTool
from agent_framework_azure_ai import AzureAIAgentClient
from azure.ai.agentserver.agentframework import from_agent_framework
from azure.identity.aio import DefaultAzureCredential

def get_agent() -> ChatAgent:
    """Create and return a ChatAgent with Bing Grounding search tool."""
    assert "AZURE_AI_PROJECT_ENDPOINT" in os.environ, (
        "AZURE_AI_PROJECT_ENDPOINT environment variable must be set."
    )
    assert "AZURE_AI_MODEL_DEPLOYMENT_NAME" in os.environ, (
        "AZURE_AI_MODEL_DEPLOYMENT_NAME environment variable must be set."
    )

    chat_client = AzureAIAgentClient(
        endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        async_credential=DefaultAzureCredential(),
    )

    # Create ChatAgent with the Bing search tool
    agent = ChatAgent(
        chat_client=chat_client,
        name="msft-learn-mcp-agent",
        instructions="You are a helpful assistant that can help with microsoft documentation questions.",
        tools=MCPStreamableHTTPTool(
            name="Microsoft Learn MCP",
            url="https://learn.microsoft.com/api/mcp",
        ),
    )
    return agent

if __name__ == "__main__":
    from_agent_framework(get_agent()).run()
