# Microsoft Foundry Hosted Agent Workshop

This repository contains a starter template for building an Microsoft Foundry that hosts AI agents using the Microsoft Foundry Hosted Agent Service.

## Getting Started

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/hatasaki/hosted-agent-workshop.git
cd hosted-agent-workshop
```

### Prerequisites

* Install [azd](https://aka.ms/install-azd)
  * Windows: `winget install microsoft.azd`
  * Linux: `curl -fsSL https://aka.ms/install-azd.sh | bash`
  * MacOS: `brew tap azure/azd && brew install azd`

### Quickstart

0. Create new directory and navigate into it:

    ```shell
    mkdir my-hosted-agent
    cd my-hosted-agent
    ```

1. Bring down the template code:

    ```shell
    azd init -t https://github.com/Azure-Samples/azd-ai-starter-basic
    ```
    - input your unique project name when prompted. Ex. `<username>-hosted-agent`

    This will perform a git clone

2. Sign into your Azure account:

    ```shell
    azd auth login
    ```

3. Download a sample agent definition:

    ```shell
    azd ai agent init -m ../msft-docs-agent/agent.yaml
    ```
  - install agent extension if prompted.
  - select your subscription when prompted.
  - select `North Central US` region.
  - select `GlobalStandard` for mode SKU.
  - deployment name of model cab be left as default. (gpt-4o-mini)
  - container memory, CPU, and replicas can be left as default. (2GB, 1 CPU, 1 min replica and 3 max replicas)

4. Provision Microsoft Foundry and the sample agent:

    ```shell
    azd up
    ```

5. Open Microsoft [Foundry portal](https://ai.azure.com) and test the agent
  - Note: azd up creates new Microsoft Foundry account. Navigate to your Microsoft Foundry (should be listed under resource group `rg-<username>-hosted-agent` you specified in step 1).

## Resource Clean-up

- **Deleting Resources:**
  To delete all associated resources and shut down the application, execute the following command:
  
    ```bash
    azd down
    ```

    Please note that this process may take up to 20 minutes to complete.

⚠️ Alternatively, you can delete the resource group directly from the Azure Portal to clean up resources.

## Run the agent in a local environment

### Prerequisites

* Install the [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)
  * Windows: `winget install --id Microsoft.AzureCLI`
  * Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
  * MacOS: `brew update && brew install azure-cli`

* You have already provisioned a Foundry project and deployed a model (for example by running `azd up`).

* Your signed-in user has Azure RBAC access to the Foundry project (at minimum the `Azure AI User` role on the project).

* Python 3.10+ is installed. Using a virtual environment (such as `venv`) is strongly recommended.
  * Example (Linux/MacOS):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
  * Example (Windows PowerShell):
    ```powershell
    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

### Steps

1. In a terminal, set the following environment variables using values from the Foundry portal (https://ai.azure.com):
   * `AZURE_AI_PROJECT_ENDPOINT`
   * `AZURE_AI_MODEL_DEPLOYMENT_NAME`

   Example (Linux/MacOS):
   ```bash
   export AZURE_AI_PROJECT_ENDPOINT="<your-project-endpoint>"
   export AZURE_AI_MODEL_DEPLOYMENT_NAME="<your-model-deployment-name>"
   ```

   Example (Windows PowerShell):
   ```powershell
   $env:AZURE_AI_PROJECT_ENDPOINT = "<your-project-endpoint>"
   $env:AZURE_AI_MODEL_DEPLOYMENT_NAME = "<your-model-deployment-name>"
   ```

2. Sign in with Azure CLI and ensure you are using the tenant and subscription that contain your Foundry project:
   ```bash
   az login
   ```
   If needed, select a subscription:
   ```bash
   az account set --subscription "<subscription-id>"
   ```

3. Install dependencies:
   ```bash
   cd msft-docs-agent
   python3 -m pip install -r requirements.txt
   ```

4. Run the agent locally:
   ```bash
   python3 main.py
   ```
   This starts a local server (see `sample.http` for the request format).

5. Test the agent:
   * Using VS Code REST Client: open `sample.http` and send the request.
   * Or with `curl`:
     ```bash
     curl -sS http://0.0.0.0:8088/responses \
       -H 'Content-Type: application/json' \
       -d '{"input":"Explain overview of Microsoft Foundry in Japanese?"}'
     ```

