# Istio Zone Lister

This project exposes a `/list_zones` endpoint that lists Kubernetes nodes grouped by their zones.

## How to Use

1. Build the Docker image:
   ```bash
   docker build -t <your-dockerhub-username>/zone-lister:latest ./app
   docker push <your-dockerhub-username>/zone-lister:latest
