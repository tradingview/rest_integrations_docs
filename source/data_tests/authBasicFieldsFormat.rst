.. links
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize

authBasicFieldsFormat
---------------------
.. Response format correctness test (`/authorize`_).

* In addition to general validation, it is verified that expiration is in the future.

Request error
  Error on sending HTTP request to `/authorize`_ endpoint

Read error
  Error reading body of HTTP response to request to `/authorize`_ endpoint

Invalid status code
  Response status code is not ``200``

Parse error
  Response body format is not compliant with the `/authorize`_ specification:

  * Response body is not a JSON data.
  * The ``s`` field is not equal to ``ok``.
  * ``access_token`` field is empty string or missing.
  * ``expiration`` field is not a number.
  * ``expiration`` field is not an integer number.

Invalid expiration time
  Expiration time of the token is wrong (is not in the future).