import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(page_title="The Digital Experience | Shop Console", page_icon="🛍️", layout="wide")

st.markdown("""
<style>
:root {
  --ink: #17233b;
  --muted: #66758e;
  --accent: #176b87;
  --accent2: #28a7a1;
  --line: #dce5ee;
}
.stApp {
  background:
    radial-gradient(ellipse at 88% 0%, rgba(40,167,161,.13), transparent 33%),
    radial-gradient(ellipse at 0% 18%, rgba(71,128,190,.10), transparent 35%),
    linear-gradient(135deg, #f6f9fc 0%, #edf3f8 52%, #f8fbfd 100%);
  color: var(--ink);
}
[data-testid="stHeader"] { background: rgba(246,249,252,.82); }
[data-testid="stAppViewContainer"] > .main { background: transparent; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1500px; }
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #10243d 0%, #163b55 55%, #13505b 100%);
  border-right: 1px solid rgba(255,255,255,.10);
}
section[data-testid="stSidebar"] * { color: #edf7ff; }
section[data-testid="stSidebar"] [data-testid="stRadio"] label { 
  padding: 7px 10px; border-radius: 9px; 
}
section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
  background: rgba(255,255,255,.10);
}
section[data-testid="stSidebar"] [data-testid="stAlert"] {
  background: rgba(255,255,255,.09); border: 1px solid rgba(255,255,255,.15);
}
h1, h2, h3 { color: #142b45; letter-spacing: -0.5px; }
h1 { font-weight: 800; }
h2, h3 { font-weight: 700; }
p, label, [data-testid="stCaptionContainer"] { color: #5e6f86; }
div[data-testid="stMetric"] {
  background: rgba(255,255,255,.86);
  border: 1px solid #dbe5ef;
  padding: 18px 18px 15px;
  border-radius: 16px;
  box-shadow: 0 7px 22px rgba(27,55,82,.055);
}
div[data-testid="stMetric"] label { color: #64748b; font-weight: 600; }
div[data-testid="stMetric"] [data-testid="stMetricValue"] { color: #153653; font-weight: 800; }
div[data-testid="stVerticalBlockBorderWrapper"] {
  border-radius: 16px; border-color: #dce5ee;
}
.stButton > button, .stDownloadButton > button, div[data-testid="stFormSubmitButton"] > button {
  border-radius: 10px; border: 1px solid #cbd9e6; font-weight: 650;
  transition: all .18s ease;
}
.stButton > button[kind="primary"], div[data-testid="stFormSubmitButton"] > button[kind="primary"] {
  background: linear-gradient(100deg, #176b87, #218f98);
  color: white; border: none;
}
.stButton > button:hover, .stDownloadButton > button:hover {
  border-color: #218f98; color: #176b87; transform: translateY(-1px);
}
div[data-testid="stDataFrame"], div[data-testid="stTable"] {
  border: 1px solid #dce5ee; border-radius: 12px; overflow: hidden;
}
hr { border-color: #dce5ee; }
.small-muted { color: #718198; }
</style>
""", unsafe_allow_html=True)
def seed_state():
    if "products" not in st.session_state:
        st.session_state.products = pd.DataFrame([
            {"SKU":"DX-1001","Product":"Wireless Earbuds","Category":"Audio","Price (R)":699.00,"Stock":8,"Reorder Level":10},
            {"SKU":"DX-1002","Product":"USB-C Charger 65W","Category":"Accessories","Price (R)":449.00,"Stock":24,"Reorder Level":8},
            {"SKU":"DX-1003","Product":"Bluetooth Speaker","Category":"Audio","Price (R)":899.00,"Stock":5,"Reorder Level":8},
            {"SKU":"DX-1004","Product":"Smart Watch","Category":"Wearables","Price (R)":1299.00,"Stock":14,"Reorder Level":6},
            {"SKU":"DX-1005","Product":"USB-C Cable","Category":"Accessories","Price (R)":149.00,"Stock":31,"Reorder Level":12},
            {"SKU":"DX-1006","Product":"Power Bank 20K","Category":"Accessories","Price (R)":599.00,"Stock":7,"Reorder Level":10},
        ])
    if "sales" not in st.session_state:
        today = date.today()
        st.session_state.sales = pd.DataFrame([
            {"Date": today - timedelta(days=6), "Receipt":"DX-501","Product":"Wireless Earbuds","Qty":2,"Unit Price (R)":699.00,"Payment":"Card"},
            {"Date": today - timedelta(days=5), "Receipt":"DX-502","Product":"USB-C Charger 65W","Qty":1,"Unit Price (R)":449.00,"Payment":"Card"},
            {"Date": today - timedelta(days=4), "Receipt":"DX-503","Product":"Smart Watch","Qty":1,"Unit Price (R)":1299.00,"Payment":"EFT"},
            {"Date": today - timedelta(days=3), "Receipt":"DX-504","Product":"USB-C Cable","Qty":3,"Unit Price (R)":149.00,"Payment":"Cash"},
            {"Date": today - timedelta(days=2), "Receipt":"DX-505","Product":"Bluetooth Speaker","Qty":1,"Unit Price (R)":899.00,"Payment":"Card"},
            {"Date": today - timedelta(days=1), "Receipt":"DX-506","Product":"Power Bank 20K","Qty":2,"Unit Price (R)":599.00,"Payment":"Card"},
            {"Date": today, "Receipt":"DX-507","Product":"Wireless Earbuds","Qty":1,"Unit Price (R)":699.00,"Payment":"EFT"},
        ])
    if "customers" not in st.session_state:
        st.session_state.customers = pd.DataFrame([
            {"Customer ID":"C-101","Name":"Demo Customer 1","Contact":"demo1@example.com","Segment":"Returning","Last Purchase":date.today()-timedelta(days=2),"Follow-up":"Due"},
            {"Customer ID":"C-102","Name":"Demo Customer 2","Contact":"demo2@example.com","Segment":"New","Last Purchase":date.today()-timedelta(days=1),"Follow-up":"Pending"},
            {"Customer ID":"C-103","Name":"Demo Customer 3","Contact":"demo3@example.com","Segment":"VIP","Last Purchase":date.today()-timedelta(days=12),"Follow-up":"Due"},
        ])
    if "tasks" not in st.session_state:
        st.session_state.tasks = pd.DataFrame([
            {"Task":"Follow up on VIP customer","Owner":"Shop Team","Due":date.today(),"Priority":"High","Status":"Open"},
            {"Task":"Review low-stock products","Owner":"Inventory","Due":date.today(),"Priority":"High","Status":"Open"},
            {"Task":"Prepare weekly sales summary","Owner":"Manager","Due":date.today()+timedelta(days=1),"Priority":"Medium","Status":"In progress"},
        ])
    if "campaigns" not in st.session_state:
        st.session_state.campaigns = pd.DataFrame([
            {"Campaign":"Weekend Audio Offer","Channel":"In-store + Social","Budget (R)":1200,"Leads":18,"Conversions":5,"Status":"Active"},
            {"Campaign":"Accessories Bundle","Channel":"In-store","Budget (R)":600,"Leads":12,"Conversions":4,"Status":"Completed"},
        ])

seed_state()
products = st.session_state.products
sales = st.session_state.sales.copy()
sales["Sales (R)"] = sales["Qty"] * sales["Unit Price (R)"]
customers = st.session_state.customers
tasks = st.session_state.tasks
campaigns = st.session_state.campaigns

st.sidebar.title("🛍️ The Digital Experience")
st.sidebar.caption("Shop App Console · Fourways Crossing")
page = st.sidebar.radio("WORKSPACE", [
    "Executive Overview", "Sales & Transactions", "Products & Inventory",
    "Customers & CRM", "Marketing Intelligence", "Automation & Tasks",
    "AI Insights", "Data & Governance", "Growth & Reports"
])
st.sidebar.divider()
st.sidebar.info("Demo mode is active. Sample records are fictional and stored in this session.")
st.sidebar.caption("Version 1–8 foundation")

def money(value):
    return f"R {value:,.2f}"

if page == "Executive Overview":
    st.title("Shop Performance Overview")
    st.caption("A single view of sales, products, customers, and daily operations.")
    total_sales = sales["Sales (R)"].sum()
    transactions = sales["Receipt"].nunique()
    units = int(sales["Qty"].sum())
    low_stock = int((products["Stock"] <= products["Reorder Level"]).sum())
    a,b,c,d = st.columns(4)
    a.metric("Demo sales", money(total_sales))
    b.metric("Transactions", transactions)
    c.metric("Units sold", units)
    d.metric("Low-stock items", low_stock, delta="Needs review" if low_stock else "On track", delta_color="inverse")
    chart1, chart2 = st.columns(2)
    with chart1:
        daily = sales.groupby("Date", as_index=False)["Sales (R)"].sum()
        st.subheader("Sales trend")
        st.plotly_chart(px.line(daily, x="Date", y="Sales (R)", markers=True, template="plotly_white").update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.55)", font_color="#243b53", margin=dict(l=10,r=10,t=25,b=10)), use_container_width=True)
    with chart2:
        mix = sales.groupby("Product", as_index=False)["Sales (R)"].sum().sort_values("Sales (R)", ascending=False)
        st.subheader("Sales by product")
        st.plotly_chart(px.bar(mix, x="Product", y="Sales (R)", template="plotly_white").update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.55)", font_color="#243b53", margin=dict(l=10,r=10,t=25,b=10)), use_container_width=True)
    left, right = st.columns(2)
    with left:
        st.subheader("Stock alerts")
        st.dataframe(products.loc[products["Stock"] <= products["Reorder Level"], ["SKU","Product","Stock","Reorder Level"]], hide_index=True, use_container_width=True)
    with right:
        st.subheader("Open tasks")
        st.dataframe(tasks.loc[tasks["Status"] != "Done"], hide_index=True, use_container_width=True)

elif page == "Sales & Transactions":
    st.title("Sales & Transactions")
    st.caption("Review demo transactions and add a sale to the current session.")
    with st.form("new_sale", clear_on_submit=True):
        p1,p2,p3 = st.columns(3)
        product_name = p1.selectbox("Product", products["Product"].tolist())
        qty = p2.number_input("Quantity", min_value=1, max_value=100, value=1)
        payment = p3.selectbox("Payment method", ["Card","Cash","EFT"])
        submitted = st.form_submit_button("Record sale", type="primary")
    if submitted:
        selected = products.loc[products["Product"] == product_name].iloc[0]
        if int(selected["Stock"]) < qty:
            st.error("Not enough stock to record this sale. Update inventory first.")
        else:
            new_id = f"DX-{501 + len(st.session_state.sales)}"
            st.session_state.sales.loc[len(st.session_state.sales)] = [date.today(), new_id, product_name, int(qty), float(selected["Price (R)"]), payment]
            st.session_state.products.loc[st.session_state.products["Product"] == product_name, "Stock"] -= int(qty)
            st.success(f"Sale {new_id} recorded in this session.")
            st.rerun()
    view = st.session_state.sales.copy()
    view["Sales (R)"] = view["Qty"] * view["Unit Price (R)"]
    search = st.text_input("Search receipt or product")
    if search:
        view = view[view.astype(str).apply(lambda col: col.str.contains(search, case=False, na=False)).any(axis=1)]
    st.dataframe(view.sort_values("Date", ascending=False), hide_index=True, use_container_width=True)
    st.metric("Displayed sales total", money(view["Sales (R)"].sum()))

elif page == "Products & Inventory":
    st.title("Products & Inventory")
    st.caption("Monitor stock and edit quantities. Changes are session-only in demo mode.")
    edited = st.data_editor(st.session_state.products, num_rows="dynamic", use_container_width=True, key="products_editor")
    if st.button("Save inventory edits", type="primary"):
        st.session_state.products = edited
        st.success("Inventory updated for this session.")
        st.rerun()
    current = st.session_state.products
    low = current[current["Stock"] <= current["Reorder Level"]]
    st.subheader(f"Reorder alerts ({len(low)})")
    st.dataframe(low, hide_index=True, use_container_width=True)
    st.download_button("Download product CSV", current.to_csv(index=False).encode("utf-8"), "digital_experience_products.csv", "text/csv")

elif page == "Customers & CRM":
    st.title("Customers & CRM")
    st.caption("Customer profiles, segmentation, and follow-up tracking using fictional demo contacts.")
    edited = st.data_editor(st.session_state.customers, num_rows="dynamic", use_container_width=True, key="customers_editor")
    if st.button("Save customer changes", type="primary"):
        st.session_state.customers = edited
        st.success("Customer records updated for this session.")
        st.rerun()
    with st.form("add_customer", clear_on_submit=True):
        n1,n2,n3 = st.columns(3)
        name = n1.text_input("Customer name")
        contact = n2.text_input("Email or phone")
        segment = n3.selectbox("Segment", ["New","Returning","VIP","At risk"])
        add = st.form_submit_button("Add customer")
    if add:
        if not name.strip() or not contact.strip():
            st.error("Enter a name and contact detail.")
        else:
            st.session_state.customers.loc[len(st.session_state.customers)] = [f"C-{101+len(st.session_state.customers)}",name,contact,segment,date.today(),"Pending"]
            st.success("Customer added.")
            st.rerun()

elif page == "Marketing Intelligence":
    st.title("Marketing Intelligence")
    st.caption("Track campaign activity and compare leads with conversions.")
    edited = st.data_editor(st.session_state.campaigns, num_rows="dynamic", use_container_width=True, key="campaign_editor")
    if st.button("Save campaign changes", type="primary"):
        st.session_state.campaigns = edited
        st.success("Campaign data updated for this session.")
        st.rerun()
    c1,c2 = st.columns(2)
    with c1:
        st.metric("Campaigns", len(st.session_state.campaigns))
        st.metric("Demo leads", int(st.session_state.campaigns["Leads"].sum()))
    with c2:
        st.metric("Conversions", int(st.session_state.campaigns["Conversions"].sum()))
        st.metric("Conversion rate", f"{(st.session_state.campaigns['Conversions'].sum()/max(st.session_state.campaigns['Leads'].sum(),1))*100:.1f}%")
    st.plotly_chart(px.bar(st.session_state.campaigns, x="Campaign", y=["Leads","Conversions"], barmode="group", template="plotly_white").update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.55)", font_color="#243b53", margin=dict(l=10,r=10,t=25,b=10)), use_container_width=True)

elif page == "Automation & Tasks":
    st.title("Automation & Tasks")
    st.caption("A lightweight task queue for follow-ups and store operations.")
    edited = st.data_editor(st.session_state.tasks, num_rows="dynamic", use_container_width=True, key="tasks_editor")
    if st.button("Save task updates", type="primary"):
        st.session_state.tasks = edited
        st.success("Task list updated for this session.")
        st.rerun()
    with st.form("add_task", clear_on_submit=True):
        task = st.text_input("Task description")
        owner = st.text_input("Owner", value="Shop Team")
        due = st.date_input("Due date", value=date.today())
        priority = st.selectbox("Priority", ["Low","Medium","High"])
        add_task = st.form_submit_button("Add task")
    if add_task:
        if task.strip():
            st.session_state.tasks.loc[len(st.session_state.tasks)] = [task, owner, due, priority, "Open"]
            st.success("Task added.")
            st.rerun()
        else:
            st.error("Enter a task description.")

elif page == "AI Insights":
    st.title("AI Insights")
    st.caption("Rule-based recommendations generated from the demo dataset. These are not external AI predictions.")
    current_products = st.session_state.products
    current_sales = st.session_state.sales.copy()
    current_sales["Sales (R)"] = current_sales["Qty"] * current_sales["Unit Price (R)"]
    low = current_products[current_products["Stock"] <= current_products["Reorder Level"]]
    top = current_sales.groupby("Product")["Sales (R)"].sum().sort_values(ascending=False)
    st.subheader("Suggested actions")
    if len(low):
        for _, row in low.iterrows():
            st.warning(f"Restock **{row['Product']}**: {int(row['Stock'])} units on hand; reorder level is {int(row['Reorder Level'])}.")
    else:
        st.success("No products currently meet the low-stock rule.")
    if len(top):
        st.info(f"Top demo sales product by revenue: **{top.index[0]}** ({money(top.iloc[0])}). Consider checking availability before promotions.")
    due = st.session_state.customers[st.session_state.customers["Follow-up"].astype(str).str.lower().isin(["due","pending"])]
    st.write(f"Customer follow-ups to review: **{len(due)}**.")

elif page == "Data & Governance":
    st.title("Data & Governance")
    st.caption("Demo data controls and basic operating guidance.")
    st.warning("This prototype uses fictional data and session memory. It is not connected to a POS, payment gateway, CRM, or live shop inventory.")
    st.markdown("""
    **Before production use**
    - Connect approved point-of-sale and inventory data sources.
    - Add authentication and role-based permissions.
    - Store records in a persistent database with backups.
    - Add audit logs for price, stock, customer, and user changes.
    - Define consent and retention rules for customer contact details.
    - Test calculations against actual shop reports.
    """)
    st.subheader("Current dataset sizes")
    a,b,c,d = st.columns(4)
    a.metric("Products", len(st.session_state.products))
    b.metric("Transactions", len(st.session_state.sales))
    c.metric("Customers", len(st.session_state.customers))
    d.metric("Tasks", len(st.session_state.tasks))
    if st.button("Reset demo data"):
        for key in ["products","sales","customers","tasks","campaigns"]:
            del st.session_state[key]
        seed_state()
        st.success("Demo data reset.")
        st.rerun()

elif page == "Growth & Reports":
    st.title("Growth & Reports")
    st.caption("Downloadable snapshots and basic performance comparisons.")
    current_sales = st.session_state.sales.copy()
    current_sales["Sales (R)"] = current_sales["Qty"] * current_sales["Unit Price (R)"]
    a,b,c = st.columns(3)
    a.metric("Total demo revenue", money(current_sales["Sales (R)"].sum()))
    b.metric("Units sold", int(current_sales["Qty"].sum()))
    c.metric("Average transaction", money(current_sales.groupby("Receipt")["Sales (R)"].sum().mean() if len(current_sales) else 0))
    st.subheader("Revenue by product")
    report = current_sales.groupby("Product", as_index=False).agg(Units=("Qty","sum"), Revenue=("Sales (R)","sum")).sort_values("Revenue", ascending=False)
    st.dataframe(report, hide_index=True, use_container_width=True)
    st.download_button("Download sales report CSV", current_sales.to_csv(index=False).encode("utf-8"), "digital_experience_sales_report.csv", "text/csv")
    st.download_button("Download customer list CSV", st.session_state.customers.to_csv(index=False).encode("utf-8"), "digital_experience_customers.csv", "text/csv")

st.sidebar.divider()
st.sidebar.caption("The Digital Experience Shop Console · Demo build")
