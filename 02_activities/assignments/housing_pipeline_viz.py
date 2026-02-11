import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

# ============================================================================
# CONFIGURATION
# ============================================================================

DATA_PATH = 'Affordable_Rental_Housing_Pipeline_-_4326.csv'
OUTPUT_MAP_SVG = 'housing_map.svg'
OUTPUT_MAP_PNG = 'housing_map.png'
OUTPUT_WARD_SVG = 'housing_by_ward.svg'
OUTPUT_WARD_PNG = 'housing_by_ward.png'

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.5

# ============================================================================
# LOAD AND CLEAN DATA
# ============================================================================

print("="*70)
print("Toronto Affordable Housing - Geographic Visualization")
print("="*70)
print(f"\nLoading data from: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)
print(f"✓ Loaded {len(df)} projects")

# Extract coordinates from geometry JSON
def extract_coords(geo_str):
    try:
        geo = json.loads(geo_str)
        coords = geo['coordinates'][0]
        return coords[0], coords[1]  # longitude, latitude
    except:
        return None, None

df['longitude'], df['latitude'] = zip(*df['geometry'].apply(extract_coords))
df = df.dropna(subset=['longitude', 'latitude'])

print(f"✓ Extracted coordinates for {len(df)} projects")

# Simplify status names
status_map = {
    'Approved OPAs and Zoning By-Law Amendments': 'Approved',
    'Planning Applications Under Review': 'Under Review',
    'Started Construction': 'Construction',
    'Occupied': 'Occupied',
    'Pre-Planning': 'Pre-Planning',
    'Building Permit Application': 'Permit Stage',
    'Approved Site Plan Application': 'Permit Stage',
    'Issued Building Permit': 'Permit Stage'
}

df['Status_Simple'] = df['Status'].map(status_map)

# ============================================================================
# VISUALIZATION 1: Geographic Map with Project Locations
# ============================================================================

print("\nCreating geographic map...")

fig1, ax1 = plt.subplots(figsize=(14, 12))

# Define colors for each status
status_colors = {
    'Pre-Planning': '#E74C3C',      # Red
    'Under Review': '#E67E22',      # Orange
    'Approved': '#F39C12',          # Yellow-orange
    'Permit Stage': '#F1C40F',      # Yellow
    'Construction': '#2ECC71',      # Green
    'Occupied': '#27AE60'           # Dark green
}

# Plot each status separately for legend
for status in ['Pre-Planning', 'Under Review', 'Approved', 'Permit Stage', 'Construction', 'Occupied']:
    status_df = df[df['Status_Simple'] == status]
    if len(status_df) > 0:
        scatter = ax1.scatter(status_df['longitude'], status_df['latitude'],
                            s=status_df['Affordable Homes Approved'] * 2,  # Size by homes
                            c=status_colors[status],
                            alpha=0.6,
                            edgecolors='black',
                            linewidth=0.5,
                            label=f"{status} ({len(status_df)} projects)")

# Titles and labels
ax1.set_xlabel('Longitude', fontsize=12, fontweight='bold')
ax1.set_ylabel('Latitude', fontsize=12, fontweight='bold')
ax1.set_title('Toronto Affordable Housing Projects by Location\nSize = Number of Homes, Color = Project Stage',
             fontsize=14, fontweight='bold', color='#2C3E50', pad=15)

# Legend
ax1.legend(loc='upper left', fontsize=9, frameon=True, shadow=True, title='Project Status')

# Grid
ax1.grid(True, alpha=0.3, linestyle='--')

# Add note about interpreting the map
fig1.text(0.5, 0.02,
         'Data Source: City of Toronto Open Data - Affordable Rental Housing Pipeline\n'
         'Each dot represents a project. Larger dots = more housing units. Colors show development stage.',
         ha='center', fontsize=8, style='italic', color='#7F8C8D')

plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save
fig1.savefig(OUTPUT_MAP_SVG, format='svg', dpi=300, bbox_inches='tight')
fig1.savefig(OUTPUT_MAP_PNG, format='png', dpi=300, bbox_inches='tight', facecolor='white')
print(f"✓ Saved: {OUTPUT_MAP_PNG}")

# ============================================================================
# VISUALIZATION 2: Stacked Bar Chart by Ward and Status
# ============================================================================

print("\nCreating ward comparison chart...")

# Aggregate by Ward and Status
ward_status = df.groupby(['Ward Name', 'Status_Simple'])['Affordable Homes Approved'].sum().unstack(fill_value=0)

# Select TOP 10 wards by total homes
top_wards = df.groupby('Ward Name')['Affordable Homes Approved'].sum().nlargest(10).index
ward_status_top = ward_status.loc[top_wards]

# Order columns by pipeline stage
column_order = ['Pre-Planning', 'Under Review', 'Approved', 'Permit Stage', 'Construction', 'Occupied']
ward_status_top = ward_status_top[[col for col in column_order if col in ward_status_top.columns]]

# Create stacked bar chart
fig2, ax2 = plt.subplots(figsize=(14, 8))

ward_status_top.plot(kind='barh', stacked=True, ax=ax2,
                     color=[status_colors[col] for col in ward_status_top.columns],
                     edgecolor='black', linewidth=0.5)

ax2.set_xlabel('Number of Affordable Homes', fontsize=13, fontweight='bold')
ax2.set_ylabel('Ward', fontsize=13, fontweight='bold')
ax2.set_title('TOP 10 Toronto Wards by Affordable Housing\nBreakdown by Development Stage',
             fontsize=15, fontweight='bold', color='#2C3E50', pad=15)

# Format x-axis
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000)}K' if x >= 1000 else str(int(x))))

# Legend
ax2.legend(title='Project Stage', fontsize=10, loc='lower right', frameon=True, shadow=True)

# Grid
ax2.grid(axis='x', alpha=0.3, linestyle='--')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig2.text(0.5, 0.02,
         'Data Source: City of Toronto Open Data - Affordable Rental Housing Pipeline\n'
         'Shows distribution of housing projects across development stages for top 10 wards',
         ha='center', fontsize=8, style='italic', color='#7F8C8D')

plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save
fig2.savefig(OUTPUT_WARD_SVG, format='svg', dpi=300, bbox_inches='tight')
fig2.savefig(OUTPUT_WARD_PNG, format='png', dpi=300, bbox_inches='tight', facecolor='white')
print(f"✓ Saved: {OUTPUT_WARD_PNG}")

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

print("\n" + "="*70)
print("DATA SUMMARY")
print("="*70)

print("\n TOP 5 Wards by Total Housing:")
top5_wards = df.groupby('Ward Name')['Affordable Homes Approved'].sum().nlargest(5)
for i, (ward, homes) in enumerate(top5_wards.items(), 1):
    projects = len(df[df['Ward Name'] == ward])
    print(f"  {i}. {ward:30s}: {int(homes):5,} homes ({projects:3d} projects)")

print("\n Projects by Stage:")
stage_summary = df.groupby('Status_Simple').agg({
    'Project ID': 'count',
    'Affordable Homes Approved': 'sum'
}).sort_values('Affordable Homes Approved', ascending=False)

for status, row in stage_summary.iterrows():
    print(f"  {status:20s}: {int(row['Project ID']):3d} projects, {int(row['Affordable Homes Approved']):6,} homes")

print("\n Key Finding:")
under_review = stage_summary.loc['Under Review', 'Affordable Homes Approved']
occupied = stage_summary.loc['Occupied', 'Affordable Homes Approved']
print(f"   {int(under_review):,} homes under review vs only {int(occupied):,} occupied")
print(f"   Ratio: {under_review/occupied:.1f}x more homes in planning than completed")

print("\n" + "="*70)
print(" DONE! Check your files:")
print(f"   - {OUTPUT_MAP_PNG} (geographic map)")
print(f"   - {OUTPUT_WARD_PNG} (ward comparison)")
print("="*70)
