import sys
from utils import load_knowledge_base, save_knowledge_base, get_yes_no_input, get_all_symptoms
from inference import run_diagnosis, generate_explanation

KB_FILE = "knowledge_base.json"

def display_menu():
    print("\n" + "="*45)
    print("  SMART MEDICAL DIAGNOSIS SYSTEM  ")
    print("="*45)
    print("1. Enter patient symptoms & Get Diagnosis")
    print("2. Add new disease to knowledge base")
    print("3. Exit")
    print("="*45)

def handle_diagnosis(knowledge_base: dict):
    if not knowledge_base.get("diseases"):
        print("\nKnowledge base is empty. Please add diseases first.")
        return

    all_symptoms = get_all_symptoms(knowledge_base)
    
    if not all_symptoms:
        print("No symptoms found in knowledge base.")
        return

    print("\nPlease enter the symptoms the patient is experiencing.")
    print("Separate them with commas (e.g., 'fever, headache, loss of taste').")
    user_input = input("Symptoms: ").strip().lower()
    
    # Initialize all known symptoms to False
    patient_symptoms = {symptom: False for symptom in all_symptoms}
    
    # Check which symptoms match the user's input
    matched_symptoms = []
    import re
    
    # Tokenize user input to words for better matching
    user_input_lower = user_input.lower()
    user_words = set(re.findall(r'\b\w+\b', user_input_lower))
    stop_words = {'and', 'or', 'in', 'of', 'the', 'a', 'with', 'to', 'is', 'are', 'feeling', 'has', 'have', 'my', 'i', 'am'}
    
    for symptom in all_symptoms:
        # Replace underscores with spaces for matching
        readable_symptom = symptom.replace("_", " ").lower()
        
        # 1. Exact substring match (e.g., "fever" in "high fever, cough")
        if readable_symptom in user_input_lower:
            patient_symptoms[symptom] = True
            if readable_symptom not in matched_symptoms:
                matched_symptoms.append(readable_symptom)
            continue
            
        # 2. Keyword matching (handles word reordering and partial matches)
        symptom_words = set(re.findall(r'\b\w+\b', readable_symptom))
        significant_words = {w for w in symptom_words if w not in stop_words and len(w) > 2}
        
        if len(significant_words) > 0:
            # Match if all significant words are found in the user input as partial words
            # (e.g. 'diminish' matches 'diminished', 'cough' matches 'coughing')
            all_words_matched = True
            for word in significant_words:
                # We check if the root/prefix of the word exists in any of the user's words
                # Using a simple heuristic: match the first 4 characters or the whole word if shorter
                prefix_len = min(4, len(word))
                prefix = word[:prefix_len]
                if not any(prefix in u_word for u_word in user_words):
                    all_words_matched = False
                    break
            
            if all_words_matched:
                patient_symptoms[symptom] = True
                if readable_symptom not in matched_symptoms:
                    matched_symptoms.append(readable_symptom)
                    
    if not matched_symptoms:
        print("\nNote: Could not match any symptoms to the knowledge base. Using default baseline.")
    else:
        print(f"\nMatched the following symptoms: {', '.join(matched_symptoms)}")
        
    print("\nAnalyzing symptoms...")
    
    ranked_results = run_diagnosis(knowledge_base, patient_symptoms)
    
    if not ranked_results:
        print("Could not reach a diagnosis based on the provided data.")
        return
        
    top_disease, top_prob = ranked_results[0]
    
    print("\n--- DIAGNOSIS RESULTS ---")
    print(f"Top Diagnosis: {top_disease} ({top_prob * 100:.1f}%)")
    
    print("\n--- EXPLANATION ---")
    explanation = generate_explanation(top_disease, top_prob, patient_symptoms, knowledge_base)
    print(explanation)
    
    print("\n--- TOP 15 PROBABILITIES (RANKED) ---")
    for disease, prob in ranked_results[:15]:
        print(f"{disease}: {prob * 100:.2f}%")

def handle_add_disease(knowledge_base: dict):
    print("\n--- ADD NEW DISEASE ---")
    disease_name = input("Enter disease name: ").strip()
    
    if not disease_name:
        print("Disease name cannot be empty.")
        return
        
    if disease_name in knowledge_base.get("diseases", {}):
        print(f"Disease '{disease_name}' already exists.")
        return
        
    try:
        prior_prob = float(input("Enter prior probability of the disease (e.g., 0.05 for 5%): "))
        if not (0 <= prior_prob <= 1):
            print("Probability must be between 0 and 1.")
            return
    except ValueError:
        print("Invalid number format.")
        return
        
    print("\nEnter symptoms and their probabilities given the disease (e.g., 0.8 for 80%).")
    print("Type 'done' when finished.")
    
    symptoms = {}
    while True:
        symptom_name = input("Symptom name (or 'done'): ").strip().lower().replace(" ", "_")
        if symptom_name == 'done':
            break
            
        if not symptom_name:
            continue
            
        try:
            symptom_prob = float(input(f"Probability of '{symptom_name}' given {disease_name} (0-1): "))
            if not (0 <= symptom_prob <= 1):
                print("Probability must be between 0 and 1. Try again.")
                continue
            symptoms[symptom_name] = symptom_prob
        except ValueError:
            print("Invalid number format. Try again.")
            
    if "diseases" not in knowledge_base:
        knowledge_base["diseases"] = {}
        
    knowledge_base["diseases"][disease_name] = {
        "prior_probability": prior_prob,
        "symptoms": symptoms
    }
    
    if save_knowledge_base(KB_FILE, knowledge_base):
        print(f"\nSuccessfully added {disease_name} to the knowledge base.")

def main():
    print("Initializing Smart Medical Diagnosis System...")
    knowledge_base = load_knowledge_base(KB_FILE)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            handle_diagnosis(knowledge_base)
        elif choice == '2':
            handle_add_disease(knowledge_base)
        elif choice == '3':
            print("Exiting system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
