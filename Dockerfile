# Copyright (c) 2023 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

FROM python:3.10-alpine
WORKDIR /app 
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]