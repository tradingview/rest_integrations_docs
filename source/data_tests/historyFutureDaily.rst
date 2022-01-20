.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyFutureDaily
------------------
.. Test for handling history requests with ``to`` in the future (for daily resolution).

Checking correct behavior, when ``to`` parameter is in the future for daily resolutions. Expecting to receive the 
correct answer, then checking the time bars in the response --- they should not exceed the time at which the request 
was made. If ``has-daily`` is equal to false for the symbol in the symbol info, then this test for the symbol will be 
skipped.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

.. 🔥 needs explanation with pictures

Wrong no_data response
  * there are data available before range for which the ``no_data`` response without ``nb`` field was received. There 
    should be no such data available.
  * there are data available for wider range with the same ``to`` param as in narrower range for which the ``no_data`` 
    response without ``nb`` field was received. There should be no such data available.
  * ``nb`` field in ``no_data`` response contains time which is after ``from`` time.

Incorrect bar time
  Time of the bar is in the future.