.. links
.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/getOrders
.. _`/ordersHistory`: https://www.tradingview.com/rest-api-spec/#operation/getOrdersHistory
.. _`/quotes`: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _`Modify Position`: https://www.tradingview.com/rest-api-spec/#operation/modifyPosition
.. _`Close Position`: https://www.tradingview.com/rest-api-spec/#operation/closePosition

Concepts
--------

.. contents:: :local:
   :depth: 1

.. _trading-concepts-orders:

Orders
......

The orders statuses can be divided into two groups in our API:

* transitional (``placing``, ``inactive``, ``working``),
* final (``rejected``, ``filled``, ``canceled``).

The status of an order can only change from transitional to final, but not vice versa.

Requests:

* In response to the `/orders`_ request, we expect ALL orders of the current trading session and orders with
  transitional statuses from previous trading sessions.
* In response to the `/ordersHistory`_ request, we expect ALL orders with final statuses from previous trading
  sessions.

Tab Display:

* The Orders tab displays all orders that come in response to the `/orders`_ request.
* The History tab displays all orders that come in response to the `/ordersHistory`_ request and orders from
  `/orders`_ that have the final status. So, orders with final statuses from `/orders`_ are simultaneously displayed
  on both the Orders and the History tabs.

`/orders`_ is used to get current session orders and orders with ``working`` status from the previous sessions. However,
orders, that have recieved final status must should be included in the list till the end of the trading session, or at 
least within 1 minute after changing order status.

`/ordersHistory`_ is used to get order history for the account. It is expected that returned orders would have a final
status. This endpoint is optional. If you don\’t support orders history, please set ``supportOrdersHistory: false`` in 
the `/accounts`_ to ``false``. The ``accountId`` parameter is required.

.. _trading-concepts-brackets:

Brackets
........

By brackets in our UI we mean :ref:`orders<trading-concepts-orders>`, the meaning of which is to protect the
:ref:`position<trading-concepts-positions>`. Brackets always have the opposite side to the order or position compared
to its parent. The quantity in bracket orders is always equal to the quantity of their parent order.

Brackets can exist either in a pair (:term:`Stop-Loss` and :term:`Take-Profit`) or separately. This means that the
order or position can have only one bracket order (*Stop-Loss* or *Take-Profit*). If a pair exists, bracket orders are
linked by an :term:`OCO` (One-Cancels-the-Other) ​condition. It means that when one bracket order is executed, the other
(if any) is automatically cancelled. When one of the brackets is partially executed, the ``quantity​`` in the second 
bracket order ​should be​ automatically reduced to the remaining ​quantity of​ the partially executed bracket order ​on the 
broker’s side​.

