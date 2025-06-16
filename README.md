# Rini's Kubernetes App

This project sets up a simple Kubernetes application stack with:
- **Flask API** (Python)
- **MySQL** (as backend database)
- **Nginx** (as reverse proxy frontend)

## 📁 Components

- `Dockerfile`: Flask app container
- `flask-deployment.yaml`: Deployment + Service for Flask
- `mysql-deployment.yaml`: MySQL Deployment + Service
- `nginx-deployment.yaml`: Nginx Deployment + Service
- `mysql-secret.yaml`: Kubernetes Secret for DB credentials

## Steps Taken to Deploy on Minikube
1. Set up Minikube
2. Deployed MySQL with Secrets
3. Deployed Flask backend (Dockerized)
4. Deployed Nginx frontend using ConfigMap
5. Connected backend to database
6. Exposed frontend via NodePort

## Folders
- `db/`: MySQL configs
- `backend/`: Flask app & Dockerfile
- `frontend/`: Nginx config & HTML
- `screenshots/`: Evidence of running app

## How to Apply
```bash
minikube start
kubectl apply -f db/
kubectl apply -f backend/
kubectl apply -f frontend/
minikube service nginx-service --url