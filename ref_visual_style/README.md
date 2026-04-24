# Visual Style References

This directory is where you store your visual reference images, organized by category.

## Suggested Structure

Create subdirectories for different reference categories:

```
ref_visual_style/
├── architecture/          # Architectural references (spaces, materials, light)
├── color-palettes/        # Color palette references and swatches
├── design-styles/         # Specific design movements and aesthetics
├── patterns/              # Pattern and texture references
├── product-design/        # Product and industrial design
├── typography/            # Typography and lettering references
├── tech-ui/               # Tech interfaces, dashboards, data visualization
└── illustrations/         # Illustration and digital art references
```

## How Conclave Uses This

When you run the Visual Identity Builder (via `_conclave/_memory/visual-identity.md`), 
the AI agent will analyze the images in this folder to extract your design DNA —
recurring themes, color temperatures, layout preferences, and aesthetic patterns.

The more curated and intentional your references are, the better the AI will 
understand your visual taste.

## Tips

- **Quality over quantity**: 20 highly intentional references > 200 random pins
- **Organize by feeling**: Group references by the emotion or aesthetic they evoke, not just by medium
- **Include anti-references**: Create a `_avoid/` subfolder with examples of what you DON'T want
