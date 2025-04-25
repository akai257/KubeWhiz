import openai
from kubernetes import client, config
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load Kube config
config.load_kube_config()
v1 = client.CoreV1Api()

# Set your API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/query', methods=['POST'])
def handle_query():
    user_prompt = request.json.get("prompt")

    system_prompt = (
        "You are a Kubernetes assistant. Translate the user's prompt into a kubectl-style instruction. "
        "Be specific, concise, and return only the logic or selectors needed."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0
        )

        instruction = response.choices[0].message['content'].strip().lower()

        if "list pods" in instruction or "get pods" in instruction:
            pods = v1.list_pod_for_all_namespaces()
            return jsonify([{
                "name": pod.metadata.name,
                "namespace": pod.metadata.namespace,
                "status": pod.status.phase
            } for pod in pods.items])

        return jsonify({"instruction": instruction, "message": "Demo supports basic 'list pods' only."})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

