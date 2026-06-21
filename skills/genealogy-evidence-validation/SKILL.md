---
name: genealogy-evidence-validation
description: Evidence validation protocol for genealogy research. Scores findings, prevents homonym drift, separates records from people, and turns each search into confirmed evidence, actionable clue, qualified negative, access block, or discard.
description_pt-BR: Protocolo de validacao de evidencias genealogicas. Pontua achados, evita homonimos, separa registro de pessoa e transforma cada busca em prova, pista acionavel, negativo qualificado, bloqueio de acesso ou descarte.
type: prompt
version: "1.0.0"
categories: [genealogy, research, evidence, validation]
contract:
  inputs:
    - name: search_unit
      required: true
      description: Person + event + place + date window + known relatives.
    - name: source_or_finding
      required: true
      description: The document, index, catalog entry, public source, or access result being evaluated.
    - name: evidence_ledger
      required: false
      description: Existing structured ledger used to avoid duplicate searches and repeated false positives.
  quality_criteria:
    - "Every finding is classified as A, B, C, D, X, qualified_negative, or access_block."
    - "No person in the family tree is updated from an index, OCR hit, third-party tree, or isolated name match alone."
    - "Each accepted identity match includes at least two discriminators: spouse, parent, child, place, date/window, or book/page/term reference."
    - "Each qualified negative includes source, place, period, variants tested, access mode, and reason for the conclusion."
    - "Each access block includes the block type and the next non-web action."
    - "Next action is one of: update_tree, transcribe, request_certificate, manual_search, refine_query, quarantine, discard, or stop."
  on_failure: halt
---

# Genealogy Evidence Validation

Core principle: genealogy is a chain of proof, not a list of matching names.

Use this skill whenever a genealogy agent maps gaps, searches records, evaluates findings, updates a tree, or decides whether to continue a research branch.

## Evidence Scale

| Grade | Name | Definition | Authorized use |
|---|---|---|---|
| A | confirmed_primary | Certificate, book image, civil/parish record, or official file with identity and relationship fields. | May update the tree. |
| B | confirmed_secondary | Official transcript, clear index tied to a specific source, or certificate excerpt with enough discriminators. | May guide requests; update only with caveat. |
| C | strong_clue | Name plus at least two coherent discriminators, but no image/term/certificate yet. | Creates the next search or request. |
| D | weak_clue | Partial name/place/date, third-party tree, unsourced OCR, cemetery note, or loose newspaper mention. | Backlog only. |
| X | discarded | Spouse, parents, child, date, place, or event conflicts with the target. | Do not reuse unless new data appears. |
| qualified_negative | qualified_negative | Search was executed with enough scope to be useful and reproducible, with no result. | Prevents duplicate search. |
| access_block | access_block | Search could not be completed because of login, center restriction, captcha, missing image, or formal request requirement. | Triggers non-web action. |

## Identity Gate

Never accept a record as belonging to a target person from name alone.

To classify a record as A, B, or C, require at least two discriminators:

- spouse
- father or mother
- child
- coherent place
- coherent date or date window
- book, page, term, DGS, cartorio, parish, or archive reference

If only one discriminator exists, keep the finding as D or quarantine it until another source appears.

## Record-Person Separation

Always treat a found record as a candidate record first.

Process:

1. Create or update a finding row.
2. Extract fields exactly as the source presents them.
3. Compare fields to the target person.
4. Assign grade and status.
5. Decide the next action.
6. Only then update the tree, and only for A or controlled B evidence.

## Qualified Negative Gate

A negative result is useful only when it is reproducible.

Required fields:

- source
- place or jurisdiction
- period searched
- variants tested
- access mode
- search method
- reason the result is negative

Without these fields, classify as `incomplete_search`, not `qualified_negative`.

## Access Block Gate

When blocked by login, FamilySearch Center restriction, captcha/human verification, missing image, or formal archive request:

1. Classify as `access_block`, not as negative.
2. Record block type.
3. Stop web expansion for that branch.
4. Create the next non-web action: manual logged search, FamilySearch Center visit, cartorio request, parish request, archive request, or human transcription.

## Output Schema

Use this compact structure in artifacts and ledger rows:

```text
finding_id:
target_id:
person_name:
event:
source:
source_ref:
place:
period:
variants_tested:
discriminators:
grade:
status:
confidence_note:
next_action:
next_action_ref:
privacy:
last_checked:
```

## Hard Stops

Stop and downgrade or reject the finding if:

- it relies on a living person's private data for web search;
- it promotes a third-party tree without source;
- it treats an index or OCR hit as a certificate;
- it repeats a broad web search after an access block;
- it uses a leak, CPF dump, or illicit personal-data source;
- it makes a citizenship/legal conclusion without a continuous documented line.
