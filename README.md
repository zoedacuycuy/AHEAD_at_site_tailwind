# AHEAD_AT_site

This repository serves as the website for AHEAD's Adaptive Testing Website.

# Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)

## Prerequisites

The site is made with Django so to use this repository, Python and Django should both be installed.
1. Download [Python](https://www.python.org/downloads/)
2. Use a terminal to navigate to the directory you want to store the repository.
    - OPTIONAL BUT RECOMMENDED: Create Python [Virtual Environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
3. Clone the repository using `git clone [repository link]`
4. Install the requirements using `pip install -r requirements.txt`

## Project Structure

The current project structure is as follows:
- main app
    - Main site's app that handles the landing page, and the redirects/about page
- registration app
    - Site's app that handles login, register, logout, viewing and changing user data
- dashboard app
    - Site's app that serves as the main menu
    - Handles redirecting after authentication
    - Redirects to testing, viewing test results, viewing user data, about page, changing user data, logout
- at_test app
    - Site's app that handles the testing
    - adaptive testing
- at_results app
    - Site's app that handles viewing test results easier
    - charts
    - improvement
    - recommendations and all that