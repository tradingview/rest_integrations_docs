.. links
.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/getOrders
.. _`/ordersHistory`: https://www.tradingview.com/rest-api-spec/#operation/getOrdersHistory
.. _`Modify Position`: https://www.tradingview.com/rest-api-spec/#operation/modifyPosition

Concepts
--------

.. contents:: :local:
   :depth: 2

.. _section-concepts-orders:

🎾 Orders 
.........
`/orders`_ is used to get current session orders and orders with ``working`` status from previous sessions. Orders with
``rejected``, ``filled``, ``cancelled`` status should be included in the list till the end of the trading session or
at least within 1 minute after changing order status.

🎾 Orders history
.................
`/ordersHistory`_ is used to get order history for an account. It is expected that returned orders will have a final status 
(``rejected``, ``filled``, ``cancelled``). This endpoint is optional. If you don\'t support orders history, please set 
``AccountFlags::supportOrdersHistory`` to ``false``.
The ``accountId`` parameter is required.

.. _section-concepts-brackets:

🎾 Brackets
...........
By brackets in our UI we mean :ref:`orders<section-concepts-orders>`, the meaning of which is to protect the 
:ref:`position<section-concepts-positions>`. Brackets always have the opposite side to the order or position that is their 
parent. The quantity in bracket orders is always equal to the quantity of their parent order. 

Brackets can exist either in a pair (:term:`Stop-Loss` and :term:`Take-Profit`) or separately. This means that an
order or a position can have only one bracket order (*Stop-Loss* or *Take-Profit*). If a pair exists, bracket orders
are linked by an :term:`OCO` (One-Cancels-the-Other) ​condition. It means that when one bracket order is executed, the 
other (if any) is automatically cancelled. When one of the brackets is partially executed, the quantity​ in the second 
bracket order ​should be​ automatically reduced to the left ​quantity of​ the partially executed bracket order ​on the 
broker's side​.

🎾 Order Brackets
~~~~~~~~~~~~~~~~~
To support order brackets in our UI, the ``supportOrderBrackets`` flag must be set to ``true``. In this case, when 
switching to the order editing mode, sections for bracket orders will appear.

Placing a parent order with brackets
''''''''''''''''''''''''''''''''''''
When placing an order with brackets through our UI, a POST request is sent to the broker's server with ``stopLoss`` 
and ``takeProfit`` fields or one of them. If the parent order has not been executed immediately, then in the next 
response to the request `/orders`_, we expect the parent order to appear in ``working`` status and one or two (depending 
on the presence of fields ``stopLoss`` and ``takeProfit``) in ``inactive`` status. Bracket orders in `/orders`_ 
necessarily have a ``parentId`` field, the value of which is the ``id`` of their parent order. The ``parentType`` field 
of bracket orders has the value ``order``.

Modifying parent order with brackets, adding or removing brackets
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
The result of editing the order in our UI is a PUT request to the broker's server with new order parameters, including 
``stopLoss`` and ``takeProfit`` fields or one of them. If the user has deleted one of the brackets when changing the 
parent order, then it is necessary to send a removed bracket order with ``cancelled`` status in subsequent responses to 
the `/orders`_ request. Otherwise, an error will be occur: this bracket will "hang" in our user interface in the table 
of orders and on the chart. The cancellation of one of the brackets should not drive to the cancellation of another 
bracket order and parent order.

Execution of a parent order with brackets
'''''''''''''''''''''''''''''''''''''''''
Bracket orders are bound to the parent order by the :term:`OSO` (One-Send-Other) condition. When a parent order 
executed, bracket orders are transferred to the ``working`` status. If bracket positions are supported, the 
``parentId`` field of the brackets gets the ``id`` value of the position that resulted from the parent order execution, 
and the ``parentType`` field of the bracket orders changes its value to ``position``.

Canceling a parent order with brackets
''''''''''''''''''''''''''''''''''''''
Bracket orders are bound to the parent order by the :term:`OSO` condition. Therefore, when cancelling a parent order,
the brackets must also be cancelled.

🎾 Position brackets
~~~~~~~~~~~~~~~~~~~~
Support of position brackets becomes problematic if a broker does not have support for multi positions. To support 
position brackets in our UI, the ``supportPositionBrackets`` flag must be set to ``true``. When the user switches to
edit mode, sections for bracket orders will appear.

Position brackets are supported
'''''''''''''''''''''''''''''''
When one of the bracket orders is executed, the position is reset ot zero, and the other bracket order (if any) 
is transferred to the ``cancelled`` status. When one of the bracket orders is partially executed, the ​quantity​ in the 
position is reduced by the executed ​quantity​. The ​quantity​ in the other bracket order is given according to the left ​
quantity​ in the partially executed bracket order.

When the user adds brackets to the position, the broker's server recieves a PUT request `Modify Position`_, which
contains ``stopLoss`` and ``takeProfit`` fields, or one of them.

Then these bracket orders returns with ``working`` status to `/orders`_ with next values:
* ``parentId`` --- the value of the position id,
* ``parentType`` --- the value of the ``position``,
* ``qty`` --- 	the number of units.

When the user closes position, the brackets should be cancelled and sent to `/orders`_ with the ``cancelled`` 
status.

Position brackets are not supported
'''''''''''''''''''''''''''''''''''
In this case, after the parent order is executed, the brackets don't receive the position id to the ``parentId`` field
and are no longer linked to the parent order. But the :term:`OSO` brackets binding between each other must 
be kept on the broker's side. When a position closed, all orders in the transit statuses (``placing``, ``inactive``,
``working``) are usually canceled.

.. _section-concepts-positions:

.. 🚧
Positions
..........

Positions come in two main types. A :term:`Long position` formed as a result of buying a symbol, in contrast, a 
:term:`Short position` is a result of selling a symbol.

There are no positions for the *Crypto Spots*, but they are present for the *Crypto Derivatives*.
For the *Forex* you can use multidirectional positions. Enable ``supportMulitposition`` flag on the 
`/accounts`_ endpoint to use it.

Available operations for the postions:
* Protect Position
* Close Position
* Reverse Position

You can display *Position* in the :ref:`Account Manager<section-ui-accountmanager>` and on the 
:ref:`Chart<section-ui-chart>`.

.. tip::

  #. Open a position using a market order with TP and SL.
  #. Got a position with brackets (TP and SL).
  #. Close the position.
  #. brackets are canceled too.


🎾 Pip Value
............

For Forex instruments, the ``pipValue`` size depends on the rapidly changing cross rate of currencies. You should always
send the actual value. Besides `/instruments`_ ``pipValue`` can be sended via `/quotes`_ in the ``buyPipValue`` and 
``sellPipValue`` fields. But, if you do not have support for different ``pipValue`` for buy and sell, you should pass
the same values in both fields. The main purpose of ``pipValue`` is calculate risks in an
:ref:`Order Ticket<section-uielements-orderticket>` (for those who use it).

.. tip::

   Calculating the *Pip Value* is easy. Let's say the currency is equal to ``CCC``.

   * For the ``XXXCCC`` pair: ``pipValue = pipSize``
   * For the ``CCCXXX`` pair: ``pipValue = 1 / CCCXXX * pipSize``
   * For the ``YYYXXX`` pair: ``pipValue = pipSize * XXXCCC`` or ``pipValue = pipSize / CCCXXX``

   Next, we multiply by ``lotSize`` and ``qty`` for the current order.

* ``minTick`` --- a minimum price movement,
* ``pipSize`` --- size of 1 pip, for Forex symbol usually equals ``minTick * 10``.

For example for EURUSD pair ``minTick = 0.00001`` and ``pipSize = 0,0001``.
