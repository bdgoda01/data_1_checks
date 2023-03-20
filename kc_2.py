import pandas as pd
import matplotlib.pyplot as plt

#yearly music video views for Gangnam Style by PSY
views_df = pd.read_csv("assets/YearlyViews.csv")

print("Line graph: ")
plt.plot(views_df["Year"], views_df["Approx. Total Views"])
plt.title("Total Views by Year for Gangname Stlye by PSY")
plt.xlabel("Year")
plt.ylabel("Total Views (billions)")
plt.show()