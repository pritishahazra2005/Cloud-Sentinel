# ai/explainer.py
import google.generativeai as genai

def explain_finding(finding):
    prompt = f"""
    You are a cloud security expert. Explain this AWS security issue to a developer:
    
    Issue: {finding['issue']}
    Resource: {finding['resource']}
    Severity: {finding['severity']}
    
    Provide:
    1. Why this is dangerous (2 sentences)
    2. Step-by-step fix (numbered list)
    3. AWS CLI command to fix it
    """
    # your Gemini call here