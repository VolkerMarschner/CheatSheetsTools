import re
import sys
from typing import Dict, Any

def parse_variables_tf(content: str) -> Dict[str, Any]:
    """Parse variables.tf content and extract variable names and default values."""
    # Regular expressions for matching variable blocks and their components
    variable_block_pattern = r'variable\s+"([^"]+)"\s+{([^}]+)}'
    default_value_pattern = r'default\s+=\s+([^\n]+)'
    type_pattern = r'type\s+=\s+([^\n]+)'
    
    variables = {}
    
    # Find all variable blocks
    for match in re.finditer(variable_block_pattern, content, re.DOTALL):
        var_name = match.group(1)
        var_block = match.group(2)
        
        # Try to find default value
        default_match = re.search(default_value_pattern, var_block)
        type_match = re.search(type_pattern, var_block)
        
        if default_match:
            # Use the default value if it exists
            default_value = default_match.group(1).strip()
            variables[var_name] = default_value
        else:
            # If no default, use a placeholder based on type
            if type_match:
                var_type = type_match.group(1).strip()
                if 'string' in var_type:
                    variables[var_name] = '""'
                elif 'number' in var_type:
                    variables[var_name] = '0'
                elif 'bool' in var_type:
                    variables[var_name] = 'false'
                elif 'list' in var_type or 'set' in var_type:
                    variables[var_name] = '[]'
                elif 'map' in var_type:
                    variables[var_name] = '{}'
                else:
                    variables[var_name] = '""'
            else:
                # If no type is specified, use empty string as default
                variables[var_name] = '""'
    
    return variables

def generate_tfvars(variables: Dict[str, Any]) -> str:
    """Generate terraform.tfvars content from variables dictionary."""
    return '\n'.join(f'{key} = {value}' for key, value in variables.items())

def main(variables_tf_path: str, tfvars_path: str):
    """Main function to read variables.tf and generate terraform.tfvars."""
    try:
        # Read variables.tf
        with open(variables_tf_path, 'r') as f:
            variables_content = f.read()
        
        # Parse variables
        variables = parse_variables_tf(variables_content)
        
        # Generate tfvars content
        tfvars_content = generate_tfvars(variables)
        
        # Write to terraform.tfvars
        with open(tfvars_path, 'w') as f:
            f.write(tfvars_content)
        
        print(f"Successfully generated {tfvars_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find {variables_tf_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [path_to_variables.tf] [path_to_output.tfvars]")
        print("If output path is not specified, defaults to './terraform.tfvars'")
        sys.exit(1)
    
    variables_tf_path = sys.argv[1]
    tfvars_path = sys.argv[2] if len(sys.argv) > 2 else 'terraform.tfvars'
    main(variables_tf_path, tfvars_path)
