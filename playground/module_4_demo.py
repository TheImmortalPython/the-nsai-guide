"""
Module 4 Demo: Paninian Kāraka Logit Masking (pklm-core)
Demonstrates the core mechanics of pklm-core using PyTorch/LogitsProcessor logic.
"""

try:
    import torch
    from transformers import LogitsProcessor

    class SimplePKLMMaskProcessor(LogitsProcessor):
        def __init__(self, allowed_token_ids: list[int]):
            self.allowed_token_ids = allowed_token_ids

        def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
            mask = torch.full_like(scores, -float('inf'))
            mask[:, self.allowed_token_ids] = 0.0
            return scores + mask

    if __name__ == "__main__":
        print("=== Module 4: pklm-core Negative Infinity Masking Demo ===")
        # Simulated logit scores for a batch of 1 with vocab size 5
        fake_logits = torch.tensor([[1.0, 2.0, 5.0, 0.5, 3.0]])
        processor = SimplePKLMMaskProcessor(allowed_token_ids=[1, 4])
        
        masked_logits = processor(None, fake_logits)
        print(f"Original Logits: {fake_logits.tolist()}")
        print(f"Masked Logits:   {masked_logits.tolist()}")

except ImportError:
    if __name__ == "__main__":
        print("=== Module 4: pklm-core Concept Demo (PyTorch/Transformers not installed) ===")
        print("pklm-core intercepts logit vectors at step t and adds -inf to forbidden indices.")
