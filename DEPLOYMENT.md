# Deployment Guide

This guide provides step-by-step instructions for deploying the Executive CRM Dashboard.

## 🚀 Quick Deploy to Streamlit Cloud

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at [share.streamlit.io](https://share.streamlit.io/))

### Step-by-Step Deployment

#### 1. Prepare Repository
```bash
# Fork or clone this repository
git clone https://github.com/your-username/crm-dashboard.git
cd crm-dashboard

# Ensure all files are present
ls -la
```

#### 2. Push to GitHub
```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit - Executive CRM Dashboard"
git branch -M main

# Add remote origin (replace with your repository URL)
git remote add origin https://github.com/YOUR-USERNAME/crm-dashboard.git
git push -u origin main
```

#### 3. Deploy to Streamlit Cloud

1. **Visit [share.streamlit.io](https://share.streamlit.io/)**
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Fill in the deployment form:**
   - **Repository**: `YOUR-USERNAME/crm-dashboard`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): Choose a custom name

5. **Click "Deploy"**

#### 4. Access Your Dashboard
Your dashboard will be available at:
```
https://your-app-name.streamlit.app/
```

## 🖥️ Local Development

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

#### 1. Clone Repository
```bash
git clone https://github.com/your-username/crm-dashboard.git
cd crm-dashboard
```

#### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Run Application
```bash
streamlit run app.py
```

#### 5. Access Locally
Open your browser and navigate to:
```
http://localhost:8501
```

### Quick Setup Script
Alternatively, use the provided setup script:
```bash
chmod +x setup.sh
./setup.sh
```

## 📊 Data Configuration

### Using Your Own Data

#### 1. Replace Data Files
Replace the files in the `data/` and `processed_data/` folders with your own data:

**Original Data (data/ folder):**
- `Agent.csv` - Agent information
- `Lead.csv` - Lead data
- `LeadCall.csv` - Call activity
- `Schedule.csv` - Task scheduling
- Other lookup tables

**Processed Data (processed_data/ folder):**
- `enhanced_lead_data.csv` - Enhanced lead data with AI predictions
- `dashboard_data.json` - Aggregated metrics and KPIs
- `call_activity_details.csv` - Processed call data
- `agent_availability.csv` - Availability matrix

#### 2. Update Configuration
Modify `processed_data/dashboard_data.json` to reflect your metrics:
```json
{
  "executive_summary": {
    "total_leads": 50,
    "total_calls": 80,
    "success_rate": 31.2,
    "total_revenue_potential": 1290000,
    "high_risk_leads": 13,
    "conversion_rate": 10.0,
    "agents_count": 5,
    "countries_coverage": 5,
    "avg_churn_risk": 54.2
  }
}
```

#### 3. Redeploy
Push changes to GitHub and Streamlit Cloud will automatically redeploy.

## 🔐 Security Configuration

### Environment Variables
For sensitive data, use Streamlit Cloud secrets:

1. **Go to your app** in Streamlit Cloud
2. **Navigate to Settings** → **Secrets**
3. **Add your configuration:**
```toml
[database]
host = "your-database-host"
username = "your-username" 
password = "your-password"

[api]
key = "your-api-key"
```

4. **Access in code:**
```python
import streamlit as st

db_host = st.secrets["database"]["host"]
api_key = st.secrets["api"]["key"]
```

## 🐳 Docker Deployment

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run
```bash
# Build image
docker build -t crm-dashboard .

# Run container
docker run -p 8501:8501 crm-dashboard
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Import Errors
**Problem:** Module not found errors
**Solution:** 
```bash
pip install -r requirements.txt
# or
pip install streamlit pandas plotly numpy scikit-learn
```

#### 2. Data Loading Issues
**Problem:** CSV files not found
**Solution:**
- Verify file paths in `data/` and `processed_data/` folders
- Check file permissions and formats
- Ensure CSV files match expected structure

#### 3. Performance Issues
**Problem:** Dashboard loads slowly
**Solution:**
- Use `@st.cache_data` for data loading functions
- Optimize large dataset processing
- Consider pagination for large tables

#### 4. Styling Issues
**Problem:** Custom CSS not loading
**Solution:**
- Verify `.streamlit/config.toml` exists
- Check CSS syntax in `app.py`
- Clear browser cache

### Getting Help

1. **Check logs** in Streamlit Cloud deployment
2. **Review documentation** in README.md
3. **Search issues** in the repository
4. **Create new issue** with detailed description

## 🚀 Advanced Deployment Options

### Custom Domain
1. **Upgrade to Streamlit Cloud Pro**
2. **Configure custom domain** in settings
3. **Update DNS records** as instructed

### Load Balancing
For high-traffic deployments:
1. **Use container orchestration** (Kubernetes, Docker Swarm)
2. **Implement load balancer** (nginx, AWS ALB)
3. **Scale horizontally** with multiple instances

### Database Integration
For real-time data:
1. **Connect to database** (PostgreSQL, MySQL, MongoDB)
2. **Implement caching strategy**
3. **Use connection pooling**

## 📊 Monitoring and Analytics

### Application Monitoring
- **Streamlit Cloud Analytics** (built-in)
- **Google Analytics** integration
- **Custom metrics** tracking

### Performance Monitoring
- **Response time** tracking
- **Error rate** monitoring
- **User engagement** metrics

---

**Need more help?** Contact the development team or create an issue in the repository.
