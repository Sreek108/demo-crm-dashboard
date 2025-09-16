# Executive CRM Dashboard

A comprehensive, AI-powered CRM dashboard built with Streamlit for executive-level business intelligence and decision making.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app/)

## Features

### 📊 Multi-Dashboard Views
- **Executive Summary**: Key performance indicators and AI insights
- **Lead Status Dashboard**: Pipeline visualization and lead analysis
- **AI Call Activity**: Call patterns and success rate analytics  
- **Follow-up & Tasks**: Task management and priority tracking
- **Agent Availability**: Resource management and performance metrics
- **Conversion Dashboard**: Revenue forecasting and funnel analysis
- **Geographic Dashboard**: Global market analysis and expansion insights

### 🤖 AI/ML Insights
- Predictive lead scoring and churn risk analysis
- Conversion probability forecasting
- Optimal call time recommendations
- Agent performance optimization
- Revenue potential calculations
- Market expansion opportunities

### 📈 Key Metrics Tracked
- Lead conversion rates and pipeline health
- Call success rates and activity patterns
- Revenue potential and forecasting
- Agent performance and workload distribution
- Geographic market performance
- Task completion and follow-up efficiency

## Quick Start

### Option 1: Deploy to Streamlit Cloud (Recommended)

1. **Fork this repository** to your GitHub account
2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**
3. **Click "New app"** and select your forked repository
4. **Set main file path** to `app.py`
5. **Click "Deploy"**

Your dashboard will be live at: `https://your-app-name.streamlit.app/`

### Option 2: Local Development

```bash
# Clone repository
git clone https://github.com/your-username/crm-dashboard.git
cd crm-dashboard

# Run setup script
chmod +x setup.sh
./setup.sh

# Or manual setup:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run application
streamlit run app.py
```

## Project Structure

```
crm-dashboard/
├── .github/workflows/
│   └── deploy.yml              # CI/CD pipeline
├── .streamlit/
│   └── config.toml            # App configuration
├── data/                      # Original CSV datasets
├── processed_data/            # AI-enhanced datasets
├── app.py                     # Main Streamlit application
├── requirements.txt           # Dependencies
├── README.md                  # This file
├── DEPLOYMENT.md              # Deployment guide
├── LICENSE                    # MIT License
├── .gitignore                # Git ignore patterns
└── setup.sh                  # Setup script
```

## Dashboard Sections

### 1. Executive Summary
- **Total Leads**: 50 across 5 countries
- **Success Rate**: 31.2% with optimization insights
- **Revenue Pipeline**: $1.29M potential identified
- **Risk Management**: 13 high-risk leads flagged
- AI insights and performance trends

### 2. Lead Status Dashboard  
- Pipeline visualization with 10 status categories
- Lead filtering and analysis tools
- AI-powered conversion predictions
- Churn risk assessment

### 3. AI Call Activity Dashboard
- Daily call volume trends and patterns
- Hourly success rate analysis
- Peak performance time identification
- Call optimization recommendations

### 4. Follow-up & Tasks Dashboard
- Task timeline and priority management
- Urgent task alerts and tracking
- Workload distribution analysis
- AI-powered scheduling optimization

### 5. Agent Availability Dashboard
- Real-time availability heatmap
- Agent performance comparisons
- Win rate and lead distribution
- Capacity planning insights

### 6. Conversion Dashboard
- Revenue potential by lead score
- Conversion funnel visualization
- Win/loss rate tracking
- Revenue forecasting models

### 7. Geographic Dashboard
- Global lead distribution mapping
- Country-wise performance metrics
- Market expansion opportunities
- Regional risk assessments

## AI/ML Features

### Predictive Analytics
- **Lead Scoring**: Machine learning model predicting lead quality
- **Churn Risk**: Probability analysis for lead retention
- **Revenue Forecasting**: Pipeline-based revenue predictions
- **Optimal Timing**: Best call times based on success patterns

### Feature Importance Analysis
1. **Days since creation** (22.6% importance)
2. **Assigned agent** (20.8% importance)  
3. **Lead status** (20.3% importance)
4. **Geographic location** (13.1% importance)

### Business Intelligence
- Performance benchmarking across teams and regions
- Trend analysis and future projections
- Risk assessment and early warning systems
- Resource optimization recommendations

## Data Sources

The dashboard processes data from multiple sources:
- **Lead Management**: Lead profiles, status, and scoring
- **Call Activity**: Call logs, success rates, and patterns
- **Agent Performance**: Individual and team metrics
- **Geographic Data**: Regional performance and opportunities
- **Task Management**: Follow-up scheduling and completion

## Technology Stack

- **Frontend**: Streamlit with custom CSS styling
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly Express and Graph Objects
- **Machine Learning**: Scikit-learn (Random Forest)
- **Deployment**: Streamlit Cloud with GitHub integration

## Business Impact

### Decision Making Support
- Real-time KPI monitoring and alerts
- Predictive insights for strategic planning
- Performance benchmarking and optimization
- Risk identification and mitigation

### Operational Efficiency
- Automated lead scoring and prioritization
- Optimal resource allocation recommendations
- Performance bottleneck identification
- Streamlined task and follow-up management

### Revenue Optimization
- $1.29M pipeline potential identified
- 25% vs 9% conversion rate optimization (HOT vs COLD leads)
- Geographic expansion opportunities
- Agent performance enhancement strategies

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 [Deployment Guide](DEPLOYMENT.md)
- 🐛 [Report Issues](https://github.com/your-username/crm-dashboard/issues)
- 💬 [Discussions](https://github.com/your-username/crm-dashboard/discussions)

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Plotly](https://plotly.com/)
- Machine learning with [Scikit-learn](https://scikit-learn.org/)

---

**Executive CRM Dashboard** | Transforming data into actionable business intelligence
