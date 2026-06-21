#!/bin/bash
# ============================================
# 🎨 Exportador de Slides — Poética Racional
# ============================================
# Uso:
#   ./export.sh                          → Exporta tema 'brutalist'
#   ./export.sh mint                     → Exporta tema 'mint'
#   ./export.sh all                      → Exporta todos os temas
# ============================================

cd "$(dirname "$0")/.." || exit 1
SQUAD_ROOT=$(pwd)
SCRIPTS="$SQUAD_ROOT/scripts"
OUTPUT="$SQUAD_ROOT/output/carousel"
MD_INPUT="$SQUAD_ROOT/output/post-final.md"

export NVM_DIR="$SQUAD_ROOT/../../.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

THEME="${1:-brutalist}"

if [ "$THEME" = "all" ]; then
  THEMES="brutalist mint deep_sea cyber"
else
  THEMES="$THEME"
fi

for T in $THEMES; do
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "🎨 Gerando tema: $T"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  
  # 1. Gera o HTML
  python3 "$SCRIPTS/carousel_html_renderer_v5_brutalist.py" "$MD_INPUT" "$T"
  
  # 2. Cria pasta do tema
  THEME_DIR="$OUTPUT/$T"
  mkdir -p "$THEME_DIR"
  
  # 3. Exporta PNGs
  node "$SCRIPTS/export_slides_png.mjs" "$OUTPUT/preview_v5_${T}.html" "$THEME_DIR"
  
  echo "✅ Tema '$T' pronto em: $THEME_DIR/"
done

echo ""
echo "🎉 Exportação completa!"
echo "📂 Seus PNGs estão em: $OUTPUT/<tema>/"
