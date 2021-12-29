.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyRepeatability
--------------------
.. Test for historical data repeatability

Checking if historical API returns the same data for the same requests. If ``has-intraday`` value is equal to false 
for the symbol in the symbol info, then the test for this symbol will be skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

Data mismatch
  The exact same request returns different data.