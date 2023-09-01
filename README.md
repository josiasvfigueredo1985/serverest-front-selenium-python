# Locators Strategies with Python

Site used for this project: [Metal Archives](https://www.metal-archives.com/)

**_ Project purpose: _** Describe some strategies that can be used for Selenium and also other testing frameworks such as Robot Framework, PlayWright and WebDriver.IO
**_ Note: _** This project is developed in Python but locators strategies are the same, despise the fact some frameworks like Cypress use slightly different locators approach like ".class_name" instead of "class_name"

## Module Structure

**_ Project folders _**

- driver_factory: where the driver is created and exposed to Selenium use it. (Note that for this project the approach is intentionally simple to focus on the locators, feel free do improve as you wish on your own project)
- selenium_utils: where we use all the methods from Selenium to interact with DOM elements(Document Object Model, in short, the internal elements from the webpage), note that all the most common methods are modified to be easy to use and separated by modules to be simple to understand each command purpose
- pages: where the page elements is mapped to be easy to identify each component, all the possible strategies is described to guide to best practices to best performance.

## Recommendations

- Use VS Code to practice, mostly of the tech companies are using and so the tutorials creators, so will be easy and faster to understand when you need to clarify some questions
- Always read the documentation from the framework used for automation and also from official [Selenium](https://www.selenium.dev/documentation/webdriver/elements/locators/)
