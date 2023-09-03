# Locators Strategies with Python

**Project Description and Purpose:** This Python project aims to describe strategies applicable to Selenium and other testing frameworks like Robot Framework, Playwright, and WebDriver.IO. Its simplicity allows for a straightforward exploration of these strategies.  
 Please feel free to provide any suggestions to enhance the project's usefulness to the testing community.

Site used for this project: [Metal Archives](https://www.metal-archives.com/)

_Note:_ This project is developed in Python, but locator strategies are the same, despite the fact that some frameworks, like Cypress, use slightly different locator approaches.

## Requirements

- [Python](https://www.python.org/downloads/)
- [Python VS Code Extensions](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Selenium](https://www.selenium.dev/downloads/)

## How to Run or Debug

- [Easy Way (Run or Debug)](https://code.visualstudio.com/docs/python/debugging)
- Hard Way (Run):
  - Right-click on the main folder.
  - Select the "Open in Integrated Terminal" option.
  - In the terminal, type: `python main.py`
- Hard Way (Debug):
  - Set your breakpoint.
  - Right-click on the main folder.
  - Select the "Open in Integrated Terminal" option.
  - In the terminal, type: `python -m pdb main.py`

## Module Structure

**Project Modules**

- `driver_factory`: where the driver is created and exposed to be used with Selenium. (Note that for this project, the approach is intentionally kept simple to focus on locators; feel free to improve it as you wish for your own project)
- `pages`: where the page elements are mapped for easy identification of each component. All possible strategies are described to guide best practices for optimal performance.  
  _Note:_ The page elements are structured as simply as possible to avoid confusing the focus of this project.
- `selenium_utils`: where we use all the most common methods from Selenium to interact with DOM elements (Document Object Model, in short, the internal elements of the webpage). Note that all the most common methods are modified to be easy to use and are separated by modules to make it simple to understand each command's purpose.

## Recommendations

- Use VS Code for coding whenever possible, unless your company mandates the use of another IDE. Most tech companies and tutorial creators use it, so it will be easier and faster to understand when you need clarification on certain topics.
- Always read the documentation of the automation framework being used, as well as the official [Selenium documentation](https://www.selenium.dev/documentation/webdriver/elements/locators/).

---

Made with ❤️ by [Josias](https://www.linkedin.com/in/josias-valentim-de-figueredo-0347455b/)
