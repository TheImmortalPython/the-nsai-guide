[← Back to Main README](../../README.md)

# Module 4: Runtime Core, Compiler & Consensus Layer

## 4.1 Pāṇinian Kāraka Logit Masking (PKLM Core / `pklm-core`)
Theoretical frameworks meet real-time execution at the token probability level through **Pāṇinian Kāraka Logit Masking (PKLM Core / `pklm-core`)**. By evaluating incoming logit vectors at step $t$, the interception core identifies unauthorized or out-of-bounds token paths before sampling can occur.

### 4.1.1 Negative Infinity ($-\infty$) Vector Boundaries
To ensure a model cannot select a forbidden or unvalidated token under any stochastic variance, `pklm-core` applies **Negative Infinity ($-\infty$) as a Hard Boundary** directly onto the logits. When a token's probability weight is masked to $-\infty$, its resulting value after softmax evaluation becomes absolute zero, physically eliminating token drift, semantic leakage, and unauthorized outputs.

In autonomous agentic loops and Recursive Self-Improvement (RSI) workflows, pklm-core does not generate weight updates or serve as an introspective optimizer on its own; rather, its $-\infty$ vector masking acts as an immutable downstream firewall. While upstream representations continuously adapt (The Interpretation Contract), pklm-core ensures that self-referential token generation cannot breach structural invariants (The Enforcement Contract), preventing compounding drift during recursive cycles.

## 4.2 Deterministic Agent Architecture & Intent Routing
Applying Non-Stochastic AI to autonomous agent execution requires a hybrid execution framework that bridges open-ended natural language reasoning with strict structural determinism. Rather than locking an agent into rigid single-mode sampling, the runtime implements a dual-mode router paired with an under-the-hood verification pipeline.

### 4.2.1 Hybrid Execution: Dynamic Switching
The system evaluates ingress prompts through an intent-routing layer to dynamically determine the appropriate execution mode:
* **Probabilistic Ideation Mode:** Active during open-ended brainstorming, creative synthesis, and exploratory dialogue, allowing standard temperature and top-$p$ sampling where divergent outputs provide value.
* **Deterministic `pklm-core` Mode:** Automatically triggered when processing structured commands, state machine transitions, API payload execution, or mathematical operations. The runtime clamps token distributions using Pāṇinian Kāraka logit masking to enforce zero-drift containment.

### 4.2.2 Pre-Emission Verification Loops
To preserve low latency and avoid verbose chat-level retries, token verification occurs *under the hood* prior to token release:
1. **Candidate Draft Generation:** The base model generates candidate next-token logits based on current working context.
2. **In-Flight Interception & Validation:** The `pklm-core` engine intercepts candidate tokens against structural schemas, state boundaries, or Kāraka dependency rules.
3. **Zero-Drift Emission:** Invalid token paths are instantly suppressed ($-\infty$) and re-sampled within the allowed logit space before token emission to the client, guaranteeing zero-drift output with zero added retry latency.

## 4.3 Production Orchestration & Execution Core
Running deterministic checks at scale in production requires robust pipeline architecture. The **Determinism Runtime Core (`determinism-runtime-core`)** serves as the compiler, execution, and orchestration layer. It provides asynchronous request queuing, containerized API wrappers, and low-latency validation loops to ensure non-stochastic constraints operate seamlessly across high-throughput production environments.

## 4.4 Runtime Execution Contracts
To explore the precise architectural boundary between upstream semantic role binding and step-by-step token containment during decoding, read the **[Architectural Deep Dive: The Interpretation Contract vs. The Enforcement Contract](./interpretation_vs_enforcement.md)** (also referenced in Module 3).

<div align="center">

[← Previous Module](../03_paninian_karaka_lattices/README.md) | [Main README](../../README.md) | [Next Module →](../05_tooling_and_hardware/README.md)

</div>
