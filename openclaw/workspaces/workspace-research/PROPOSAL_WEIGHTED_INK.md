# PROPOSAL: Dynamic Risk-Weighted Routing (Project "Weighted-Ink")

## 1. THE PROBLEM: "Permanent Ink" Overspend
Currently, Tommy (Coding/System Agent) defaults to **GPT-5.4** for nearly all tasks. 
- **The Financial Cost:** Every interaction, including simple file-reads, directory listings, and brainstorming, costs ~$0.05 - $1.80. Over a month of heavy development, this creates massive overhead.
- **The Cognitive Mismatch:** Using a "Core-Knowledge" model for "File-Summary" tasks is overkill. It’s like using a high-pressure permanent ink pen to sketch a rough anatomy: mistakes are expensive and hard to undo.
- **The Risk Paradox:** High-tier models are less prone to hallucinations, but using them for *everything* depletes the budget needed for truly critical system surgery.

## 2. THE SOLUTION: Mission Difficulty (MD) Scaling
We propose a grading system (1-100) that determines which "Weight of Ink" (Model) to use based on the **Likelihood of Hallucination** and **Potential System Damage**.

### **The MD Tiers**
- **MD 1-30: "The Erasable Sketch"** (Brainstorming, reading logs, outlining). 
  - *Model:* Gemini 3 Flash / GPT-5 Nano.
- **MD 31-70: "The Pencil Drawing"** (Writing standalone scripts, non-core bug fixes). 
  - *Model:* Claude 4.6 Sonnet / Gemini 3 Pro.
- **MD 71-100: "The High-Pressure Pen"** (Editing `openclaw.json`, Gateway routing, mass deletions). 
  - *Model:* GPT-5.4 (Turbo/O1).

## 3. THE PROTOCOL: Intake & Grade
Tommy's new operating procedure for every request:
1. **Analyze:** Parse the user request.
2. **Grade:** Assign a Mission Difficulty (MD) Score (1-100).
3. **Select:** Recommend a model based on the tier.
4. **Confirm:** Ask Andre: *"This is a [MD Score] task. I recommend [Model]. Proceed?"*

---

## 4. TOMMY'S ASSIGNMENT
Tommy, review this "sketch" of the protocol. Your task is to:
1. **Critique:** Identify any flaws in how MD scores should be calculated.
2. **Finalize:** Write the specific **IDENTITY.md** or **SOUL.md** updates that will hard-code this logic into your persona.
3. **Implementation Plan:** How will you handle "Context Carryover" when moving from a Flash-MD-10 sketch to a 5.4-MD-90 implementation?

**Await Andre's review before editing your core files.**
