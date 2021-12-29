.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyPriceMatch
-----------------
.. Test for open and close prices of a daily bar

Checking that open and close prices of a daily bar match the corresponding open price of the first 1-minute bar and 
close price of the last 1-minute bar of the session. If ``has-daily`` value is equal to false or ``has-intraday`` 
value is equal to false for the symbol in the symbol info, then the test for this symbol will be skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

.. 🔥 needs explanation with pictures

Wrong no_data response.
  * There are data available before range for which the ``no_data`` response without ``nb`` field was received. There 
    should be no such data available.
  * There are data available for wider range with the same ``to`` param as in narrower range for which the ``no_data`` 
    response without ``nb`` field was received. There should be no such data available.
  * ``nb`` field in ``no_data`` response contains time which is after ``from`` time.

Invalid open price
  An open price of a daily bar does not match an open price of a minute bar.

Invalid close price
  A close price of a daily bar does not match a close price of a minute bar.