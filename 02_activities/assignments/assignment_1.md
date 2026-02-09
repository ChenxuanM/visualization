# Data Visualization

## Assignment 1: Participation (Ongoing)

### Requirements:

- During every class, follow along with sample code from the slides. All code that you should be running in Python is formatted as follows:
  
  > If code in a slide looks like this, you should be running it to generate results.

- When there are individual or group activities in submodules, make notes of answers and key points from discussions
- Following each lesson with code, submit a document (either .py or a Jupyter notebook) containing the functioning code from that day's lesson, along with any written notes or comments.

- In-class Notes
### Class 1
- 1 why visualization is inportant;
- a crucial for communication
- b Evaluate whether visualizations are clear, accurate
- c Appropriate; Guide AI to make the right changes and customize designs
- d Understand principles and theory behind effective visualization

- 2 Numbers alone don't tell the full story

- 3 Good vs Bad Visualization 
- a Aesthetic qualities: Visual appeal, design principles
* Clarity - easy to understand at a glance
* Accuracy - represents data truthfully
* Purpose-driven - serves the intended message
* Accessible - considers colorblind users, clear labels

- 4 Matplotib
- Matplotlib is Python's primary visualization library, Figure: The overall container (like a canvas); Axes: The actual plot area where data is drawn; A figure can contain multiple axes (subplots)
import matplotlib.pyplot as plt
  fig, ax = plt.subplots()
  # fig = overall container
  # ax = plotting area

### Class 2
- Review from Class 1 
## Data visualization as an interpretative, rhetorical act is not necessarily a bad thing, but one that we should be aware of.
* Why visualization is important
* Good vs bad visualization examples
* Three qualities to consider:
- Aesthetic - visual appeal and design
- Substantive - accurate data representation
- Perceptual - ease of interpretation

- Two data visualizations can share the same substantive qualities while, intentionally or not, being perceived completely differently
- When we are aware of the choices we make while creating data visualizations, we can design data visualizations that are suited to the situation at hand (perceptual quali

- different type of visualization, different audience, different form-different requirement
-  Identifying the attribute types for our data will help us make choices about how to visualize it.

- Depends on purpose, audience, and medium!
* A good goal is to satisfy: “to find one of the many possible good solutions rather than one of the even larger number of bad ones”- 

- How different visualization types are perceived:
- congitive loac

### Class 3
- Images and visualizations are often the best way to communicate our data and insights…
- But if we can’t trust that visualizations are representing the ‘real’ data, we can’t trust what their creators are trying to communicate…

- The ability to reproduce a result does not necessarily indicate correctness, nor does the inability to do so mean a result is incorrect.
- But “science is incremental: it is only through transparency and by enabling reproducibility that scientific knowledge evolves.”

- Work in plain text
- Code should be written in a simple, plain-text format (eg. R scripts or .txt files)
- Code should not be written in a word processor (eg. Microsoft Word)
- Ideally, our ‘pretty’ final products (images, graphs, charts) can be procedurally (and reproducibly!) generated just by running our code

- FAIR principles

### Class 4
- 1. Color
* **The Issue:** Relying solely on color to convey meaning excludes people with Color Vision Deficiency (CVD/Colorblindness).
    * *Monochromacy:* No color perception.
    * *Dichromacy:* Missing one of the three cone pigments (e.g., Red-Green colorblindness).
    * *Anomalous Trichromacy:* All cones present but one is sensitive to wrong wavelengths.
* **Best Practices:**
    * **Double Encoding:** Use color *plus* another visual cue (patterns, textures, or direct labels).
    * **Contrast:** Ensure high contrast between text/data and the background.
    * **Tools:** Use colorblind-friendly palettes (e.g., Viridis).
- 2. Text
* **Typography:**
    * Avoid complex serif fonts; Sans-serif fonts are generally more readable.
    * Avoid condensed or extremely thin fonts.
* **Hierarchy:** Use headings and font sizes to guide the reader through the information logic.
* **Language:** Use plain language; avoid jargon where possible.

**3. Image Descriptions (Alt Text)**
* **Purpose:** Allows screen reader users to understand the content of a visualization.
* **Components:**
    * **Alt Text:** Brief description of the image's function or main content.
    * **Long Description:** Detailed explanation of the data, trends, and axes (often linked or in the surrounding text).
* **Strategy:** "Five Ws" (Who, What, Where, When, Why) + How (the trend/pattern).

### Access to Data Products
* **Economic Accessibility:** High costs (paywalls, expensive software) limit who can see or use visualizations.
* **Solutions:**
    * **Open Access:** Distributing research/data free of cost.
    * **Creative Commons:** Licenses that facilitate sharing and reuse.

### Class 5
Data visualization is not just for analysis; it is a tool for **advocacy**—promoting a cause, idea, or policy.

### Modes of Advocacy in Viz
1.  **Rational:** Uses logic, facts, and clean data to persuade (e.g., scientific charts).
2.  **Moral:** Appeals to a sense of right and wrong / justice.
3.  **Emotional:** Uses design to evoke feelings (empathy, anger, hope) to drive action.

### Historical Examples
* **Florence Nightingale:** Used the "Rose Diagram" (Coxcomb) to advocate for better sanitary conditions in military hospitals.
* **W.E.B. Du Bois:** Used visualizations at the 1900 Paris Exposition to advocate for the humanity and progress of Black Americans, countering racist narratives.

### Representation & Ethics
* **Deficit-Based Approach:** Focuses on what a community *lacks* (problems, gaps). Can reinforce negative stereotypes.
* **Asset-Based Approach:** Focuses on a community's *strengths*, opportunities, and existing resources.
* **Principle:** "Nothing about us without us" — visualize *with* communities, not just *about* them.

### Credit & "Underwater Labor"
* **The Concept:** Data visualization is just the "tip of the iceberg."
* **Hidden Labor:** We must acknowledge the invisible work that makes viz possible:
    * Community organizers who collected data.
    * Designers of color palettes.
    * Technical writers (alt-text).
    * Support staff and caregivers.
* **Goal:** Make this invisible labor visible and valued through proper citation and credit.

---

### Why am I doing this assignment?:

- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes:
*	Create and customize data visualizations from start to finish in Python
*	Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component          | Scoring                 | Requirement                                              |
|--------------------|-------------------------|----------------------------------------------------------|
| Completion         | Complete/Incomplete for each class| - All required work from a given class is included in the file |
| Markdown file format | Complete/Incomplete for each class| - File is readable and contains functional code, when needed |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Note:

* You should make a commit after each session with that lesson's code and notes. Your PR should have the same number of commits as there are sessions. It is important to make the commits to your branch in a timely manner right after each class.

### Submission Parameters:
* Submission Due Date: 23:59 - 02/02/2026
* The branch name for your repo should be: `assignment-1`
* What to submit for this assignment:
    * The `participation` folder/directory should be populated with the above mentioned .py/.ipynb files along with any written notes or comments (preferably in .md or .txt format).
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-1`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
