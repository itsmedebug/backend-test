# agent2-evidence/main.py

# Import necessary tools
import os
import json


def process_request(original_text, initial_analysis):
   
    print("--- Starting Agent 2: Evidence Gathering ---")
    
   
    evidence_object = get_evidence(original_text)
    
   
    final_output = {
        "initial_analysis": initial_analysis,
        "evidence": evidence_object
    }
    
    print("--- Agent 2 Finished ---")
    return final_output


def get_evidence(original_text):
    
    query = original_text + " fact check"
    
   
    print("Plan A: Searching on DuckDuckGo...")
   
    evidence = None 
    
    if evidence:
        return evidence
    
   
    print("Plan A failed. Now trying Plan B: Searching on NewsAPI...")
   
    evidence = {
        "source": "NewsAPI",
        "title": "Fact Check: Viral Claim Is False",
        "url": "https://example-news.com/fact-check-123",
        "snippet": "Our investigation found the message to be fabricated..."
    } 
    
    if evidence:
        return evidence
        
   
    print("Plan B failed. Now trying Plan C: Searching on Google...")
    
    evidence = None
    
    if evidence:
        return evidence
        
    return {"error": "No evidence found."}


if __name__ == "__main__":
    # Result received from Agent 1 (sample)
    sample_agent1_analysis = {
        "claim": "Chocolate cures all diseases.",
        "preliminary_verdict": "Likely False"
    }
    
   
    sample_original_text = "Scientists have discovered that chocolate cures all diseases."
    
   
    final_result = process_request(sample_original_text, sample_agent1_analysis)
    
    # Print the final result
    print("\n=== FINAL COMBINED OUTPUT ===")
    print(json.dumps(final_result, indent=2))
