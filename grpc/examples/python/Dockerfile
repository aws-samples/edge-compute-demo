FROM python:3.12
RUN pip install protobuf grpcio
COPY ./helloworld /app/helloworld
WORKDIR /app/helloworld
CMD ["python", "greeter_server.py"]
EXPOSE 50051