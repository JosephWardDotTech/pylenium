![](/.github/.images/sylenium.png)

[![Build Status](https://api.travis-ci.org/symonk/pylenium.svg?branch=master)](https://travis-ci.org/symonk/pylenium)
[![License MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/symonk/pylenium/blob/master/LICENSE)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=symonk_pylenium&metric=bugs)](https://sonarcloud.io/dashboard?id=symonk_pylenium)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=symonk_pylenium&metric=alert_status)](https://sonarcloud.io/dashboard?id=symonk_pylenium)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=symonk_pylenium&metric=coverage)](https://sonarcloud.io/dashboard?id=symonk_pylenium)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=symonk_pylenium&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=symonk_pylenium)
[![Find_Me LinkedIn](https://img.shields.io/badge/Find_Me-LinkedIn-brightgreen.svg)](https://www.linkedin.com/in/simonk09/)
[![Find_Me Slack](https://img.shields.io/badge/Find_Me-Slack-brightgreen.svg)](https://testersio.slack.com)

## What is Pylenium? :flags: 

Pylenium is a test automation harness for web applications written in python. Why spend time fussing around boilerplate code and instability in your end to end tests, Pylenium takes care of it. Let's see how simple it really is:

```python
    # Page Objects and business logic sold separately! 
    @case_description("Pylenium can help you login!")
    @issue_id("issue-100")
    @testcase_id("testcase-101")
    def test_my_login(self):
      start(self.login_page())
      find(By.name("user.name")).set_value("simon")
      find(By.name("password")).set_value("securepassword")
      find("#submit").click() # default css_selector lookup
      find("#username").should_have(text("Hello, Simon!")) # default css_selector lookup
```

---
