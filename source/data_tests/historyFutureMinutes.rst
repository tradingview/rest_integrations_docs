.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyFutureMinutes
--------------------
..Test for handling history requests with ``to`` in the future (for 1-minute resolution).

Checking correct behavior, when to parameter is in the future for minute resolutions. Expecting to receive the correct 
answer. Then checking that the last bar is opened, that is the time in minutes of the last bar >= time at which the 
request was made. If not executed, then the corresponding warning is added to the logs. It is not considered an error, 
as there might be gaps and you can\'t always expect an opened bar. It is recommended to look for warnings in the logs 
during testing, and analyze if this is normal or not. If ``has-intraday`` field is equal to ``false`` for the symbol in 
the symbol info, then the test for this symbol will be skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

.. 🔥 needs explanation with pictures

Wrong no_data response
  * There are data available before range for which the ``no_data`` response without ``nb`` field was received. There 
    should be no such data available.
  * There are data available for wider range with the same ``to`` param as in narrower range for which the ``no_data`` 
    response without ``nb`` field was received. There should be no such data available.
  * ``nb`` field in ``no_data`` response contains time which is after ``from`` time.
