import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def run_manual_array_chatbot():
    client = genai.Client()
    model_id = "gemini-2.5-flash"
    
    chat_history = []
    
    print(f"--- Manual In-Memory List Chatbot Initialized ({model_id}) ---")
    print("Type your message below. Type 'exit', 'quit', or 'q' to end the session.\n")
    
    while True:
        try:
            user_input = input("User: ")
            
            if user_input.strip().lower() in ["exit", "quit", "q"]:
                print("\nTerminating chat session. Goodbye!")
                break
          
            if not user_input or not user_input.strip():
                print("System Warning: Input cannot be empty. Please enter a valid message.\n")
                continue
          
            chat_history.append({
                "role": "user", 
                "parts": [user_input]
            })
            
            response = client.models.generate_content(
                model=model_id,
                contents=chat_history
            )
            
            model_response_text = response.text
            print(f"\nAI: {model_response_text}\n")
            print("-" * 50)
            
            chat_history.append({
                "role": "model", 
                "parts": [model_response_text]
            })
            
        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\nAPI Error Encountered: {e}\n")

if __name__ == "__main__":
    run_manual_array_chatbot()