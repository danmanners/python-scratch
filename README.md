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
