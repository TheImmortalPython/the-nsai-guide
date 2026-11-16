[← Back to Main README](../../README.md)

# Module 3: Grammatical Dependency Lattices

## 3.1 Pāṇinian Kāraka Dependency Frameworks & Lattices
Integrating Pāṇinian syntactic structures into neural constraints allows language models to operate with strict grammatical and semantic precision. Rather than relying solely on superficial token adjacency or unconstrained probabilistic attention, the Pāṇinian Kāraka framework maps deep semantic relationships and structural roles directly into an active constraint lattice:

- **Kartā (Agent Role Masking):** Restricts token selection to ensure the active agent or subject governing the action remains structurally valid and within designated authority boundaries.
- **Karma (Goal/Target Mapping):** Constrains the output trajectory toward the exact objective or target object of the action, eliminating semantic drift and parameter variance.
- **Karaṇa (Instrumental Role Masking):** Enforces constraints on the instruments, tools, or execution mechanisms utilized to perform an action.
- **Sampradāna (Recipient/Beneficiary Mapping):** Restricts the target destination, recipient, or beneficiary receiving the outcome of the action.
- **Apādāna (Source/Ablative Boundary Mapping):** Maps structural boundaries around source origins, ablative separations, and initial state departures.
- **Adhikaraṇa (Locus/Context Boundaries):** Enforces spatial, temporal, or logical context boundaries to keep generation anchored within valid execution spaces.

Together, these lattices maintain rigorous grammatical logic and zero-drift structural execution across the entire token sequence.

## 3.2 The Bridge to Runtime Execution
To see how these semantic role bindings are handed off and mathematically enforced as allowlists during autoregressive decoding, see the **[Architectural Deep Dive: The Interpretation Contract vs. The Enforcement Contract](../04_runtime_core/interpretation_vs_enforcement.md)**.

<div align="center">

[← Previous Module](../02_mathematical_foundations/README.md) | [Main README](../../README.md) | [Next Module →](../04_runtime_core/README.md)

</div>
