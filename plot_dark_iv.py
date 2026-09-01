import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('dark_iv_data.csv')

# Split the data
fwd = df[df['Bias_Type'] == 'Forward'].copy()
rev = df[df['Bias_Type'] == 'Reverse'].copy()

# ==========================================
# PLOT 1: Forward Bias (Neat Turn-on Curve)
# ==========================================
plt.figure(figsize=(8, 6))
plt.plot(fwd['V_cell'], fwd['I_mA'], marker='o', color='#1f77b4', linewidth=1.5, markersize=4)

plt.title('Solar Cell Dark I-V: Forward Bias', fontsize=14)
plt.xlabel('Cell Voltage $V_{cell}$ (V)', fontsize=12)
plt.ylabel('Forward Current $I$ (mA)', fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlim(0, 0.65)
plt.ylim(0, 50)

plt.savefig('dark_iv_forward.png', dpi=300, bbox_inches='tight')
print("Saved: dark_iv_forward.png")
plt.close()

# ==========================================
# PLOT 2: Reverse Bias (Tightly spaced for clarity)
# ==========================================
plt.figure(figsize=(8, 6))
# Plotting magnitudes so it's easy to read in the report
plt.plot(rev['V_cell'], rev['I_mA'], marker='s', color='#d62728', linewidth=1.5, markersize=4)

plt.title('Solar Cell Dark I-V: Reverse Bias Leakage', fontsize=14)
plt.xlabel('Reverse Voltage $V_R$ (V)', fontsize=12)
plt.ylabel('Reverse Leakage Current $I_R$ (mA)', fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# Tight axis limits to show the curve cleanly
plt.xlim(0, 9)
plt.ylim(0, 16)

plt.savefig('dark_iv_reverse.png', dpi=300, bbox_inches='tight')
print("Saved: dark_iv_reverse.png")
plt.close()

# ==========================================
# PLOT 3: Combined Full I-V Curve (FIXED)
# ==========================================
# For the full curve, reverse voltage and current must be negative (3rd quadrant)
rev_full = rev.copy()
rev_full['V_cell'] = -rev_full['V_cell']
rev_full['I_mA'] = -rev_full['I_mA']

# Combine the data
full_df = pd.concat([rev_full, fwd])

# THE FIX: Sort the data by voltage from lowest (-8.5V) to highest (+0.6V)
# so matplotlib connects the dots strictly from left to right.
full_df = full_df.sort_values(by='V_cell')

plt.figure(figsize=(9, 6))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.plot(full_df['V_cell'], full_df['I_mA'], marker='^', linestyle='-', color='#2ca02c', linewidth=1.5, markersize=4)

plt.title('Solar Cell Full Dark I-V Characteristics', fontsize=14)
plt.xlabel('Cell Voltage $V_{cell}$ (V)', fontsize=12)
plt.ylabel('Cell Current $I$ (mA)', fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.savefig('dark_iv_combined.png', dpi=300, bbox_inches='tight')
print("Saved: dark_iv_combined.png")
plt.close()
