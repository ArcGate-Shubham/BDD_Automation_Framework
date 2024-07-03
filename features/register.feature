Feature: Register Account functionality

    @register
    Scenario: Register with mandatory fields
        Given I navigate to Register page
        When I enter below details into mandatory fields
             |first_name|last_name|telephone |password|
             |Arun      |motoori  |1234567890|12345   |
        And I select privacy policy option
        And I click on continue button
        Then Account should get created

    @register
    Scenario: Register with all fields
        Given I navigate to Register page
        When I enter below details into all fields
             |first_name|last_name|telephone |password|
             |Arun      |motoori  |1234567890|12345   |
        And I select privacy policy option
        And I click on continue button
        Then Account should get created

    @register
    Scenario: Register with a duplicate email address
        Given I navigate to Register page
        When I enter details into all fields except email field
             |first_name|last_name|telephone |password|
             |Arun      |motoori  |1234567890|12345   |
        And I enter existing accounts email into email field
        And I select privacy policy option
        And I click on continue button
        Then Proper warning message informing about duplicate account should be displayed

    @register
    Scenario: Register without providing any details
        Given I navigate to Register page
        When I dont enter anything into the fields
