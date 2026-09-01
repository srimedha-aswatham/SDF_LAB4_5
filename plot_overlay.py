import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Experimental Data (Using your raw data EXACTLY as it is)
df_exp = pd.read_csv('buffer_data.csv')

# 2. Load the updated LTspice Simulated Data (4th Quadrant)
df_sim = pd.read_csv('ltspice_expected.csv')

# 3. Create the Overlay Plot
plt.figure(figsize=(10, 7))

# Draw zero-crossing axes just like the textbook
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Plot LTspice Simulation (Smooth dashed orange line)
plt.plot(df_sim['V_cell'], df_sim['I_mA'], 
         linestyle='--', color='#ff7f0e', linewidth=2.5, 
         label='LTspice Simulated (Ideal Buffer)')

# Plot Experimental Data (Solid blue dots, no connecting lines)
plt.plot(df_exp['V_cell (V)'], df_exp['I_c (mA)'], 
         marker='o', linestyle='none', color='#1f77b4', 
         markersize=5, label='Experimental Data')

# Formatting
plt.title('Solar Cell Light I-V: Experimental vs. Simulated', fontsize=14)
plt.xlabel('Cell Voltage $V$ (Volts)', fontsize=12)
plt.ylabel('Current $I$ (mA)', fontsize=12)

plt.grid(True, which='both', linestyle=':', linewidth=0.7)

# Focus the axes to match the textbook framing
plt.xlim(-1.1, 0.7)
plt.ylim(-35, 60) 

# Add annotations to match textbook style
plt.annotate('Voc', xy=(0.52, 0), xytext=(0.35, 10),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))
plt.annotate('Isc', xy=(0, -26.08), xytext=(0.1, -30),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))

plt.legend(loc='upper left', fontsize=11)

# Save the final image
plt.savefig('overlay_graph_corrected.png', dpi=300, bbox_inches='tight')
print("Saved: overlay_graph_corrected.png")
plt.close()