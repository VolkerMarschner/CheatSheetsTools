# AWS EKS with Cilium and Hubble Cheatsheet

## Connect to EKS Cluster

```bash
# Configure kubectl
aws eks update-kubeconfig --name your-cluster-name --region your-region

# Verify connection
kubectl get nodes
```

## Install Helm (if needed)

```bash
# Install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verify installation
helm version
```

## Install Cilium and Hubble

### Add Helm Repository

```bash
helm repo add cilium https://helm.cilium.io/
helm repo update
```

### Install Cilium with Hubble

```bash
# Installation with kube-proxy replacement
helm install cilium cilium/cilium --namespace kube-system \
  --set hubble.relay.enabled=true \
  --set hubble.ui.enabled=true \
  --set kubeProxyReplacement=true \
  --set k8sServiceHost=$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}') \
  --set k8sServicePort=443 \
  --set hubble.metrics.enabled="{dns:query;ignoreAAAA;destinationContext=pod-short,drop:sourceContext=pod;destinationContext=pod,tcp,flow,icmp,http}"

# OR: Installation without kube-proxy replacement
helm install cilium cilium/cilium --namespace kube-system \
  --set hubble.relay.enabled=true \
  --set hubble.ui.enabled=true \
  --set kubeProxyReplacement=false \
  --set hubble.metrics.enabled="{dns:query;ignoreAAAA;destinationContext=pod-short,drop:sourceContext=pod;destinationContext=pod,tcp,flow,icmp,http}"
```

### Verify installation

```bash
kubectl -n kube-system get pods -l k8s-app=cilium
```

## Install Cilium CLI

```bash
# Install Cilium CLI
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}

# Alternative local installation (if sudo not available)
mkdir -p ~/bin
tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz ~/bin
export PATH=$PATH:~/bin
echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
```

## Cilium and Hubble Commands

```bash
# Check Cilium status
cilium status

# Set up port forwarding for Hubble UI
kubectl port-forward -n kube-system svc/hubble-ui 12000:80 &

# Set up port forwarding for Hubble Relay
kubectl port-forward -n kube-system svc/hubble-relay 4245:80 &

# Observe network flows with Hubble
hubble observe
```

## Test Applications via Helm

```bash
# Install Nginx
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-nginx bitnami/nginx

# Install Kubernetes Dashboard
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
helm install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard
```
