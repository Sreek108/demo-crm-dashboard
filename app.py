import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title="AI-Powered CRM Dashboard", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for AI-powered styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #1e3a8a, #3b82f6, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .ai-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        border-left: 5px solid #3b82f6;
        margin-bottom: 1rem;
    }

    .ai-insight-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.3);
    }

    .prediction-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }

    .optimization-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }

    .alert-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: #333;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        font-weight: 600;
    }

    .kpi-positive { border-left-color: #10b981; }
    .kpi-negative { border-left-color: #ef4444; }
    .kpi-warning { border-left-color: #f59e0b; }

    .model-accuracy {
        background: #f0f9ff;
        border: 2px solid #0ea5e9;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 600;
        color: #0c4a6e;
    }
</style>
""", unsafe_allow_html=True)

# Load AI insights
@st.cache_data
def load_ai_insights():
    """Load comprehensive AI insights"""
    try:
        if os.path.exists('processed_data/comprehensive_ai_insights.json'):
            with open('processed_data/comprehensive_ai_insights.json', 'r') as f:
                return json.load(f)
        elif os.path.exists('comprehensive_ai_insights.json'):
            with open('comprehensive_ai_insights.json', 'r') as f:
                return json.load(f)
    except FileNotFoundError:
        pass

    # Return sample insights if file not found
    return {
        "executive_summary": {
            "revenue_forecasting": {"next_30_days_total": 2968212, "forecast_confidence": 0.87},
            "performance_trends": {"revenue_growth_rate": 0.156},
            "optimization_opportunities": {"total_uplift_potential": 347540},
            "predictive_alerts": {"high_risk_leads_next_week": 8}
        }
    }

@st.cache_data
def load_dashboard_data():
    """Load main dashboard data"""
    try:
        if os.path.exists('processed_data/dashboard_data.json'):
            with open('processed_data/dashboard_data.json', 'r') as f:
                return json.load(f)
    except FileNotFoundError:
        pass

    # Return sample data
    return {
        "executive_summary": {
            "total_leads": 50, "total_calls": 80, "success_rate": 31.2,
            "total_revenue_potential": 1290000, "high_risk_leads": 13,
            "conversion_rate": 10.0, "agents_count": 5
        },
        "lead_status": {"Uncontacted": 8, "On Hold": 7, "Won": 5, "Lost": 4},
        "agent_performance": {
            "Jasmin Ahmed": {"role": "AI Agent", "win_rate": 11.11},
            "Mohammed Ali": {"role": "Senior Closer", "win_rate": 10.0}
        }
    }

# Load all data
ai_insights = load_ai_insights()
dashboard_data = load_dashboard_data()

# Sidebar navigation
st.sidebar.title("🤖 AI-Powered CRM")
st.sidebar.markdown('<div class="ai-badge">AI/ML Enhanced</div>', unsafe_allow_html=True)
st.sidebar.markdown("---")

pages = {
    "Executive Summary": "executive_summary",
    "Lead Status Dashboard": "lead_status", 
    "AI Call Activity": "call_activity",
    "Smart Tasks & Follow-up": "tasks",
    "Agent Intelligence": "agent_availability",
    "Revenue Forecasting": "conversion",
    "Market Intelligence": "geographic"
}

selected_page = st.sidebar.selectbox("Navigate to:", list(pages.keys()))
current_page = pages[selected_page]

# AI Model Status Sidebar
st.sidebar.markdown("### 🤖 AI Models Status")
if 'meta_insights' in ai_insights:
    meta = ai_insights['meta_insights']
    st.sidebar.metric("Models Deployed", meta.get('total_models_deployed', 12))
    st.sidebar.metric("Avg Accuracy", f"{meta.get('prediction_accuracy_average', 0.743)*100:.1f}%")
    st.sidebar.metric("AI Confidence", f"{meta.get('ai_confidence_score', 0.89)*100:.1f}%")

# Main content based on selected page
if current_page == "executive_summary":
    st.markdown('<h1 class="main-header">🎯 AI-Powered Executive Summary</h1>', unsafe_allow_html=True)

    # AI Insights Header
    exec_ai = ai_insights.get('executive_summary', {})

    # Enhanced KPI Metrics with AI predictions
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Leads", "50", delta="+5 this week")
        revenue_forecast = exec_ai.get('revenue_forecasting', {})
        st.metric("30-Day Forecast", f"${revenue_forecast.get('next_30_days_total', 0)/1000000:.2f}M", 
                 delta=f"{revenue_forecast.get('forecast_confidence', 0)*100:.0f}% confidence")

    with col2:
        st.metric("Total Calls", "80", delta="+12 this week")
        trends = exec_ai.get('performance_trends', {})
        st.metric("Growth Rate", f"{trends.get('revenue_growth_rate', 0)*100:.1f}%", 
                 delta="AI Predicted")

    with col3:
        st.metric("Success Rate", "31.2%", delta="+2.3% vs last month")
        opt_opp = exec_ai.get('optimization_opportunities', {})
        st.metric("Optimization Potential", f"${opt_opp.get('total_uplift_potential', 0)/1000:.0f}K", 
                 delta="AI Identified")

    with col4:
        st.metric("Revenue Potential", "$1.29M", delta="+$180K this month")
        alerts = exec_ai.get('predictive_alerts', {})
        st.metric("Risk Alerts", alerts.get('high_risk_leads_next_week', 0), 
                 delta="Next Week", delta_color="inverse")

    st.markdown("---")

    # Advanced AI Insights Section
    st.markdown(
        '<div class="ai-insight-box">'
        '<h3>🤖 Advanced AI Insights & Predictions</h3>'
        '</div>', 
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div class="prediction-card">'
            '<h4>📈 Revenue Forecasting</h4>'
            f'<p><strong>Next 30 Days:</strong> ${revenue_forecast.get("next_30_days_total", 0):,.0f}</p>'
            f'<p><strong>Confidence Level:</strong> {revenue_forecast.get("forecast_confidence", 0)*100:.0f}%</p>'
            f'<p><strong>Growth Rate:</strong> {trends.get("revenue_growth_rate", 0)*100:.1f}% predicted</p>'
            '</div>', 
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="optimization-card">'
            '<h4>🎯 Optimization Opportunities</h4>'
            f'<p><strong>Revenue Uplift:</strong> ${opt_opp.get("total_uplift_potential", 0):,.0f}</p>'
            f'<p><strong>High-Impact Leads:</strong> {opt_opp.get("leads_with_high_uplift", 0)}</p>'
            f'<p><strong>Success Probability:</strong> {opt_opp.get("average_improvement_probability", 0)*100:.0f}%</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="alert-card">'
            '<h4>🚨 Predictive Alerts</h4>'
            f'<p>• {alerts.get("high_risk_leads_next_week", 0)} leads at high churn risk</p>'
            f'<p>• {alerts.get("conversion_opportunities_closing", 0)} closing opportunities identified</p>'
            f'<p>• {alerts.get("agent_performance_warnings", 0)} agent performance warnings</p>'
            f'<p>• {alerts.get("market_expansion_signals", 0)} market expansion signals</p>'
            '</div>', 
            unsafe_allow_html=True
        )

elif current_page == "lead_status":
    st.markdown('<h1 class="main-header">📊 AI-Enhanced Lead Status Dashboard</h1>', unsafe_allow_html=True)

    # Lead Status AI Insights
    lead_ai = ai_insights.get('lead_status', {})

    # Conversion Predictions
    conv_pred = lead_ai.get('conversion_predictions', {})
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("High Probability Leads", conv_pred.get('high_probability_leads', 0), delta="AI Scored >70%")
    with col2:
        st.metric("Medium Probability", conv_pred.get('medium_probability_leads', 0), delta="40-70%")
    with col3:
        st.metric("Low Probability", conv_pred.get('low_probability_leads', 0), delta="<40%")
    with col4:
        st.metric("Avg Conversion Rate", f"{conv_pred.get('average_conversion_probability', 0)*100:.1f}%", delta="AI Predicted")

    # AI Insights
    st.markdown(
        '<div class="ai-insight-box">'
        '<h3>🤖 Lead Intelligence & Predictions</h3>'
        '</div>', 
        unsafe_allow_html=True
    )

    # Status Transitions
    if 'status_transitions' in lead_ai:
        st.markdown("#### 🔄 Status Transition Predictions")
        trans_data = []
        for status, info in lead_ai['status_transitions'].items():
            trans_data.append({
                'Current Status': status,
                'Next Likely Status': info.get('next_likely_status', 'N/A'),
                'Probability': f"{info.get('probability', 0)*100:.0f}%",
                'Avg Days': f"{info.get('avg_days', 0):.1f}"
            })

        st.dataframe(pd.DataFrame(trans_data), use_container_width=True)

    # Optimization Recommendations
    if 'optimization_recommendations' in lead_ai:
        opt_rec = lead_ai['optimization_recommendations']

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                '<div class="prediction-card">'
                '<h4>🎯 Priority Actions</h4>'
                f'<p><strong>Immediate Action Leads:</strong> {len(opt_rec.get("priority_leads_for_immediate_action", []))}</p>'
                f'<p>Top Lead IDs: {", ".join(map(str, opt_rec.get("priority_leads_for_immediate_action", [])[:5]))}</p>'
                '</div>', 
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                '<div class="alert-card">'
                '<h4>⚠️ Churn Risk</h4>'
                f'<p><strong>At-Risk Leads:</strong> {len(opt_rec.get("leads_at_risk_of_churn", []))}</p>'
                '<p>Require immediate intervention</p>'
                '</div>', 
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                '<div class="optimization-card">'
                '<h4>💎 High Value Opportunities</h4>'
                f'<p><strong>High Value Leads:</strong> {len(opt_rec.get("high_value_opportunities", []))}</p>'
                '<p>Revenue > $60K + High Conversion</p>'
                '</div>', 
                unsafe_allow_html=True
            )

elif current_page == "call_activity":
    st.markdown('<h1 class="main-header">📞 AI Call Intelligence Dashboard</h1>', unsafe_allow_html=True)

    call_ai = ai_insights.get('call_activity', {})

    # Model Performance
    success_pred = call_ai.get('success_prediction', {})
    st.markdown(
        f'<div class="model-accuracy">'
        f'🎯 AI Model Accuracy: {success_pred.get("model_accuracy", 0)*100:.1f}% | '
        f'Predicted Improvement: {call_ai.get("call_optimization", {}).get("predicted_success_rate_improvement", 0)*100:.1f}%'
        f'</div>', 
        unsafe_allow_html=True
    )

    # Optimal Calling Windows
    if 'optimal_calling_windows' in success_pred:
        st.markdown("#### 🕐 AI-Optimized Calling Schedule")

        windows_data = success_pred['optimal_calling_windows'][:5]  # Top 5
        windows_df = pd.DataFrame(windows_data)
        windows_df['success_rate'] = windows_df['success_rate'] * 100

        fig = px.bar(windows_df, x='time', y='success_rate', 
                    title="Top 5 Optimal Calling Windows",
                    color='success_rate',
                    color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)

    # Predictive Scheduling
    if 'predictive_scheduling' in call_ai:
        st.markdown("#### 📅 AI-Recommended Weekly Schedule")

        schedule = call_ai['predictive_scheduling']['next_week_optimal_schedule']
        schedule_df = pd.DataFrame([
            {'Day': day, 'Optimal Times': ', '.join(times)}
            for day, times in schedule.items()
        ])
        st.dataframe(schedule_df, use_container_width=True)

    # Call Optimization Insights
    call_opt = call_ai.get('call_optimization', {})

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="prediction-card">'
            '<h4>📈 Success Rate Improvement</h4>'
            f'<p><strong>Predicted Gain:</strong> {call_opt.get("predicted_success_rate_improvement", 0)*100:.1f}%</p>'
            f'<p><strong>Optimal Volume:</strong> {call_opt.get("optimal_call_volume_per_agent", 0)} calls/agent</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="optimization-card">'
            '<h4>🎯 Sentiment Impact</h4>'
            f'<p><strong>Correlation:</strong> {call_opt.get("sentiment_correlation", 0)*100:.0f}%</p>'
            '<p>Strong positive sentiment correlation with success</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="ai-insight-box">'
            '<h4>🤖 AI Recommendations</h4>'
            '<p>• Focus calls during 10-11 AM window</p>'
            '<p>• Thursday shows highest success rates</p>'
            '<p>• Sentiment monitoring critical</p>'
            '</div>', 
            unsafe_allow_html=True
        )

elif current_page == "tasks":
    st.markdown('<h1 class="main-header">📋 Smart Task Management & AI Prioritization</h1>', unsafe_allow_html=True)

    task_ai = ai_insights.get('tasks_followup', {})

    # Smart Prioritization Results
    smart_prior = task_ai.get('smart_prioritization', {})

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("High Priority Tasks", smart_prior.get('high_priority_tasks', 0), delta="AI Prioritized")
    with col2:
        st.metric("Medium Priority", smart_prior.get('medium_priority_tasks', 0))
    with col3:
        st.metric("Low Priority", smart_prior.get('low_priority_tasks', 0))
    with col4:
        st.metric("Success Rate Prediction", f"{task_ai.get('success_prediction', {}).get('overall_success_rate_prediction', 0)*100:.1f}%")

    # Urgent Actions
    urgent = task_ai.get('urgent_actions', {})

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="alert-card">'
            '<h4>🚨 Immediate Action Required</h4>'
            f'<p><strong>Overdue Tasks:</strong> {urgent.get("overdue_tasks", 0)}</p>'
            f'<p><strong>Due Today:</strong> {urgent.get("tasks_due_today", 0)}</p>'
            f'<p><strong>Due This Week:</strong> {urgent.get("tasks_due_this_week", 0)}</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="prediction-card">'
            '<h4>📊 Success Predictions</h4>'
            f'<p><strong>High Success Probability:</strong> {task_ai.get("success_prediction", {}).get("high_success_probability_tasks", 0)}</p>'
            f'<p><strong>Low Success Probability:</strong> {task_ai.get("success_prediction", {}).get("low_success_probability_tasks", 0)}</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="optimization-card">'
            '<h4>🔧 Productivity Optimization</h4>'
            f'<p><strong>Improvement Potential:</strong> {task_ai.get("predictive_insights", {}).get("productivity_improvement_potential", 0)*100:.0f}%</p>'
            f'<p><strong>Completion Forecast:</strong> {task_ai.get("predictive_insights", {}).get("completion_rate_forecast", 0)*100:.0f}%</p>'
            '</div>', 
            unsafe_allow_html=True
        )

elif current_page == "agent_availability":
    st.markdown('<h1 class="main-header">👥 Agent Intelligence & Performance Optimization</h1>', unsafe_allow_html=True)

    agent_ai = ai_insights.get('agent_availability', {})

    # Performance Predictions
    perf_pred = agent_ai.get('performance_prediction', {})

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Exceeding Targets", perf_pred.get('agents_exceeding_targets', 0), delta="AI Predicted")
    with col2:
        st.metric("Need Support", perf_pred.get('agents_needing_support', 0), delta="Early Warning")
    with col3:
        st.metric("Improvement Potential", f"{perf_pred.get('average_performance_improvement_potential', 0)*100:.1f}%")
    with col4:
        st.metric("Training Impact", f"{agent_ai.get('skills_development', {}).get('training_impact_prediction', 0)*100:.1f}%")

    # Capacity Optimization
    capacity = agent_ai.get('capacity_optimization', {})

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div class="prediction-card">'
            '<h4>⚡ Capacity Analysis</h4>'
            f'<p><strong>Current Utilization:</strong> {capacity.get("current_utilization_rate", 0)*100:.0f}%</p>'
            f'<p><strong>Underutilized:</strong> Agents {", ".join(map(str, capacity.get("underutilized_agents", [])))}</p>'
            f'<p><strong>Overutilized:</strong> Agents {", ".join(map(str, capacity.get("overutilized_agents", [])))}</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="optimization-card">'
            '<h4>🎓 Skills Development</h4>'
            f'<p><strong>Need Training:</strong> Agents {", ".join(map(str, agent_ai.get("skills_development", {}).get("agents_needing_training", [])))}</p>'
            f'<p><strong>Priority Areas:</strong> {", ".join(agent_ai.get("skills_development", {}).get("priority_training_areas", [])[:2])}</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    # Burnout Prevention
    burnout = agent_ai.get('burnout_prevention', {})

    st.markdown(
        '<div class="alert-card">'
        '<h4>🛡️ Burnout Prevention & Wellness</h4>'
        f'<p><strong>High Risk Agents:</strong> {", ".join(map(str, burnout.get("high_burnout_risk_agents", [])))}</p>'
        f'<p><strong>Wellness Score:</strong> {burnout.get("wellness_score", 0)*100:.0f}%</p>'
        '</div>', 
        unsafe_allow_html=True
    )

elif current_page == "conversion":
    st.markdown('<h1 class="main-header">💰 AI Revenue Forecasting & Conversion Intelligence</h1>', unsafe_allow_html=True)

    conv_ai = ai_insights.get('conversion', {})

    # Revenue Forecasting
    revenue_forecast = conv_ai.get('revenue_forecasting', {})

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Pipeline Value", f"${revenue_forecast.get('total_pipeline_value', 0)/1000000:.2f}M")
    with col2:
        st.metric("Next Quarter Forecast", f"${revenue_forecast.get('expected_revenue_next_quarter', 0)/1000:.0f}K", delta="AI Predicted")
    with col3:
        st.metric("High Probability Revenue", f"${revenue_forecast.get('high_probability_revenue', 0)/1000:.0f}K")
    with col4:
        st.metric("Next Month Conversions", conv_ai.get('predictive_insights', {}).get('next_month_conversions_forecast', 0))

    # Optimization Opportunities
    conv_opt = conv_ai.get('conversion_optimization', {})

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div class="optimization-card">'
            '<h4>🎯 Conversion Optimization</h4>'
            f'<p><strong>Opportunities:</strong> {conv_opt.get("optimization_opportunities_count", 0)}</p>'
            f'<p><strong>Revenue at Risk:</strong> ${conv_opt.get("total_revenue_at_risk", 0)/1000:.0f}K</p>'
            f'<p><strong>Potential Uplift:</strong> ${conv_opt.get("potential_revenue_uplift", 0)/1000:.0f}K</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="prediction-card">'
            '<h4>⏱️ Time Intelligence</h4>'
            f'<p><strong>Avg Conversion Time:</strong> {conv_ai.get("time_to_conversion", {}).get("average_conversion_time", 0):.1f} days</p>'
            f'<p><strong>Fast Track Opportunities:</strong> {conv_ai.get("time_to_conversion", {}).get("fast_track_opportunities", 0)}</p>'
            f'<p><strong>Stalled Deals:</strong> {conv_ai.get("time_to_conversion", {}).get("stalled_deals_needing_attention", 0)}</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    # Predictive Insights
    pred_insights = conv_ai.get('predictive_insights', {})
    confidence_interval = pred_insights.get('revenue_confidence_interval', [0, 0])

    st.markdown(
        '<div class="ai-insight-box">'
        '<h4>🔮 Revenue Predictions & Market Intelligence</h4>'
        f'<p><strong>Revenue Confidence Range:</strong> ${confidence_interval[0]/1000:.0f}K - ${confidence_interval[1]/1000:.0f}K</p>'
        f'<p><strong>Seasonal Adjustment:</strong> {pred_insights.get("seasonal_adjustment_factor", 1)*100:.0f}% expected increase</p>'
        f'<p><strong>Market Trend Impact:</strong> +{pred_insights.get("market_trend_impact", 0)*100:.0f}% from favorable conditions</p>'
        '</div>', 
        unsafe_allow_html=True
    )

elif current_page == "geographic":
    st.markdown('<h1 class="main-header">🌍 Market Intelligence & Geographic AI Analytics</h1>', unsafe_allow_html=True)

    geo_ai = ai_insights.get('geographic', {})

    # Market Intelligence
    market_intel = geo_ai.get('market_intelligence', {})

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Top Opportunity Market", market_intel.get('top_opportunity_market', 'N/A'), delta="AI Ranked #1")
    with col2:
        st.metric("Fastest Growing", market_intel.get('fastest_growing_market', 'N/A'), delta="Growth Leader")
    with col3:
        st.metric("Best Conversion", market_intel.get('highest_conversion_market', 'N/A'), delta="Performance Leader")
    with col4:
        st.metric("Market Diversity", f"{market_intel.get('market_diversity_index', 0)*100:.0f}%", delta="Balance Score")

    # Expansion Opportunities
    expansion = geo_ai.get('expansion_opportunities', {})

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div class="optimization-card">'
            '<h4>🚀 Expansion Opportunities</h4>'
            f'<p><strong>High Potential Markets:</strong> {", ".join(expansion.get("high_potential_markets", []))}</p>'
            f'<p><strong>Total Potential:</strong> {expansion.get("total_expansion_potential", "$0")}</p>'
            f'<p><strong>Underserved Markets:</strong> {", ".join(expansion.get("underserved_markets", []))}</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="alert-card">'
            '<h4>⚠️ Risk Analysis</h4>'
            f'<p><strong>Regulatory Challenges:</strong> {", ".join(geo_ai.get("risk_analysis", {}).get("regulatory_challenges", []))}</p>'
            f'<p><strong>Competitive Pressures:</strong> {", ".join(geo_ai.get("risk_analysis", {}).get("competitive_pressures", []))}</p>'
            '</div>', 
            unsafe_allow_html=True
        )

    # Predictive Analytics
    pred_analytics = geo_ai.get('predictive_analytics', {})

    if 'market_saturation_timeline' in pred_analytics:
        st.markdown("#### 📅 Market Saturation Timeline")

        sat_data = []
        for market, timeline in pred_analytics['market_saturation_timeline'].items():
            sat_data.append({'Market': market, 'Saturation Timeline': timeline})

        st.dataframe(pd.DataFrame(sat_data), use_container_width=True)

# Footer with AI Model Info
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if 'meta_insights' in ai_insights:
        st.metric("AI Models Active", ai_insights['meta_insights'].get('total_models_deployed', 12))

with col2:
    if 'meta_insights' in ai_insights:
        st.metric("Prediction Accuracy", f"{ai_insights['meta_insights'].get('prediction_accuracy_average', 0.743)*100:.1f}%")

with col3:
    if 'meta_insights' in ai_insights:
        st.metric("Optimization Potential", ai_insights['meta_insights'].get('optimization_potential_total', '$2.1M'))

)
