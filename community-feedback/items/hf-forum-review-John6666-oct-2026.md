# Community Feedback: John6666 (Hugging Face Forums — Show and Tell)

**Reviewer:** `John6666`  
**Source:** [Hugging Face Community Forums (Show and Tell)](https://discuss.huggingface.co/t/the-nsai-guide-non-stochastic-ai-architecture-and-execution/191033)  
**Topic:** *The NSAI Guide: Non-Stochastic AI Architecture and Execution*  
**Date:** October 28, 2026  

---

### John6666:

I took a quick look at the public implementation and ran a few small experiments:

---

## The connection between the public modules

The interesting idea here is to apply semantic boundaries **during generation**, rather than rely only on a prompt or reject the output afterward. A hard mask can exclude prohibited token IDs before selection. What I wanted to understand next was how the permitted set is derived: which event and Kāraka relation are active, who determines their roles, and how the permitted tokens change as generation proceeds.

I looked through the public [NSAI Guide](https://github.com/TheImmortalPython/the-nsai-guide) and its runnable [Module 3 role-filter example](https://github.com/TheImmortalPython/the-nsai-guide/blob/1e18834fbef2532b532060ea415b55999f20377e/playground/module_3_demo.py) and [Module 4 masking example](https://github.com/TheImmortalPython/the-nsai-guide/blob/1e18834fbef2532b532060ea415b55999f20377e/playground/module_4_demo.py). Module 3 filters candidate strings that already have role/category labels. Module 4 applies a `LogitsProcessor` to an explicitly supplied set of token IDs. Both are understandable teaching examples. The part I could not trace **in the public examples** is the bridge from an input-specific Kāraka interpretation to an updated allowed-token set at each decoding step.

The repository distinguishes its public teaching material from the private `pklm-core`. A bridge not shown in the public demo is **not** evidence that it is absent from the private engine. This is a documentation question, not a bug report.

A short role-to-token trace would make the distinctive point easier to see: a JSON schema can require a `Kartā` field, but the schema alone does not establish whether its value is the right participant for the chosen event.

## One small example could make that connection visible

Consider this sentence:

> Alice sent the red parcel to Bob.

For this **illustrative sending event**, suppose `Kartā = Alice`, `Karma = red parcel`, and `Sampradāna = Bob`. This is a deliberately simplified example, not an assertion about the full Pāṇinian theory or the private NSAI ontology.

Both candidate records below have the same valid JSON structure:

```json
{"Kartā":"Alice","Karma":"red parcel","Sampradāna":"Bob"}

```

```json
{"Kartā":"Bob","Karma":"red parcel","Sampradāna":"Alice"}

```

A grammar checking keys and value types accepts both, as does a rule merely requiring two different people. A constraint based on the **correct binding for this sending event** excludes the second. That illustrates what role-sensitive enforcement can add beyond formatting.

A minimal teaching trace might show these stages:

| Stage | Information worth exposing |
|----|----|
| Input and event | The chosen predicate/event, and whether it is asserted, denied, quoted, or hypothetical if relevant |
| Role bindings | The active Kāraka labels, associated participants, and where those assignments came from |
| Generated prefix | For example, the point just after `{"Kartā":"` |
| Allowed pieces | Which next token IDs or tokenizer pieces are legal under that prefix and those bindings |
| State transition | How accepting one piece changes the parser/role state |
| Completion | Why EOS is legal, or why the system must stop, abstain, or report an impossible constraint |

A hand-annotated trace or pseudocode would be enough; no private code is needed. For a guide, it explains the interface between the modules. For a runtime, the same positive/negative pair can serve as a regression test.

There are **two distinct contracts**:

1. **Interpretation:** determine which event and participants the sentence describes, and assign the intended roles.
2. **Enforcement:** given accepted role bindings, prevent the output from violating those bindings.

A parser, LLM, application, or hybrid can supply the interpretation; a constrained decoder can enforce the accepted binding. The second contract can succeed even when the first is wrong.

## What a few independent experiments suggested

I ran an independent finite-state toy and two Colab probes with **Qwen2.5-0.5B-Instruct**. None used `pklm-core`; the results concern **the separation of these contracts, not NSAI performance**.

In the finite toy, I could enumerate the entire permitted output language:

| Toy constraint | Accepted completed outputs |
|----|---:|
| Only the fixed record grammar | 4 |
| Record grammar, with different people in two slots | 2 |
| Correct externally supplied event-role binding | 1, correct |
| Incorrect externally supplied binding | 1, incorrect |

The last row matters: a mask can perfectly enforce a wrong binding. This does not make enforcement defective; it identifies a separate interpretation test.

The first real-model probe forced the expected values **when those values were supplied in advance**: an *oracle enforcement* test, not autonomous role inference. In the second probe, the reference sender/recipient answers were withheld from generation. On **16 synthetic cases**, JSON-constrained generation produced valid JSON in **16/16** but identified the task-level participants correctly in **10/16**. Prompt-only generation scored **11/16** for the roles after Markdown code fences were removed for parsing. A separate role-estimation branch scored **8/16 correct, 11/16 parseable** under a strict parser; case-only normalization of names gave **10/16 correct, 14/16 parseable**. Two unresolved outputs included `UNKNOWN`.

This was a tiny, presentation-sensitive synthetic set; changing A/B order frequently changed decisions. The tests used task-level *sender/recipient* slots, **not all six Kāraka relations**. The useful distinction is between **format validity, constraint compliance, role accuracy, and parser acceptance**.

A small comparison could show *supplied roles* and *inferred roles* side by side. The first tests enforcement; the second, with a withheld key, tests interpretation. Ambiguity and abstention can be reported separately.

## Different goals suggest different next steps

The appropriate next example depends on what “non-stochastic” and “zero semantic drift” are meant to cover:

| If the main goal is… | A particularly useful small example |
|----|----|
| **Explaining the architecture** | One role binding, a generated prefix, an allowlist, a state update, and a stopping condition |
| **Enforcing supplied semantic constraints** | Same-schema positive/negative records, with an externally validated binding |
| **Inferring roles from language** | Active/passive paraphrases and reversed participants, scored against an independent key |
| **Ensuring deterministic execution** | Separate mask correctness from sampling, tie-breaking, environment, and repeated-run equality |
| **Using the result to control actions** | Define impossible-constraint handling, authority checks, and validation before an external action |

For an introductory Show and Tell post, **the first two rows are probably enough**. The remaining branches are optional. I have placed longer technical notes below for readers who want to pursue them.

<details>
  <summary><b>The public modules and a possible role-to-token interface</b></summary>
### What is visible, and what remains a conditional interface

In the public `playground/module_3_demo.py`, candidates already have labels such as `Agent`, `Target`, and `Locus`. Filtering those candidates by an active label shows how a symbolic decision can reduce a candidate set. It does not show automatic role labeling from unrestricted natural language, and the three demonstrated categories should not be described as a tested implementation of all six Kāraka roles.

The public `playground/module_4_demo.py` illustrates the other end: a fixed `allowed_token_ids` list is used to construct an additive mask over model scores, with `-inf` for disallowed IDs and zero for admitted IDs. Under normal finite-score decoding assumptions, a forbidden ID cannot be sampled from that masked distribution. The example does not, by itself, calculate an allowlist from the evolving prefix or from the output of Module 3. Such machinery may exist elsewhere; the public sample simply leaves it outside the demonstration.

The useful interface to document is approximately:

```python
# Explanatory pseudocode; NOT an implementation of pklm-core.
event = select_event(input_text, requested_task)
roles = infer_or_receive_role_bindings(event)
state = initialize_output_state(roles, grammar, tokenizer)

while not state.complete:
    allowed_ids = legal_next_token_ids(state)
    if not allowed_ids:
        return abstain_or_fail("no legal continuation")
    scores = model_scores(state.prefix_ids)
    selected_id = decode_with_mask(scores, allowed_ids)
    state = consume_and_update(state, selected_id)

output = render(state)
if not independently_validate(output, requested_task):
    return abstain_or_fail("validation failed")
return output

```

This is only an **interface sketch**, not a description of `pklm-core` internals. It highlights three questions: where accepted bindings come from, how uncertainty is represented, and what preserves the bindings during decoding.

### A compact trace readers could reproduce

Suppose the accepted state says that the current event is `send(Alice, parcel, Bob)`. The structured output prefix is `{"Kartā":"`. The semantic part identifies Alice as the permitted filler for that slot; the grammar part decides how the value can be represented as tokens at that point. After the value is completed, the grammar moves on to the next field. At the `Sampradāna` value, Bob is permitted and Alice is excluded. Finally, the state must recognize a completed valid record and permit the appropriate terminal behavior.

A conceptual trace can use readable pieces rather than numeric IDs, provided it says so. Real IDs depend on the tokenizer; quotes, names, and separators may share a token. What matters is that **the accepted event binding, generated prefix, and output specification jointly determine the permitted continuations**.

A further column could indicate whether the current prefix still has *any complete valid continuation*. That property is stronger than allowing each next token in isolation. It also makes contradictory semantic constraints easy to explain without demanding a proprietary parser or a large benchmark.

</details>

<details>
  <summary><b>Independent experiments, controls, and what the measurements mean</b></summary>
### Why the toy was intentionally small

The toy used a tiny vocabulary, three illustrative fields, and two people. Exhaustive enumeration found four schema-valid completions, two with distinct participants, one with the correct supplied binding, and one wrong completion with an inverted supplied binding. It also included token fragments spanning boundaries. This tests a **finite acceptance language**, not language comprehension.

Exhaustive enumeration lets us inspect all valid completions instead of trusting one sampled response. It cannot establish behavior on ambiguous natural language, novel events, long outputs, or a proprietary ontology.

### The blind-role probe and its limits

The second T4 run withheld gold mappings and used 16 constructed cases with direction reversals and varied wording. Prompt-only correctness was **11/16** after fence removal; JSON-constrained correctness was **10/16**. The structure-constrained mode emitted valid JSON on all 16 fixtures without thereby ensuring the right semantic direction.

When the model separately proposed the participants and the output was then constrained to reproduce its proposals, the constraint faithfully propagated both good and bad proposals. The strict parser initially accepted **11/16** and scored **8/16** correct. Case-only normalization raised these to **14/16** accepted and **10/16** correct. This changes evaluation, **not the model’s outputs**. `UNKNOWN`, malformed formatting, and confidently inverted roles should be separate categories.

The direction-sensitive subset was striking but not conclusive: in the earlier audit, prompt-only correctness for a conventional ordering was **8/8** and for the reversed direction **3/8**; the structured branch showed **8/8** versus **2/8**. An A/B option-order control changed the selected answer in **12/16** cases. That is a diagnostic of these prompts and this small model, not a population statistic or a demonstrated property of NSAI. It suggests that names, ordering, surface phrasing, and answer parsing are worth balancing in any later evaluation.

### A small evaluation ladder

| Layer | Minimal test | What it can establish | What it cannot establish |
|----|----|----|----|
| Formatting | Same output schema, varied content | JSON/grammar compliance | Participant truth |
| Relationship constraint | Equal versus different participants | A cross-field invariant | Which person had which role |
| Oracle role enforcement | Supply known correct bindings | The decoder preserves accepted constraints | Independent role identification |
| Blind role inference | Hide gold roles; score selected event and bindings | Task-specific interpretation on test inputs | Universal semantic correctness |
| End-to-end behavior | Combine inference, mask, termination, independent checker | Observed joint behavior on stated cases | Guarantees outside the modeled assumptions |

When evaluating inference, keep gold answers outside the mask builder. Call externally supplied bindings *oracle* or *trusted input*. Use wrong-but-schema-valid controls and track ambiguity and abstention.

### A practical, low-cost set of paired tests

One can begin with only four pairs. (1) Swap Alice and Bob in the event and expect the bindings to swap. (2) Rewrite an active transfer as a passive while preserving the event relation. (3) Switch from `send` to `receive` and specify whether the target is a normalized transfer record or predicate-relative roles. (4) Put the event in a quotation or negate it, but only if the intended task cares about assertion status. A successful role constraint should be tested against *wrong-but-well-formed* records, not only malformed JSON.

For a trace-based demonstration, record the selected event, role input, tokenizer identity, generated prefix, legal IDs, chosen ID, state after commitment, EOS handling, and an independent final check. The first small positive/negative example need not include all of these columns; the extra records become useful when a discrepancy appears. A short failure analysis is usually more reusable than a single aggregate percentage.

</details>

<details>
  <summary><b>Kāraka, predicate meaning, and event scope</b></summary>
### Keep the project’s terms while distinguishing different analyses

The public documentation discusses the familiar role names `Kartā`, `Karma`, `Karaṇa`, `Sampradāna`, `Apādāna`, and `Adhikaraṇa`, with an explanatory vocabulary around agency, target, instrument, recipient, source, and locus. Those labels are useful as an organizing scheme, but assigning them is not generally equivalent to labeling the first two people in an English sentence as sender and recipient. The [Pāṇinian syntactico-semantic relations paper](https://aclanthology.org/W19-7724/) and a [cross-framework study of meaning representations](https://aclanthology.org/2020.cl-3.3/) are useful context on why role inventories depend on the chosen grammatical and semantic conventions.

Our original proxy looked primarily at a sender and a recipient. It did not independently test `Karma` as the transferred parcel or systematically exercise `Karaṇa`, `Apādāna`, and `Adhikaraṇa`. It is more accurate to call those experiments *a task-level analogy to one part of the role-binding problem* than a validation of Pāṇinian grammar. The sample assignment for Alice and Bob is deliberately limited to one sending event.

### The predicate matters more than mention order

`Alice sent the parcel to Bob` and `The parcel was sent to Bob by Alice` can describe the same transfer, despite different word order and grammatical subject. A transaction extractor might normalize both to `transfer(sender=Alice, item=parcel, recipient=Bob)`. The general point is that a surface-position rule is not a reliable semantic analysis.

`Bob received the parcel from Alice` introduces a subtler choice. A **task-oriented transfer record** can still have sender Alice and recipient Bob, while a **predicate-relative Kāraka analysis of receive** must assign its formal roles under the semantics of the receiving predicate. The grammatical subject in `receive` is not automatically the `Kartā` of an independently normalized sending event. A specification should say which representation is being enforced; a decoder cannot resolve a disagreement between two different target ontologies merely by making its output stricter.

Similarly, in `Alice moved the parcel from Room A to Room B`, a source, destination, moved object, and mover are present. Neither source nor destination is automatically a recipient of a transfer. An instrument such as `with a trolley` introduces another relation. Which slot is active must follow the selected predicate/event representation, not just a list of named entities. That question can be handled explicitly without claiming that any one modern semantic-role framework fully captures the author’s design.

### Selecting an event is separate from deciding whether it occurred

Consider:

* `Alice did not send the parcel to Bob.`
* `Carol said Alice sent the parcel to Bob.`
* `Carol denied that Alice sent the parcel to Bob.`
* `If Alice sends the parcel to Bob, a receipt is required.`
* `Did Alice send the parcel to Bob?`

All mention a sending event, but they do not all assert that it happened. A system asked to extract *mentioned propositions* may include it with a negation, attribution, question, or hypothetical marker. A system asked to record *completed transactions* should not convert every mentioned event into an asserted fact. It is possible for the participant roles to be internally consistent while the wrong event or assertion status is being reported.

This creates three separable decisions: **which event**, **which roles within that event**, and **what commitment the text makes to the event**. A basic guide need not model all this; it matters if the guarantee extends to facts or actions.

### Multiple plausible interpretations and missing arguments

Natural language frequently leaves roles implicit or permits several interpretations. If a system has only a partial role binding, it can either preserve multiple candidates, mark an unknown slot, invoke a domain-specific rule, or abstain. A forced single completion may be perfectly consistent with one assumption while not representing what the input actually determines. In an execution context, the distinction matters even more: an apparently grammatical `Kartā` value does not grant permission to perform an action or establish that the statement describes a verified real-world event.

I would regard this as a **modeling choice to expose**, not a reason to reject hard decoding. A clearly stated conditional guarantee, such as “given a validated event and role assignment, output is restricted to records consistent with it,” is both strong and testable. A broader guarantee that the system always picks the right event and roles from arbitrary language would require different evidence.

</details>

<details>
  <summary><b>Runtime contracts: token boundaries, termination, and determinism</b></summary>
### A mask is one step in a stateful protocol

An actual generator repeatedly calculates admissible next tokens, selects one, commits it to an evolving state, and eventually ends or declines to continue. The mask may be locally correct while the overall output fails because the constraint state is stale, the tokenizer splits a meaningful unit unexpectedly, a required continuation becomes impossible, or the system stops too early. These are general implementation boundaries, **not observed failures of NSAI**.

A real tokenizer’s unit is not necessarily an English word. A token may contain whitespace and punctuation, join a quote to a colon, cover only part of a name, or cross a grammar boundary. The independent source inspection confirmed examples of merged punctuation pieces in an actual tokenizer, while the finite proxy deliberately included cross-boundary fragments. In such cases an implementation has to evaluate the *whole token’s effect on the current accepted prefix*, not simply ask whether the next English word is allowed. The [DOMINO paper](https://proceedings.mlr.press/v235/beurer-kellner24a.html) is particularly useful on matching formal constraints to subword vocabularies.

A practical check is to take a field boundary such as `"Kartā":"` and inspect tokens that may span the closing quote, separator, or part of the following value. A parser and tokenizer may each be locally reasonable yet disagree about when a token can be consumed. A reported [llguidance token-boundary issue](https://github.com/guidance-ai/llguidance/issues/366) illustrates why such cases deserve a regression test; it is not evidence that the NSAI runtime has the same problem.

### Local legality is not always completion feasibility

Suppose a decoder emits two role fields with a rule that their values differ. At the first field, choosing either person may be locally legal. But if the second field has additional restrictions, one first choice can make the final record impossible. More generally, a prefix can satisfy everything checked *so far* yet have no legal completed extension. This is a reason to distinguish **allowed next token** from **allowed prefix with a valid completion**.

For a small finite candidate language one can enumerate all continuations and compare the implementation against the known set. For a richer grammar, a state machine or parser may detect contradictions before stopping. For semantic constraints, the required lookahead depends on their structure and the claimed guarantee. The [ChopChop work](https://doi.org/10.1145/3776708) is a useful adjacent comparison for semantically constrained program outputs; it is not a plug-in proof of natural-language Kāraka correctness.

### Empty candidate sets and EOS need explicit rules

The public Module 4’s simple additive mask is a valid way to illustrate hard exclusion, but its educational snippet does not prescribe every failure policy. An all-`-inf` score vector can yield invalid sampling probabilities. An empty set of allowed token IDs can mean an inconsistent specification, an impossible prefix, a state error, or an omitted terminal rule. A robust runtime must decide whether to reject, abstain, backtrack, or use a defined completion transition. It should not silently open the vocabulary to make the example finish.

The [Transformers generation-processor documentation](https://huggingface.co/docs/transformers/v4.56.2/en/internal/generation_utils) and [generation tests](https://github.com/huggingface/transformers/blob/main/tests/generation/test_logits_process.py) are useful version-sensitive references for how a general-purpose implementation handles prefix restrictions. They are not a universal runtime policy. Behavior can change across versions, so a test should record the installed library and model settings.

Completion also is not identical to appending EOS whenever a JSON parser seems happy. Some tasks permit trailing whitespace; others require an explicit terminal token; others stop at a well-defined semantic final state. The implementation needs to know when stopping is legal and what happens if `max_new_tokens` is reached before completion. An invalid intermediate state, deliberate refusal, normal completion, and runtime exception should not all be reported as one kind of failure.

### Hard exclusion is not the same as deterministic output

If several tokens remain legal, the mask can still leave a distribution from which the decoder samples. Greedy selection may choose one, but deterministic selection in a particular algorithm is distinct from reproducibility across software, hardware, batching, and numeric implementations. Conversely, a single permitted token at every step can yield a forced sequence without proving that the selected role interpretation was correct. There are at least four different properties worth naming:

1. **Safety of the allowlist:** forbidden IDs are excluded when the mask applies.
2. **Semantic correctness of the allowed language:** the rules describe the intended relationship.
3. **Decision policy:** which legal candidate is chosen when more than one remains.
4. **Run reproducibility:** whether identical requests yield identical sequences under specified execution conditions.

For the fourth question, the [vLLM reproducibility documentation](https://docs.vllm.ai/en/stable/usage/reproducibility/) is a useful example of why operating conditions matter. A “non-stochastic” claim could concern the second or third property, or a stronger end-to-end invariant; an explicit definition would keep readers from attaching an unintended interpretation to the project name.

### A compact optional regression matrix

| Case | Property to observe |
|----|----|
| One legal ID, and then two | Exclusion works; selection among legal IDs is separately defined |
| Empty allowlist or out-of-range ID | Defined error/abstention and validation of constraints |
| Quoted field separator inside one token | Prefix-state and tokenizer alignment |
| Name split into several pieces | Candidate continuation remains correct across pieces |
| Contradictory cross-field roles | Impossibility is detected rather than masked over |
| EOS before all required fields | Incomplete output is not reported as success |
| Two requests in one batch | Each output uses its own role state |
| Repeated identical prefix | State updates and allowlists can be reproduced under stated conditions |

These are optional regression tests, not requirements for an introductory guide. Issues in other projects illustrate test conditions, not defects in NSAI.

</details>

<details>
  <summary><b>Related work and optional routes for a future reader</b></summary>
### Compare the boundary being guaranteed, not project labels

There are useful predecessors and adjacent designs, but they answer different questions. [Transformers prefix constraints](https://huggingface.co/docs/transformers/v4.56.2/en/internal/generation_utils) expose a generic next-token interface. [PICARD](https://aclanthology.org/2021.emnlp-main.779/) shows incremental parsing to reject structurally inadmissible continuations in text-to-SQL generation. [DOMINO](https://proceedings.mlr.press/v235/beurer-kellner24a.html) studies token-aligned grammatical constraints and the cost of applying them. [llguidance](https://github.com/guidance-ai/llguidance/blob/main/parser/README.md) and [XGrammar](https://xgrammar.mlc.ai/docs/latest/api/python/grammar_matcher.html) are concrete sources for stateful token-mask interfaces. [ChopChop](https://doi.org/10.1145/3776708) explores programmable semantic restrictions for generated programs. None is automatically equivalent to Kāraka-based semantic role inference from unrestricted natural language.

These references make a useful map rather than a leaderboard:

| Component or research line | Reusable idea | Boundary not settled by that idea alone |
|----|----|----|
| Grammar, schema, and prefix-constrained decoding | Exclude malformed or disallowed continuations | Whether the semantic specification is true |
| Stateful parsing/matching | Track legal prefixes as tokens arrive | Which underlying event was intended |
| Tokenizer-aware decoding | Handle subword and cross-boundary pieces | Correct assignment of participants |
| Semantic/type-aware program constraints | Restrict a defined program/output language | Broad linguistic meaning in arbitrary prose |
| Pāṇinian dependency/role analysis | Name predicate-relative relations explicitly | Correctness of a private role-to-mask compiler |

These boundaries can be explained independently, without asking the guide to prove every type of semantic guarantee at once.

A single scoped teaching trace showing how an accepted Kāraka binding enters the legal-token calculation would connect the public examples without requiring disclosure of the private engine.
</details>

