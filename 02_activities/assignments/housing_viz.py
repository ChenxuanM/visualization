import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# CONFIGURATION - Paths
# ============================================================================

# OPTION 1: If CSV is in the SAME folder as this Python file (RECOMMENDED)
DATA_PATH = 'Social_and_Affordable_Housing.csv'

# OPTION 2: If CSV is somewhere else, use full path (uncomment and modify):
# DATA_PATH = '/Users/chenxuan/Desktop/Data Project/visualization/02_activities/assignments/Social_and_Affordable_Housing.csv'

# Output files will be saved in the same folder as this script
OUTPUT_SVG = 'housing_trends.svg'
OUTPUT_PNG = 'housing_trends.png'

# ============================================================================
# VISUALIZATION SETTINGS
# ============================================================================

plt.rcParams['svg.fonttype'] = 'none'  # Keep text editable in Illustrator
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.5

# Colors
SUBSIDIZED_COLOR = '#E74C3C'  # Red for declining trend
AFFORDABLE_COLOR = '#27AE60'  # Green for growing trend

# ============================================================================
# DATA LOADING AND CLEANING
# ============================================================================

print("="*70)
print("Toronto Housing Trends Visualization")
print("="*70)
print(f"\nLoading data from: {DATA_PATH}")

try:
    df = pd.read_csv(DATA_PATH)
    print(f"✓ Successfully loaded {len(df)} quarters of data")
except FileNotFoundError:
    print("\n❌ ERROR: Cannot find CSV file!")
    print(f"\nLooked for file at: {DATA_PATH}")
    print("\nPlease make sure:")
    print("  1. The CSV file is in the same folder as this Python file")
    print("  2. Or update DATA_PATH with the correct location")
    print("\nYour current folder structure should be:")
    print("  assignments/")
    print("    ├── housing_viz.py (this file)")
    print("    └── Social_and_Affordable_Housing.csv")
    exit()

# Clean data: remove commas and convert to numeric
df['Subsidized Housing Units'] = df['Subsidized Housing Units'].replace(' n/a ', np.nan)
df['Subsidized Housing Units'] = df['Subsidized Housing Units'].astype(str).str.replace(',', '').str.strip()
df['Affordable Housing Units'] = df['Affordable Housing Units'].astype(str).str.replace(',', '').str.strip()

df['Subsidized Housing Units'] = pd.to_numeric(df['Subsidized Housing Units'], errors='coerce')
df['Affordable Housing Units'] = pd.to_numeric(df['Affordable Housing Units'], errors='coerce')

# ============================================================================
# CREATE VISUALIZATION
# ============================================================================

print("\nCreating visualization...")

fig, ax1 = plt.subplots(figsize=(14, 8))

# Prepare data
quarters = df['Quarter'].tolist()
subsidized = df['Subsidized Housing Units'].tolist()
affordable = df['Affordable Housing Units'].tolist()
x_pos = range(len(quarters))

# LEFT AXIS: Subsidized Housing (red line)
line1 = ax1.plot(x_pos[4:], subsidized[4:],  # Start from Q1 2021
                 color=SUBSIDIZED_COLOR, linewidth=3, marker='o', markersize=8,
                 label='Subsidized Housing Units', zorder=3)

ax1.set_xlabel('Quarter', fontsize=14, fontweight='bold', color='#2C3E50')
ax1.set_ylabel('Subsidized Housing Units', fontsize=14, fontweight='bold', 
               color=SUBSIDIZED_COLOR)
ax1.tick_params(axis='y', labelcolor=SUBSIDIZED_COLOR, labelsize=11)
ax1.set_xticks(x_pos[::2])
ax1.set_xticklabels([quarters[i] for i in range(0, len(quarters), 2)], 
                     rotation=45, ha='right', fontsize=10)

# RIGHT AXIS: Affordable Housing (green line)
ax2 = ax1.twinx()
line2 = ax2.plot(x_pos, affordable,
                 color=AFFORDABLE_COLOR, linewidth=3, marker='s', markersize=8,
                 label='Affordable Housing Units', zorder=3)

ax2.set_ylabel('Affordable Housing Units', fontsize=14, fontweight='bold', 
               color=AFFORDABLE_COLOR)
ax2.tick_params(axis='y', labelcolor=AFFORDABLE_COLOR, labelsize=11)

# Title
ax1.set_title('Toronto Housing Shift: From Subsidized to Affordable\nQuarterly Data (2020-2025)',
             fontsize=16, fontweight='bold', color='#2C3E50', pad=20)

# Grid
ax1.grid(True, alpha=0.3, linestyle='--', zorder=0)

# Legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=12, frameon=True, shadow=True)

# Start and End Value Annotations
ax1.annotate(f'{subsidized[4]:,.0f}', 
            xy=(4, subsidized[4]), xytext=(4, subsidized[4]+2000),
            fontsize=10, fontweight='bold', color=SUBSIDIZED_COLOR,
            ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                                   edgecolor=SUBSIDIZED_COLOR))

ax1.annotate(f'{subsidized[-1]:,.0f}', 
            xy=(len(quarters)-1, subsidized[-1]), 
            xytext=(len(quarters)-1, subsidized[-1]-2000),
            fontsize=10, fontweight='bold', color=SUBSIDIZED_COLOR,
            ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                                   edgecolor=SUBSIDIZED_COLOR))

ax2.annotate(f'{affordable[0]:,.0f}', 
            xy=(0, affordable[0]), xytext=(0, affordable[0]-500),
            fontsize=10, fontweight='bold', color=AFFORDABLE_COLOR,
            ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                                   edgecolor=AFFORDABLE_COLOR))

ax2.annotate(f'{affordable[-1]:,.0f}', 
            xy=(len(quarters)-1, affordable[-1]), 
            xytext=(len(quarters)-1, affordable[-1]+500),
            fontsize=10, fontweight='bold', color=AFFORDABLE_COLOR,
            ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                                   edgecolor=AFFORDABLE_COLOR))

# Trend labels
mid_point = len(quarters) // 2
ax1.annotate('↓ Decreasing\n-1.3%', 
            xy=(mid_point+2, 84000), fontsize=12, fontweight='bold',
            color=SUBSIDIZED_COLOR, ha='center',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='white', 
                     edgecolor=SUBSIDIZED_COLOR, linewidth=2, alpha=0.9))

ax2.annotate('↑ Increasing\n+76.9%', 
            xy=(mid_point-2, 8000), fontsize=12, fontweight='bold',
            color=AFFORDABLE_COLOR, ha='center',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='white', 
                     edgecolor=AFFORDABLE_COLOR, linewidth=2, alpha=0.9))

# Data source
fig.text(0.5, 0.02,
         'Data Source: City of Toronto Open Data - Social and Affordable Housing\n'
         'Shows policy shift from subsidized social housing to affordable housing model (2020-2025)',
         ha='center', fontsize=9, style='italic', color='#7F8C8D')

plt.tight_layout(rect=[0, 0.05, 1, 1])

# ============================================================================
# SAVE FILES
# ============================================================================

print(f"\nSaving files...")

try:
    fig.savefig(OUTPUT_SVG, format='svg', dpi=300, bbox_inches='tight')
    fig.savefig(OUTPUT_PNG, format='png', dpi=300, bbox_inches='tight', facecolor='white')
    
    print(f"✓ {OUTPUT_SVG} created (open in Illustrator)")
    print(f"✓ {OUTPUT_PNG} created (final image)")
    
except Exception as e:
    print(f"\n❌ Error saving files: {e}")

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

print("\n" + "="*70)
print("DATA SUMMARY")
print("="*70)

print(f"\n Subsidized Housing:")
print(f"  Start (2021 Q1): {subsidized[4]:>8,.0f} units")
print(f"  End (2025 Q2):   {subsidized[-1]:>8,.0f} units")
change_sub = subsidized[-1] - subsidized[4]
pct_sub = (change_sub / subsidized[4]) * 100
print(f"  Change:          {change_sub:>8,.0f} units ({pct_sub:+.1f}%)")

print(f"\n Affordable Housing:")
print(f"  Start (2020 Q1): {affordable[0]:>8,.0f} units")
print(f"  End (2025 Q2):   {affordable[-1]:>8,.0f} units")
change_aff = affordable[-1] - affordable[0]
pct_aff = (change_aff / affordable[0]) * 100
print(f"  Change:          {change_aff:>8,.0f} units ({pct_aff:+.1f}%)")

print("\n Key Finding:")
print("   Toronto is shifting from subsidized social housing to")
print("   affordable housing partnerships - a fundamental policy change.")

print("\n" + "="*70)
print("DONE! Check your files:")
print(f"   - {OUTPUT_SVG}")
print(f"   - {OUTPUT_PNG}")
print("="*70)




