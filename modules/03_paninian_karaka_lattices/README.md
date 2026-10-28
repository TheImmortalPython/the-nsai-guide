[← Back to Main README](../../README.md)

# Module 3: Grammatical Dependency Lattices

## 3.1 Pāṇinian Kāraka Dependency Frameworks & Lattices
Integrating Pāṇinian syntactic structures into neural constraints allows language models to operate with absolute grammatical and semantic precision. Rather than relying on superficial token adjacency or unconstrained probabilistic attention, the Pāṇinian Kāraka framework maps deep semantic relationships and structural roles directly into an active constraint lattice.

## 3.2 Agent & Goal Mapping Mechanics
To enforce structural correctness during real-time generation, we apply precise role-based logit masking across key karaka dependencies:
- **Kartā (Agent Role Masking):** Restricts token selection to ensure the active agent or subject governing the action remains structurally sound and within designated authority boundaries.
- **Karma (Goal/Target Mapping):** Constrains the output trajectory toward the exact objective or target object of the action, eliminating semantic drift and parameter variance.

## 3.3 Contextual, Instrumental & Boundary Constraints
Advanced grammatical containment requires mapping every environmental, relational, and locative boundary:
- **Adhikaraṇa (Locus/Context Boundaries):** Enforces spatial, temporal, or logical context boundaries to keep generation anchored within valid execution spaces.
- **Karaṇa, Sampradāna, and Apādāna (Instrumental, Recipient, & Ablative Constraints):**
  - **Karaṇa:** Enforces constraints on the instruments or mechanisms used in an action.
  - **Sampradāna:** Restricts the destination, recipient, or beneficiary of the action.
  - **Apādāna:** Maps structural boundaries around source origins, ablative separations, and initial state boundaries.

Together, these lattices maintain rigorous grammatical logic and zero-drift structural execution across the entire token sequence.

---

## 3.4 The Bridge to Runtime Execution
To see how these semantic role bindings are handed off and mathematically enforced as allowlists during autoregressive decoding, see the **[Architectural Deep Dive: The Interpretation Contract vs. The Enforcement Contract](../04_runtime_core/interpretation_vs_enforcement.md)**.

<div align="center">

[← Previous Module](../02_mathematical_foundations/README.md) | [Main README](../../README.md) | [Next Module →](../04_runtime_core/README.md)

</div>
