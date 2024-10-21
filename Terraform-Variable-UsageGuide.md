# Terraform Variable Usage Guide

## Where Variables Are Allowed

1. **Resource Arguments**: 
   ```hcl
   resource "aws_instance" "example" {
     instance_type = var.instance_type
   }
   ```

2. **Data Source Arguments**:
   ```hcl
   data "aws_ami" "example" {
     owners = [var.ami_owner]
   }
   ```

3. **Module Arguments**:
   ```hcl
   module "vpc" {
     source = "./modules/vpc"
     cidr_block = var.vpc_cidr
   }
   ```

4. **Output Values**:
   ```hcl
   output "instance_ip" {
     value = aws_instance.example.public_ip
   }
   ```

5. **Locals**:
   ```hcl
   locals {
     full_name = "${var.first_name} ${var.last_name}"
   }
   ```

6. **Most Attribute References**:
   ```hcl
   resource "aws_route53_record" "example" {
     zone_id = aws_route53_zone.primary.zone_id
     name    = var.record_name
     type    = "A"
     ttl     = 300
     records = [aws_eip.lb.public_ip]
   }
   ```

## Where Variables Are Not Allowed

1. **Resource Names**:
   ```hcl
   # Incorrect
   resource "aws_instance" "${var.instance_name}" {
     # ...
   }
   
   # Correct
   resource "aws_instance" "example" {
     tags = {
       Name = var.instance_name
     }
   }
   ```

2. **Data Source Names**:
   ```hcl
   # Incorrect
   data "aws_ami" "${var.ami_name}" {
     # ...
   }
   
   # Correct
   data "aws_ami" "example" {
     name = var.ami_name
   }
   ```

3. **Module Names**:
   ```hcl
   # Incorrect
   module "${var.module_name}" {
     # ...
   }
   
   # Correct
   module "example" {
     name = var.module_name
   }
   ```

4. **Provider Names**:
   ```hcl
   # Incorrect
   provider "${var.provider_name}" {
     # ...
   }
   
   # Correct
   provider "aws" {
     region = var.aws_region
   }
   ```

5. **Terraform Block Settings**:
   ```hcl
   # Incorrect
   terraform {
     required_version = var.terraform_version
   }
   
   # Correct (if needed, use locals)
   locals {
     terraform_version = "1.0.0"
   }
   terraform {
     required_version = local.terraform_version
   }
   ```

Remember, while variables aren't allowed in these name fields, you can often achieve similar flexibility by using variables within the resource, data source, or module block to set names or other identifying attributes.
