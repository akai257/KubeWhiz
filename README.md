# KubeWhiz 🧠🚀  
Natural Language Kubernetes Assistant

KubeWhiz is a lightweight MVP tool that lets you interact with your Kubernetes cluster using natural language commands. Designed for DevOps, SREs, and platform engineers, it leverages the power of OpenAI and Kubernetes Python client to turn human-friendly prompts into real K8s operations.

---

## ✨ Features
- 🔍 Query Kubernetes resources using simple English  
- 💡 Intelligent translation via OpenAI GPT-4  
- 📦 Built with Flask + K8s Python SDK  
- 🔐 Local `kubeconfig` authentication (more secure options planned)  
- 🌐 REST API-based interface – easy to integrate with CLI or frontend  

---

## 🧪 Example Prompts
- “List all pods in CrashLoopBackOff”
- “Show all services in the staging namespace”
- “Restart the vault pod in util”
- “What node has the highest memory usage?”

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API Key
- Access to a Kubernetes cluster (`kubeconfig` setup)

### Setup

```bash
git clone https://github.com/akai257/KubeWhiz.git
cd KubeWhiz
pip install -r requirements.txt
export OPENAI_API_KEY=your_openai_key
python app.py
