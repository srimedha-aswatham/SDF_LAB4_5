import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('buffer_data.csv')
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

# Add breathing room around the edges (expanded for buffer data)
ax.set_xlim(-1.2, 0.8)
ax.set_ylim(-35, 55)

# Add arrow heads to axes
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Custom tick marks (removing 0 to avoid clutter)
ax.set_xticks([-1.0, -0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6])
ax.set_yticks([-30, -20, -10, 10, 20, 30, 40, 50])

# Manually place axis labels
ax.text(0.85, -2.5, 'V (Volts)', fontsize=12, fontweight='bold', va='center')
ax.text(-0.08, 58, 'I (mA)', fontsize=12, fontweight='bold', ha='center')

# 4. Annotate Voc and Isc clearly with pointing arrows
# Voc is approximately 0.52V based on the data
ax.annotate('Voc ≈ 0.52V', 
            xy=(0.52, 0), xytext=(0.2, 15), 
            fontsize=11, arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

# Isc is approximately -25mA based on the interpolation near V=0
ax.annotate('Isc ≈ -25.2mA', 
            xy=(0, -25.2), xytext=(0.1, -30), 
            fontsize=11, arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

# Add dots on the intercepts
ax.plot([0.52], [0], marker='o', markersize=6, color="black")
ax.plot([0], [-25.2], marker='o', markersize=6, color="black")

# 5. Save the plot (Fixes the FigureCanvasAgg error!)
plt.tight_layout()
plt.savefig('buffer_iv_curve_formatted.png', dpi=300)
print("Graph generated! Look for 'buffer_iv_curve_formatted.png' in your folder.")