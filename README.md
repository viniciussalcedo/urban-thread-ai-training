# Urban Thread AI Training System

**Self-improving AI for institutional-grade stock analysis**

[![Live Demo](https://img.shields.io/badge/demo-live-green)](https://viniciussalcedo.github.io/urban-thread-ai-training/)
[![Status](https://img.shields.io/badge/status-active-success)]()
[![Corrections](https://img.shields.io/badge/corrections-11%2F100-blue)]()

## 🎯 What This Is

A professional AI training platform that captures expert corrections to improve stock analysis AI. Built for Urban Thread's institutional-grade analysis pipeline.

**Core Concept:** AI training AI to be better using expert feedback as training data.

## 🚀 Quick Start

### Option 1: Use the Web Dashboard
Visit: [https://viniciussalcedo.github.io/urban-thread-ai-training/](https://viniciussalcedo.github.io/urban-thread-ai-training/)

The dashboard works in your browser with mock data. Corrections are saved to localStorage.

### Option 2: Run Locally with Full Integration
```bash
# Clone the repo
git clone https://github.com/viniciussalcedo/urban-thread-ai-training.git
cd urban-thread-ai-training

# Make scripts executable
chmod +x capture_correction.sh

# Install Python dependencies
pip install requests beautifulsoup4

# Open the dashboard
open index.html  # or double-click index.html
```

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Rex Analysis  │───▶│   AI Makes      │───▶│   Expert        │
│   (Python)      │    │   Prediction    │    │   Correction    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Stock Data    │    │   Dashboard     │    │   Training      │
│   (Yahoo Finance)│   │   (HTML/JS)     │    │   Dataset       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📊 Current Training Progress

**11 corrections captured** (Goal: 100 for institutional-grade AI)

### Example Corrections Learned:
1. **QQQ/SPY** - "ETFs need different technical analysis vs individual stocks"
2. **NVDA** - "Adjust risk assessment for semiconductor sector context"
3. **AAPL** - "High D/E ratio driven by buybacks, not dangerous debt"

## 🛠️ Integration with Urban Thread Pipeline

This system integrates with Urban Thread's automated trading alert pipeline:

```
NewsBot (Finnhub) → Toby (Validation) → Nick (Approval) → Rex (Analysis) → AI Training
```

### Key Scripts:
- `capture_correction.sh` - Command-line tool to add corrections
- `simple_integration.py` - Apply learned rules to new analyses
- `corrections.json` - Training dataset (11 examples)

## 🔧 How It Works

### 1. Analyze a Stock
```bash
# In production, this calls Rex:
python3 /path/to/agent-rex-analyzer/analyzer.py NVDA
```

### 2. Identify AI Mistakes
- Review the AI's analysis
- Spot errors in valuation, trend assessment, risk calibration

### 3. Capture Correction
```bash
./capture_correction.sh
```
Enter:
- Ticker symbol
- AI's mistake
- Expert correction
- Rule category

### 4. AI Learns
Future analyses check for learned rules and apply corrections automatically.

## 📈 Dashboard Features

- **Real-time Analysis** - Connect to Rex AI for live stock analysis
- **Correction Capture** - Save expert feedback with rule categorization
- **Progress Tracking** - Visual progress toward 100-correction goal
- **Data Export** - Download corrections as JSON for training
- **Recent Corrections** - View and manage training history

## 🎯 Use Cases

### For Urban Thread:
- Improve Rex AI's analysis accuracy
- Build institutional-grade training dataset
- Scale expert knowledge across all analyses

### For Traders/Investors:
- Train personal AI analyst
- Capture investment thesis as rules
- Maintain consistent analysis framework

### For AI Researchers:
- Example of human-in-the-loop AI training
- Real-world financial AI correction dataset
- Production deployment patterns

## 🔮 Roadmap

- [x] Basic dashboard with mock data
- [x] 11 example corrections
- [ ] Connect to live Rex API
- [ ] Automated rule extraction from corrections
- [ ] Integration with Urban Thread alert pipeline
- [ ] 100 corrections (institutional-grade milestone)
- [ ] Public API for third-party integration

## 📝 License

This project contains proprietary Urban Thread technology. The dashboard interface is open for demonstration purposes.

## 🤝 Contributing

While this is primarily an Urban Thread internal tool, we welcome:
- Bug reports via Issues
- Documentation improvements
- UI/UX suggestions

For major changes, please open an issue first to discuss.

---

**Built by [Urban Thread](https://urbanthread.co.uk)** · "Most finance creators are wrong. We have the data to prove it."