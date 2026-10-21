[← Back to Main README](../../README.md)

# Module 4: The Runtime & Interception Core

## 4.1 Pāṇinian Kāraka Logit Masking (pklm-core)
Theory must meet execution at the token probability level. Pāṇinian Kāraka Logit Masking (`pklm-core`) is the primary mechanism that intercepts model generation in real-time. By evaluating incoming logit vectors at step $t$, the system identifies unauthorized or out-of-bounds token paths before sampling occurs.

## 4.2 Negative Infinity ($-\infty$) Vector Boundaries
To ensure a model cannot select a forbidden token, `pklm-core` applies negative infinity ($-\infty$) as a hard mathematical boundary directly onto the logits. When a token's probability weight is set to $-\infty$, its resulting probability after softmax evaluation becomes absolute zero, physically eliminating token drift and unauthorized outputs.

## 4.3 Asynchronous Production Orchestration
Running deterministic checks at scale requires robust pipeline architecture. The Determinism Runtime Core (`determinism-runtime-core`) provides the production execution layer, featuring asynchronous request queuing, containerized API wrappers, and low-latency validation loops to ensure non-stochastic constraints operate seamlessly in production environments.

<div align="center">

[← Previous Module](../03_paninian_karaka_lattices/README.md) | [Main README](../../README.md) | [Next Module →](../05_tooling_and_hardware/README.md)

</div>
