# 🌐 PostForge AI — Frontend

This is the React-based frontend for **PostForge AI**, built with Vite and designed with a premium, high-performance dark-mode aesthetic.

## 🚀 Getting Started

### 1. Install Dependencies
```bash
npm install
```

### 2. Run Development Server
```bash
npm run dev
```
The frontend will be available at `http://localhost:5173`.

### 🔗 Backend Integration
The frontend is configured to proxy `/api/*` requests to `http://localhost:8000`. Ensure the FastAPI backend is running for the app to function.

## 🛠️ Features
- **React 18** + **Vite 5**.
- **Glassmorphism Design**: Custom CSS design system.
- **API Helper**: Centralized fetch logic in `src/api.js`.
- **Responsive Layout**: Works across all device sizes.
