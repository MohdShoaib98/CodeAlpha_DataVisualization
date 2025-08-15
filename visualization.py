import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_excel("screentime.xlsx")
df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])

VISUALS_DIR = "visuals"
os.makedirs(VISUALS_DIR, exist_ok=True)

plt.figure(figsize=(8, 5))
sns.barplot(x="Age", y="Avg_Daily_Screen_Time_hr", data=df, palette="viridis", ci=None)
plt.title("Average Screen Time by Age")
plt.xlabel("Age")
plt.ylabel("Screen Time (hours)")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "avg_screen_time_by_age.png"))
plt.show()

device_counts = df["Primary_Device"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(device_counts, labels=device_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Primary Device Distribution")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "primary_device_distribution.png"))
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(x="Gender", y="Avg_Daily_Screen_Time_hr", data=df, palette="Set2")
plt.title("Screen Time by Gender")
plt.xlabel("Gender")
plt.ylabel("Screen Time (hours)")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "screen_time_by_gender.png"))
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(x="Urban_or_Rural", y="Avg_Daily_Screen_Time_hr", data=df, palette="coolwarm", ci=None)
plt.title("Screen Time by Urban vs Rural Kids")
plt.xlabel("Location")
plt.ylabel("Screen Time (hours)")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "screen_time_by_location.png"))
plt.show()

health_limit_counts = df.groupby(["Exceeded_Recommended_Limit", "Health_Impacts"]).size().unstack(fill_value=0)
health_limit_counts.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="tab20")
plt.title("Health Impacts vs Exceeded Screen Time Limit")
plt.xlabel("Exceeded Recommended Limit")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "health_impacts_vs_limit.png"))
plt.show()

bins = [0, 0.3, 0.6, 1.0]
labels = ["Low", "Medium", "High"]
df["Edu_Rec_Category"] = pd.cut(df["Educational_to_Recreational_Ratio"], bins=bins, labels=labels, include_lowest=True)

plt.figure(figsize=(7, 5))
sns.countplot(x="Edu_Rec_Category", data=df, palette="pastel")
plt.title("Educational-to-Recreational Ratio Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(VISUALS_DIR, "edu_rec_ratio_categories.png"))
plt.show()

print(f"✅ All charts saved in '{VISUALS_DIR}' directory.")
