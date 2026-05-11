from bayesian_model import calculate_posterior_probabilities
from utils import get_all_symptoms

def generate_explanation(disease: str, probability: float, patient_symptoms: dict, knowledge_base: dict) -> str:
    """Generates a text explanation of why a diagnosis was reached."""
    disease_info = knowledge_base["diseases"].get(disease, {})
    expected_symptoms = disease_info.get("symptoms", {})
    
    explanation = f"The model predicts '{disease}' with a {probability * 100:.1f}% confidence.\n"
    
    contributing_symptoms = []
    for symptom, is_present in patient_symptoms.items():
        if is_present:
            prob = expected_symptoms.get(symptom, 0)
            if prob >= 0.5:
                contributing_symptoms.append(f"{symptom.replace('_', ' ')} (strongly associated, {prob*100:.0f}% of cases)")
            elif prob > 0.1:
                contributing_symptoms.append(f"{symptom.replace('_', ' ')} (mildly associated, {prob*100:.0f}% of cases)")
                
    if contributing_symptoms:
        explanation += "This diagnosis is supported by the presence of the following symptoms:\n"
        for symptom_desc in contributing_symptoms:
            explanation += f"  - {symptom_desc}\n"
    else:
        explanation += "The patient presented none of the primary symptoms heavily associated with this disease.\n"
        
    return explanation

def run_diagnosis(knowledge_base: dict, patient_symptoms: dict) -> list:
    """Runs the diagnosis and returns a ranked list of diseases with their probabilities."""
    posteriors = calculate_posterior_probabilities(knowledge_base, patient_symptoms)
    
    # Sort the diseases by probability in descending order
    ranked_diseases = sorted(posteriors.items(), key=lambda item: item[1], reverse=True)
    return ranked_diseases
