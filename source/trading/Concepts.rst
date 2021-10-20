.. links
.. _/orders: https://www.tradingview.com/rest-api-spec/#operation/getOrders
.. _/ordersHistory: https://www.tradingview.com/rest-api-spec/#operation/getOrdersHistory

Concepts
--------

.. contents:: :local:
   :depth: 3

Orders
......
Use `/orders`_ to get current session orders for the account. It also includes working orders from previous sessions. 
Filled/cancelled/rejected orders should be included in the list till the end of the session.
The ``accountId`` parameter is required.

Orders history
..............
Use `/ordersHistory`_ to get order history for an account. It is expected that returned orders will have a final status 
(``rejected``, ``filled``, ``cancelled``). This endpoint is optional. If you don\'t support orders history, please set 
``AccountFlags::supportOrdersHistory`` to ``false``.
The ``accountId`` parameter is required.

.. todo
   - Positions
   - Brackets
   - PipValue
