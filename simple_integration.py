#!/usr/bin/env python3
"""
Simple AI Training Integration for Urban Thread
"""

import json
import datetime
from pathlib import Path

workspace = Path("/root/.openclaw/workspace")

def capture_correction_simple(ticker, ai_analysis, your_correction):
    """Simple correction capture"""
    training_file = workspace / "ai_training" / "corrections.json"
    
    # Load existing corrections
    if training_file.exists():
        with open(training_file, 'r') as f:
            corrections = json.load(f)
    else:
        corrections = []
    
    # Add new correction
    correction = {
        "timestamp": datetime.datetime.now().isoformat(),
        "ticker": ticker,
        "ai_analysis": ai_analysis,
        "your_correction": your_correction,
        "learned": extract_learning(ai_analysis, your_correction)
    }
    
    corrections.append(correction)
    
    # Save
    with open(training_file, 'w') as f:
        json.dump(corrections, f, indent=2)
    
    print(f"✅ Correction captured for ${ticker}")
    print(f"   Learning: {correction['learned']}")
    
    return correction

def extract_learning(ai_analysis, your_correction):
    """Extract learning from correction"""
    learning = []
    
    # Check for ETF context
    if "ETF" in your_correction and "technical" in ai_analysis.lower():
        learning.append("ETFs need different technical analysis")
    
    # Check for sector context
    if "sector" in your_correction.lower() or "industry" in your_correction.lower():
        learning.append("Consider sector/industry context")
    
    # Check for comparative analysis
    if "vs" in your_correction or "compared" in your_correction or "peer" in your_correction:
        learning.append("Use comparative analysis vs peers")
    
    # Check for risk context
    if "risk" in your_correction.lower() and ("normal" in your_correction.lower() or "typical" in your_correction.lower()):
        learning.append("Adjust risk assessment for market norms")
    
    return learning if learning else ["Context-specific insight"]

def get_training_stats():
    """Get training statistics"""
    training_file = workspace / "ai_training" / "corrections.json"
    
    if not training_file.exists():
        return {
            "total_corrections": 0,
            "tickers_trained": [],
            "last_correction": None,
            "learning_progress": "Just starting"
        }
    
    with open(training_file, 'r') as f:
        corrections = json.load(f)
    
    # Count by ticker
    ticker_counts = {}
    for corr in corrections:
        ticker = corr["ticker"]
        ticker_counts[ticker] = ticker_counts.get(ticker, 0) + 1
    
    return {
        "total_corrections": len(corrections),
        "tickers_trained": ticker_counts,
        "last_correction": corrections[-1]["timestamp"] if corrections else None,
        "learning_progress": f"{len(corrections)} corrections captured"
    }

def apply_learnings_to_analysis(ticker, analysis_text):
    """Apply learned insights to analysis"""
    training_file = workspace / "ai_training" / "corrections.json"
    
    if not training_file.exists():
        return analysis_text
    
    with open(training_file, 'r') as f:
        corrections = json.load(f)
    
    # Get corrections for this ticker
    ticker_corrections = [c for c in corrections if c["ticker"] == ticker]
    
    if not ticker_corrections:
        return analysis_text
    
    # Apply learnings
    enhanced = analysis_text
    
    # Check for ETF learnings
    for corr in ticker_corrections:
        if "ETF" in str(corr.get("learned", [])):
            if "technical" in enhanced.lower():
                enhanced += "\\n\\n[AI Learning: ETF technical analysis adjusted]"
    
    # Check for sector learnings
    for corr in ticker_corrections:
        if "sector" in str(corr.get("learned", [])):
            enhanced += "\\n\\n[AI Learning: Sector context considered]"
    
    return enhanced

# Test the system
if __name__ == "__main__":
    print("Testing AI Training Integration...")
    
    # Test capturing a correction
    result = capture_correction_simple(
        ticker="QQQ",
        ai_analysis="Technical Score: 35/100 - Bearish",
        your_correction="QQQ is an ETF, technicals less relevant. Focus on holdings."
    )
    
    print(f"\\nCorrection ID: {result['timestamp']}")
    print(f"Learned: {result['learned']}")
    
    # Test getting stats
    stats = get_training_stats()
    print(f"\\nTraining Stats:")
    print(f"  Total corrections: {stats['total_corrections']}")
    print(f"  Tickers trained: {stats['tickers_trained']}")
    
    # Test applying learnings
    test_analysis = "QQQ shows weak technicals with RSI at 35."
    enhanced = apply_learnings_to_analysis("QQQ", test_analysis)
    print(f"\\nEnhanced analysis:\\n{enhanced}")
    
    print("\\n✅ AI Training System Ready!")
