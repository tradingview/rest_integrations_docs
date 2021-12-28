.. links
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming

Streaming
---------

Server constantly keeps the connection with `/streaming`_ alive. If the connection is broken - the server constantly 
tries to restore it. TradingView establishes up to 4 simultaneous connections to this endpoint and expects to get the 
same data to all of them. Unnecessary restrictions (firewall, rate limits, etc.) should be disabled on the broker's 
side for the provided TradingView IP addresses.

Websocket isn\'t supported. Transfer mode is ``chunked encoding`` using the ``Transfer-Encoding: chunked`` mechanism. 
All intermediate proxies must also support this mode. All messages must end with ``\n``. Streaming should contain 
real-time data only. It shouldn\'t contain snapshots of data. The connection should not be interrupted by the server.

Data feed should provide trades and quotes:

* If trades are not provided, then data feeds should set trades with bid price and bid size (mid price with ``0`` size 
  in case of Forex).
* Size is always greater than 0, except for the correction. In that case size can be ``0``.
* Quote must contain prices of the best ask and the best bid.
* Daily bars are required if they cannot be built from trades (has-daily should be set to true in the symbol information 
  in that case).

Aggregation of ticks is possible within no more than one second. We monitor delays, and they should not exceed the 
:ref:`set threshold <trading-configuring-pulling-intervals>`.