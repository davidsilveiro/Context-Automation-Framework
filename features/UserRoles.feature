Feature: User Role Functionality


  Scenario Outline: As a user i want to upload a file
      Given I have logged into qainterview as "<role>"
      When I navigate to the upload page
  	  Then I proceed to upload a "<filetype>"

    Examples: Roles and file types
      | role  | filetype |
      | user  | jpeg     |
      | user  | pdf      |
      | user  | gif      |
      | user  | png      |
      | user  | txt      |
      | user  | rtf      |
      | user  | doc      |
      | user  | xls      |
      | user  | xlsx     |
      | user  | docx     |
      | admin | jpeg     |
      | admin | gif      |
      | admin | png      |
      | admin | txt      |
      | admin | rtf      |
      | admin | doc      |
      | admin | xls      |
      | admin | xlsx     |
      | admin | docx     |
      | admin | pdf      |


      
