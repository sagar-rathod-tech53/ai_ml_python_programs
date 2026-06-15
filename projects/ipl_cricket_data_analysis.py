import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ipl_data.csv')

print("IPL Dataset")

print(df)

player_runs = df.groupby("Player")['Run'].sum()

player_wickets = df.groupby("Player")["Wickets"].sum()

team_runs = df.groupby("Team")["Run"].sum()

average_runs = np.mean(df["Run"])

max_runs = np.max(df["Run"])

print("\nAverage Runs: ",average_runs)
print("Highest Runs: ",max_runs)
print("Run by player")
print(player_runs)

print("Wickets by player")
print(player_wickets)


# plt.figure(figsize=(8,5))
# sns.barplot(
#     x=player_runs.index,
#     y=player_runs.values,
#     palette="Blues"
# )

# plt.title("Total runs by player")
# plt.xticks(rotation=45)
# plt.show()

# plt.figure(figsize=(8,5))
# sns.barplot(
#     x=player_wickets.index,
#     y=player_wickets.values,
#     palette="Reds"
# )

# plt.title("Total wickets by player")
# plt.xticks(rotation=45)
# plt.show()

# plt.figure(figsize=(8,5))
# sns.barplot(
#     x=team_runs.index,
#     y=team_runs.values,
#     palette="viridis"
# )

# plt.title("Team-wise Total Runs")
# # plt.xticks(rotation=45)
# plt.show()


plt.figure(figsize=(6,4))
sns.heatmap(
    df[["Run", "Wickets"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Run",
    y="Wickets",
    hue="Team",
    s=100
)
plt.title("Runs vs Wickets")
plt.show()