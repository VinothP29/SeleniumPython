Feature: demo crm

  Scenario: Verify a valid user is able to login successfully
    Given I am in demo crm login page
     When I enter the below credential in crm login page
      | fieldname | fieldvalue |
      | Username  | Admin      | 
      | Password  | admin123   |
      And I click login button
     Then I verify user is logged in successfully
