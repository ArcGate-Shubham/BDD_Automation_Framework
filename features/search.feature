Feature: Search Functionality

    @search
    Scenario: Search for a valid product
        Given I got navigated to Home page
        When I enter valid product say "HP" into the search box field
        And I click on search button
        Then valid product should get displayed in search results

    @search
    Scenario: Search for a invalid product
        Given I got navigated to Home page
        When I enter invalid product say "Honda" into the search box field
        And I click on search button
        Then Proper message should be displayed in search results

    @search
    Scenario: Search without entering any product
        Given I got navigated to Home page
        When I dont enter anything into the search box field
        And I click on search button
        Then Proper message should be displayed in search results
