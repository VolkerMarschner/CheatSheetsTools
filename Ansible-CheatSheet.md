# Ansible Cheatsheet

## Basic Commands

```
ansible <host-pattern> -m <module> -a "<module args>"   # Run an ad-hoc command
ansible-playbook <playbook.yml>                        # Run a playbook
ansible-galaxy install <role>                          # Install a role from Ansible Galaxy
ansible-vault create <file>                            # Create an encrypted file
ansible-vault edit <file>                              # Edit an encrypted file
ansible-vault decrypt <file>                           # Decrypt an encrypted file
```

## Inventory

```ini
# /etc/ansible/hosts or custom inventory file
[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.example.com
db2.example.com

[all:vars]
ansible_user=myuser
```

## Playbook Structure

```yaml
---
- name: Playbook Name
  hosts: all
  become: yes
  vars:
    var1: value1
  tasks:
    - name: Task 1
      module_name:
        arg1: value1
        arg2: value2
```

## Common Modules

- `apt`: Manage apt packages
- `yum`: Manage yum packages
- `copy`: Copy files to remote hosts
- `file`: Set file attributes
- `template`: Copy and process Jinja2 templates
- `service`: Manage services
- `user`: Manage user accounts
- `git`: Manage git repositories
- `debug`: Print statements during execution

## Variables

```yaml
vars:
  - variable1: value1
  - variable2: value2

# Using variables
{{ variable_name }}
```

## Conditionals

```yaml
tasks:
  - name: Install Apache on Debian
    apt: name=apache2 state=present
    when: ansible_os_family == "Debian"
```

## Loops

```yaml
tasks:
  - name: Create multiple users
    user: name={{ item }} state=present
    loop:
      - user1
      - user2
      - user3
```

## Handlers

```yaml
tasks:
  - name: Copy Apache config file
    copy:
      src: httpd.conf
      dest: /etc/apache2/httpd.conf
    notify: Restart Apache

handlers:
  - name: Restart Apache
    service: name=apache2 state=restarted
```

## Roles

```
roles/
  common/
    tasks/
    handlers/
    files/
    templates/
    vars/
    defaults/
    meta/
```

## Best Practices

1. Use version control for your Ansible code
2. Keep secrets in encrypted files using `ansible-vault`
3. Use roles to organize and reuse your Ansible code
4. Always test your playbooks in a non-production environment first
5. Use tags to selectively run parts of your playbook
6. Keep your playbooks idempotent (can be run multiple times without changing the result)
7. Use `--check` mode to perform a dry run of your playbooks
8. Regularly update Ansible and your roles to get the latest features and security fixes
