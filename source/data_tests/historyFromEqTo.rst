.. links
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory

historyFromEqTo
---------------
.. It is expected that only one bar is returned to the request where ``from`` quals ``to``.

If bar exists, then this bar will be returned to the request where ``from`` equals ``to`` and quals this bar\'s time.

Request error
  Error on sending HTTP request to `/history`_ endpoint.

Read error
  Error reading body of HTTP response to request to `/history`_ endpoint.

Invalid status code
  Response status code is not ``200``.

Parse error
  Error parsing response body.

Invalid bars number
  🔥

Wrong bar
  Returned bar does not match the requested one.