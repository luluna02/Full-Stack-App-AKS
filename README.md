# Full-Stack To-Do Application with Kubernetes and AKS  

A simple To-Do application built with Angular (frontend), Flask (backend), and PostgreSQL (database). The app is containerized using Docker and deployed locally on Minikube and on the cloud using Azure Kubernetes Service (AKS).  

You can find directly the Docker images published on DockerHub.

![DockerHub Images](https://github.com/luluna02/Full-Stack-App-AKS/blob/c7fcdcdcf698229c721d5325656eb849a41aa578/Assets/docker%20hub%20images.png)  

## Features  
- **Frontend**:  
  - Built with Angular for managing to-do tasks.  
  - Supports adding, updating, and deleting tasks.  

- **Backend**:  
  - Developed with Flask, providing RESTful APIs for CRUD operations.  
  - Connected to a PostgreSQL database running in a container.  

- **Deployment**:  
  - Containerized with Docker and images pushed to DockerHub.  
  - Deployed locally using Minikube for Kubernetes orchestration.  
  - Deployed to Azure Kubernetes Service (AKS) with ingress controllers for public accessibility and DNS management.

To deploy the application using Kubernetes, use the YAML files provided in the `k8s` folder. Follow these steps:  
- **Prerequisites**:  
1. Kubernetes Cluster: Set up a Kubernetes cluster using Minikube or a cloud provider like Azure Kubernetes Service (AKS).  
2. kubectl: Ensure you have `kubectl` installed and configured to connect to your cluster.  
3. Docker Images: Use the images pushed to DockerHub. 

## Screenshots  

### 1. Application publicly accessible 
![Containers Communication](https://github.com/luluna02/Full-Stack-App-AKS/blob/c7fcdcdcf698229c721d5325656eb849a41aa578/Assets/Screenshot%202024-08-08%20at%2010.03.55%E2%80%AFAM.png)  

### 2. Containers deployments on AKS  
![Application on AKS](https://github.com/luluna02/Full-Stack-App-AKS/blob/42f3b8e6c67d5ee6b540e998c1322b113254e07a/Assets/Screenshot%202025-01-13%20at%208.24.13%E2%80%AFPM.png) 

### 2. Containers orchestration on AKS using Ingresses.  
![Application with ingresses](https://github.com/luluna02/Full-Stack-App-AKS/blob/a129abeac884b81479bde2c6f1dad2018453d9a1/Assets/Screenshot%202025-01-13%20at%208.34.38%E2%80%AFPM.png)

### Steps to Deploy  

1. **Clone the repository**: 
   ```bash
   git clone https://github.com/your-username/your-repo-name.git  
   cd your-repo-name
   ```
2. **Navigate to the k8s folder**:

   ```bash
   cd k8s
   ```
3. **Apply the YAML files in the correct order**:

   ```bash
   kubectl apply -f pgadmin-postgres.yaml 
   kubectl apply -f flask.yaml
   kubectl apply -f angular.yaml
   ```
   
   Configure ingress to expose services:
   
   ```bash
   kubectl apply -f ingress.yaml
   kubectl apply -f ingress-api.yaml
   ```


   




