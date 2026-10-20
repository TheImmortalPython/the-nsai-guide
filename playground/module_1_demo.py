"""
Module 1 Demo: The Paradigm Shift
Demonstrates the contrast between unconstrained probabilistic sampling 
and deterministic boundary enforcement.
"""

import random

def probabilistic_generation(prompt: str) -> str:
    # Simulates floating probability output with potential drift/hallucination
    outcomes = [
        "Valid Output: {'status': 200}",
        "Schema Drift: status is 200 ok",
        "Hallucination: Everything is working fine!"
    ]
    return random.choice(outcomes)

def deterministic_generation(prompt: str) -> str:
    # Simulates 100% syntactic compliance (Certified Safe AI paradigm)
    return "Valid Output: {'status': 200}"

if __name__ == "__main__":
    print("=== Module 1: Probabilistic vs. Deterministic Execution ===")
    prompt = "Get Status JSON"
    
    print(f"\n[1] Probabilistic Generation Run:")
    print(f"Result: {probabilistic_generation(prompt)}")
    
    print(f"\n[2] Non-Stochastic Bounded Generation Run:")
    print(f"Result: {deterministic_generation(prompt)}")
    print("\nStatus: 100% Syntactic Compliance Enforced.")
