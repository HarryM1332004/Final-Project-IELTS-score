import pandas as pd
from scipy.stats import pearsonr


file_path = "./Data.xlsx"
df = pd.read_excel(file_path)


mapping = {"FREE": 2, "PARTLY FREE": 1, "NOT FREE": 0}
if df['Freedoms'].dtype == object:
    df['Freedom'] = df['Freedoms'].map(mapping)
else:
    df['Freedom'] = df['Free nums']


df_corr = df[['Overall', 'Total', 'Freedom']].dropna()


results = []
variables = ['Overall', 'Total', 'Freedom']
for i in range(len(variables)):
    for j in range(i + 1, len(variables)):
        var1, var2 = variables[i], variables[j]
        r, p = pearsonr(df_corr[var1], df_corr[var2])
        n = len(df_corr)
        t = r * ((n - 2) ** 0.5) / ((1 - r ** 2) ** 0.5)
        significance = "Yes" if p < 0.05 else "No"
        results.append({
            'Variable 1': var1,
            'Variable 2': var2,
            'R-value': round(r, 4),
            'T-value': round(t, 4),
            'P-value': round(p, 6),
            'Significant (p<0.05)': significance
        })

results_df = pd.DataFrame(results)


print("Correlation Analysis: Overall, Total, Freedom")
print(results_df.to_string(index=False))