# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      BAD VISUALIZATION
      Source: https://public.tableau.com/app/profile/arjen.groeneveld/viz/24healthstatsfeb25/Dashboard1

      Reason 1 - Excessive Cognitive Load:
      The radial chart format creates significant extraneous cognitive load. As discussed in class, unfamiliar or rare chart types require more mental effort to interpret. Viewers must first decode the circular layout before accessing the actual health data. The multiple concentric rings displaying steps, energy, sleep, and weight simultaneously overwhelm the viewer rather than facilitate understanding.

      Reason 2 - Poor Perceptual Quality:
      This visualization fails the fundamental perceptual quality test posed in our course: "Can we understand what message the maker is attempting to convey?" Without hovering over elements or consulting the left panel, the concentric rings are nearly indecipherable. The central blue bars require extensive guesswork to interpret. Effective visualizations should communicate their message independently.

      Reason 3 - Violation of Gestalt Principles:
      The multiple data layers (steps, energy, weight, sleep, workouts) are visually disconnected, which violates Gestalt principles of proximity and connection. As covered in class, "connected objects are perceived as related." In this data visualization, readers cannot perceive meaningful relationships between different health metrics/layers or understand why these variables are grouped together.

      Reason 4 - Accessibility Concerns:
      The blue-cyan-purple color palette creates accessibility barriers for colorblind readers. As noted in our course, colors that are "very close" make differentiation difficult. The similar hues used for different data categories would be challenging for individuals with color vision deficiencies.

      GOOD VISUALIZATION
      Source: https://public.tableau.com/app/profile/mateusz.karmalski/viz/CountrieswiththeMostHolidaysin2024makeovermonday/Dashboard12

      Reason 1 - Strong Perceptual Quality:
      In this visualization, we can immediately discern the maker's intent: "What message is he trying to convey?"  The title "Countries with the Most Holidays in 2024" is clear and ranked annotations (#1 Nepal: 39 days, #2 Myanmar: 32 days, #3 Iran: 26 days) make the main finding instantly accessible.

      Reason 2 - Effective Cognitive Load Management:
      By using explanatory composition, the designer minimizes cognitive load. There are three visual techniques that guide attention: (a) darker colors for top-ranked countries, (b) text annotations with specific values, and (c) pointer lines connecting labels to bars. As discussed in class, guided visualizations with "headlines, annotations, highlights" require less mental effort than exploratory ones.

      Reason 3 - Application of Gestalt Proximity:
      The side-by-side placement of the bar chart and world map leverages the Gestalt principle of proximity—"objects that are close together are perceived as belonging to a group." Readers naturally connect the statistical ranking with geo-locations, enriching understanding without requiring additional explanation.

      Reason 4 - Provenance Rhetoric:
      The visualization includes a clear data source (worldpopulationreview.com), showing provenance rhetoric. As emphasized in our course, citing data sources "signals transparency and trustworthiness to the audience" and increases the persuasiveness of the visualization.





      ```
    - How could this data visualization have been improved?  
      ```
      BAD VISUALIZATION Improvements:

      1. Replace the radial chart with multiple smaller charts—each health metric (steps, energy, sleep, weight) corresponds to a simple line chart arranged in a grid. This familiar chart type significantly reduces cognitive load while still showing annual trends.

      2. Use a colorblind-friendly color palette and ensure sufficient contrast between data categories. Using vibrant hues (e.g., blue-orange contrast) so that ensure all readers can view the data without barriers.

      ---

      GOOD VISUALIZATION Improvements:

      1. Expand the color gradient range. The current blue color scale is too narrow, countries with similar holiday counts (e.g., 12-18 days) appear nearly the same. Diverging color schemes or wider gradients would help differentiate mid-range values more clearly.

      2. Add visual cues to the interactive features. While the "highlight country/region" search function already exists, first-time visitors might not notice it. Adding a simple prompt or icon can encourage users to explore this useful feature.






      
      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 01/26/2026`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
