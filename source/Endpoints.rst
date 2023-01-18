Endpoint requirements
**********************

Required endpoints
...................

The table below lists the required endpoints and their descriptions.

+------------------+------------------------------------------------------------------------------------------------------+
| Endpoint         | Description                                                                                          |
+==================+======================================================================================================+
| `/accounts`_     | Gets a list of accounts owned by a user.                                                             |
+------------------+------------------------------------------------------------------------------------------------------+
| `/config`_       | Gets localized configuration.                                                                        |
+------------------+------------------------------------------------------------------------------------------------------+
| `/instruments`_  | Gets the list of the instruments that are available for trading with the specified account.          |
+------------------+------------------------------------------------------------------------------------------------------+
| `/orders`_       | Gets current session orders for the account.                                                         |
+------------------+------------------------------------------------------------------------------------------------------+
| `/state`_        | Gets account information.                                                                            |
+------------------+------------------------------------------------------------------------------------------------------+
| `/quotes`_       | Gets current prices of the instruments.                                                              |
|                  |                                                                                                      |
|                  | Note that `/quotes`_ is not a strictly required endpoint.                                            |
|                  | However, TradingView highly recommends implementing it due to possible delays in data from exchange. |
|                  | This may lead users' orders to execute at unexpected prices.                                         |
+------------------+------------------------------------------------------------------------------------------------------+

Optional endpoints
...................

The table below describes optional endpoints which can be required in several cases.

+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Endpoint           | Description                                                                   | When required                                                                                                          |
+====================+===============================================================================+========================================================================================================================+
| `/authorize`_      | Authenticates users by their usernames and passwords.                         | Required when Password Bearer authentication type is used.                                                             |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/logout`_         | Logs users out from broker accounts.                                          | Required when ``supportLogout: true``` is set in the `/accounts`_ endpoint.                                            |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/mapping`_        | Gets all broker symbols matched to TradingView ones.                          | Required when you use TradingView market data that is available from a third-party source.                             |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/positions`_      | Modifies an existing position stop loss or take profit or both.               | Required unless ``supportPositions: false`` is set in `/accounts`_. Not used in Crypto Spot trading.                   |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/balances`_       | Gets crypto balances for an account.                                          | Required for Crypto brokers.                                                                                           |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/executions`_     | Gets a list of executions (fills or trades) for an account and an instrument. | Required when ``supportExecutions: true`` is set in `/accounts`_.                                                      |
|                    |                                                                               | If `/executions`_ is not implemented, transactions will not be displayed on the Chart.                                 |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/ordersHistory`_  | Gets order history for an account.                                            | Required when ``supportOrdersHistory: true`` is set in `/accounts`_.                                                   |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/previewOrder`_   | Gets estimated cost, commission, and other order information                  | Required when either ``supportPlaceOrderPreview`` or ``supportModifyOrderPreview`` is set to ``true`` in `/accounts`_. |
|                    | without the order actually being placed or modified.                          |                                                                                                                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/quotes`_         | Gets current prices of the instruments.                                       | Required when instruments with ``hasQuotes: true`` are present in the `/instruments`_ response.                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/depth`_          | Gets current depth of market for the instrument.                              | Required when ``supportLevel2Data: true`` is set in `/accounts`_.                                                      |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/getLeverage`_    |                                                                               | Required when ``supportLeverage: true`` is set in `/accounts`_.                                                        |
|                    |                                                                               |                                                                                                                        |
| `/setLeverage`_    |                                                                               |                                                                                                                        |
|                    |                                                                               |                                                                                                                        |
| `/previewLeverage`_|                                                                               |                                                                                                                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/groups`_         | Gets a list of possible symbol groups.                                        | Required when different types of instruments are used or when you need to restrict access on market data for users.    |
|                    |                                                                               |                                                                                                                        |
| `/permissions`_    | Gets a list of symbol groups allowed for a user.                              |                                                                                                                        |
+--------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| `/symbol_info`_    | Gets a list of all instruments.                                               | Required when data integration is used.                                                                                |
|                    |                                                                               |                                                                                                                        |
| `/history`_        | Gets history data for instruments.                                            |                                                                                                                        |
|                    |                                                                               |                                                                                                                        |
| `/streaming`_      | Gets real-time prices for instruments.                                        |                                                                                                                        |
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
