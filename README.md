# CountY: A Closer Look
### A TEAMe project (Daniel Chung, Edward Lee, Henry Koelling)

## Summary
This website allows users to easily search regions of the United States, whether a county, state, or the nation at large, and view the distribution of their votes from the 2016 presidential election.

## Source
SETUPS: Voting Behavior: The 2016 Election ([ICPSR 36853](https://doi.org/10.3886/ICPSR36853.v2))

### Citation
Prysby, Charles, Scavo, Carmine, American Political Science Association, and Inter-university Consortium for Political and Social Research. SETUPS: Voting Behavior: The 2016 Election. Inter-university Consortium for Political and Social Research [distributor], 2018-10-25.


## Intended Audience
* teachers passionate about history- or political science-related subjects
* students interested in American government or political science
* campaign managers for candidates running for political offices
* relocating homeowners and families who consider the local political climate when looking at a home
* voters newly eligible to vote in local, state, and federal elections


## Goals
* *Whet the appetite for more knowledge* particularly for educators interested in 2016 voting tendencies.
* *Present reliable data and visual representations* students can trust.
* *Graphically display county-level voter distributions* to conduce successful campaign strategies.
* *Make navigation quick and easy* for homeowners and heads of households that have someplace to be.
* *Be generally appealing* to positively influence public curiosity in local politics.

## Tech Stack
* Language: Python 3.8, JavaScript
* Framework: Flask
* Hosting: PythonAnywhere, running uWSGI
* Database: MySQL. Made trivial migration from PostgreSQL to eliminate hosting fees

## Roadmap
### Functional
- [X] Search for voter information based on geographic location (country, state, county)
- [ ] Search for voter information based on race, ethnicity, or socioeconomic background
- [ ] Option to view data in different styles and outputs (graphs, maps, spreadsheet/table)
- [X] Ready access to citation/bibliographic information
- [ ] Graphic visualizations have appropriate legends
- [ ] Graphic visualizations have appropriate titles
- [ ] Graphic visualizations have appropriate color differentiation between different variables
- [ ] Graphic visualizations have the option to switch to a colorblind friendly scheme

### Nonfunctional
- [X] Search/Browse feature easily navigable
- [X] Graphs clear and uncluttered, without unnecessary correlations or trends
- [ ] Clearly indicate which each graphic visualization represents
- [X] Visualizations colorblind friendly