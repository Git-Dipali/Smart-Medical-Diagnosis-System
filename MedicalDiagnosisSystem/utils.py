import json
import os

def load_knowledge_base(file_path: str) -> dict:
    """Loads the knowledge base from a JSON file."""
    if not os.path.exists(file_path):
        print(f"Error: Could not find '{file_path}'. Starting with an empty knowledge base.")
        return {"diseases": {}}
    
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' contains invalid JSON. Starting with an empty knowledge base.")
        return {"diseases": {}}
    except Exception as e:
        print(f"An unexpected error occurred while reading the knowledge base: {e}")
        return {"diseases": {}}

def save_knowledge_base(file_path: str, data: dict) -> bool:
    """Saves the knowledge base to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error: Could not save to '{file_path}'. {e}")
        return False

def get_yes_no_input(prompt: str) -> bool:
    """Prompts the user for a yes/no answer and returns a boolean."""
    while True:
        response = input(f"{prompt} (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_all_symptoms(knowledge_base: dict) -> list:
    """Extracts a unique list of all symptoms known in the knowledge base."""
    symptoms = set()
    for disease_info in knowledge_base.get("diseases", {}).values():
        symptoms.update(disease_info.get("symptoms", {}).keys())
    return sorted(list(symptoms))
