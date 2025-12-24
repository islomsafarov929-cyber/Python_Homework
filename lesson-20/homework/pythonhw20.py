# Homework 1:

# Using chinook.db write pandas code.

# Task 1. Customer Purchases Analysis:
# Find the total amount spent by each customer on purchases (considering invoices).
# Identify the top 5 customers with the highest total purchase amounts.
# Display the customer ID, name, and the total amount spent for the top 5 customers.
import pandas as pd
import sqlite3

with sqlite3.connect("Data/chinook.db") as conn:
    customers = pd.read_sql_query(
        "SELECT CustomerId, FirstName, LastName FROM customers",
        conn,
        index_col="CustomerId"
    )

    invoices = pd.read_sql_query(
        "SELECT CustomerId, Total FROM invoices",
        conn
    ).groupby("CustomerId", as_index=True)["Total"].sum().to_frame("Total_spent")

combined = (
    customers
    .join(invoices, how="inner")
    .sort_values(by="Total_spent", ascending=False)
)

print(combined.head(5))


# Task 2.Album vs. Individual Track Purchases:
# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
import pandas as pd
import sqlite3

# -------------------------------
# Load data
# -------------------------------
with sqlite3.connect("Data/chinook.db") as conn:
    tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM tracks", conn)
    invoice_items = pd.read_sql_query("SELECT InvoiceId, TrackId FROM invoice_items", conn)
    invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM invoices", conn)

# -------------------------------
# Total tracks per album
# -------------------------------
album_track_counts = (
    tracks.groupby("AlbumId")["TrackId"]
    .count()
    .reset_index(name="TotalAlbumTracks")
)

# -------------------------------
# Tracks purchased per album per invoice
# -------------------------------
invoice_album_tracks = (
    invoice_items
    .merge(tracks, on="TrackId")
    .groupby(["InvoiceId", "AlbumId"])["TrackId"]
    .count()
    .reset_index(name="TracksBought")
)

# -------------------------------
# Compare bought vs total
# -------------------------------
invoice_album_tracks = invoice_album_tracks.merge(
    album_track_counts, on="AlbumId"
)

invoice_album_tracks["IsFullAlbum"] = (
    invoice_album_tracks["TracksBought"] == invoice_album_tracks["TotalAlbumTracks"]
)

# -------------------------------
# Attach customers
# -------------------------------
invoice_album_tracks = invoice_album_tracks.merge(
    invoices, on="InvoiceId"
)

# -------------------------------
# CUSTOMER-LEVEL classification
# -------------------------------
customer_summary = (
    invoice_album_tracks
    .groupby("CustomerId")
    .agg(
        bought_full_album=("IsFullAlbum", "any"),
        bought_partial_album=("IsFullAlbum", lambda x: (~x).any())
    )
    .reset_index()
)

def classify_customer(row):
    if row["bought_full_album"] and not row["bought_partial_album"]:
        return "Full Albums"
    else:
        return "Individual Tracks"

customer_summary["Preference"] = customer_summary.apply(
    classify_customer, axis=1
)

# -------------------------------
# Final percentage summary
# -------------------------------
summary = (
    customer_summary["Preference"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
    .reset_index()
)

summary.columns = ["Category", "Percentage"]

print(summary)
