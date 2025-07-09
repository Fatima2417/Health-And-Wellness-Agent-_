import requests
import os

class OpenRouterClient:
    def __init__(self):
        self.api_key = "put you openrouter api key here"
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = "deepseek/deepseek-r1-0528:free"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    async def chat_completion(self, system_prompt: str, user_message: str, max_tokens: int = 1000) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": max_tokens,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                return f"API Error {response.status_code}"
                
        except Exception as e:
            return f"Error: {str(e)}"
