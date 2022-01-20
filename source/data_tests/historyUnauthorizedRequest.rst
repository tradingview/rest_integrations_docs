.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyUnauthorizedRequest
--------------------------
.. Unauthorized request to `/history`_

Sending `/history`_ request without token, expecting to get status code ``401``. This test will be skipped if the API 
does not use authorization.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is expected to be ``401 Unauthorized``.