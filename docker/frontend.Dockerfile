FROM node:22-bullseye AS build

WORKDIR /frontend

COPY ../frontend/package*.json ./

RUN npm install

COPY ../frontend/ ./

RUN npm run build

FROM nginx:stable

COPY --from=build /frontend/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]