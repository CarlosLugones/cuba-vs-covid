FROM node as frontend

ENV NUXT_HOST 0.0.0.0
ENV NUXT_PORT 3000

RUN mkdir /frontend
ADD . /frontend
WORKDIR /frontend

CMD ["bash", "-c", "yarn install; yarn build; yarn start;"]

EXPOSE 3000
