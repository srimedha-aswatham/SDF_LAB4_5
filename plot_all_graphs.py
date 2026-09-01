import pandas as pd
import matplotlib.pyplot as plt

def plot_combined(csv_filename, res_label, out_filename, unit="mA", mult=1):
    df = pd.read_csv(csv_filename)
    
    # Forward Bias Data
    fwd = df[df['Bias_Type'] == 'Forward'].copy()
    
    # Reverse Bias Data (Flip signs to plot in the bottom-left quadrant)
    rev = df[df['Bias_Type'] == 'Reverse'].copy()
    rev['V_diode'] = -rev['V_diode']
    rev['I_mA'] = -rev['I_mA']
    
    # Merge them for the continuous plot
    full_df = pd.concat([rev, fwd])
    
    plt.figure(figsize=(9, 6))
    
    # Draw central axis lines crossing at (0,0)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    plt.plot(full_df['V_diode'], full_df['I_mA'] * mult, marker='o', linestyle='-', color='#1f77b4', linewidth=1.5, markersize=3)
    
    plt.title(fr'1N4007 Diode Full I-V Curve (R = {res_label})', fontsize=14)
    plt.xlabel('Diode Voltage $V_D$ (V)', fontsize=12)
    plt.ylabel(fr'Diode Current $I_D$ ({unit})', fontsize=12)
    
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig(out_filename, dpi=300, bbox_inches='tight')
    print(f"Saved: {out_filename}")
    plt.close()

def plot_separate_100_ohm():
    df = pd.read_csv('diode_100_ohms.csv')
    fwd = df[df['Bias_Type'] == 'Forward']
    rev = df[df['Bias_Type'] == 'Reverse']
    
    # 1. Separate Forward Plot
    plt.figure(figsize=(8, 6))
    plt.plot(fwd['V_diode'], fwd['I_mA'], marker='o', color='#1f77b4', linewidth=1.5, markersize=3)
    plt.title(r'1N4007 Diode: Forward Bias (R = 100 $\Omega$)', fontsize=14)
    plt.xlabel('Forward Voltage $V_D$ (V)', fontsize=12)
    plt.ylabel('Forward Current $I_D$ (mA)', fontsize=12)
    plt.grid(True, linestyle='--')
    plt.savefig('separate_forward_100ohm.png', dpi=300, bbox_inches='tight')
    print("Saved: separate_forward_100ohm.png")
    plt.close()

    # 2. Separate Reverse Plot (Magnitudes only for standard reverse viewing)
    plt.figure(figsize=(8, 6))
    plt.plot(rev['V_diode'], rev['I_mA'] * 1000, marker='s', color='#d62728', linewidth=1.5, markersize=4)
    plt.title(r'1N4007 Diode: Reverse Bias (R = 100 $\Omega$)', fontsize=14)
    plt.xlabel('Reverse Voltage $V_R$ (V)', fontsize=12)
    plt.ylabel(r'Reverse Current $I_R$ ($\mu$A)', fontsize=12)
    plt.grid(True, linestyle='--')
    plt.savefig('separate_reverse_100ohm.png', dpi=300, bbox_inches='tight')
    print("Saved: separate_reverse_100ohm.png")
    plt.close()

# --- Execution ---
print("Generating Plots...")
plot_separate_100_ohm()
plot_combined('diode_100_ohms.csv', r'100 $\Omega$', 'combined_100ohm.png')
plot_combined('diode_1k_ohms.csv', r'1 k$\Omega$', 'combined_1kohm.png')

# Note: Multiplying current by 1000 for the 100k plot so it displays in uA, 
# otherwise the values are too small to see a good curve.
plot_combined('diode_100k_ohms.csv', r'100 k$\Omega$', 'combined_100kohm.png', unit=r"$\mu$A", mult=1000)

print("Done!")