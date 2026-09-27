import os

GITHUB_USERNAME = "apexmetrics"
COINBASE_PAY_LINK = "https://coinbase.com"
BASE_URL = f"https://{GITHUB_USERNAME}.github.io"

print("⚡ INJECTING ROOT-ALIGNED 5,000 ENTERPRISE PLATFORM MATRIX...")

industries = [
    "Real Estate", "E-commerce", "SaaS Startups", "Healthcare Clinics", "Crypto Exchanges", 
    "Logistics", "Digital Marketing Agencies", "Retail Stores", "Automotive", "Fintech",
    "Edtech", "Renewable Energy", "Construction", "Hospitality and Hotels", "Agriculture tech",
    "Cybersecurity", "Legal Firms", "Fitness Brands", "Food Delivery", "Gaming Studios",
    "Aviation", "Fashion Labels", "Pharmaceuticals", "Manufacturing", "Insurance Agencies",
    "Telecommunications", "Media and Entertainment", "Mining and Metals", "Venture Capital", "Hedge Funds",
    "Recruitment Agencies", "Event Planning", "Consulting Firms", "Architecture Studios", "Pet Care Brands",
    "Beauty and Cosmetics", "Subscription Boxes", "Interior Design", "Luxury Goods", "Mental Health Apps",
    "Cleantech", "Biotech", "Robotics", "AI Startups", "Micro-SaaS", "3D Printing", "Commercial Space",
    "Drone Services", "E-sports Teams", "Virtual Reality", "Augmented Reality", "Podcasting Networks",
    "Online Marketplaces", "B2B Wholesalers", "Maritime Shipping", "Chemical Production", "Waste Management",
    "Water Treatment", "Smart Home Automation", "Wearable Tech", "Influencer Networks", "Affiliate Portals",
    "Local Plumbers", "HVAC Contractors", "Dental Practices", "Optometry Clinics", "Veterinary Hospitals",
    "Chiropratic Centers", "Boutique Gyms", "Yoga Studios", "Co-working Spaces", "Storage Facilities",
    "Car Rentals", "Private Security", "Catering Services", "Cleaning Franchises", "Landscaping Companies",
    "Roofing Contractors", "Solar Installers", "Electricians", "Photography Studios", "Videography Agencies",
    "Graphic Design Shops", "Copywriting Agencies", "Translation Bureaus", "Accounting Firms", "Bookkeeping Services",
    "Tax Consultants", "Wealth Management", "Estate Planning", "Public Relations", "SEO Agencies",
    "Social Media Managers", "UI-UX Studios", "App Developers", "Web Development Shops", "Cyber Auditing",
    "Data Analytics Firms", "Cloud Hosting Brokers", "IT Support Centers", "Managed Service Providers"
]

metrics = [
    {"name": "Customer Acquisition Cost", "code": "CAC", "category": "Marketing Efficiency"},
    {"name": "Lifetime Value", "code": "LTV", "category": "Revenue Sustainability"},
    {"name": "Monthly Churn Rate", "code": "CHURN", "category": "Retention Analytics"},
    {"name": "Average Revenue Per User", "code": "ARPU", "category": "Monetization Optimization"},
    {"name": "Burn Rate Metric", "code": "BURN", "category": "Capital Efficiency"},
    {"name": "Net Promoter Score", "code": "NPS", "category": "Product-Market Fit"},
    {"name": "Viral Coefficient", "code": "KFACTOR", "category": "Organic Growth Strategy"},
    {"name": "Payback Period", "code": "PAYBACK", "category": "Financial Modeling"},
    {"name": "Gross Margin Percentage", "code": "MARGIN", "category": "Operational Profitability"},
    {"name": "Active User Ratio", "code": "ENGAGEMENT", "category": "Product Engagement"},
    {"name": "Trial Conversion Rate", "code": "CONVERSION", "category": "Marketing Efficiency"},
    {"name": "Expansion Revenue Rate", "code": "EXPANSION", "category": "Revenue Sustainability"},
    {"name": "Lead-to-Customer Velocity", "code": "VELOCITY", "category": "Marketing Efficiency"},
    {"name": "Customer Retention Cost", "code": "CRC", "category": "Retention Analytics"},
    {"name": "Revenue Runway Timeline", "code": "RUNWAY", "category": "Capital Efficiency"},
    {"name": "Organic Search Traffic Share", "code": "SEO_SHARE", "category": "Marketing Efficiency"},
    {"name": "Paid Ad ROI Coefficient", "code": "ROAS", "category": "Marketing Efficiency"},
    {"name": "Social Sentiment Index", "code": "SENTIMENT", "category": "Product-Market Fit"},
    {"name": "Infrastructure Cost Per User", "code": "INFRA_COST", "category": "SaaS Infrastructure"},
    {"name": "Support Ticket Resolution Time", "code": "TICKET_TIME", "category": "Operations Performance"},
    {"name": "Employee LTV Multiplier", "code": "HR_ROI", "category": "Operations Performance"},
    {"name": "Contract Value Velocity", "code": "ACV", "category": "Monetization Optimization"},
    {"name": "Pipeline Coverage Ratio", "code": "COVERAGE", "category": "Financial Modeling"},
    {"name": "Win Rate Metric", "code": "WIN_RATE", "category": "Marketing Efficiency"},
    {"name": "Quota Attainment Average", "code": "QUOTA", "category": "Operations Performance"},
    {"name": "Net Revenue Retention", "code": "NRR", "category": "Revenue Sustainability"},
    {"name": "Gross Revenue Retention", "code": "GRR", "category": "Revenue Sustainability"},
    {"name": "Logo Churn Index", "code": "LOGO_CHURN", "category": "Retention Analytics"},
    {"name": "Feature Adoption Coefficient", "code": "FEATURE_ADOPT", "category": "Product Engagement"},
    {"name": "Time to Value", "code": "TTV", "category": "Product Engagement"},
    {"name": "Session Duration Standard", "code": "SESSION", "category": "Product Engagement"},
    {"name": "Bounce Rate Threshold", "code": "BOUNCE", "category": "Marketing Efficiency"},
    {"name": "Cart Abandonment Average", "code": "ABANDON", "category": "Monetization Optimization"},
    {"name": "Repeat Purchase Velocity", "code": "REPEAT_BUY", "category": "Revenue Sustainability"},
    {"name": "Inventory Turnover Rate", "code": "INVENTORY", "category": "Operations Performance"},
    {"name": "Supplier Lead Time Index", "code": "SUPPLIER_TIME", "category": "Operations Performance"},
    {"name": "Order Fulfillment Accuracy", "code": "ACCURACY", "category": "Operations Performance"},
    {"name": "Return Rate Metric", "code": "RETURN_RATE", "category": "Product-Market Fit"},
    {"name": "Affiliate Commission Yield", "code": "AFFILIATE", "category": "Monetization Optimization"},
    {"name": "Referral Program Velocity", "code": "REFERRAL", "category": "Organic Growth Strategy"},
    {"name": "Email Open Rate Standard", "code": "EMAIL_OPEN", "category": "Marketing Efficiency"},
    {"name": "Click-Through Rate", "code": "CTR", "category": "Marketing Efficiency"},
    {"name": "Cost Per Lead", "code": "CPL", "category": "Marketing Efficiency"},
    {"name": "Subscriber Growth Velocity", "code": "SUBSCRIBERS", "category": "Revenue Sustainability"},
    {"name": "API Uptime Coefficient", "code": "UPTIME", "category": "SaaS Infrastructure"},
    {"name": "Data Processing Latency", "code": "LATENCY", "category": "SaaS Infrastructure"},
    {"name": "Security Vulnerability Index", "code": "SECURITY", "category": "SaaS Infrastructure"},
    {"name": "Server Cost Optimization Rate", "code": "SERVER_OPT", "category": "SaaS Infrastructure"},
    {"name": "Code Deployment Frequency", "code": "DEPLOY", "category": "SaaS Infrastructure"},
    {"name": "Bug Regression Percentage", "code": "BUGS", "category": "SaaS Infrastructure"}
]

if not os.path.exists('articles'):
    os.makedirs('articles')

article_links = []
sitemap_urls = []

html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Enterprise {m_name} Hub for {i_name}</title>
    <style>
        body {{ font-family: system-ui, sans-serif; padding: 30px; background: #0f172a; color: #f3f4f6; max-width: 800px; margin: 0 auto; }}
        .card {{ background: #1e293b; padding: 25px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px; }}
        .metric-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; }}
        .metric-item {{ background: #0f172a; padding: 15px; border-radius: 6px; text-align: center; border: 1px solid #334155; }}
        .metric-val {{ font-size: 1.5rem; font-weight: bold; color: #34d399; margin-top: 5px; }}
        .checkout {{ background: linear-gradient(135deg, #1e1b4b, #311042); padding: 30px; border-radius: 8px; text-align: center; border: 1px solid #4c1d95; }}
        .pay-btn {{ display: inline-block; background: #10b981; color: #fff; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 15px; }}
    </style>
</head>
<body>
    <a href="../index.html" style="color: #94a3b8; text-decoration: none;">← Back to Directory Hub</a>
    <div class="card">
        <h1>{m_name} ({m_code}) Data Layer for {i_name}</h1>
        <div class="metric-grid">
            <div class="metric-item">Lower Bound<div class="metric-val">Top 25%</div></div>
            <div class="metric-item">Median Bound<div class="metric-val">Top 50%</div></div>
            <div class="metric-item">Target Bound<div class="metric-val">Top 10%</div></div>
        </div>
    </div>
    <div class="checkout">
        <h3>Unlock Live API Programmatic Feeds for {i_name}</h3>
        <div style="font-size: 1.5rem; font-weight: bold; color: #34d399; margin: 10px 0;">$499 / Lifetime Full Access</div>
        <a href="{c_link}" target="_blank" class="pay-btn">Unlock via Coinbase Commerce</a>
    </div>
</body>
</html>"""

print("🔄 Generating root-aligned operational data files...")

categories_map = {}
for ind in industries:
    for met in metrics:
        m_cat = met["category"]
        m_name = met["name"]
        m_code = met["code"]
        slug = f"optimize-{m_code.lower()}-for-{ind.lower().replace(' ', '-').replace('&', 'and')}"
        
        formatted_html = html_template.format(i_name=ind, m_name=m_name, m_code=m_code, c_link=COINBASE_PAY_LINK)
        with open(f"articles/{slug}.html", "w", encoding="utf-8") as f:
            f.write(formatted_html)
            
        link_str = f'<a href="articles/{slug}.html">📊 {ind} — {m_name}</a>'
        if m_cat not in categories_map:
            categories_map[m_cat] = []
        categories_map[m_cat].append(link_str)