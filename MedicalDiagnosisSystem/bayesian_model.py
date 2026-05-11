def calculate_posterior_probabilities(knowledge_base: dict, patient_symptoms: dict) -> dict:
    """
    Calculates the posterior probability of each disease given the patient's symptoms
    using Naive Bayes inference.
    
    P(Disease | Symptoms) = (P(Symptoms | Disease) * P(Disease)) / P(Symptoms)
    
    Since P(Symptoms) is the same for all diseases, we can just calculate the numerator
    for each disease and then normalize them so they sum to 1.
    """
    diseases = knowledge_base.get("diseases", {})
    unnormalized_posteriors = {}
    
    for disease, info in diseases.items():
        prior_prob = info.get("prior_probability", 0.0)
        
        # Start with the prior probability P(Disease)
        likelihood = prior_prob
        
        disease_symptoms = info.get("symptoms", {})
        
        for symptom, is_present in patient_symptoms.items():
            # P(Symptom | Disease)
            prob_symptom_given_disease = disease_symptoms.get(symptom, 0.01) # Default small probability if symptom unknown for disease
            
            if is_present:
                # If the patient has the symptom, multiply by P(Symptom | Disease)
                likelihood *= prob_symptom_given_disease
            else:
                # If the patient DOES NOT have the symptom, multiply by P(Not Symptom | Disease)
                # which is 1 - P(Symptom | Disease)
                likelihood *= (1.0 - prob_symptom_given_disease)
                
        unnormalized_posteriors[disease] = likelihood

    # Normalize the probabilities so they sum up to 1 (or 100%)
    total_likelihood = sum(unnormalized_posteriors.values())
    
    if total_likelihood == 0:
        # Prevent division by zero if all probabilities evaluate to 0
        return {disease: 0.0 for disease in diseases}
        
    normalized_posteriors = {
        disease: (likelihood / total_likelihood)
        for disease, likelihood in unnormalized_posteriors.items()
    }
    
    return normalized_posteriors
