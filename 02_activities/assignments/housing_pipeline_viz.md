###  What software did you use to create your data visualization?
I used a combination of Python and Adobe Illustrator.
***Python:** Used to generating the base vector map and bar chart from the raw data.
***Adobe Illustrator:** I am using illustrator, which is one of my most familiar tools editing vector data. Also it is very easy to adjust colors and shapes, and work very well with photoshop if I want to edit any image background.

###  Who is your intended audience? 
My primary audience is housing advocates, policymakers, and residents seeking affordable housing in Toronto.
This includes:
- Community organizations responsible for overseeing housing development.
- City councilors assessing progress in their districts.
- Urban planners assessing geographic distribution.
- Potential renters looking to identify which neighborhoods will soon have affordable housing available.

### What information or message are you trying to convey with your visualization?
The visualization conveys the current situation in Toronto's affordable housing pipeline.
- While there are many projects labeled as "Under Review" or "Active," the number of units actually "Occupied" is very low.
- The bar chart shows a huge gap between the planned homes and the finished homes. The map shows that development is not evenly distributed across the wards.
- We need to speed up the process from "Planning" to "Occupancy."

### What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?
I combined a Geographic Map (to show location) with a Pie Chart (to show proportion).
Layout Strategy (Why Pie Chart?): Initially, I planned to use a bar chart. However, during the layout process, I found that the bar chart made the overall composition look cluttered and difficult to read alongside the map. So I decided to switch to a pie chart. This circular shape is better suited for layout and allows me to clearly highlight the significant difference between "Under Review" (large sectors) and "Occupied" (small sectors).
- Visual Hierarchy: In Illustrator, I used different colors to differentiate the different states. This contrast draws attention to the small "Occupied" sectors and the large "Under Review" sectors, thus emphasizing the backlog.
- Simplification: The original dataset contained complex status codes. I used Python to group them into simplified categories to make the chart easier for my general audience to understand.

### How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?
The core data processing is fully reproducible via my Python script (`housing_pipeline_viz.py`).  It reads raw CSV data from Toronto Open Data. Any user with Python and matplotlib installed can run this script and generate the same charts.
But the part where I demonstrated in illustrator is difficult to reproduct, I have attched the pdf file, people who have the software can open and edit. 

### How did you ensure that your data visualization is accessible?
I focused on visual contrast and geographic intuition to make the data accessible to a wider audience.
- Color Contrast: In Illustrator, I adjusted the colors to ensure clear distinctions between different housing types. I increased the differences in hue and brightness so that people with color vision deficiencies could also clearly distinguish these categories.
- Geographic Recognition: I used a map of Toronto as the primary visual element. This helps local residents with dyslexia or speech impairments identify their neighborhoods by spatial location and shape, without relying solely on complex text labels or ward names.

### Who are the individuals and communities who might be impacted by your visualization?
The groups most affected are residents in areas without new projects and applicants on waiting lists.
By making the backlog of projects visible, this work can encourage municipal officials to expedite the approval process. Simultaneously, it can help applicants who want to relocate to determine where to apply for new housing.

### How did you choose which features of your chosen dataset to include or exclude from your visualization?
I included variables such as "Selection Area Name," "Status," and "Number of Approved Affordable Housing Units" to illustrate the entire project process.
Exclusions: I filtered out rows lacking geographic location data to ensure map accuracy. I also excluded specific address information to focus more on macro trends at the selection area level. Visually, I only selected the top five areas with the most housing units on the map to ensure that key data is displayed without redundancy.

### What 'underwater labour' contributed to your final data visualization product?
The most crucial behind-the-scenes work was writing a function to extract coordinates from the complex JSON-formatted data in the "geometry" column. Without this coding, the data couldn't be mapped.
I relied on staff from the City of Toronto who maintained the "Affordable Housing Rental Program" dataset and regularly updated the program's status.

