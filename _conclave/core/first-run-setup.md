# Conclave First-Run Setup Pipeline

> This pipeline runs automatically the first time a user activates Conclave.
> It ensures ALL configuration files are properly populated so the environment
> is fully functional for any squad.

<!--
  TRIGGER CONDITIONS:
  This pipeline is triggered when ANY of these are true:
  1. company.md contains `<!-- NOT CONFIGURED -->`
  2. preferences.md has empty identity fields
  3. global-preferences.md has only instructional comments (no actual rules)
  4. visual-identity.md has only instructional comments (no actual design data)
  5. visual-voice.md has only instructional comments (no actual voice data)

  EXECUTION MODEL:
  This pipeline runs as a guided conversation with the user, broken into phases.
  Each phase ends with a checkpoint asking the user to confirm or adjust.
  The AI agent reads the embedded instructions in each file and uses them
  to interview the user.
-->

---

## Phase 0: Welcome & Language

**Goal:** Identify the user and set communication preferences.

### Steps:
1. Welcome the user warmly to Conclave.
2. Ask their **name** (first name or nickname they prefer).
3. Ask their **preferred language** for all outputs.
4. Ask which **IDEs** they use (comma-separated).
5. Ask their preferred **date format**.
6. Save to `_conclave/_memory/preferences.md`:
   - Fill the Identity section with name, language
   - Fill the IDEs in Use section

### Files Written:
- `_conclave/_memory/preferences.md`

---

## Phase 1: Company / Project Profile

**Goal:** Build the user's company.md — the central context file for all squads.

### Steps:
1. Ask the user: "What is this project about? Are you a company, personal brand, freelancer, or building a product?"
2. Ask for their **website URL** (if any).
3. If URL provided:
   - Use WebFetch to analyze the website content
   - Use WebSearch with the company/project name
   - Extract: description, sector, target audience, products/services, tone of voice, social media profiles
4. If no URL:
   - Ask structured questions to fill each section:
     - Name, type, location, contact
     - Online presence (primary/secondary channels)
     - Positioning (what they stand for)
     - Sector
     - Target audience
     - Tone of voice
     - Strategic objective (12-24 months)
5. Present the findings in a clean summary.
6. **CHECKPOINT:** Ask the user to confirm or correct the profile.
7. Save to `_conclave/_memory/company.md` (remove the `<!-- NOT CONFIGURED -->` marker).

### Files Written:
- `_conclave/_memory/company.md`

---

## Phase 2: Visual Identity Discovery

**Goal:** Build the user's visual identity — colors, typography, layout philosophy.

### Steps:
1. Inform the user: "Now let's define your visual identity. This affects all visual outputs (carousels, presentations, design assets)."
2. **Quick-path check:** Ask "Do you already have brand guidelines or a style guide? (Yes / No / Skip for now)"
   - If **Yes**: Ask for the URL or file path, analyze it, extract visual rules.
   - If **No**: Run the full discovery interview (questions from `visual-identity.md` instructions).
   - If **Skip**: Leave `visual-identity.md` with the template — squads will use sensible defaults.

3. If running full discovery, ask in sequence:
   a. "Show me 3 designs, websites, or brands you love visually — URLs or descriptions."
   b. "What visual style makes you cringe or feels generic?"
   c. "Do you prefer dark mode, light mode, or contextual switching?"
   d. "What colors represent your brand? (hex codes if you have them)"
   e. "What colors should NEVER appear in your outputs?"
   f. "Do you have preferred fonts? Or describe the vibe (modern, editorial, technical, warm)."
   g. "Dense layouts or breathing, minimal ones?"

4. Synthesize answers into:
   - Core philosophy (2-3 sentences)
   - Color palette (80/15/5 rule)
   - Typography system (display, body, code, optional editorial)
   - Layout patterns
   - Anti-patterns (forbidden elements)

5. **CHECKPOINT:** Present the visual identity document for approval.
6. Save to `_conclave/_memory/visual-identity.md` (replace instructional comments with real data).

### Conditional: Visual Voice
If the user completed the visual identity:
7. Generate the `visual-voice.md` document from the same data — this is the design language guide used by rendering agents.
8. Save to `_conclave/_memory/visual-voice.md`.

### Files Written:
- `_conclave/_memory/visual-identity.md`
- `_conclave/_memory/visual-voice.md`

---

## Phase 3: Writing Style & Global Preferences

**Goal:** Populate the global-preferences.md with the user's actual design and writing rules.

### Steps:
1. Ask about writing style:
   a. "How would you describe your writing tone? (technical, conversational, poetic, direct, etc.)"
   b. "Any phrases or clichés you hate?"
   c. "Emoji usage — how do you feel about them? (None / Minimal / Liberal)"
   d. "What kind of CTAs do you prefer? (Reflective questions, calls to action, soft closes, none)"

2. Ask about content structure:
   a. "What platforms do you publish on?"
   b. "Any length limits? (e.g., max words per carousel slide, post character limits)"

3. Ask about explicit prohibitions:
   a. "Anything else you absolutely want to avoid in outputs?"

4. **CHECKPOINT:** Present the global preferences document.
5. Save to `_conclave/_memory/global-preferences.md` (replace instructional comments with real rules).

### Files Written:
- `_conclave/_memory/global-preferences.md`

---

## Phase 4: Social Media Insights (Optional)

**Goal:** Populate audience data for content strategy squads.

### Steps:
1. Ask: "Do you want to set up social media audience insights now? (Yes / Skip)"
   - If **Skip**: Leave `linkedin-insights.md` as template — it can be filled later.
2. If Yes:
   a. "What's your primary social media platform?"
   b. "How many connections/followers do you have?"
   c. "What are your top 5 audience locations? (Check your platform analytics)"
   d. "What percentage of your audience is international?"
   e. "What content types perform best for you?"
3. Save to `_conclave/_memory/linkedin-insights.md` (rename file if not LinkedIn — use `social-insights.md`).

### Files Written:
- `_conclave/_memory/linkedin-insights.md` (or `social-insights.md`)

---

## Phase 5: Reference Materials (Optional)

**Goal:** Guide the user to populate visual and brand reference directories.

### Steps:
1. Inform: "Conclave uses reference images and brand writing samples to learn your style."
2. Explain the two reference directories:
   - `ref_visual_style/` — Visual reference images (architecture, color, typography, products, etc.)
   - `ref_brand-style/` — Brand writing samples, tone analyses, content examples
3. Ask: "Would you like to add reference materials now, or do it later?"
   - If **Now**: Guide them to drag/drop files into the directories, or provide URLs for the AI to analyze.
   - If **Later**: Inform them they can always add files and run `/conclave edit-company` or re-trigger this setup.

### Files Written:
- None directly (user populates directories manually)

---

## Phase 6: Squad Configuration Health Check

**Goal:** Ensure all example squads reference valid files.

### Steps:
1. For each squad in `squads/`:
   a. Read `squad.yaml` and check all `data:` entries point to existing files.
   b. Read each agent `.agent.md` and check file references exist.
   c. If a reference points to a file that needs user data (e.g., `visual-identity.md`):
      - If already populated in Phase 2 → PASS
      - If still template → WARN: "Squad `{name}` will use defaults until visual identity is configured."
2. Check `_conclave/core/intention_matrix.json` — regenerate if descriptions are stale.
3. Run the Conclave validator: `python _conclave/scripts/validate_conclave.py` (if available).

### Output:
- Console report: ✅ READY / ⚠️ NEEDS ATTENTION per squad.

---

## Phase 7: Finalization

### Steps:
1. Generate the `user-model.md` base profile from all data collected:
   - Name (from preferences)
   - Professional context (from company.md)
   - Primary content domain (from company.md channels)
   - Visual identity name (from visual-identity.md philosophy)
   - Tone of voice (from company.md + global-preferences.md)
2. Save to `_conclave/_memory/user-model.md`.
3. Write initial session log entry to `_conclave/_memory/session_logs.md`.
4. Display final summary:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Conclave Setup Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Profile:    {company/project name}
  Language:   {language}
  Squads:     {count} ready
  Skills:     {count} available

  Visual ID:  {✅ Configured / ⚠️ Pending}
  Voice:      {✅ Configured / ⚠️ Pending}

  Next steps:
  • /conclave run <squad>  — Run a squad
  • /conclave create       — Create a new squad
  • /conclave skills       — Browse available skills

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

5. Show the main menu.

### Files Written:
- `_conclave/_memory/user-model.md`
- `_conclave/_memory/session_logs.md`

---

## File Dependency Map

This table shows every file that needs user data and which phase populates it:

| File | Phase | Status if Skipped | Impact |
|---|---|---|---|
| `preferences.md` | Phase 0 | ❌ Blocks all | System cannot start without language |
| `company.md` | Phase 1 | ❌ Blocks squads | No context for any agent |
| `visual-identity.md` | Phase 2 | ⚠️ Defaults used | Visual outputs will be generic |
| `visual-voice.md` | Phase 2 | ⚠️ Defaults used | Design agents lack guidance |
| `global-preferences.md` | Phase 3 | ⚠️ No rules | Agents use built-in defaults |
| `linkedin-insights.md` | Phase 4 | ✅ No impact | Only affects content strategy squads |
| `ref_visual_style/` | Phase 5 | ✅ No impact | Only affects visual discovery depth |
| `ref_brand-style/` | Phase 5 | ✅ No impact | Only affects brand voice extraction |
| `design-philosophy.md` | Auto | ✅ No impact | Populated over time from feedback |
| `user-model.md` | Phase 7 | ✅ Auto-populated | Inferred from collected data |

---

## Reference Resolution Map

When squads reference design/voice files, here's how they resolve:

| Old Reference (pre-export) | New Location | Populated By |
|---|---|---|
| `squads/sexy_content/_memory/douglas-visual-voice.md` | `_conclave/_memory/visual-voice.md` | Phase 2 |
| `squads/sexy_content/_memory/douglas-brand-voice.md` | `_conclave/_memory/company.md` (tone section) | Phase 1 |
| `squads/sexy_content/_memory/douglas-color-palettes.md` | `_conclave/_memory/visual-identity.md` (color section) | Phase 2 |
| `pipeline/data/visual-identity.md` | `_conclave/_memory/visual-identity.md` | Phase 2 |
| `pipeline/data/color-palettes.md` | `_conclave/_memory/visual-identity.md` (color section) | Phase 2 |
| `ref_visual_style/*` (images) | `ref_visual_style/` (user populates) | Phase 5 |
| `ref_brand-style/*` (analyses) | `ref_brand-style/` (user populates) | Phase 5 |
