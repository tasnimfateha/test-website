from behave import given, when, then

@given(u'I navigate to the Home page')
def nav(context):
    """ 
    Navigate to the Home page
    """
    context.browser.get('http://localhost:5000/index.html')

@when(u'I click on the link to Apply')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('1').click()

@then(u'I should see a page which contains job details and an application form')
def details(context):
    """ 
    if successful, then we should be directed to the applicationform page
    """
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/job/2/apply'
    
  assert 'AMERIA Investment Consulting Company Chief Financial Officer Middle East AMERIA Investment Consulting Company is seeking a Chief Financial Officer. This position manages the company's fiscal and administrative functions, provides highly responsible and technically complex staff assistance to the Executive Director. The work performed requires a high level of technical proficiency in financial management and investment management, as well as management, supervisory, and  administrative skills' in context.browser.page_source