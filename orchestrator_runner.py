"""
orchestrator_runner.py
Simple demo helper: instructions to run the orchestrator in the ADK web UI.
"""

import os

def print_demo_instructions():
    print("=== SmartHealthTech Orchestrator Demo ===")
    print("1) Ensure smarthealth_agent/.env has GOOGLE_API_KEY")
    print("2) From project root run: adk web")
    print("3) Open http://localhost:8000 and select 'smarthealth_agent'")
    print("")
    print("Demo sequence examples:")
    print(" - User: 'Hello'  -> agent will ask for symptoms")
    print(" - User: 'I have fever and headache since yesterday' -> agent will ask one follow-up (if needed), then triage, meds check, plan.")
    print("")
    print("CLI alternative:")
    print("  adk run smarthealth_agent")

if __name__ == '__main__':
    print_demo_instructions()
