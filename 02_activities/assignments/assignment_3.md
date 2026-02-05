# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?
    I am using illustrator, which is one of my most familiar tools editing victor data. Also it is very easy to adjust colors and shapes, and work very well with photoshop if I want to edit any image background.

    > Who is your intended audience? 
    My primary audience is housing advocates, policymakers, and residents seeking affordable housing in Toronto. This includes community organizations that oversee housing development, city councilors assessing ward progress, urban planners evaluating geographic distribution, and potential renters looking to know which neighborhoods are about to launch affordable housing. 
    > What information or message are you trying to convey with your visualization? 
    Because I analyzed two datasets, I wanted to present the information to the audience on two levels. The first level is the overall trend of affordable housing in Toronto, which was analyzed using Python. The second level is the affordable housing situation in each region. For this part, I used illustrations and a map of Toronto to show the overall situation in each region, and pie charts to show the details of the top five regions. 
    > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
    I had several layers of consideration. First, the geographical context: based on the official Toronto electoral borough map, it allows local viewers to quickly identify spatial locations. The borough boundaries are familiar reference points, helping viewers locate their own neighborhoods. Next, the color choice: I used a six-level gradient (from light beige to deep red/orange) to represent the total number of homes in each borough. This gradient visually conveys the message that "the more homes, the darker the color," eliminating the need to consult a detailed legend. I chose warm tones (orange/red hues) rather than cool tones to visually emphasize the urgency of the housing crisis. Then, the pie charts are carefully selected. Instead of piling 25 pie charts onto the map, I strategically placed only the first five boroughs, connected by simple arrows. This creates a visual hierarchy—viewers first see the overall geographical layout, then can see the development stage of priority areas. Finally, the white space and typography: I left ample white space around the map and used a clean sans-serif font (the font size of the borough labels and data annotations is consistent). The top five constituencies are annotated with bold numbers (e.g., "3,412 homes") for easy reference to the specific numbers.
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    The Python script (housing_pipeline_viz.py) is reproducible. It reads the raw CSV from Toronto Open Data, aggregates by ward and development stage, calculates totals. There is a partial reproducibility of the Illustrator portion. In addition to documentation of every design decision, I listed which hex colors correspond to which data ranges (#DD7E6B for 2000+ homes, #FEF5E7 for 0-300 homes), where to position pie charts (top 5 wards only), and how arrows should be styled.For the target audience (advocates and policymakers), the reproducibility of the data summary is more important than design replication. They need to be confident that the figure "York Centre has 3412 homes" is accurate and verifiable. While color allocation and visual layout are important for effective communication, data integrity is secondary. I've provided both the Python code and the CSV output for full data validation.
    > How did you ensure that your data visualization is accessible?  
    Although I used a warm color gradient, I ensured sufficient contrast between adjacent color layers. More importantly, I didn't rely solely on color—each area is labeled, and the top five areas are explicitly marked with numbers (e.g., "3412 households"). Colorblind people can still identify the areas and read the specific numbers using the labels. In addition, key information is presented in multiple forms: (1) color intensity to indicate overall intensity; (2) pie chart size variations; (3) text labels containing specific numbers; and (4) geographic locations on the map. This redundant design ensures that even if one channel malfunctions (e.g., poor color perception), the other channels will still function normally.
    > Who are the individuals and communities who might be impacted by your visualization?  
    Firstly, I think this research will have an impact on developers, allowing them to identify development potential projects. Secondly, I believe it will be very helpful for people looking for affordable housing, enabling them to quickly understand the general situation of areas of interest.
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    The purpose of this data visualization is to provide a general overview of affordable housing in Toronto. Therefore, I chose two levels of information. I didn't want the visualization to contain too much information, but I still wanted to show the overall picture and key areas. I believe the design intent guided me to select the data I wanted to highlight.
    > What ‘underwater labour’ contributed to your final data visualization product?
    In this assignment, I'd like to discuss the underwater labour work in the following three areas: Geographic and Policy Research: Understanding Toronto's 2018 ward reorganization (reducing wards from 44 to 25) and investigating why Scarborough North had no projects, ultimately determining that this reflected insufficient actual development, not data errors. Design Iteration: Testing various options—all 25 pie charts (too crowded), maps only without charts (lacking depth), and the first 10 charts (still crowded), ultimately finalizing the first 5 charts based on audience feedback. Hand-drawn Maps: Coloring each of the 25 irregularly shaped wards in Illustrator, placing 25 name tags to match the polygon boundaries, drawing five precise curved connecting arrows to avoid intersections with other wards, and adjusting the pie chart positions to balance the composition.
- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 02/02/2026`
* The branch name for your repo should be: `assignment-3`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_3.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
