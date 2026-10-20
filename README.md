# The NSAI Guide: Non-Stochastic AI Architecture and Execution

> **Enterprise Governance:** Managed under **TheImmortalPython Labs** (IP Incubator & Enterprise Governance).  
> **Pioneered By:** Joshua St. Germain.

---

## Scope & Architecture
This repository provides a complete, production-grade educational architecture for learning and implementing Non-Stochastic AI (NSAI) and its supporting tooling. It covers the full public specification, mathematical foundations, and runtime mechanics, serving as a comprehensive instructional guide.

---

## Curriculum Roadmap

* **Module 1: Foundational Paradigm & Governance**
  * Confronting the probabilistic black-box myth.
  * Enterprise governance under TheImmortalPython Labs.
  * The **Certified Safe AI** benchmark standard (100% syntactic compliance).
* **Module 2: Mathematical & Topological Foundations**
  * Tensor-Topology Constraint Calculus.
  * Zero-Drift / Zero-Trace Linguistic Containment (10,000+ token horizons with zero overhead penalty).
  * Dynamic Finite State Machine (FSM) Logit Geometry.
* **Module 3: Grammatical Dependency Lattices**
  * Paninian Karaka dependency frameworks (*Kartā*, *Karma*, *Adhikaraṇa*, *Karaṇa*, *Sampradāna*, *Apādāna*).
* **Module 4: The Runtime & Interception Core**
  * Paninian Karaka Logit Masking (`pklm-core`) utilizing negative infinity ($-\infty$) vector boundaries.
  * Asynchronous production orchestration via `determinism-runtime-core`.
* **Module 5: Tooling, Ecosystem & Hardware**
  * Middleware verification via `pklm-sandbox` and the `pklm_sandbox` PyPI package.
  * Offline Field Tool Middleware (low-resource edge deployment).
  * Physical hardware containment via the Akasha Silicon / Akasha CIS-1 PCIe card concept.

  ---

## Interactive Code Playground (`/playground`)
To put theory into practice, each module is paired with a runnable demonstration script located in the `playground/` directory. These scripts provide lightweight, hands-on examples of the core mechanisms taught across the curriculum:

* **Module 1 (`module_1_demo.py`):** Demonstrates the structural shift from unconstrained probabilistic sampling to deterministic boundary enforcement.
* **Module 2 (`module_2_demo.py`):** Simulates applying spatial boundary constraints (`-inf`) to raw logit vectors using FSM geometry.
* **Module 3 (`module_3_demo.py`):** Implements Pāṇinian Kāraka role-based dependency filtering (*Kartā*, *Karma*, *Adhikaraṇa*).
* **Module 4 (`module_4_demo.py`):** Shows core logit interception and negative infinity boundary masking using PyTorch/Transformers logic.
* **Module 5 (`module_5_demo.py`):** Emulates zero-drift execution for offline field tool middleware.

### Quickstart: How to Run the Playground

1. **Clone the repository:**
```bash
git clone https://github.com/TheImmortalPython/the-nsai-guide.git
```

2. **Enter the directory:**
```bash
cd the-nsai-guide
```

3. **Run any module demonstration script:**

```bash
python playground/module_1_demo.py
```

```bash
python playground/module_2_demo.py
```

```bash
python playground/module_3_demo.py
```

```bash
python playground/module_4_demo.py
```

```bash
python playground/module_5_demo.py
```
