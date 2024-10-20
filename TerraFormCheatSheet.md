# Terraform Cheatsheet

## Basic Commands

- `terraform init`: Initialize a Terraform working directory
- `terraform plan`: Generate and show an execution plan
- `terraform apply`: Builds or changes infrastructure
- `terraform destroy`: Destroy Terraform-managed infrastructure

## Configuration Syntax

```hcl
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

## Variables

```hcl
variable "region" {
  default = "us-west-2"
}
```

Usage: `var.region`

## Outputs

```hcl
output "instance_ip_addr" {
  value = aws_instance.server.private_ip
}
```

## Data Sources

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
}
```

## Modules

```hcl
module "vpc" {
  source = "./vpc"
  region = var.region
}
```

## State Management

- `terraform state list`: List resources in the state
- `terraform state show`: Show a resource in the state
- `terraform state mv`: Move an item in the state
- `terraform state rm`: Remove instances from the state

## Workspaces

- `terraform workspace new`: Create a new workspace
- `terraform workspace select`: Select a workspace
- `terraform workspace list`: List workspaces

## Import Existing Resources

```
terraform import aws_instance.example i-abcd1234
```

## Formatting and Validation

- `terraform fmt`: Rewrite config files to canonical format
- `terraform validate`: Validates the configuration files

## Useful Flags

- `-auto-approve`: Skip interactive approval of plan before applying
- `-var 'foo=bar'`: Set a variable in the Terraform configuration
- `-var-file=foo.tfvars`: Set variables from a file

Remember to always review the official Terraform documentation for the most up-to-date and detailed information.
