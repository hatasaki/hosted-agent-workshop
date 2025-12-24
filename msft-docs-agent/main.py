import os
from agent_framework import ChatAgent, MCPStreamableHTTPTool
from agent_framework_azure_ai import AzureAIAgentClient
from azure.ai.agentserver.agentframework import from_agent_framework
from azure.identity import DefaultAzureCredential

def get_agent():
    """Create and return a ChatAgent with Bing Grounding search tool."""
    assert "AZURE_AI_PROJECT_ENDPOINT" in os.environ, (
        "AZURE_AI_PROJECT_ENDPOINT environment variable must be set."
    )
    assert "AZURE_AI_MODEL_DEPLOYMENT_NAME" in os.environ, (
        "AZURE_AI_MODEL_DEPLOYMENT_NAME environment variable must be set."
    )

    agent = AzureAIAgentClient(
        endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential(),
    ).create_agent(
        name="msft-learn-mcp-agent",
        instructions="You are a helpful assistant that can help with microsoft documentation questions.",
        tools=MCPStreamableHTTPTool(
            name="Microsoft Learn MCP",
            url="https://learn.microsoft.com/api/mcp",
        ),
    )
    return agent

if __name__ == "__main__":
    from_agent_framework(lambda _: get_agent()).run()