.. links
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize

authBasicNewTokenPerRequest
---------------------------
.. New token in each response

* Expect that each request to `/authorize`_ returns new unique token.

Request error
  Error on sending HTTP request to `/authorize`_ endpoint

Read error
  Error reading body of HTTP response to request to `/authorize`_ endpoint

Status code
  Response status code is not 200

Parse error
  Error parsing response body

  * Response body is not a JSON data.
  * The ``s`` field is not equal to ``ok``.
  * ``access_token`` field is empty.
  * ``expiration`` field is not a number.
  * ``expiration`` field is not an integer number.

Duplicate token
  One or more tokens are equal in 10 sequential requests to `/authorize`_ endpoint.