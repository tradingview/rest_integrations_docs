Integration architecture
========================

What are the parts of the integration
-------------------------------------
| The broker's integration consists of two independent parts: data integration based on a server-to-server architecture
  and trading integration based on a client-server architecture.

Why data integration is needed
------------------------------
| The TradingView website can only receive data from the TradingView server. Indicators are counted on this server,
  as well as server alerts, etc. In order for the market data to be first received by the TradingView server, and then
  transferred to the client side, data integration is required.

In what cases it is possible not to integrate data
--------------------------------------------------
| Market data can come to the TradingView server from another source, for example, directly from the exchange.
  There is no need for market data integration in this case.
  Implement only the `/mapping <https://www.tradingview.com/rest-api-spec/#operation/getMapping>`_
  endpoint to :ref:`map the names<mapping-symbols-label>` of the broker's instruments to TradingView.

How trading integration works
-----------------------------
| The trading integration uses a "client-server" architecture: requests from the user's browser are sent directly to
  the broker's server. The TradingView server is not involved in this data exchange.
  An exception is a request to `/permissions <https://www.tradingview.com/rest-api-spec/#operation/getPermissions>`_.
  It is sent from the TradingView server to give the user access to the data.
  
| Requests from the client browser require a configured :ref:`CORS policy<cors-policy-label>` on the broker side.