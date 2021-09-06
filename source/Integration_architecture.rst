Integration architecture
========================

What are the parts of the integration
-------------------------------------
The broker's integration consists of two independent parts: data integration based on a server-to-server architecture
and trading integration based on a client-server architecture.

Why data integration is needed
------------------------------
Data integration is necessary because the TradingView website can receive data from the TradingView server only,
where indicators are counted, server alerts work, etc. Therefore, market data must first be received by the TradingView
server and then transferred to the client side of the application.

In what cases it is possible not to integrate data
--------------------------------------------------
| It is possible not to integrate market data if it is already available on the TradingView server from another source,
  for example, directly from the exchange. This option is available for exchange data only.
| In this case, the broker implements the `/mapping <https://www.tradingview.com/rest-api-spec/#operation/getMapping>`_
  endpoint to solve the problem of :ref:`mapping<mapping-symbols-label>` symbols between TradingView and broker.

How trade integration works
---------------------------
When integrating trading, a client-server architecture is used, requests from the user's browser are sent directly to
the broker's server. The TradingView Server does not participate in this communication. An exception is the
`/permissions <https://www.tradingview.com/rest-api-spec/#operation/getPermissions>`_ request, which is sent from
the TradingView server to grant the user access to the data. When making requests from the client's browser, there is
a need to :ref:`configure the CORS policy<cors-policy-label>` on the broker's side.
