# Simple dashboard generator using pandas + plotly
import pandas as pd
import plotly.express as px
import os

os.makedirs('../dist', exist_ok=True)
df = pd.read_csv('../data/sample_sales.csv', parse_dates=['order_date'])
# KPIs
df['revenue'] = df['quantity'] * df['price']
kpis = {
    'total_revenue': df['revenue'].sum(),
    'total_orders': df['order_id'].nunique(),
    'avg_order_value': df.groupby('order_id')['revenue'].sum().mean()
}
# Simple chart
daily = df.groupby(df['order_date'].dt.date).agg({'revenue':'sum'}).reset_index()
fig = px.bar(daily, x='order_date', y='revenue', title='Daily Revenue')
out_file = '../dist/dashboard.html'
with open(out_file, 'w') as f:
    f.write('<html><head><meta charset="utf-8"></head><body>')
    f.write(f'<h1>E-Commerce Sales Dashboard</h1>')
    f.write(f'<p>Total revenue: ${kpis["total_revenue"]:.2f}</p>')
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write('</body></html>')
print('Dashboard written to', out_file)
