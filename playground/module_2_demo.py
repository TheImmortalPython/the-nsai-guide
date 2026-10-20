"""
Module 2 Demo: Dynamic FSM Logit Geometry & Tensor Topology
Simulates applying a spatial boundary constraint on a raw logit vector.
"""

def apply_topological_constraint(logits: list[float], valid_indices: list[int]) -> list[float]:
    """
    Sets out-of-bounds logit indices to -infinity.
    """
    bounded_logits = list(logits)
    for i in range(len(bounded_logits)):
        if i not in valid_indices:
            bounded_logits[i] = -float('inf')
    return bounded_logits

if __name__ == "__main__":
    print("=== Module 2: Tensor-Topology & FSM Geometry Demo ===")
    
    # Simulated vocabulary logit vector (e.g., 5 candidate tokens)
    raw_logits = [2.1, 4.5, 0.3, 8.9, 1.2]
    allowed_token_indices = [0, 1]  # FSM state allows only indices 0 and 1
    
    print(f"Raw Logit Vector:         {raw_logits}")
    
    bounded = apply_topological_constraint(raw_logits, allowed_token_indices)
    print(f"Bounded Logit Vector (-inf): {bounded}")
    
    print("\nResult: Out-of-bounds tokens mathematically eliminated before sampling.")
