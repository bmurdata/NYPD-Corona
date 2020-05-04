# NYPD-Corona
Analysis of NYPD Coronavirus(COVID-19) reported response and affected rate using the NYPD News Twitter

# Introduction

   Goverment agencies around the world are responding in new ways to the pandemic. The NYPD has been by posting regular information to its NYPD News Twitter 
   on locations visited, locations closed, and sick report numbers. However, there is no chart or clear way to see how it has changed over time, nor how it compares to regional, state,
   or national levels of the pandemic. This project aims to solve this.
   
# Tools

  Python- a programming language chosen for its wide range of supporting libraries
 
  twint-a Python package to scrape Twitter information.
  
  SQL Server- to store tweets, and extract the ones I wanted
  
  pyodbc- a Python package to run SQL Commands on my SQL Server
  
# Progress-code to be posted after cleanup

-Scraped tweets using twint, generated SQL table and populated with  JSON objects.

-Made inital CSV files of the tweets, analysis using Python ongoing.