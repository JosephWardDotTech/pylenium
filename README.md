![](/.github/.images/sylenium.png)

[![Build Status](https://api.travis-ci.org/symonk/sylenium.svg?branch=master)](https://travis-ci.org/symonk/sylenium)
[![License MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/symonk/selenide-testng-allure2-test-automation-framework/blob/master/LICENSE)
[![Sonar Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=io.symonk.sylenium%3Asylenium&metric=alert_status)](https://sonarcloud.io/dashboard?id=io.symonk.sylenium%3Asylenium)
[![Sonar Code Coverage](https://sonarcloud.io/api/project_badges/measure?project=io.symonk.sylenium%3Asylenium&metric=coverage)](https://sonarcloud.io/component_measures?id=io.symonk.sylenium%3Asylenium&metric=coverage)
[![Sonar Maintainability](https://sonarcloud.io/api/project_badges/measure?project=io.symonk.sylenium%3Asylenium&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=io.symonk.sylenium%3Asylenium)
[![Find_Me LinkedIn](https://img.shields.io/badge/Find_Me-LinkedIn-brightgreen.svg)](https://www.linkedin.com/in/simonk09/)
[![Find_Me Slack](https://img.shields.io/badge/Find_Me-Slack-brightgreen.svg)](https://testersio.slack.com)

## What is Sylenium? :flags: 

Sylenium is a test automation harness for web applications written in java.  Why spend time fussing around
boilerplate code and instability in your end to end tests, Sylenium takes care of it.  Let's see how simple it really is:


```java

    /** Page Objects and business logic sold seperately! Credit @ Selenide with a bit more juice! **/
    @Test()
    @CaseDescription("Sylenium can help you login!")
    @Issue("jira-100")
    @TmsLink("jira-101")
    public void testLogin() {
      start(LoginPage.class);
      $(By.name("user.name")).setValue("Simon");
      $(By.name("password")).setValue("securepassword");
      $("#submit").click();
      $("#username").shouldHave(text("Hello, Simon!"));
    }

```


The aim of this project is simple, provide a powerful test automation harness for testing web applications with java.  Because test automation (especially) at the ui layer is plagued with bad practice
I would like to start by outlining a few things of what **NOT** to use this harness for.  If such a license existed that would ban you from doing the following, I would apply it to this repository...

---

### :crossed_flags: Writing pointless short tests :crossed_flags:

This framework should be used to test end to end flows of your application under no isolation of the stack.  Writing tests for simple ui
functionality such as buttons being clickable, dropdown having values etc should be done by component tests.  Modern frameworks make this a piece of cake (angular, react etc).

---

### :crossed_flags: Only automating at the ui layer :crossed_flags:

Using this test automation harness as your only automated tests.  Focus on unit and integration tests as a primary method of coverage.

---

### :crossed_flags: Using unstable locators :crossed_flags:

Using google chrome `copy-as-xpath` and using it directly etc.  Favour adding unique identifiers to your frontend to aid with automation.  `data-` attributes etc can be extremely useful.
Using complex xpaths will end in hassle later, and please account for the page state being different later with parallel tests running.  Your useless xpath locator finding row 3 in a table won't 
work later when 10 parallel tests have flooded the table data!

---

### :crossed_flags: Overcomplicating page objects :crossed_flags:

The beauty of this framework is we have **NO** driver or page factory code in our page objects, its all handled behind the scenes using custom reflection and java dynamic proxies, coupled with smart webdriver management.
Keep your page objects simple, exposing a fluent interface for the tests to consume.  Always remember a page object is **NOT** equal to a page `!=`.  A page object can encapsulate a simple
dropdown on a page, which can be injected or reused as part of another page object.  `KISS`.

---

### :crossed_flags: Managing test data poorly :crossed_flags:

Managing test data using this harness itself through the ui for example, terrible practice.  Hopefully you have or can get access to some cool restful services to help you manage the data.  Managing test data
is most certainly not easy and becomes a behemoth over time.  The debate of randomising data is a long going one.  Please dont use your browsers for prepping and tearing down test data.  I don't even like direct database manipulation either,
from experience you will spend too long doing maintenance.

---

### :crossed_flags: Running sequential tests :crossed_flags:

Write your tests with parallelisation in mind.  Independent tests aren't enough, consider cross contamination (`system wide settings`) contaminating your tests at runtime.  For example if test A modifies
a system wide setting it can impact other tests, even though they are not remotely reliant on each other.  Multi tenancy applications can really help with this, otherwise run a `@NotThreadSafe` run at the end of your run.
If you are running one test at a time.

---

### :crossed_flags: Pointless noise in page objects :crossed_flags:

Page objects should encapsulate user actions grouped together, not individual actions that interact on a per element basis.  Writing a `Login();` method is better than writing 3 methods to do the steps of logging in.

---

### :crossed_flags: Using field injection :crossed_flags:

Using field injection with any sort of DI mechanism. Yes its easier, but it sucks.  Its gimmicky magic, decreases class testability, masks design errors with large classes.  When you inject into the field often you will 
not see beefy constructors that can prompt you to do some refactoring.

---

### :crossed_flags: Not using CI :crossed_flags:

Running tests locally is easy, get your tests into a scalable distributed execution mechanism within a CI pipeline. **note:** running locally is very useful, we can guard our feature branches that way. CI can help guard master PRs and production

---

### Please contribute!

Now that we have that out of the way, I would also like that you create atleast 1 pull request to the selenide project when using this framework.  You can find the repository here:

https://github.com/codeborne/selenide

and ofcourse, open PRs here

--- 

### :earth_africa: Feature: Managed Logging capabilities on a per test basis
Sylenium takes care of log management by providing custom annotations for tests and sensible assumed defaults.

- By default sylenium stores one log per test execution
- By default sylenium only stores logs which pass
- By default sylenium uses the testNG method name as the logger name

Below is an example of how you can configure your tests on a test by test basis to override such values.  Sylenium is
smart enough to handle invocationCount usage of testNG by using the iteration as part of the log file name.

```java
  @Test(invocationCount = 50)
  @ConfigureLog(name = "custom-name", splitLogFiles = false, keepFailures = true)
  public void canUpdateAndGetProperties() {
    sy.updateProperty("sy.enable.localisation", "true");
    assertThat(sy.getProperty("sy.enable.localisation")).isEqualTo("true");
  }
  ```

---

### :earth_africa: Feature: Strategy based test data management across suites
Anyone familiar with cucumber BDD will typically be aware of state persistence across step definitions, Sylenium takes this approach to the
standard multi threaded environment, allowing you register any test data objects in a world which is accessible across suites, using a Queued approach
Sylenium makes tidying up after yourself an absolute breeze!

```java
      /** World test data objects should implement the following interface **/
      public interface SyleniumObject {
        void cleanUp();
      }
    
      /** Now simply add them to the world **/
      @Test
      public void registeringObjects() {
        world.registerObject(new DummyWorldObject());
        assertThat(world.getWorldSize()).isEqualTo(1);
      }
    
      /** Need to remove something manually from the world? **/
      @Test
      public void unregisteringObjects() {
        final DummyWorldObject obj = new DummyWorldObject();
        world.registerObject(obj);
        world.unregisterObject(obj);
        assertThat(world.getWorldSize()).isEqualTo(0);
      }
    
      /** Want to manually flush the world? alternatively configure a clean up strategy. **/
      @Test
      public void cleaningUpEmptiesTheWorld() {
        world.registerObject(new DummyWorldObject());
        world.cleanUpWorld();
        assertThat(world.getWorldSize()).isEqualTo(0);
      }
```

---

### :earth_africa: Feature: Solving pesky localisation issues
We all know that using LinkText explicitly or using hard coded strings for ui tests that may change under a difference language are
flaky and known to break. Any time you need a localised value in your tests Sylenium comes straight to the rescue. 
These are determined by your framework properties at runtime for language(s). For example:

```java
    /** Given a runtime argument of -Dsylenium.language=spanish, Sylenium does a lookup in your spanish.resources file for the K:V pair **/
    @Test
    public void canFindExactLinkTextElement() {
        sy.start(DummyWorldObject.class);
        $(sy.localisedLinkTextOf("link.text")).shouldBe(Condition.visible);
    }
  ```

---

##  :star: Backers of the project who provide us with free tools:

[![Intellij IDEA](https://cloud.google.com/tools/images/icon_IntelliJIDEA.png)](http://www.jetbrains.com/idea)
[![BrowserStack](https://www.browserstack.com/images/mail/browserstack-logo-footer.png)](https://www.browserstack.com)

---

### Attributions! :star:

Here are all the great freebie / open-source things I have used as part of building $ylenium.  A massive thanks to the following:

- Nothing... (yet!)

