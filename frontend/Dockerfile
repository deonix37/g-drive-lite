FROM node:18.17.1-bullseye-slim

WORKDIR /app

COPY package*.json .

RUN npm install

CMD ["npm", "run", "dev"]

EXPOSE 5173
