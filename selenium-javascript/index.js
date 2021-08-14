// Click the button to open the system
var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    Key = webdriver.Key,
    until = webdriver.until;
var chrome = require("selenium-webdriver/chrome");
var fs= require("fs");

var options = new chrome.Options();
options.addArguments("--start-maximized"); // Maximize at startup, instead of maximizing after using maximize () later
options.addArguments("--disable-popup-blocking");
options.addArguments("no-sandbox");
options.addArguments("disable-extensions");
options.addArguments("no-default-browser-check");

if(chrome.getDefaultService() == null) {
    var service;        

    // After installing exe, find chromedriver.exe in the root directory
    if(fs.existsSync(path.join(__dirname, '../../chromedriver.exe'))) {
        console.log(path.join(__dirname, '../../chromedriver.exe'));
        service = new chrome.ServiceBuilder(path.join(__dirname, '../../chromedriver.exe')).build();            
    }

    // Look for chromedriver during development
    if(fs.existsSync(path.join(__dirname, './chromedriver.exe'))) {
        console.log(path.join(__dirname, './chromedriver.exe'));
        service = new chrome.ServiceBuilder(path.join(__dirname, './chromedriver.exe')).build();
    }

    chrome.setDefaultService(service);    
}

driver = new webdriver.Builder()
    .setChromeOptions(options)
    .withCapabilities(webdriver.Capabilities.chrome())
    .forBrowser('chrome')
    .build();
