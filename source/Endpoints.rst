Endpoint requirements
-----------------------

Before integrating your broker's platform into TradingView,
you should review the list of required and optional endpoints.
This will allow you to understand which endpoints are needed for the features you'd like to have.

.. note::
  If you are not sure what endpoints you need in your particular case, contact the TradingView team.

Required endpoints
...................

The endpoints listed below are required for both trading and data integration.

+------------------+----------------------------------------------------------------------------------------------------------+
| Endpoint         | Description                                                                                              |
+==================+==========================================================================================================+
| `/accounts`_     | Gets a list of accounts owned by a user.                                                                 |
+------------------+----------------------------------------------------------------------------------------------------------+
| `/config`_       | Gets localized configuration.                                                                            |
+------------------+----------------------------------------------------------------------------------------------------------+
| `/instruments`_  | Gets the list of the instruments that are available for trading with the specified account.              |
+------------------+----------------------------------------------------------------------------------------------------------+
| `/orders`_       | Gets current session orders for the account.                                                             |
+------------------+----------------------------------------------------------------------------------------------------------+
| `/state`_        | Gets account information.                                                                                |
+------------------+----------------------------------------------------------------------------------------------------------+

Data related endpoints
=======================

If you plan to use :ref:`data integration <data-integration>`, you also need to implement the following endpoints.

+--------------------+-------------------------------------------------------------------------------+
| Endpoint           | Description                                                                   |
+====================+===============================================================================+
| `/symbol_info`_    | Gets a list of all :ref:`instruments <symbol-info-endpoint>`                  |
|                    | and a set of rules for them.                                                  |
+--------------------+-------------------------------------------------------------------------------+
| `/history`_        | Gets :ref:`history data <history-endpoint>` for instruments.                  |
+--------------------+-------------------------------------------------------------------------------+
| `/streaming`_      | Gets :ref:`real-time prices <streaming-endpoint>` for instruments.            |
+--------------------+-------------------------------------------------------------------------------+
| `/mapping`_        | Gets all broker symbols that match TradingView ones.                          |
|                    | Required for :ref:`symbol mapping <symbol-mapping>` when you                  |
|                    | use TradingView market data that is available from a third-party source.      |
+--------------------+-------------------------------------------------------------------------------+
| `/groups`_         | Gets a list of possible :ref:`symbol groups <groups-endpoint>`.               |
|                    | Required when you use different instrument types and when you need to         |
|                    | restrict access to market data, hide symbols for some users,                  |
|                    | or prevent them from paying twice for a real-time data subscription.          |
+--------------------+-------------------------------------------------------------------------------+
| `/permissions`_    | Gets a list of symbol groups allowed for a user.                              |
|                    | Use it when you need to :ref:`restrict access <permissions-endpoint>` to      |
|                    | market data, hide symbols for some users,                                     |
|                    | or prevent them from paying twice for a real-time data subscription.          |
+--------------------+-------------------------------------------------------------------------------+

Optional endpoints
...................

The table below describes optional endpoints which can be required in several cases.

+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Endpoint           | Description                                                                   | When required                                                                                                          |
+====================+===============================================================================+========================================================================================================================+
| `/authorize`_      | Authenticates users by their usernames and passwords.                         | Required when :ref:`Password Bearer <password-bearer-flow>` authentication type is used.                               |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/logout`_         | Logs users out from broker accounts.                                          | Required when ``supportLogout: true``` is set in the `/accounts`_ endpoint.                                            |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/positions`_      | Modifies an existing position stop loss or take profit or both.               | Required unless ``supportPositions: false`` is set in `/accounts`_. Not used in Crypto Spot Trading.                   |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/balances`_       | Gets crypto balances for an account.                                          | Required for Crypto Spot Trading.                                                                                      |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/executions`_     | Gets a list of executions (fills or trades) for an account and an instrument. | Required when ``supportExecutions: true`` is set in `/accounts`_.                                                      |
|                    |                                                                               | If `/executions`_ is not implemented, transactions will not be displayed on the chart.                                 |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/ordersHistory`_  | Gets order history for an account.                                            | Required when ``supportOrdersHistory: true`` is set in `/accounts`_. All :ref:`orders <trading-concepts-orders>`       |
|                    |                                                                               | that come in response to ``/ordersHistory`` requests are displayed on the *History* tab.                               |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/previewOrder`_   | Gets estimated cost, commission, and other order information                  | Required when either ``supportPlaceOrderPreview`` or ``supportModifyOrderPreview`` is set to ``true`` in `/accounts`_. |
|                    | without the order actually being placed or modified.                          |                                                                                                                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/quotes`_         | Gets current instrument prices.                                               | TradingView highly recommends implementing `quotes`_ due to possible delays in data from the exchange.                 |
|                    |                                                                               | This may lead users' orders to execute at unexpected prices.                                                           |
|                    |                                                                               |                                                                                                                        |
|                    |                                                                               | Required when instruments with ``hasQuotes: true`` are present in the `/instruments`_ response.                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/depth`_          | Gets current :ref:`depth of market <depth-of-market>` for the instrument.     | Required when ``supportLevel2Data: true`` is set in `/accounts`_.                                                      |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/getLeverage`_    | Gets changes on every action users do in order tickets.                       | Required when ``supportLeverage: true`` is set in `/accounts`_.                                                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/previewLeverage`_| Displays preview information when users edit the leverage.                    | Required when ``supportLeverage: true`` is set in `/accounts`_.                                                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/setLeverage`_    | Sets the leverage when users confirm changing it.                             | Required when ``supportLeverage: true`` is set in `/accounts`_.                                                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

.. links
.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/authorize`: https://www.tradingview.com/rest-api-spec/#operation/authorize
.. _`/balances`: https://www.tradingview.com/rest-api-spec/#operation/getBalances
.. _`/config`: https://www.tradingview.com/rest-api-spec/#operation/getConfiguration
.. _`/depth`: https://www.tradingview.com/rest-api-spec/#operation/getDepth
.. _`/executions`: https://www.tradingview.com/rest-api-spec/#operation/getExecutions
.. _`/getLeverage`: https://www.tradingview.com/rest-api-spec/#operation/getLeverage
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/history`: https://www.tradingview.com/rest-api-spec/#operation/getHistory
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/logout`: https://www.tradingview.com/rest-api-spec/#operation/logout
.. _`/mapping`: https://www.tradingview.com/rest-api-spec/#operation/getMapping
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/getOrders
.. _`/ordersHistory`: https://www.tradingview.com/rest-api-spec/#operation/getOrdersHistory
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions
.. _`/previewLeverage`: https://www.tradingview.com/rest-api-spec/#operation/previewLeverage
.. _`/previewOrder`: https://www.tradingview.com/rest-api-spec/#operation/previewOrder
.. _`/positions`: https://www.tradingview.com/rest-api-spec/#operation/getPositions
.. _`/quotes`: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _`/setLeverage`: https://www.tradingview.com/rest-api-spec/#operation/setLeverage
.. _`/state`: https://www.tradingview.com/rest-api-spec/#operation/getState
.. _`/streaming`: https://www.tradingview.com/rest-api-spec/#operation/streaming
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo
