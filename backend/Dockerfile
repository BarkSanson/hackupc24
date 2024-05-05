FROM node:20

WORKDIR /back

COPY . .

ARG AI_HOST=localhost
ARG AI_PORT=5000

RUN npm i

EXPOSE 3000

CMD ["npm", "run", "start"]