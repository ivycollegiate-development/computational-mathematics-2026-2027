# U5 L19 — Paper Check: The Engine Works. Does the Model?

Names: ___________________________  Date: Mar 15

Closed notes. Calculator allowed. 50 minutes. No laptop. The engine running correctly tells you nothing about the model being right, and that distinction separates a number you may publish from one you may only preview.

## 1: Three questions about a result — The three-threat model

The engine reports:

- `p_any_closed_form = 0.592`
- `p_any_empirical = 0.591` (100,000 years)
- `ev_closed_form = 10350`
- `ev_empirical = 10402.1`
- `worst_case = 60000`, occurring in 1.2% of years

☐  Q1: the engine agrees with the closed form to within 0.001. What does that establish: ______________

☐  Q1 again: what does it not establish: ______________

☐  Q2: suppose the true likelihoods are each half what you entered. What happens to `p_any_closed_form`, roughly, and why: ______________

☐  Q3: the engine would still agree with the closed form in that case, so what is the engine actually a test of: ______________

☐  Write that as one sentence suitable for your report: ______________

## 2: The assumption audit — Fill in from your own work

| #          | assumption                               | status     | evidence     | what breaks if false     |
| ---------- | ---------------------------------------- | ---------- | ------------ | ------------------------ |
| 1          | T-phish fires with p = 2/5 a year        | ______     | ______       | ______                   |
| 2          | T-ransom fires with p = 3/20 a year      | ______     | ______       | ______                   |
| 3          | T-doxs fires with p = 2/10 a year        | ______     | ______       | ______                   |
| 4          | the three are independent                | ______     | ______       | ______                   |
| 5          | each costs exactly its stated impact     | ______     | ______       | ______                   |
| 6          | at most one occurrence per threat per year | ______     | ______       | ______                   |
| 7          | impacts do not interact with each other  | ______     | ______       | ______                   |
| 8          | a year is the right horizon              | ______     | ______       | ______                   |

☐  Which assumption is doing the most work in the final number: ______________

☐  Which is doing the least, and would you bother to justify it in the report: ______________

☐  Assumption 5 deserves more than you gave it. An impact of exactly 45,000 is a number with no spread at all. Does a real loss distribution weaken the EV — does it double it, inflate it, or leave it alone: ______________

☐  Assumption 8: consider a threat whose likelihood is per-year but whose response takes eighteen months. Which of your eight rows breaks: ______________

## 3: What would change your mind

1. A scan shows the misconfigured share is reachable from two internal subnets, not one. ______________
2. A CERT advisory reports a 90% ransomware rate in your sector, against your 15% assumption. ______________
3. Your org's actual incident history is 1 in 6 years, against your 1 in 20. ______________
4. A vendor's tool claims 99% accuracy. ______________
5. A peer organisation of the same size and sector reports 1 in 4. ______________
6. Nothing new; you simply have more confidence now. ______________

☐  All six, with your reasoning: ______________

☐  Which single item would move your model most, and why that one: ______________

☐  Item 4: does a vendor claim change your likelihood at all, and what would you need before it did: ______________

☐  Item 6: how do you tell the difference between gaining confidence and merely wanting to be right: ______________

## 4: The two-sentence version

Your model will be read by someone who sees one paragraph.

☐  Sentence 1 — what the model says, in one sentence with the number and its qualifiers: ______________

☐  Sentence 2 — what the model does not know, in one sentence: ______________

☐  Is sentence 2 something you would put in a document that goes to a lawyer: ______________

☐  Write the sentence you left out on purpose — the most important caveat nobody asked for: ______________

☐  Why did you leave it out: ______________

## 5: Before tomorrow — Seal this prediction

Tomorrow's bug is in a program that has passed every test you wrote. Predict where the error will be: in the arithmetic, in the implementation, or in an assumption nobody encoded: ______________

**TURN IN** — Parts 1–3 photographed with all work shown, the eight-row assumption audit, your two-sentence version plus the sentence you left out, your error log updated, and this prediction sealed before tomorrow.
