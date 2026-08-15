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

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def explain_finding(finding: dict) -> dict:
    prompt = f"""
    You are a cloud security expert. A security scan found this issue:

    Resource: {finding['resource']}
    Issue: {finding['issue']}
    Severity: {finding['severity']}
    Recommendation: {finding['recommendation']}

    Respond in this exact format:
    RISK: (1 sentence — why this is dangerous)
    IMPACT: (1 sentence — what an attacker could do)
    FIX: (2-3 bullet points — how to fix it)
    CLI: (one AWS CLI command to fix it, or "N/A")
    """

    response = model.generate_content(prompt)
    return parse_explanation(response.text, finding)


def parse_explanation(text: str, finding: dict) -> dict:
    lines = text.strip().split("\n")
    parsed = {
        "resource": finding["resource"],
        "severity": finding["severity"],
        "issue": finding["issue"],
        "risk": "",
        "impact": "",
        "fix": [],
        "cli": ""
    }

    for line in lines:
        if line.startswith("RISK:"):
            parsed["risk"] = line.replace("RISK:", "").strip()
        elif line.startswith("IMPACT:"):
            parsed["impact"] = line.replace("IMPACT:", "").strip()
        elif line.startswith("FIX:"):
            parsed["fix"].append(line.replace("FIX:", "").strip())
        elif line.startswith("-") or line.startswith("•"):
            parsed["fix"].append(line.strip("- •").strip())
        elif line.startswith("CLI:"):
            parsed["cli"] = line.replace("CLI:", "").strip()

    return parsed


def explain_all_findings(findings: list) -> list:
    explained = []
    for finding in findings:
        try:
            result = explain_finding(finding)
            explained.append(result)
        except Exception as e:
            finding["risk"] = "Could not generate explanation."
            finding["impact"] = ""
            finding["fix"] = []
            finding["cli"] = ""
            explained.append(finding)
    return explained