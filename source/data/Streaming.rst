.. links
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo
.. _`chunked transfer encoding`: https://en.wikipedia.org/wiki/Chunked_transfer_encoding

Streaming
---------

Our client keeps the connection with `/streaming`_ endpoint alive. If the connection is broken, the client immediately 
tries to recreate it. TradingView establishes up to 4 simultaneous connections to this endpoint and expects to get the 
same data to all of them. Unnecessary restrictions (firewall, rate limits, etc.) should be disabled on the broker's 
side for the provided TradingView IP addresses.

We use HTTP 1.1 `chunked transfer encoding`_ as a streaming transport, WebSocket protocol is not supported. All 
intermediate proxies must also support this mode. All messages must end with ``\n``. Streaming should contain real-time
data only. It shouldn\'t contain snapshots of data. Server must not close the connection.

Data feed should provide trades and quotes:

* If trades can't be provided, then the API should send artificial trades with bid price and bid size (mid price with 
  ``0`` size in case of Forex).
* Size must be greater than ``0``.
* Quote must contain prices of the best ask and the best bid.
* Daily updates are required only if the API provides daily resolution in historical data (``has-daily`` field in 
  `/symbol_info`_ must be set to ``true``).

Aggregation of trades is possible within one second or less.

Streaming updates must be send as soon as possible. Delay must not exceed 1 second.