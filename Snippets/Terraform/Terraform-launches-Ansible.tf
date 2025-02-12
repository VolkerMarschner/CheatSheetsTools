resource "null_resource" "run_ansible" {
  provisioner "local-exec" {
    command = "ansible-playbook -i inventory.yml playbook.yml"
    # Optional: Working Directory setzen
    working_dir = "../ansible"
  }
  
  # Wichtig: Nur ausführen, wenn sich wirklich was geändert hat
  triggers = {
    instance_ids = join(",", aws_instance.example[*].id)  # Beispiel für AWS
  }
}

Erklärung:
Der triggers Block ist ein wichtiger Mechanismus in Terraform, der kontrolliert, wann ein null_resource neu ausgeführt werden soll. Hier die detaillierte Erklärung:

Funktionsweise:

triggers = {
    instance_ids = join(",", aws_instance.example[*].id)
}

Terraform speichert den Wert des Triggers im State
Bei jedem Apply vergleicht Terraform den aktuellen mit dem gespeicherten Wert
Nur wenn sich der Wert ändert, wird der null_resource neu ausgeführt


Praktisches Beispiel:

resource "aws_instance" "web" {
    count = 2
    ami = "ami-123456"
    instance_type = "t2.micro"
}

resource "null_resource" "run_ansible" {
    triggers = {
        instance_ids = join(",", aws_instance.web[*].id)
        instance_ips = join(",", aws_instance.web[*].private_ip)
        # Mehrere Trigger sind möglich
    }

    provisioner "local-exec" {
        command = "ansible-playbook playbook.yml"
    }
}
In diesem Fall wird Ansible nur ausgeführt wenn:

Neue Instanzen erstellt werden
Bestehende Instanzen gelöscht werden
Instanzen ersetzt werden (neue ID)

Nicht ausgeführt wird es bei:

Änderungen die die Instance-ID nicht betreffen (z.B. Tags)
Wenn terraform apply ohne Änderungen läuft

Sie können auch andere Trigger definieren, z.B.:
triggers = {
    playbook_hash = filemd5("../ansible/playbook.yml")  # Änderungen am Playbook
    always = timestamp() # Läuft bei jedem Apply (nicht empfohlen)
    config_version = "1.2" # Manuelle Versionskontrolle
