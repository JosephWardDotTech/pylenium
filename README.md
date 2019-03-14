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
      start(self.login_page()) # no driver hassle, just get started! we will handle the thread-safe driver for you!
      find(By.name("user.name")).set_value("simon")
      find(By.name("password")).set_value("securepassword")
      find("#submit").click() # default css_selector lookup
      find("#username").should_have(text("Hello, Simon!")) # default css_selector lookup
```

---

### Configuration :computer:
Pylenium has a easy to use configuration which assumes sensible defaults, configurable programmatically or via environment variables.

```python
    __browser = os.getenv('pylenium.browser', Browser.CHROME)  # the browser, duh!
    __headless = os.getenv('pylenium.headless', False)  # headless browser or not?
    __remote = os.getenv('pylenium.remote', False)  # is a remote web driver for distributed testing 
    __browser_size = os.getenv('pylenium.browser_size', '1366x768')  # browser window size
    __browser_version = os.getenv('pylenium.browser_version', None)  # browser version 
    __browser_position = os.getenv('pylenium.browser_position', None)  # browser position
    __browser_maximized = os.getenv('pylenium.maximized', True)  # is browser maximized?
    __wdm_enabled = os.getenv('pylenium.wdm_enabled', True)  # let us handle webdriver binary management / download etc
    __browser_binary = os.getenv('pylenium.browser_binary', '')  # binary if you don't want to use __wdm_enabled
    __page_load_strategy = os.getenv('pylenium.page_load_strategy', PageLoadStrategy.NORMAL)  # how should pylenium load pages, (normal, fast, eager)
    __desired_capabilities = DesiredCapabilities()  # custom browser desired capabilities
    __base_url = os.getenv('pylenium.base_url', 'http://localhost:8080')  # web application base url
    __explicit_wait_timeout = os.getenv('pylenium.wait_timeout', 15000)  # predicate/explicit waiting max timeout
    __polling_timeout = os.getenv('pylenium.polling_timeout', 200)  # how often should predicate be polled for truth
    __capture_screenshot = os.getenv('pylenium.screenshot', True)  # should we capture screenshots on failure
    __capture_pagesource = os.getenv('pylenium.pagesource', True)  # should we capture page source as HTML on failure
    __javascript_clicking = os.getenv('pylenium.js_click', False)  # should pylenium click with javascript?
    __javascript_sendkeys = os.getenv('pylenium.js_sendkeys', False) # should pylenium send keys with javascript?
    __selector_default = Selector.CSS  # default find() lookup, takes CSS by default but customisable
```

---
