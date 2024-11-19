# Base image for building Vue.js app
FROM node:22 AS build-stage

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy application source code
COPY . .

# Build the application
RUN npm run build

# Base image for serving built files
FROM nginx:alpine AS production-stage

# Copy built files to Nginx's html directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose the Nginx default port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
