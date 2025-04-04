import pandas as pd
import plotly.express as px

from preswald import connect, get_df, plotly, text

text("# Supermarket Sales Analytics Dashboard")
text("Explore product performance and customer purchasing patterns")
df = get_df("Supermk")
print(df)
from preswald import query

connect()
sql = "SELECT * FROM Supermk WHERE Quantity > 5"
filtered_df = query(sql, "Supermk")

from preswald import text, table
text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

from preswald import slider

threshold = slider("Threshold", min_val=0, max_val=40, default=10)
table(df[df["Quantity"] > threshold], title="Dynamic Data View")

from preswald import plotly
import plotly.express as px
fig_scatter = px.scatter(
    df[df["Quantity"] > threshold],  
    x="Quantity",
    y="Total",
    color="Blue", 
    title="Quantity vs Total",
    labels={"Quantity": "Quantity", "Total": "Total"}
)
plotly(fig_scatter)

from preswald import plotly
import plotly.express as px
fig_bar = px.bar(
    df[df["Quantity"] > threshold],
    x="Category",  # Replace with a categorical column
    y="Total",
    title="Total by Category",
    labels={"Category": "Category", "Total": "Total"}
)
plotly(fig_bar)



