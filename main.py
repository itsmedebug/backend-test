# agent2-evidence/main.py

# === PROMPT 4: Setup starts here ===
# Import necessary tools
import os
import json

# This is the function requested in Prompt 4.
# It takes original_text and initial_analysis as input.
def process_request(original_text, initial_analysis):
    """
    Combines the analysis from Agent 1 with the evidence from Agent 2.
    """
    print("--- Starting Agent 2: Evidence Gathering ---")
    
    # === PROMPT 5: Logic is called here ===
    # We are calling the get_evidence function which will search the internet.
    evidence_object = get_evidence(original_text)
    
    # === PROMPT 6: Task is performed here ===
    # We are combining the result from Agent 1 and the evidence from Agent 2.
    final_output = {
        "initial_analysis": initial_analysis,
        "evidence": evidence_object
    }
    
    print("--- Agent 2 Finished ---")
    return final_output

# === PROMPT 5: Fallback Logic (Plan A, Plan B, Plan C) ===
def get_evidence(original_text):
    """
    This function finds evidence.
    """
    query = original_text + " fact check"
    
    # Plan A: Search on DuckDuckGo
    print("Plan A: Searching on DuckDuckGo...")
    # Real search code would go here; for now, we assume it failed.
    evidence = None # Assuming nothing was found
    
    if evidence:
        return evidence
    
    # Plan B: If Plan A failed, search on NewsAPI
    print("Plan A failed. Now trying Plan B: Searching on NewsAPI...")
    # Real NewsAPI code would go here; for now, we assume it worked.
    evidence = {
        "source": "NewsAPI",
        "title": "Fact Check: Viral Claim Is False",
        "url": "https://example-news.com/fact-check-123",
        "snippet": "Our investigation found the message to be fabricated..."
    } # Assuming this result was found
    
    if evidence:
        return evidence
        
    # Plan C: If Plan B also failed, search on Google
    print("Plan B failed. Now trying Plan C: Searching on Google...")
    # Real Google Search code would go here.
    evidence = None
    
    if evidence:
        return evidence
        
    # If all plans fail
    return {"error": "No evidence found."}

# --- Example (To test this script) ---
if __name__ == "__main__":
    # Result received from Agent 1 (sample)
    sample_agent1_analysis = {
        "claim": "Chocolate cures all diseases.",
        "preliminary_verdict": "Likely False"
    }
    
    # The text that needs to be checked
    sample_original_text = "Scientists have discovered that chocolate cures all diseases."
    
    # Run the full process
    final_result = process_request(sample_original_text, sample_agent1_analysis)
    
    # Print the final result
    print("\n=== FINAL COMBINED OUTPUT ===")
    print(json.dumps(final_result, indent=2))