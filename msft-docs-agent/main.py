import os
from agent_framework import ChatAgent, MCPStreamableHTTPTool
from agent_framework.azure import AzureAIAgentClient
from azure.ai.agentserver.agentframework import from_agent_framework
from azure.identity import DefaultAzureCredential

def get_agent():
    """Create and return a ChatAgent with Microsoft Learn MCP tool."""
    assert "AZURE_AI_PROJECT_ENDPOINT" in os.environ, (
        "AZURE_AI_PROJECT_ENDPOINT environment variable must be set."
    )
    assert "AZURE_AI_MODEL_DEPLOYMENT_NAME" in os.environ, (
        "AZURE_AI_MODEL_DEPLOYMENT_NAME environment variable must be set."
    )

    chat_client = AzureAIAgentClient(
        endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential(),
    )
    
    agent = ChatAgent(
        chat_client=chat_client,
        name="msft-learn-mcp-agent",
        instructions="You are a helpful assistant that can help with microsoft documentation questions.",
        tools=[
            MCPStreamableHTTPTool(
                name="Microsoft Learn MCP",
                url="https://learn.microsoft.com/api/mcp",
            )
        ],
    )
    return agent

if __name__ == "__main__":
    agent = get_agent()
    from_agent_framework(agent).run()