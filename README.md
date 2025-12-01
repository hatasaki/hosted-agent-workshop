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
    azd init --template Azure-Samples/ai-foundry-starter-basic
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
  - Navigate to your Microsoft Foundry (should be listed under resource group `rg-<username>-hosted-agent` you specified in step 1).

## Resource Clean-up

- **Deleting Resources:**
  To delete all associated resources and shut down the application, execute the following command:
  
    ```bash
    azd down
    ```

    Please note that this process may take up to 20 minutes to complete.

⚠️ Alternatively, you can delete the resource group directly from the Azure Portal to clean up resources.
