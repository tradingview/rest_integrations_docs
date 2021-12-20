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
status. This endpoint is optional. If you don\'t support orders history, please set ``supportOrdersHistory: false`` in 
the `/accounts`_ to ``false``. The ``accountId`` parameter is required.

.. _trading-concepts-brackets:

Brackets
........

By brackets in our UI we mean :ref:`orders<trading-concepts-orders>`, the meaning of which is to protect the
:ref:`position<trading-concepts-positions>`. Brackets always have the opposite side to the order or position compared
to its parent. The quantity in bracket orders is always equal to the quantity of their parent order.

Brackets can exist either in a pair (:term:`Stop-Loss` and :term:`Take-Profit`) or separately. This means that the
order or position can have only one bracket order (*Stop-Loss* or *Take-Profit*). If a pair exists, bracket orders are
linked by an :term:`OCO` (One-Cancels-the-Other) condition. It means that when one bracket order is executed, the other
(if any) is automatically cancelled. When one of the brackets is partially executed, the ``quantity`` in the second 
bracket order should be automatically reduced to the remaining quantity of the partially executed bracket order on the 
broker\'s side.

Order Brackets
~~~~~~~~~~~~~~

The ``supportOrderBrackets`` flag must be set to ``true`` to support order brackets in our UI. In this case, sections
for bracket orders will appear when switching to the order editing mode.

Placing a parent order with brackets
''''''''''''''''''''''''''''''''''''

When placing an order with brackets through our UI, a POST request is sent to the broker\'s server with ``stopLoss`` and
``takeProfit`` fields or one of them. If the parent order has not been executed immediately, then we expect the parent
order to appear in ``working`` status, and one or two (depending on the presence of fields ``stopLoss`` and 
``takeProfit``) in ``inactive`` status in the next response to the `/orders`_ request. 

It is necessary for bracket orders in `/orders`_ to have a ``parentId`` field, the value of which is the ``id`` of their
parent order. The ``parentType`` field of bracket orders has the ``order`` value.

Modifying parent order with brackets, adding or removing brackets
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The result of editing the order in our UI is a PUT request to the broker\'s server with new order parameters, including
``stopLoss`` and ``takeProfit`` fields, or one of them. If the user has deleted one of the brackets when changing the
parent order, then it is necessary to send a removed bracket order with ``cancelled`` status in subsequent responses to
the `/orders`_ request. Otherwise, an error will come up: this bracket will “hang” in our user interface in the table
of orders and on the chart. The cancellation of one of the brackets should not lead to the cancellation of another
bracket order and the parent order.

Execution of a parent order with brackets
'''''''''''''''''''''''''''''''''''''''''

Bracket orders are bound to the parent order by the :term:`OSO` (One-Send-Other) condition. When a parent order is
executed, bracket orders are transferred to the ``working`` status. If bracket positions are supported, the ``parentId``
field of the brackets gets the ``id`` value of the position that resulted from the parent order execution, and the
``parentType`` field of the bracket orders changes its value to ``position``.

Canceling a parent order with brackets
''''''''''''''''''''''''''''''''''''''

Bracket orders are bound to the parent order by the :term:`OSO` condition. Therefore, when cancelling a parent order,
the brackets must also be cancelled.

Position brackets
~~~~~~~~~~~~~~~~~

The UI behavior differs depending on whether the broker supports bracket position or not. To support position brackets,
the ``supportPositionBrackets`` flag must be set to ``true``. So, when the user switches to edit mode, sections for
bracket orders will appear.

Support of position brackets vary if a broker does not have support for multiple positions at one instrument at the
same time. Muliple position means that each trade opens its own separate position, to which you can add brackets and 
which can only be closed completely. If you support multi position set the ``supportMultiposition`` flag in the
`/accounts`_ to ``true``. Set it into ``false`` and the behavior will be as you wish. Trades will net position.

Position brackets are not supported
'''''''''''''''''''''''''''''''''''

In this case, after the parent order is executed, the brackets don\'t receive the position id to the ``parentId`` field
and are no longer linked to the parent order. But the :term:`OSO` brackets binding between each other must be kept on
the broker\'s side. When a position is closed, all orders in the transit statuses (``placing``, ``inactive``,
``working``) are usually canceled.

Position brackets are supported
'''''''''''''''''''''''''''''''

When one of the bracket orders is executed, the position is reset to zero, and the other bracket order (if any) is
transferred to the ``cancelled`` status. When one of the bracket orders is partially executed, the quantity in the
position is reduced by the executed quantity. The quantity in the other bracket order is given according to the left
quantity in the partially executed bracket order.

When the user adds brackets to the position, the broker\'s server recieves a PUT request `Modify Position`_, which
contains ``stopLoss`` and ``takeProfit`` fields, or one of them.

Then these bracket orders return with ``working`` status to `/orders`_ with next values:

* ``parentId`` --- the value of the position ``id`` field,
* ``parentType`` --- the value of the ``position`` field,
* ``qty`` --- the number of units.

When the user closes position, the brackets should be cancelled and sent to `/orders`_ with the ``cancelled`` status.

.. tip::

  #. Open a position using a market order with :term:`Take-Profit` and :term:`Stop-Loss`.
  #. Got a position with brackets (:term:`Take-Profit` and :term:`Stop-Loss`).
  #. Close the position.
  #. Brackets are canceled too.

.. _trading-concepts-positions:

Positions
..........

Positions come in two main types: a :term:`Long position` is formed as a result of buying a symbol, when a 
:term:`Short position` is formed as a result of selling a symbol.

There are no positions for the *Crypto Spots*, but they are present for the *Crypto Derivatives*.
For the *Forex* you can use multidirectional positions. Set ``supportMultiposition: true`` in the `/accounts`_ to use 
it.

You can display *Position* in the :ref:`Account Manager<trading-ui-accountmanager>` and on the 
:ref:`Chart<trading-ui-chart>`.

Available operations for the postions: *Protect Position*, *Reverse Position*, and `Close Position`_. Use flags in
the `/accounts`_ → ``d`` → ``config`` to hide its operations.

* Set ``supportPositionBrackets`` to ``false`` to hide *Protect Position*
* Set ``supportReversePosition`` to ``false`` to hide *Reverse Position*

.. _trading-concepts-pipvalue:

Pip Value
.........

The main purpose of ``pipValue`` is to calculate risks in an :ref:`Order Ticket<trading-ui-orderticket>` (for 
those who use it). This parameter\'s value is specified in the account currency.

For Forex instruments, the ``pipValue`` size depends on the rapidly changing currency cross rates. You should always 
send the actual value. Besides `/instruments`_, ``pipValue`` can be sent via `/quotes`_ in the ``buyPipValue`` and 
``sellPipValue`` fields. However, if you do not have support for different ``pipValue`` for buy and sell, you should 
pass the same values in both fields.

If ``supportPLUpdate`` is set to ``true``, ``pipValue`` used for the calculating position profit. But the profit is 
fixed when the position is closed:

* at Bid — when Short position closed,
* at Ask — whet Long position closed.

.. tip::

   Calculating the *Pip Value* is easy. Let's say the account currency is equal to ``CCC``.

   * For the ``XXXCCC`` pair: ``pipValue = pipSize``
   * For the ``CCCXXX`` pair: ``pipValue = 1 / CCCXXX * pipSize``
   * For the ``YYYXXX`` pair: ``pipValue = pipSize * XXXCCC`` or ``pipValue = pipSize / CCCXXX``

   Next, we multiply by ``lotSize`` and ``qty`` for the current order.

* ``pipSize`` --- size of 1 pip, for Forex symbol usually equals ``minTick * 10``,
* ``minTick`` --- a minimum price movement.

For example for EURUSD pair ``minTick = 0.00001`` and ``pipSize = 0,0001``.
