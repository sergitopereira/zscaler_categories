FROM python:3.8
WORKDIR /
RUN git clone https://github.com/sergitopereira/det.git /zscaler_categories/
RUN pip install -r /zscaler_categories/requirements.txt

