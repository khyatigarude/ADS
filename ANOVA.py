import pandas as pd

import pandas as pd
data = {
    'Sum of N2O': [10,12,16,22],
    'Sum of CO2': [337268,363181,368024,407032],
    'Sum of CH4': [12045,12971,13204,14860]
}


df = pd.DataFrame(data)

overall_mean = df.values.mean()
group_means = df.mean()
n_obs_per_group = df.count()
SS_between = ((group_means - overall_mean)**2 * n_obs_per_group).sum()
print("SS Between:", SS_between)

SS_within = ((df.sub(group_means, axis=1))**2).sum().sum()
print("SS Within:", SS_within)

SS_total = SS_between + SS_within
print("SS TOTAL:", SS_total)

k = len(df.columns)
N = df.size
df_between = k - 1
df_within = N - k

print("\nDegrees of Freedom (Between):", df_between)
print("\nDegrees of Freedom (Within):", df_within)

MS_between = SS_between / df_between
MS_within = SS_within / df_within

print("\nMS Between:", MS_between)
print("\nMS Within:", MS_within)

F_ratio = MS_between / MS_within

def get_tabulated_F(df_numerator, df_denominator):
    try:
        return f_table.loc[str(df_denominator), str(df_numerator)]
    except KeyError:
        print("Degrees of freedom combination not found in the table.")
        return None

df_numerator = df_between  # Degrees of freedom (between-groups)
df_denominator = df_within  # Degrees of freedom (within-groups)

tabulated_F_value = get_tabulated_F(df_numerator, df_denominator)
print("\nCalculated F-ratio:", F_ratio)
print("\nTabulated F-Ratio is",tabulated_F_value)
if tabulated_F_value is not None:
    if F_ratio > tabulated_F_value:
        print("\nReject null hypothesis")
    else:
        print("\nFail to reject null hypothesis")