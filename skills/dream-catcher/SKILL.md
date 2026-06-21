---
name: dream-catcher
description: Analyzes human figures in images, generating detailed descriptions, structured metadata tags, and optimized generative prompts for Midjourney/DALL-E to ensure character consistency.
type: prompt
version: 1.0.0
categories:
  - visual-analysis
  - image-generation
  - prompt-engineering
contract:
  inputs:
    - name: input_image
      required: true
      description: "An image containing a human subject to be analyzed."
  outputs:
    - name: detailed_description
      format: markdown
      description: "Objective, technical, and concise description of the human subject."
    - name: metadata_tags
      format: yaml
      description: "Structured tags indexing key visual and photographic attributes of the subject."
    - name: sample_prompt
      format: plain
      description: "Concise generative prompt optimized for Midjourney, DALL-E, or other models, preserving character consistency."
  quality_criteria:
    - "Written entirely in English (US)"
    - "Focuses exclusively on human analysis, ignoring background environment and narrative"
    - "Maintains a factual, technical, and objective tone, avoiding subjective speculation"
    - "Includes approximate visual age range, gender presentation, mood, style, lighting, and framing details in metadata"
    - "Sample prompt directly captures and reinforces the character's visual identity for generation consistency"
---

# Dream Catcher: Character Consistency Curator

## When to use

Activate this skill when you need to analyze human subjects within images for creative pipelines, character sheet compilation, or asset generation. This skill is critical for projects requiring **character consistency** across multiple generations, enabling generative engines (such as Midjourney, DALL-E 3, or Stable Diffusion) to reproduce the exact facial structure, hair profile, clothing style, and physical identity of a specific persona.

---

## Instructions

Analyze the human subject in the provided image using a strict bottom-up observation loop. Follow these three procedures sequentially:

### Step 1: Human-centric Visual Audit (Detailed Description)
Conduct a clinical, objective visual audit of the human figure. Focus entirely on structural, invariant features that define their unique physical identity. Avoid commenting on background elements or inventing narrative context. 

Break down your observations into these key nodes:
1. **Facial Structure & Features:** Shape of the head/face (e.g., oval, heart, square), jawline prominence, cheekbones, nose profile (e.g., straight, aquiline), eye shape and spacing, eyebrow density/arch, lip thickness, and unique features (freckles, scars, dimples, facial hair).
2. **Hair Profile:** Color, exact texture (curly, straight, wavy, coily), length (cropped, shoulder-length, waist-length), styling (undercut, parted, braided, loose), and volume.
3. **Body Proportions & Posture:** Approximate build (slender, athletic, stocky), height presentation relative to framing, shoulder width, and overall physical posture (rigid, relaxed, dynamic).
4. **Expression & Affect:** Exact muscle tension in the face representing emotional tone. Describe the micro-expressions (e.g., tight lips, slightly narrowed eyes, relaxed brow) rather than using subjective words like "happy" or "sad".
5. **Attire & Accessories:** Detail the upper and lower clothing layers, including fabric type, texture, color, necklines, sleeves, patterns, and visible accessories (jewelry, glasses, headwear).

### Step 2: Metadata Extraction
Compile key visual attributes into structured metadata tags to build a search-optimized and queryable catalog profile. Extract the following indicators:
* **Age Range:** Estimate the visual age category (e.g., infant, toddler, child, teenager, young adult, middle-aged, elderly).
* **Gender Presentation:** Visual presentation (e.g., masculine, feminine, androgynous).
* **Skin Tone & Ethnicity:** Record observable skin tone (e.g., pale, fair, olive, warm brown, deep ebony) and apparent heritage features, remaining descriptive and never assumptive.
* **Mood/Emotional Tone:** The overall micro-expression converted into a standardized emotional attribute (e.g., neutral, determined, joyful, pensive, stoic).
* **Aesthetic/Style Keywords:** Describe the photographic or artistic style of the image (e.g., cinematic, editorial, minimalist, corporate, cyberpunk, vintage film).
* **Lighting Type:** Define the illumination quality (e.g., soft studio lighting, harsh direct sunlight, dramatic chiaroscuro, side-lit neon, natural overcast diffused).
* **Camera/Framing Details:** Describe the camera angle and framing scale (e.g., extreme close-up, portrait, medium shot, three-quarter view, full-body).

### Step 3: Generative Prompt Synthesis
Synthesize the details and metadata into a highly concentrated, comma-separated generative prompt optimized for modern text-to-image engines.
* **Midjourney Format:** Start directly with the core subject description, followed by physical traits, hairstyle, clothing, lighting, camera framing, and aesthetic style. End with realistic parameters if requested, but focus on vocabulary weight.
* **Vocabulary Rule:** Use high-fidelity noun-adjective pairs. Avoid subjective filler words (e.g., "amazing", "beautiful", "hyperrealistic", "masterpiece"). Instead, use technical terms (e.g., "medium format photography", "85mm lens", "soft rim lighting").

---

## Output Format

Your final response MUST be structured in English (US) using the exact template below. Do not deviate from these headers:

```markdown
# Dream Catcher: Visual Analysis Report

## 1. Detailed Description (English, US)
[Provide a continuous, dense, and structured description covering facial structure, hair profile, body/posture, expression, and attire. Keep it under 200 words, dense with technical adjectives.]

## 2. Metadata Tags (English, US)
```yaml
character_profile:
  visual_age: "[Approximate age category or range]"
  gender_presentation: "[Masculine | Feminine | Androgynous]"
  skin_tone: "[Pale | Fair | Olive | Warm Brown | Deep Ebony | etc.]"
  micro_expression: "[Neutral | Determined | Joyful | Stoic | Pensive | etc.]"
  style_aesthetic: "[Cinematic | Editorial | Minimalist | Cyberpunk | etc.]"
  lighting: "[Lighting type details]"
  framing: "[Camera shot type and angle]"
```

## 3. Sample Prompt (English, US)
**Midjourney / DALL-E Prompt:**
`[Insert optimized generative prompt here. Start with the subject, detail facial and attire highlights, specify lighting, camera angle, lens/photographic context, and aesthetic keywords. Keep it concise, high-impact.]`
```

---

## Examples

### Example 1: Editorial Portrait
* **Input Image:** A close-up photo of a woman with sharp features and a denim jacket in a studio.
* **Output:**
```markdown
# Dream Catcher: Visual Analysis Report

## 1. Detailed Description (English, US)
A close-up portrait of a woman in her late 20s with an oval face shape, high cheekbones, and a sharp, defined jawline. She has almond-shaped dark brown eyes with dense, straight eyebrows, a straight nose bridge, and symmetrical, natural lips set in a neutral expression. Her hair is dark brown, coily, styled in a short cropped afro with high volume. She is wearing a structured medium-wash blue denim jacket with visible copper buttons and a simple white crewneck cotton shirt underneath. Her posture is front-facing, head slightly tilted to the left.

## 2. Metadata Tags (English, US)
```yaml
character_profile:
  visual_age: "Young adult (25-30)"
  gender_presentation: "Feminine"
  skin_tone: "Warm brown"
  micro_expression: "Neutral"
  style_aesthetic: "Editorial portrait"
  lighting: "Soft studio lighting with key and fill lights"
  framing: "Close-up portrait, front-facing angle"
```

## 3. Sample Prompt (English, US)
**Midjourney / DALL-E Prompt:**
`Close-up studio portrait of a young adult woman with an oval face, high cheekbones, short cropped high-volume afro hair, wearing a blue denim jacket over a white crewneck shirt, neutral expression, soft professional studio lighting, shot on 85mm lens, high-fidelity details, editorial photography style.`
```

---

## Avoid

* **Subjective Adjectives:** Never use phrases like "beautiful face," "stunning clothes," "sad expression," or "perfect body." Use exact anatomical and technical descriptions.
* **Background/Environment Noise:** Do not describe the room, street, trees, or sky unless it directly reflects lighting cast onto the character (e.g., "red neon glow on the left cheek").
* **Narrative Speculation:** Do not speculate on what the character is doing, what their profession is, or how they feel. Stick to visible physical evidence.
* **Buzzwords in Prompts:** Avoid "photorealistic," "ultra HD," "4K," "8K," or "super detailed." Generative models interpret these as low-quality indicators. Use descriptive context like "medium format photography," "studio lighting," "cinematic depth of field."
* **Language Mix:** Do not write any part of the detailed description, tags, or prompts in languages other than English (US).

---

## Error Handling

1. **Non-Human Subjects:** If the input image does not contain a human figure or a humanoid character (e.g., it is a landscape, abstract art, or an animal), output:
   `[VETO] Dream Catcher is optimized exclusively for human analysis. The input image contains no observable human subject. Execution halted.`
2. **Severely Obscured Figures:** If the human figure is mostly obscured (extremely dark shadow, blur, or heavily cropped), describe only the visible elements, tag the rest as `undetermined`, and add a warning note at the top of the report.
