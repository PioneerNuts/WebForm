FROM python:3.10.6
COPY requirements.txt ./
RUN pip install --user -r requirements.txt
COPY . app
COPY run_server.sh ./
RUN chmod +x run_server.sh
EXPOSE 8000
ENTRYPOINT ["./run_server.sh"]