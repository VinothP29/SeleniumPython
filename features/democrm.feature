Feature: OrangeHRM

  Background: Verify demo crm homepage
    Given I am in demo crm login page
  
  @positive
  Scenario: Verify a valid user is able to login successfully
     When I enter the below credential in crm login page
      | fieldname | fieldvalue | 
      | Username  | Admin      | 
      | Password  | admin123   | 
      And I click login button
     Then I verify user is logged in successfully
  
  @negative
  Scenario: Verify user is not able to login with invalid Password
     When I enter the below credential in crm login page
      | fieldname | fieldvalue | 
      | Username  | Admin      | 
      | Password  | admin      | 
      And I click login button
     Then I verify invalid credentials alert is displayed
