Data Source:
City of Toronto Open Data - Social and Affordable Housing
https://open.toronto.ca/dataset/active-affordable-and-social-housing-units/
###  What software did you use to create your data visualization?
I used Python for this data processing and visualization workflow.
*** Libraries: pandas for data cleaning and manipulation, matplotlib for plotting the dual-axis chart.
*** Environment: The script was written and executed in VS Code, generating vector-based outputs (.svg) directly from code to ensure reproducibility.

###  Who is your intended audience? 
My target audience includes urban planners, real estate developers, and housing industry professionals, as well as:
- Municipal policymakers: assessing the effectiveness of current affordable housing strategies.
- Researchers: studying shifts in housing policy and urban development.
- Community organizations: advocating for sustainable housing solutions.
My goal is to help these stakeholders understand the directional shifts in Toronto's housing investment landscape over the past five years.

### What information or message are you trying to convey with your visualization?
This visualization reveals a fundamental shift in Toronto's affordable housing strategy.
Between 2020 and 2025, the stock of government-subsidized social housing will decline slightly (-1.3%, from 85,768 units to 84,626 units), while cooperative affordable housing projects will increase significantly (+76.9%, from 6,101 units to 10,791 units).
** Visual Evidence: The dual-axis line graph clearly contrasts these two distinct paths: one line shows a downward trend (red), while the other shows a rapid upward trend (green).
** Key Takeaway: This reflects a policy shift, from government run social housing to an affordable housing model that partners with private developers and nonprofits. The message is clear: Toronto is transforming its affordable housing model.

### What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?
I chose a dual-axis design because the scale difference between the two variables is huge (approximately 85,000 vs. approximately 8,000). Plotting them on a single axis would flatten the growth line for “affordable housing,” thus masking its significant trend.
** Color Strategy: 
--- Red represents subsidized housing: I use red to indicate a "warning" or negative trend, highlighting the decline in public housing stock.
--- Green represents affordable housing: Green represents growth and new investment.
The colors of the axis labels and spines match their respective lines, thereby reducing cognitive load and helping readers associate the correct scale with the correct line.
I use direct labeling approach for this data visualization. Instead of using a legend, I placed the data labels directly at the ends of the lines (proximity principle in Gestalt) to make the chart easier to read.

### How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?
The Python script (housing_viz.py) is fully reproducible. It reads raw CSV data from Toronto Open Data, processes quarterly figures, calculates percentage changes, and generates visualizations. Any user with Python and matplotlib installed can run this script and generate the same charts.

### How did you ensure that your data visualization is accessible?
I use three approaches, double encoding, font size, and ,make sure the output is .svg format. 
-  I used both color and direct text labeling (line endpoints) to distinguish the two trends. I choose red and green to ensure people even with visual challenge can get access to the chart.
- I set the font size to 11 to ensure all text is legible.
- By saving as .svg, the visualization remains clear at any zoom levels.

### Who are the individuals and communities who might be impacted by your visualization?
The groups most affected by this visualization are low-income families, marginalized communities, and residents on social housing waiting lists.
- Potential impacts: If this visualization successfully conveys the reduction in subsidized housing, it can help advocates fight for greater protection of the existing social housing stock. Conversely, if misinterpreted, an increase in the number of "affordable housing" units could mask the sharp decline in deeply subsidized housing.

### How did you choose which features of your chosen dataset to include or exclude from your visualization?
I selected the columns “Subsidized Housing Units” and “Affordable Housing Units” because they represent two conflicting aspects of the policy shift. I excluded incomplete data points (e.g., the “n/a” value for subsidized housing at the beginning of 2020) to avoid misleading declines or missing values ​​in the line chart. 

### What 'underwater labour' contributed to your final data visualization product?
Finding suitable datasets involved browsing the Toronto Open Data Portal, reading metadata to understand the specific meaning of "subsidized housing" and "affordable housing" in the city government reports, and verifying that the data granularity was sufficiently fine (quarterly) to show trends. The CSV files required some cleaning, such as checking for missing values ​​and ensuring consistent date formatting across quarters.