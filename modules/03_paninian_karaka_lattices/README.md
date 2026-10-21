[← Back to Main README](../../README.md)

# Module 3: Grammatical Dependency Lattices

## 3.1 Pāṇinian Kāraka Dependency Frameworks
Integrating Pāṇinian syntactic structures into neural constraints allows language models to operate with absolute grammatical and semantic precision. Rather than relying on superficial token adjacency, the Pāṇinian Kāraka framework maps deep semantic relationships and syntactic dependencies directly into the constraint lattice.

## 3.2 Kartā and Karma Role Masking
To enforce structural correctness during generation, we apply precise role-based logit masking:
* **Kartā (Agent Role Masking):** Restricts token selection to ensure the active agent or subject governing the action remains structurally sound.
* **Karma (Goal/Target Mapping):** Constrains the output trajectory toward the exact objective or object of the action, eliminating semantic drift.

## 3.3 Contextual, Instrumental, and Boundary Constraints
Advanced grammatical containment requires mapping every environmental and relational boundary:
* **Adhikaraṇa (Locus/Context Boundaries):** Enforces spatial, temporal, or logical context boundaries to keep generation anchored.
* **Karaṇa, Sampradāna, and Apādāna:** Restricts instrumental mechanisms (*Karaṇa*), recipient targets (*Sampradāna*), and source/ablative separations (*Apādāna*) to maintain rigorous grammatical logic across the entire token sequence.

<div align="center">

[← Previous Module](../02_mathematical_foundations/README.md) | [Main README](../../README.md) | [Next Module →](../04_runtime_core/README.md)

</div>
