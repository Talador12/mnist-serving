FROM node:alpine
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY service /app/service
EXPOSE 8080
CMD flask start