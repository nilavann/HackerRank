#!/bin/python3

import re,sys
Regex = r'id="question-summary-(.+?)".*?class="question-hyperlink">(.+?)</a>.*?class="relativetime">(.+?)</'
webpageContent = sys.stdin.read()
questionDetails = re.findall( Regex, webpageContent, re.DOTALL)
for questionDetail in questionDetails:
    print( ";".join(questionDetail))