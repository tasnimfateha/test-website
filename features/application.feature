Feature: Application
""" 
Confirm that we can browse the applicationform page on our site
"""

Scenario: success for visiting job item and application form page.
    Given I navigate to the Home page
    When I click on the link to Apply
    Then I should see a page which contains job details and an application form
