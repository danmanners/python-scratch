# Quick Start - Podman/Docker

```bash
# Build the container
podman build -t python-learning .

# Run the container
podman run --rm -it -p 5000:5000 localhost/python-learning:latest

# Check Functionality of the container
curl -sL localhost:5000/random
curl -sL localhost:5000/random/word
curl -sL localhost:5000/random/number

# Check it 100 times
for int in {1..100}; do curl -sL localhost:5000/random; done
```

## Building Multi-Architecture Containers and pushing to `ghcr.io`

> `ghcr.io` = GitHub Container Registry

```bash
# Login to ghcr.io with Buildah
cat ~/.github/token | buildah login --username danmanners --password-stdin ghcr.io

# Create the Buildah multi-arch manifest
buildah manifest create python-learning

# Build the amd64 (Intel/AMD) Container
buildah bud --tag ghcr.io/danmanners/python-learning:v0.1.0 --manifest python-learning --arch amd64 .

# Build the arm64 (Raspberry Pi) Container
buildah bud --tag ghcr.io/danmanners/python-learning:v0.1.0 --manifest python-learning --arch arm64 .

# Push both Container Images up to ghcr.io
buildah manifest push --all python-learning docker://ghcr.io/danmanners/python-learning:v0.1.0
```

## Deploying everything to Kubernetes

```bash
➜  demo git:(main) ✗ k apply -k kubernetes
namespace/python-learning created
service/python-learning created
service/python-learning-extname created
deployment.apps/python-learning created
certificate.cert-manager.io/python-learning created
ingressroute.traefik.containo.us/python-learning-web created
ingressroute.traefik.containo.us/python-learning-websecure created
```

## Quickstart - Local Python

```bash
# Create and map the virtual environment
python3 -m venv .env
source .env/bin/activate

# Update Pip
pip install -U pip

# Install the required packages
pip install -r req.txt

# Run the python code
python app.py
```
