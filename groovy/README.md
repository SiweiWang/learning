# Learning Groovy

## Unit test

### What makes a good unit test

FIRST principle

- Fast: Good good unit test should run fast.

- Isolated: Only have single reason to fail. It should not dependent on other systems(network, database etc.) It should not also dependents on the test results/states of other tests.

- Repeatable: If the code you run never change, the test result should be consistent.

- Self-verifying: Make sure the scope of test is specific.

- Timely: Should be written as soon as the *production* code is written

### Unit testing Support in Groovy

- JUnit is built directly into the Groovy runtime

- Mocking APIs are included in the Groovy platform

- Advanced testing frameworks are also available

### Mock Object

A simulated object that mimics the behavior of a real object in a controlled way.

* Stubs
    * Can be used as stand-in objects
    * Will return canned values when asked

* Mocks
    * Support all the functionality of sutbs
    * Can verify a member was called a certain number of times
    * Can assert a specific interaction occurred