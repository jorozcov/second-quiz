# Use the official Node.js image as the base image
FROM node

# Install a simple HTTP server for serving static content
RUN npm install -g http-server

# Set the working directory in the container to /app
WORKDIR /app

# Copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# Install project dependencies
RUN npm install

#Install json-server
RUN npm i json-server

# Copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# Build the app for production with minification
RUN npm run build

# Expose port 8080
EXPOSE 8080

# Start both Vue.js server and JSON server
CMD npm run serve & npm run jsondb
