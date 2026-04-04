#!/bin/bash
# Capture AI correction for training

echo "🤖 Urban Thread AI Correction Capture"
echo "====================================="

read -p "Enter ticker (e.g., QQQ): " ticker
read -p "Enter AI analysis that needs correction: " ai_analysis
read -p "Enter your correction/expert insight: " expert_insight

python3 -c "
import sys
sys.path.append('/root/.openclaw/workspace/ai_training')
from simple_integration import capture_correction_simple

result = capture_correction_simple(
    ticker='$ticker',
    ai_analysis='$ai_analysis',
    your_correction='$expert_insight'
)

print(f'\\\\n✅ Correction captured!')
print(f'   AI will learn from this for future analysis.')
"
