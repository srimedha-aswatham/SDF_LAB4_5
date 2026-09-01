import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('solar_cell_final.csv')
df = df.sort_values(by='V_cell (V)')

# 2. Set up the plot
fig, ax = plt.subplots(figsize=(9, 6))

# Plot the combined continuous line
ax.plot(df['V_cell (V)'], df['I_c (mA)'], color='black', linewidth=1.5)

# 3. Format axes to cross at zero (textbook style)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Add breathing room around the edges
ax.set_xlim(-1.1, 0.7)
ax.set_ylim(-35, 5)

# Add arrow heads to axes
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Custom tick marks (removing 0 to avoid clutter at the origin)
ax.set_xticks([-1.0, -0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6])
ax.set_yticks([-30, -25, -20, -15, -10, -5])

# Manually place axis labels to prevent overlap with numbers
ax.text(0.72, -1.5, 'V (Volts)', fontsize=12, fontweight='bold', va='center')
ax.text(-0.06, 5.5, 'I (mA)', fontsize=12, fontweight='bold', ha='center')

# 4. Annotate Voc and Isc clearly with pointing arrows
# Annotate Voc
ax.annotate('Voc (Open circuit voltage)', 
            xy=(0.52, 0), xytext=(0.15, 2.5), 
            fontsize=11, arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

# Annotate Isc
ax.annotate('Isc (Short circuit current)', 
            xy=(0, -28.63), xytext=(0.08, -32), 
            fontsize=11, arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

# Add dots on the intercepts
ax.plot([0.52], [0], marker='o', markersize=6, color="black")
ax.plot([0], [-28.63], marker='o', markersize=6, color="black")

# 5. Save the plot
plt.tight_layout()
plt.savefig('textbook_iv_curve_formatted.png', dpi=300)
print("Graph generated! Look for 'textbook_iv_curve_formatted.png' in your folder.")