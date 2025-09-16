# CRM Dashboard

A comprehensive, AI-powered CRM dashboard built with Streamlit for executive-level business intelligence and decision making.

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

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd crm-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## Data Files

The dashboard uses several CSV files for comprehensive analysis:
- `enhanced_lead_data.csv`: Main lead dataset with AI scoring
- `dashboard_data.json`: Aggregated metrics and KPIs
- `call_activity_details.csv`: Call logs and performance data
- `agent_availability.csv`: Agent scheduling and availability

## Dashboard Sections

### Executive Summary
- Total leads, calls, and success rates
- Revenue potential and conversion metrics
- AI-powered insights and recommendations
- Lead scoring distribution
- Performance trends

### Lead Status Dashboard  
- Pipeline visualization with status breakdown
- Lead filtering by status, score, and risk level
- Conversion predictions by status
- Detailed lead analysis table

### AI Call Activity
- Daily call volume trends
- Hourly success rate analysis
- Peak performance time identification
- Call pattern predictions

### Follow-up & Tasks
- Upcoming task timeline
- Urgent and overdue task tracking
- Task type performance analysis
- Workload distribution insights

### Agent Availability
- Real-time availability heatmap
- Agent performance comparisons
- Win rate and lead distribution analysis
- Capacity planning recommendations

### Conversion Dashboard
- Revenue potential by lead score
- Conversion funnel analysis  
- Win/loss rate tracking
- Revenue forecasting models

### Geographic Dashboard
- Global lead distribution mapping
- Country-wise performance metrics
- Market expansion opportunities
- Regional risk assessments

## AI/ML Features

### Predictive Analytics
- **Lead Scoring**: Machine learning model predicting lead quality
- **Churn Risk**: Probability of lead dropping from pipeline
- **Conversion Forecasting**: Revenue predictions based on pipeline
- **Optimal Timing**: Best call times based on success patterns

### Feature Importance Analysis
Key factors influencing lead success:
1. Days since creation (22.6% importance)
2. Assigned agent (20.8% importance)  
3. Lead status (20.3% importance)
4. Geographic location (13.1% importance)

### Business Intelligence
- **Performance Benchmarking**: Agent and geographic comparisons
- **Trend Analysis**: Historical patterns and future projections
- **Risk Assessment**: Early warning systems for lead churn
- **Resource Optimization**: Workload balancing recommendations

## Technology Stack

- **Frontend**: Streamlit with custom CSS styling
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly Express and Graph Objects
- **Machine Learning**: Scikit-learn (Random Forest)
- **Data Storage**: CSV files and JSON configuration

## Executive Benefits

### Decision Making Support
- Real-time KPI monitoring
- Predictive insights for strategic planning
- Performance benchmarking across teams and regions
- Risk identification and mitigation strategies

### Operational Efficiency
- Automated lead scoring and prioritization
- Optimal resource allocation recommendations
- Performance bottleneck identification
- Task and follow-up management

### Revenue Optimization
- Revenue potential forecasting
- Conversion rate improvement strategies
- Market expansion opportunity identification
- Agent performance optimization

## Deployment

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud Deployment
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy with automatic updates

### Docker Deployment
```dockerfile
FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and add tests
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact the development team.
