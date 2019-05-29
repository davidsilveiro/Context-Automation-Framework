#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import shutil
import time
import logging


# Scenario level objects are popped off context when scenario exits

def before_scenario(context, scenario):
    print ('User data:', context.config.userdata)

    # behave -D BROWSER=chrome

    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'firefox'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'firefox'

    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print ('Browser:', BROWSER, 'is invalid')

    context.browser.maximize_window()
    print('Before scenario\n')


def after_scenario(context, scenario):
    print('starting after_scenario')
    original_Path = os.getcwd()
    if scenario.status == 'failed':
        if not os.path.exists('failed_scenarios_screenshots'):
            os.makedirs('failed_scenarios_screenshots')

        os.chdir('failed_scenarios_screenshots')
        context.browser.save_screenshot(scenario.name + '_failed.png')
        os.chdir(original_Path)

    context.browser.quit()


def after_feature(context, feature):
    context.browser.quit()
    print('\nAfter Feature')
