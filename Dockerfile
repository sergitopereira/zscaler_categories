FROM python:3.8
WORKDIR /
RUN git clone https://github.com/sergitopereira/zscaler_categories.git /zscaler_categories/
RUN pip install -r /zscaler_categories/requirements.txt

