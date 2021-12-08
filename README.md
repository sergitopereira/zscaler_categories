# Description

Updates Zscaler ZIA dbCategorizedUrls urls of a given custom category
---
# Run Locally
```bash
# Clone repo
git clone https://github.com/sergitopereira/zscaler_categories.git

# Install dependencies
pip3 install -r zscaler_categories/requirements.txt

# Usage
python3 zscaler_categories -h
```

# Run in a Virtual Environment
```bash
# Clone repo
git clone https://github.com/sergitopereira/zscaler_categories.git

# Create and enter virtual environment
python3 -m venv zscaler_categories/venv
source zscaler_categories/venv/bin/activate

# Install dependencies
pip install -r zscaler_categories/requirements.txt

# Usage
python zscaler_categories -h
```
# Run with Docker

```bash
# Download Dockerfile
curl -O https://raw.githubusercontent.com/sergitopereira/zscaler_categories/master/Dockerfile

# Build Image and Run Container
docker build -t zscaler_categories .  
docker run -it zscaler_categories bash

# Usage (program is in /app/)
python zscaler_categories -h
```
# Usage

python zscaler_categories 

---

# Credits
```
Sergio Pereira 
Zscaler Professional Services
```