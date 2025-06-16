# Rini's Kubernetes App

## Steps Taken
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

## How to Apply Kubernetes
```bash
minikube start
kubectl apply -f db/
kubectl apply -f backend/
kubectl apply -f frontend/
minikube service nginx-service --url