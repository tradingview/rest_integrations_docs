.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyTimeCorrectness
----------------------
.. Test for bars timestamps

Checking that the time of the bars is increasing. If ``has-intraday`` field is equal to false for the symbol in the 
symbol info, then the test for this symbol will be skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

Session error
  The session in specified incorrectly.

Invalid bar time
  The time is not increasing from bar to bar.