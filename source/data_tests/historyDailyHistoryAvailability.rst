.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyDailyHistoryAvailability
-------------------------------
.. Daily historical data availability test

This test checks if historical data available for symbols with daily resolutions. If ``"has-daily" = false`` is 
specified for the symbol in the symbol info, then the test for this symbol will be skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

.. 🔥 needs explanation with pictures

Wrong ``no_data`` response
  * There are data available before range for which the ``no_data`` response without ``nb`` field was received. 
    There should be no such data available.
  * There are data available for wider range with the same ``to`` param as in narrower range for which the ``no_data`` 
    response without ``nb`` field was received. There should be no such data available.
  * ``nb`` field in ``no_data`` response contains time which is after ``from`` time.

Invalid session
  Symbol session cannot be parsed.

Invalid bar time
  Time in daily bar is incorrect. The bar time must be aligned to start of the session.