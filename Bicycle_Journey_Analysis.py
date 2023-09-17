import pandas as pd

cumulative_miles = [55, 120, 180, 240, 310, 370, 435]

cumulative_series = pd.Series(cumulative_miles, name="Cumulative Miles")

daily_miles = cumulative_series.diff().fillna(cumulative_series)

df_miles = pd.DataFrame({
    'Day': range(1, len(daily_miles) + 1),
    'Cumulative Miles': cumulative_series,
    'Daily Miles': daily_miles.astype(int)  # Convert to integer for neatness
})

print(df_miles)
