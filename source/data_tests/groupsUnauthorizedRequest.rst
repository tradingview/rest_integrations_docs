.. links
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups

groupsUnauthorizedRequest
-------------------------
.. Unauthorized request

* Sending `/groups`_ request without token, expecting to get status code ``401``. 
* This test will be skipped if the API does not use authorization.

Request error
  Error on sending HTTP request to `/groups`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/groups`_ endpoint.

Invalid status code
  Response status code is expected to be ``401 Unauthorized``.