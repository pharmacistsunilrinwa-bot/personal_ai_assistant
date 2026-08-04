# Deploying the Brain (Backend) to Google Cloud Run

This guide explains how to migrate and deploy the FastAPI backend of the Personal AI Assistant to **Google Cloud Run**, which is a fully managed serverless platform that automatically scales your containerized application.

---

## Prerequisites

1. **Google Cloud Account:** Create one at [console.cloud.google.com](https://console.cloud.google.com/).
2. **Google Cloud SDK (gcloud CLI):** Installed and configured on your computer. If you don't have it, follow the [Google Cloud SDK Installation Guide](https://cloud.google.com/sdk/docs/install).
3. **Billing Enabled:** Make sure billing is enabled for your GCP project (Cloud Run requires a billing account, though there is a generous free tier).
4. **Enabled APIs:** Enable the Cloud Build and Cloud Run APIs in your project:
   ```bash
   gcloud services enable run.googleapis.com cloudbuild.googleapis.com
   ```

---

## Deployment Options

We have set up two ways to deploy your application to Google Cloud Run:

### Option A: Deploy using Google Cloud Build (Recommended)
This option uses the provided `cloudbuild.yaml` file to automate building the Docker image and deploying it directly to Cloud Run.

1. Initialize and authenticate the `gcloud` CLI:
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```
2. Run the build and deployment pipeline:
   ```bash
   cd backend
   gcloud builds submit --config cloudbuild.yaml
   ```
3. Once completed, the terminal will print the **Service URL** (e.g., `https://personal-ai-assistant-backend-xxxxxx-uc.a.run.app`).

### Option B: Deploy directly via the CLI
If you prefer to deploy directly from your local terminal using Docker:

1. Authenticate and configure Docker for GCP:
   ```bash
   gcloud auth configure-docker
   ```
2. Build and tag the Docker image locally:
   ```bash
   cd backend
   docker build -t gcr.io/YOUR_PROJECT_ID/personal-ai-assistant-backend:latest .
   ```
3. Push the image to Google Container Registry:
   ```bash
   docker push gcr.io/YOUR_PROJECT_ID/personal-ai-assistant-backend:latest
   ```
4. Deploy to Cloud Run:
   ```bash
   gcloud run deploy personal-ai-assistant-backend \
     --image gcr.io/YOUR_PROJECT_ID/personal-ai-assistant-backend:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

---

## Connecting the Flutter App to Google Cloud Run

Once your backend is successfully deployed, Google Cloud Run will provide you with a secure HTTPS endpoint (e.g., `https://personal-ai-assistant-backend-xxxxxx-uc.a.run.app`).

To connect your Flutter frontend to this backend:

1. Open `frontend/lib/main.dart`.
2. Locate the backend initialization line inside `main()`:
   ```dart
   final apiService = ApiService(baseUrl: 'http://localhost:8000');
   ```
3. Replace the local URL with your deployed Cloud Run URL:
   ```dart
   final apiService = ApiService(baseUrl: 'https://personal-ai-assistant-backend-xxxxxx-uc.a.run.app');
   ```
4. Push your changes to GitHub to automatically trigger a new APK build with the production backend connected!
