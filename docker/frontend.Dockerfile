FROM node:18 AS build

WORKDIR /frontend

COPY ../frontend/package*.json ./
RUN npm install

COPY ../client .
RUN npm run build

FROM nginx:stable
COPY --from=build /frontend/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]