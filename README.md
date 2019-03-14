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
Pylenium config is very powerful, but also assumes sensible defaults.  You can modify your config via:

 - Runtime via pytest --cli args 
 - Setting environment variables for any of the values
 - Do nothing, likely the default will be perfect for your needs!

```python
    # the browser, duh! -> default: [chrome]
    browser = os.getenv('pylenium.browser', Browser.CHROME)  
    
    # headless browser or not? -> default: [no]
    headless = os.getenv('pylenium.headless', False)
    
    # is a remote web driver for distributed testing -> default: [no -- requires a grid]
    remote = os.getenv('pylenium.remote', False) 
    
    # browser window size -> default: [1366 x 768]
    browser_size = os.getenv('pylenium.browser_size', '1366x768')
    
    # browser version -> default: [none - it doesn't really matter outside grid/ie]
    browser_version = os.getenv('pylenium.browser_version', None)
    
    # browser position -> default: [centered]
    browser_position = os.getenv('pylenium.browser_position', None)
    
    # is the browser maximized?: [default: true]
    browser_maximized = os.getenv('pylenium.maximized', True)
    
    # should pylenium handle browser binary downloading, management and caching? no more environment setup for binaries
    # only applicable for local driver(s), can support a proxy for pesky networks -> default: [enabled]
    wdm_enabled = os.getenv('pylenium.wdm_enabled', True)
    
    # with wdm_enabled disabled, specify your own binary path for the driver -> default: [empty] 
    browser_binary = os.getenv('pylenium.browser_binary', '')
    
    # how should pylenium load pages @options -> 'NORMAL', 'FAST', 'EAGER' -> default: [normal]
    # normal -> wait after click/gets, fast -> 'do some magic to move on faster', eager -> 'move on very fast!'
    page_load_strategy = os.getenv('pylenium.page_load_strategy', PageLoadStrategy.NORMAL)  
    
    # custom browser desired capabilities -> default: [Empty]
    desired_capabilities = DesiredCapabilities()
    
    # web application base url -> default: ['http://localhost:8080']
    base_url = os.getenv('pylenium.base_url', 'http://localhost:8080')
    
    # predicate/explicit waiting max timeout -> default: [15 seconds]
    explicit_wait_timeout = os.getenv('pylenium.wait_timeout', 15000)
    
    # how often should predicate be polled for truth -> default: [5 times per second]
    polling_timeout = os.getenv('pylenium.polling_timeout', 200) 
    
    # should pylenium capture screenshots on failure? -> default: [enabled]
    capture_screenshot = os.getenv('pylenium.screenshot', True)
    
    # should we capture page source as HTML on failure -> default: [enabled]
    capture_pagesource = os.getenv('pylenium.pagesource', True) 
    
    # should pylenium click with javascript?
    #  @options -> 'true', 'false', 'only-on-failure' (only when clicking is failing normally)
    # -> default: [disabled]
    javascript_clicking = os.getenv('pylenium.js_click', False)  
    
        # should pylenium send_keys with javascript?
    #  @options -> 'true', 'false', 'only-on-failure' (only when sending keys is failing normally)
    # -> default: [disabled]
    javascript_sendkeys = os.getenv('pylenium.js_sendkeys', False) 
    
    # default find() lookup, takes CSS by default but customisable
    #  @options -> All of seleniums standard BY locators
    # -> default: [css_selector]
    selector_default = Selector.CSS  
```

---
