.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyCountbackMinutes
-----------------------
.. Count back minutes

* This test requests 1-minute resolution using ``countback`` parameter, expecting that the number of bars in the 
  response is equal to ``countback`` value. 
* The test fails if more bars than the ``countback`` value were received. 
* If fewer bars were received, the test checks that there are no data available beyond the oldest bar from the first 
  response. 
* If ``"has-intraday"=false`` is specified for the symbol in the symbol info, then the test for this symbol will be 
  skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

Parse error
  Error parsing response body.

Too many bars
  The number of bars in response is greater than specified in ``countback`` param.

Too few bars
  There are more bars available, but ``countback`` request returned smaller number of bars than specified in 
  ``countback`` param.