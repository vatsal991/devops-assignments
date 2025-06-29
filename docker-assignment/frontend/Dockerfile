FROM node:20-alpine
WORKDIR /app
COPY . .
ARG VITE_BACKEND_URL
ENV VITE_BACKEND_URL=$VITE_BACKEND_URL
RUN npm install --no-cache
RUN npm run build
EXPOSE 4173
CMD ["npm", "run", "preview", "--", "--host"]