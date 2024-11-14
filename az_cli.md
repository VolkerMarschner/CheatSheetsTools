# Azure CLI Cheatsheet

## Basic Commands & Authentication
```bash
# Version & Help
az --version                     # Show CLI version
az --help                        # Get help
az find "term"                   # Search for commands

# Authentication
az login                         # Interactive login
az login --use-device-code      # Login with device code
az logout                        # Sign out
az account list                  # List subscriptions
az account set --subscription <subscription-id>  # Set subscription
```

## Resource Groups
```bash
# List and Create
az group list                    # List all resource groups
az group list --query "[].name"  # List only names
az group create \
    --name <name> \
    --location <location>        # Create resource group

# Delete and Management
az group delete --name <name>    # Delete resource group
az group update \
    --name <name> \
    --tags key=value            # Update tags
az group wait --name <name> \
    --deleted                   # Wait for deletion
```

## Virtual Networks (VNet)
```bash
# Create VNet and Subnets
az network vnet create \
    --resource-group <rg> \
    --name <name> \
    --address-prefix 10.0.0.0/16

az network vnet subnet create \
    --resource-group <rg> \
    --vnet-name <vnet> \
    --name <name> \
    --address-prefix 10.0.1.0/24

# List and Delete
az network vnet list            # List VNets
az network vnet delete \
    --resource-group <rg> \
    --name <name>              # Delete VNet
```

## Virtual Machines
```bash
# Create VM
az vm create \
    --resource-group <rg> \
    --name <name> \
    --image UbuntuLTS \
    --admin-username <user> \
    --generate-ssh-keys

# VM Management
az vm start --resource-group <rg> --name <name>    # Start VM
az vm stop --resource-group <rg> --name <name>     # Stop VM
az vm deallocate --resource-group <rg> --name <name>  # Deallocate VM
az vm delete --resource-group <rg> --name <name>   # Delete VM
az vm list                                         # List VMs
az vm list-sizes --location <location>             # List available sizes

# VM Information
az vm show \
    --resource-group <rg> \
    --name <name>              # Get VM details
az vm list-ip-addresses \
    --resource-group <rg> \
    --name <name>              # Get VM IP addresses
```

## Storage Accounts
```bash
# Create and Manage
az storage account create \
    --name <name> \
    --resource-group <rg> \
    --location <location> \
    --sku Standard_LRS

az storage account list                # List storage accounts
az storage account delete \
    --name <name> \
    --resource-group <rg>             # Delete storage account

# Blob Operations
az storage blob upload \
    --account-name <name> \
    --container-name <container> \
    --name <blobname> \
    --file <filepath>

az storage blob list \
    --account-name <name> \
    --container-name <container>
```

## App Service
```bash
# Create and Deploy
az webapp create \
    --resource-group <rg> \
    --plan <plan-name> \
    --name <app-name>

az webapp deployment source config \
    --resource-group <rg> \
    --name <app-name> \
    --repo-url <github-url> \
    --branch master \
    --manual-integration

# Management
az webapp restart \
    --resource-group <rg> \
    --name <app-name>           # Restart app

az webapp log tail \
    --resource-group <rg> \
    --name <app-name>           # View logs
```

## Network Security Groups (NSG)
```bash
# Create NSG and Rules
az network nsg create \
    --resource-group <rg> \
    --name <name>

az network nsg rule create \
    --resource-group <rg> \
    --nsg-name <nsg> \
    --name <rule-name> \
    --protocol tcp \
    --priority 1000 \
    --destination-port-range 22 \
    --access allow

# List and Delete
az network nsg list                              # List NSGs
az network nsg delete \
    --resource-group <rg> \
    --name <name>                                # Delete NSG
```

## Azure Kubernetes Service (AKS)
```bash
# Create and Manage Cluster
az aks create \
    --resource-group <rg> \
    --name <name> \
    --node-count 1 \
    --enable-addons monitoring \
    --generate-ssh-keys

az aks get-credentials \
    --resource-group <rg> \
    --name <name>              # Get credentials

az aks scale \
    --resource-group <rg> \
    --name <name> \
    --node-count 3            # Scale cluster
```

## Databases
```bash
# Azure SQL
az sql server create \
    --resource-group <rg> \
    --name <name> \
    --admin-user <user> \
    --admin-password <password>

# Cosmos DB
az cosmosdb create \
    --resource-group <rg> \
    --name <name>
```

## Output Formatting
```bash
# Output Formats
az <command> --output table    # Table format
az <command> --output json     # JSON format
az <command> --output yaml     # YAML format
az <command> --output tsv      # TSV format

# Query Examples
az vm list --query "[].{Name:name,RG:resourceGroup}" -o table
az group list --query "[?location=='westus'].name" -o tsv
```

## Extensions
```bash
# Extension Management
az extension list                        # List installed extensions
az extension add --name <extension-name> # Install extension
az extension remove --name <extension-name> # Remove extension
az extension update --name <extension-name> # Update extension
```

## Useful Tips
- Use `--debug` flag for detailed debug output
- Use `--verbose` for detailed information
- Use `--only-show-errors` to show only errors
- Use `az configure` to set default values
- Use `az interactive` for interactive mode
- Use `az account list-locations` to see available regions

## Environment Variables
```bash
export AZURE_SUBSCRIPTION_ID="<subscription-id>"
export AZURE_TENANT_ID="<tenant-id>"
export AZURE_CLIENT_ID="<client-id>"
export AZURE_CLIENT_SECRET="<client-secret>"
```
