# Description

Updates Zscaler ZIA dbCategorizedUrls urls of a given custom category
---
# Run Locally
```bash
# Clone repo
git clone https://github.com/sergitopereira/det.git

# Install dependencies
pip3 install -r det/requirements.txt

# Usage
python3 det -h
```

# Run in a Virtual Environment
```bash
# Clone repo
git clone https://github.com/sergitopereira/det.git

# Create and enter virtual environment
python3 -m venv det/venv
source det/venv/bin/activate

# Install dependencies
pip install -r det/requirements.txt

# Usage
python det -h
```
# Run with Docker

```bash
# Download Dockerfile
curl -O https://raw.githubusercontent.com/sergitopereira/det/master/Dockerfile

# Build Image and Run Container
docker build -t det .  
docker run -it det bash

# Usage (program is in /app/)
python app -h
```

---

# Credits
```
Sergio Pereira 
Zscaler Professional Services
```