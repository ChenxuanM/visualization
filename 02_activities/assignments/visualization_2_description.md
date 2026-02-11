Data Source:
City of Toronto Open Data - Social and Affordable Housing
https://open.toronto.ca/dataset/active-affordable-and-social-housing-units/

###  What software did you use to create your data visualization?
I created this time series visualization using Microsoft Excel; specifically, I recreated the same dual-axis line chart that I had previously created in Python. The reason why I choose excel is this tool is a very normal office tool. Accessibility for stakeholders who lack programming skills but need to validate or explore data.
I imported CSV data into Excel, created a pivot table to organize the quarterly data, and used Excel's charting tools to build a dual-axis line chart with a custom format to match the visual design of the Python version.

###  Who is your intended audience? 
My target audience includes urban planners, real estate developers, and housing industry professionals, as well as:
- Municipal policymakers: assessing the effectiveness of current affordable housing strategies.
- Researchers: studying shifts in housing policy and urban development.
- Community organizations: advocating for sustainable housing solutions.
In addition to the users mentioned above, Excel's ease of use makes analysis results more accessible for public comment and discussion, allowing the Excel version to reach a wider audience who want to verify and understand the data. The Excel format allows users to interact directly with data, apply custom filters, and verify calculation results without needing to install any programming environment.

### What information or message are you trying to convey with your visualization?
This visualization reveals a fundamental shift in Toronto's affordable housing strategy.
Between 2020 and 2025, the stock of government-subsidized social housing will decline slightly (-1.3%, from 85,768 units to 84,626 units), while cooperative affordable housing projects will increase significantly (+76.9%, from 6,101 units to 10,791 units).
** Visual Evidence: The dual-axis line graph clearly contrasts these two distinct paths: one line shows a downward trend (red), while the other shows a rapid upward trend (green).
** Key Takeaway: This reflects a policy shift, from government run social housing to an affordable housing model that partners with private developers and nonprofits. The message is clear: Toronto is transforming its affordable housing model.
** The Excel visualization results convey the same message as the Python version, indicating that the underlying trend is robust and tool-independent.** 

### What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?
Same as python, I chose a dual-axis design because the scale difference between the two variables is huge (approximately 85,000 vs. approximately 8,000). Plotting them on a single axis would flatten the growth line for “affordable housing,” thus masking its significant trend.
** Color Strategy: 
--- Red represents subsidized housing: I use red to indicate a "warning" or negative trend, highlighting the decline in public housing stock.
--- Green represents affordable housing: Green represents growth and new investment.
The colors of the axis labels and spines match their respective lines, thereby reducing cognitive load and helping readers associate the correct scale with the correct line.
I use direct labeling approach for this data visualization. Instead of using a legend, I placed the data labels directly at the ends of the lines (proximity principle in Gestalt) to make the chart easier to read.
*** Comparison with Python: While Python offers procedural precision, Excel interactive chart editing features make it easier to experiment with different visual layouts before finalizing the design.**

### How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?
The Excel spreadsheet has semi-reproducibility. While it's not as fully reproducible as a scripted approach, I documented my process to maximize reproducibility:
1. **Data Selection:** I manually selected a data range from Q1 2021 to Q2 2025, excluding quarters with incomplete data (e.g., subsidized housing data at the beginning of 2020 was n/a).
2. **Chart Creation:** Insert → Marked Line Chart
3. **Dual Axis Configuration:** Due to the significant difference in scale between the two data series (approximately 85,000 vs. approximately 8,000), I right-clicked the subsidized housing series and selected "Format Data Series" → "Secondary Axis".
4. **Axis Adjustment:** I manually adjusted the range of both y-axis based on the maximum and minimum values ​​of each series to improve readability and prevent any trend lines from appearing flat.
- The specific axis range I chose (e.g., 82,000-87,000 subsidized housing units) requires visual judgment to optimize readability.
- Manual formatting settings (colors, line thickness, label placement) are not automatically recorded.
- Excel's point-and-click interface means others must follow written instructions, not execute code.

### How did you ensure that your data visualization is accessible?
**1. Dual-axis design to differentiate scale differences:**
- The two housing types differ significantly in size (approximately 85,000 units vs. approximately 8,000 units)
- Using auxiliary axes ensures both trends are clearly visible
- I manually adjusted the range of each axis to prevent data compression from obscuring important changes
**2. High contrast and visibility:**
- I ensured sufficient contrast between the line colors (orange and blue) and the white background
**3. Excel's native accessibility features:**
- Excel Allows users to zoom in/out without pixelation, also allows people to make the font bigger if they want. 

### Who are the individuals and communities who might be impacted by your visualization?
The groups most affected by this visualization are low-income families, marginalized communities, and residents on social housing waiting lists.
- Potential impacts: If this visualization successfully conveys the reduction in subsidized housing, it can help advocates fight for greater protection of the existing social housing stock. Conversely, if misinterpreted, an increase in the number of "affordable housing" units could mask the sharp decline in deeply subsidized housing.
*** The Excel format makes it easy for community groups to present this data in public meetings or reports, as Excel is widely accepted in policy discussions.**

### How did you choose which features of your chosen dataset to include or exclude from your visualization?
Same as python, I selected the columns “Subsidized Housing Units” and “Affordable Housing Units” because they represent two conflicting aspects of the policy shift. I excluded incomplete data points (e.g., the “n/a” value for subsidized housing at the beginning of 2020) to avoid misleading declines or missing values ​​in the line chart. 

### What 'underwater labour' contributed to your final data visualization product?
Manually Formatting Charts: Unlike defining styles directly in code in Python, Excel requires repeated clicks to adjust colors, line thickness, axis ticks, and label positions.
