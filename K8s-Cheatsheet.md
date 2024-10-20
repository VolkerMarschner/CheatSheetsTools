# Kubernetes Cheatsheet

## Cluster Management

### Get cluster info
```
kubectl cluster-info
```

### Get nodes
```
kubectl get nodes
```

## Pod Management

### Create a pod
```
kubectl run <pod-name> --image=<image-name>
```

### List pods
```
kubectl get pods
```

### Describe pod
```
kubectl describe pod <pod-name>
```

### Delete pod
```
kubectl delete pod <pod-name>
```

## Deployment Management

### Create deployment
```
kubectl create deployment <deployment-name> --image=<image-name>
```

### List deployments
```
kubectl get deployments
```

### Scale deployment
```
kubectl scale deployment <deployment-name> --replicas=<number>
```

### Update deployment image
```
kubectl set image deployment/<deployment-name> <container-name>=<new-image>
```

## Service Management

### Expose deployment as a service
```
kubectl expose deployment <deployment-name> --type=<service-type> --port=<port>
```

### List services
```
kubectl get services
```

## Namespace Management

### List namespaces
```
kubectl get namespaces
```

### Create namespace
```
kubectl create namespace <namespace-name>
```

### Set context to a namespace
```
kubectl config set-context --current --namespace=<namespace-name>
```

## ConfigMaps and Secrets

### Create ConfigMap
```
kubectl create configmap <configmap-name> --from-file=<path/to/file>
```

### Create Secret
```
kubectl create secret generic <secret-name> --from-literal=<key>=<value>
```

## Logs and Debugging

### Get pod logs
```
kubectl logs <pod-name>
```

### Execute command in pod
```
kubectl exec -it <pod-name> -- <command>
```

### Port forwarding
```
kubectl port-forward <pod-name> <local-port>:<pod-port>
```

## Apply and Delete Resources

### Apply a YAML file
```
kubectl apply -f <filename.yaml>
```

### Delete resources defined in a YAML file
```
kubectl delete -f <filename.yaml>
```

Remember to replace placeholders (enclosed in `<>`) with actual values when using these commands.
