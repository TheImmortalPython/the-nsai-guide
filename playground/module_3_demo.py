"""
Module 3 Demo: Pāṇinian Kāraka Dependency Lattice Masking
Simulates role-based dependency masking (Kartā, Karma, Adhikaraṇa).
"""

def karaka_role_filter(current_role: str, candidate_tokens: dict) -> list[str]:
    """
    Filters candidate tokens based on active Pāṇinian Kāraka role constraints.
    """
    allowed = []
    for token, category in candidate_tokens.items():
        if current_role == "Kartā" and category == "Agent":
            allowed.append(token)
        elif current_role == "Karma" and category == "Target":
            allowed.append(token)
        elif current_role == "Adhikaraṇa" and category == "Locus":
            allowed.append(token)
    return allowed

if __name__ == "__main__":
    print("=== Module 3: Pāṇinian Kāraka Dependency Lattice Demo ===")
    
    candidates = {
        "User": "Agent",
        "System": "Agent",
        "Database": "Target",
        "ServerRoom": "Locus"
    }
    
    role = "Kartā"
    valid_tokens = karaka_role_filter(role, candidates)
    
    print(f"Active Kāraka Role: {role} (Agent)")
    print(f"Candidate Space:   {list(candidates.keys())}")
    print(f"Allowed Tokens:    {valid_tokens}")
