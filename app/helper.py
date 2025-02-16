import requests
import json

# API Endpoint
API_URL = "https://82le1lsl6e.execute-api.us-east-1.amazonaws.com/dev/test_bedrock_v5"

def invoke_text_api(prompt, max_tokens=500, temperature=0.7, top_k=100, top_p=0.95):
    """
    Calls the API for text-only input.
    """
    payload = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_k": top_k,
        "top_p": top_p
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response_json = response.json()

        # Extract text response
        return response_json.get("model_response", {}).get("content", [{}])[0].get("text", "🤖 No response received.")
    
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def invoke_text_image_api(base64_image, prompt, max_tokens=1000, temperature=0.8, top_k=150, top_p=0.98):
    """
    Calls the API for text+image input.
    """
    payload = {
        "image": base64_image,
        "media_type": "image/jpeg",  # Ensure correct media type
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_k": top_k,
        "top_p": top_p
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response_json = response.json()

        # Extract text response
        return response_json.get("model_response", {}).get("content", [{}])[0].get("text", "🤖 No response received.")
    
    except Exception as e:
        return f"⚠️ Error: {str(e)}"