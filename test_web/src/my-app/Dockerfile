FROM node:latest

RUN mkdir /web

WORKDIR /web/src

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 80

CMD ["node", "app.js"]