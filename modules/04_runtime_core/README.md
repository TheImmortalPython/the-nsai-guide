[← Back to Main README](../../README.md)

# Module 4: Runtime Core, Compiler & Consensus Layer

## 4.1 Pāṇinian Kāraka Logit Masking (PKLM Core / `pklm-core`)
Theoretical frameworks meet real-time execution at the token probability level through **Pāṇinian Kāraka Logit Masking (PKLM Core / `pklm-core`)**. By evaluating incoming logit vectors at step $t$, the interception core identifies unauthorized or out-of-bounds token paths before sampling can occur.

## 4.2 Negative Infinity ($-\infty$) Vector Boundaries
To ensure a model cannot select a forbidden or unvalidated token under any stochastic variance, `pklm-core` applies **Negative Infinity ($-\infty$) as a Hard Boundary** directly onto the logits. When a token's probability weight is masked to $-\infty$, its resulting value after softmax evaluation becomes absolute zero, physically eliminating token drift, semantic leakage, and unauthorized outputs.

## 4.3 Production Orchestration & Execution Core
Running deterministic checks at scale in production requires robust pipeline architecture. The **Determinism Runtime Core (`determinism-runtime-core`)** serves as the compiler, execution, and orchestration layer. It provides asynchronous request queuing, containerized API wrappers, and low-latency validation loops to ensure non-stochastic constraints operate seamlessly across high-throughput production environments.

<div align="center">

[← Previous Module](../03_paninian_karaka_lattices/README.md) | [Main README](../../README.md) | [Next Module →](../05_tooling_and_hardware/README.md)

</div>
