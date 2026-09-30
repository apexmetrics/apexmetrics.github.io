import os

BASE_URL = "https://github.io"
USDT_TRC20_ADDRESS = "TPcXDjVa5yBCc8zEwsc63xHeL6Prcpdekz"

print("⚡ INITIATING STREAMLINED GENERATION SYSTEM...")

# Complete Industries Array
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

# Complete Metrics Array
metrics = [
    {"name": "Customer Acquisition Cost", "code": "CAC"},
    {"name": "Lifetime Value", "code": "LTV"},
    {"name": "Monthly Churn Rate", "code": "CHURN"},
    {"name": "Average Revenue Per User", "code": "ARPU"},
    {"name": "Burn Rate Metric", "code": "BURN"},
    {"name": "Net Promoter Score", "code": "NPS"},
    {"name": "Viral Coefficient", "code": "KFACTOR"},
    {"name": "Payback Period", "code": "PAYBACK"},
    {"name": "Gross Margin Percentage", "code": "MARGIN"},
    {"name": "Active User Ratio", "code": "ENGAGEMENT"},
    {"name": "Trial Conversion Rate", "code": "CONVERSION"},
    {"name": "Expansion Revenue Rate", "code": "EXPANSION"},
    {"name": "Lead-to-Customer Velocity", "code": "VELOCITY"},
    {"name": "Customer Retention Cost", "code": "CRC"},
    {"name": "Revenue Runway Timeline", "code": "RUNWAY"},
    {"name": "Organic Search Traffic Share", "code": "SEO_SHARE"},
    {"name": "Paid Ad ROI Coefficient", "code": "ROAS"},
    {"name": "Social Sentiment Index", "code": "SENTIMENT"},
    {"name": "Infrastructure Cost Per User", "code": "INFRA_COST"},
    {"name": "Support Ticket Resolution Time", "code": "TICKET_TIME"},
    {"name": "Employee LTV Multiplier", "code": "HR_ROI"},
    {"name": "Contract Value Velocity", "code": "ACV"},
    {"name": "Pipeline Coverage Ratio", "code": "COVERAGE"},
    {"name": "Win Rate Metric", "code": "WIN_RATE"},
    {"name": "Quota Attainment Average", "code": "QUOTA"},
    {"name": "Net Revenue Retention", "code": "NRR"},
    {"name": "Gross Revenue Retention", "code": "GRR"},
    {"name": "Logo Churn Index", "code": "LOGO_CHURN"},
    {"name": "Feature Adoption Coefficient", "code": "FEATURE_ADOPT"},
    {"name": "Time to Value", "code": "TTV"},
    {"name": "Session Duration Standard", "code": "SESSION"},
    {"name": "Bounce Rate Threshold", "code": "BOUNCE"},
    {"name": "Cart Abandonment Average", "code": "ABANDON"},
    {"name": "Repeat Purchase Velocity", "code": "REPEAT_BUY"},
    {"name": "Inventory Turnover Rate", "code": "INVENTORY"},
    {"name": "Supplier Lead Time Index", "code": "SUPPLIER_TIME"},
    {"name": "Order Fulfillment Accuracy", "code": "ACCURACY"},
    {"name": "Return Rate Metric", "code": "RETURN_RATE"},
    {"name": "Affiliate Commission Yield", "code": "AFFILIATE"},
    {"name": "Referral Program Velocity", "code": "REFERRAL"},
    {"name": "Email Open Rate Standard", "code": "EMAIL_OPEN"},
    {"name": "Click-Through Rate", "code": "CTR"},
    {"name": "Cost Per Lead", "code": "CPL"},
    {"name": "Subscriber Growth Velocity", "code": "SUBSCRIBERS"},
    {"name": "API Uptime Coefficient", "code": "UPTIME"},
    {"name": "Data Processing Latency", "code": "LATENCY"},
    {"name": "Security Vulnerability Index", "code": "SECURITY"},
    {"name": "Server Cost Optimization Rate", "code": "SERVER_OPT"},
    {"name": "Code Deployment Frequency", "code": "DEPLOY"},
    {"name": "Bug Regression Percentage", "code": "BUGS"}
]

os.makedirs('articles', exist_ok=True)
article_links = []
sitemap_urls = []

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise {m_name} for {i_name}</title>
    <style>
        body {{ font-family: sans-serif; padding: 20px; background: #0f172a; color: #f3f4f6; max-width: 800px; margin: 0 auto; }}
        .card {{ background: #1e293b; padding: 20px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px; }}
        .metric-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 15px 0; }}
        .metric-item {{ background: #0f172a; padding: 10px; border-radius: 6px; text-align: center; border: 1px solid #334155; }}
        .metric-val {{ font-size: 1.1rem; font-weight: bold; color: #34d399; margin-top: 5px; }}
        .checkout {{ background: linear-gradient(135deg, #1e1b4b, #311042); padding: 25px; border-radius: 12px; text-align: center; border: 1px solid #4c1d95; }}
        .pay-btn {{ display: inline-block; background: #10b981; color: #fff; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 15px; cursor: pointer; border: none; font-size: 1rem; }}
        .modal-overlay {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); justify-content: center; align-items: center; z-index: 9999; }}
        .modal-box {{ background: #1e293b; border: 1px solid #475569; padding: 20px; border-radius: 16px; max-width: 400px; width: 90%; text-align: center; color: #fff; position: relative; }}
        .close-btn {{ position: absolute; top: 10px; right: 15px; font-size: 1.4rem; color: #94a3b8; cursor: pointer; }}
        .wallet-row {{ background: #0f172a; border: 1px solid #334155; padding: 12px; border-radius: 8px; margin: 15px 0; text-align: left; cursor: pointer; }}
        .val {{ font-family: monospace; font-size: 0.9rem; color: #34d399; word-break: break-all; margin-top: 4px; display: block; background: #1e293b; padding: 6px; border-radius: 4px; border: 1px solid #334155; }}
    </style>
</head>
<body>
    <a href="../index.html" style="color: #94a3b8; text-decoration: none;">← Back to Hub</a>
    <div class="card">
        <h1>{m_name} ({m_code}) Data Layer for {i_name}</h1>
        <div class="metric-grid">
            <div class="metric-item">Lower Bound<div class="metric-val">Top 25%</div></div>
            <div class="metric-item">Median Bound<div class="metric-val">Top 50%</div></div>
            <div class="metric-item">Target Bound<div class="metric-val">Top 10%</div></div>
        </div>
    </div>
    <div class="checkout">
        <h3>Unlock Real-time Institutional Access Flow</h3>
        <p>Compatible with all global crypto applications (Coinbase, Trust Wallet, Binance, Bybit etc.)</p>
        <div style="font-size: 1.6rem; font-weight: bold; color: #34d399; margin: 10px 0;">$499 / One-time Token</div>
        <button class="pay-btn" onclick="openGateway()">Unlock via Crypto Gateway</button>
    </div>
    <div id="cryptoModal" class="modal-overlay">
        <div class="modal-box">
            <span class="close-btn" onclick="closeGateway()">&times;</span>
            <h3 style="color:#38bdf8; margin-top:0;">Universal Crypto Checkout</h3>
            <p style="font-size:0.85rem; color:#94a3b8;">Copy the secure TRC20 address below using any wallet app to complete transaction.</p>
            <div class="wallet-row" onclick="navigator.clipboard.writeText('{trc20}'); alert('Address Copied!');">
                <span style="font-size:0.7rem; color:#38bdf8; float:right;">Click to Copy</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">USDT (TRON / TRC20)</span>
                <span class="val">{trc20}</span>
            </div>
        </div>
    </div>
    <script>
        function openGateway() {{ document.getElementById('cryptoModal').style.display = 'flex'; }}
        function closeGateway() {{ document.getElementById('cryptoModal').style.display = 'none'; }}
    </script>
</body>
</html>"""

for ind in industries:
    for met in metrics:
        slug = f"optimize-{met['code'].lower()}-for-{ind.lower().replace(' ', '-').replace('&', 'and')}"
        with open(f"articles/{slug}.html", "w", encoding="utf-8") as f:
            f.write(html_template.format(i_name=ind, m_name=met['name'], m_code=met['code'], trc20=USDT_TRC20_ADDRESS))
        article_links.append(f'<li><a href="articles/{slug}.html">{ind} Hub — {met["name"]}</a></li>')
        sitemap_urls.append(f'  <url><loc>{BASE_URL}articles/{slug}.html</loc></url>')

