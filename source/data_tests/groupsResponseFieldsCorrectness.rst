.. links
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups

groupsResponseFieldsCorrectness
-------------------------------
.. Response format correctness for `/groups`_

* This test checks if response format for `/groups`_ is correct.

Request error
  Error on sending HTTP request to `/groups`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/groups`_ endpoint.

Invalid status code
  Response status code is not ``200``.

Invalid content type
  Response header ``Content-Type`` must contain ``application/json``.

Parse error
  Response body is not compliant with the `/groups`_ specification.

  * Response body is not a JSON data.
  * ``s`` field is not equal to ``ok``.
  * ``id`` field must be a lower-case string made from Latin letters and underscore character.
  * Each ``id`` must have the same prefix ending with an underscore character.
