.. links
.. _`/accounts`: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _`/instruments`: https://www.tradingview.com/rest-api-spec/#operation/getInstruments
.. _`/orders`: https://www.tradingview.com/rest-api-spec/#operation/getOrders
.. _`/ordersHistory`: https://www.tradingview.com/rest-api-spec/#operation/getOrdersHistory
.. _`/positions`: https://www.tradingview.com/rest-api-spec/#operation/getPositions
.. _`/quotes`: https://www.tradingview.com/rest-api-spec/#operation/getQuotes
.. _`Close Position`: https://www.tradingview.com/rest-api-spec/#operation/closePosition
.. _`Modify Position`: https://www.tradingview.com/rest-api-spec/#operation/modifyPosition
.. _`Place Order`: https://www.tradingview.com/rest-api-spec/#operation/placeOrder

Concepts
--------

.. contents:: :local:
   :depth: 1

.. _trading-concepts-orders:

Orders and order history
.........................

Orders
~~~~~~~

Orders are instructions to a broker to purchase or sell assets on a user's behalf.
On the TradingView platform, the *Orders* tab displays all orders received in response to `/orders`_.

.. image:: ../../images/Trading_Concepts_OrdersTab.png
    :alt: Orders tab
    :align: center

When an order is placed, it follows a process of order execution.
In the order execution process, orders have statuses that can be divided into two groups:

- Transitional
  
  - Placing — an order is registered by the broker, but the exchange has not confirmed the status yet.
  - Working — an order is created and approved by the exchange but not executed yet.
  - Inactive — an order is in the system, but not at work.

- Final

  - Filled — an order is successfully executed.
  - Canceled — an order is canceled by a user.
  - Rejected — an order is rejected for some reason, e.g., the exchange rejected the order.

.. important::
  The order status can only change from transitional to final, not vice versa.

The `/orders`_ endpoint is used to get *all* orders of the current :term:`trading session` 
and orders with transitional statuses from previous sessions (otherwise, the user will not see that there is a pending order).
Orders that have received the final status should be included in the list before the end of the session, 
or at least within *one minute* after the change in the order status.

Order history
~~~~~~~~~~~~~~

On the TradingView platform, the *History* tab displays all orders received in response to the `/ordersHistory`_ request
and orders with the final status received from `/orders`_ .
Orders with final statuses from `/orders`_ are simultaneously displayed on both the *Orders* and the *History* tabs.

.. image:: ../../images/Trading_Concepts_HistoryTab.png
    :alt: Orders history
    :align: center

The `/ordersHistory`_ endpoint is used to get order history for the account.
To provide order history for accounts, set ``supportOrdersHistory: true`` in the `/accounts`_ endpoint.

.. _trading-concepts-brackets:

Brackets
........

By brackets in our UI we mean :ref:`orders<trading-concepts-orders>`, the meaning of which is to protect the
:ref:`position<trading-concepts-positions>`. Brackets always have the opposite side to the order or position compared
to its parent. The quantity in bracket orders is always equal to the quantity of their parent order.

Brackets can exist either in a pair (:term:`Stop-Loss` and :term:`Take-Profit`) or separately. This means that the
order or position can have only one bracket order (*Stop-Loss* or *Take-Profit*). 

If a pair exists, bracket orders are linked by an :term:`OCO` (One-Cancels-the-Other) condition. It means that when 
one bracket order is executed, the other (if any) is automatically cancelled. When one of the brackets is partially 
executed, the ``quantity`` in the second  bracket order should be automatically reduced to the remaining quantity of 
the partially executed bracket order on the  broker\'s side.

Order Brackets
~~~~~~~~~~~~~~

The ``supportOrderBrackets`` flag in the `/accounts`_ must be set to ``true`` to support order brackets in our UI. In 
this case, sections for bracket orders will appear when switching to the order editing mode.

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
``stopLoss`` and ``takeProfit`` fields, or one of them. 

If the user has deleted one of the brackets when changing the parent order, then it is necessary to send a removed
bracket order with ``cancelled`` status in subsequent responses to  the `/orders`_ request. Otherwise, an error will 
come up: this bracket will “hang” in our user interface in the table of orders and on the chart. 

The cancellation of one of the brackets should not lead to the cancellation of another bracket order and the parent 
order.

Execution of a parent order with brackets
'''''''''''''''''''''''''''''''''''''''''

Bracket orders are bound to the parent order by the :term:`OSO` (One-Send-Other) condition. When a parent order is
executed, bracket orders are transferred to the ``working`` status. 

If bracket positions are supported, the ``parentId`` field of the brackets gets the ``id`` value of the position that 
resulted from the parent order execution, and the ``parentType`` field of the bracket orders changes its value to 
``position``.

Canceling a parent order with brackets
''''''''''''''''''''''''''''''''''''''

Bracket orders are bound to the parent order by the :term:`OSO` condition. Therefore, when cancelling a parent order,
the brackets must also be cancelled.

Leverage
''''''''

If you support leverage, the ``supportLeverage`` flag in the `/accounts`_ must be set to ``true``.

Trailing stop bracket
'''''''''''''''''''''

In order to support placing Trailing Stop brackets the ``supportTrailingStop`` in the `/accounts`_ must be set to
``true``. When this parameter is enabled, it will be possible to change Stop Loss bracket to Trailing Stop by clicking
on the bracket's name in the UI.

.. important::
  No other order besides Trailing Stop should contain ``trailingStopPips`` parameter, even if the value of this
  parameter will be set to zero.

Position brackets
~~~~~~~~~~~~~~~~~

The UI behavior differs depending on whether the broker supports bracket position or not. To support position brackets,
the ``supportPositionBrackets`` flag in the `/accounts`_ must be set to ``true``. So, when the user switches to edit 
mode, sections for bracket orders will appear.

Support of position brackets vary if a broker does not have support for multiple positions at one instrument at the
same time. Multiple position means that each trade opens its own separate position, to which you can add brackets and 
which can only be closed completely. If you support multi position set the ``supportMultiposition`` flag to ``true``. 

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

When the user adds brackets to the position, the broker\'s server receives a PUT request `Modify Position`_, which
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

There are two types of positions:

- :term:`Long position` is formed as a result of buying a symbol.
- :term:`Short position` is formed as a result of selling a symbol.

You can display *Positions* in the :ref:`Account Manager<trading-ui-accountmanager>` and on the *Chart*.

There are several details about positions that you need to consider:

- There are no positions for *Crypto Spots*, but they are present for *Crypto Derivatives*.
- Available operations for the positions include *Protect Position*, :ref:`Reverse Position<reverse-position>`, and :ref:`Close Position <close-position>`. Use flags in the `/accounts`_ → ``d`` → ``config`` to hide or enable the operations.
- You can use multidirectional positions for those instruments that support this feature, e.g., for crypto derivatives and *Forex*. To do this, set ``supportMultiposition: true`` in the `/accounts`_ endpoint.

.. _close-position:

Close Position
~~~~~~~~~~~~~~~

Users can close their positions in three ways:

- Via the *Chart*.
- Via the :ref:`DOM panel <depth-of-market>`.
- Via the *Account manager* panel, by right-clicking the position and selecting *Close Position*.

If you want users to be able to close their positions partially, set ``supportPartialClosePosition: true`` in the `/accounts`_ endpoint.
In the *Close position* pop-up window, an additional *Partial close* option appears, and users can specify the number of units to close.
In this case, the specified number is returned as the ``amount`` property in the `Close Position`_ endpoint.

.. image:: ../../images/Trading_UiElements_ClosePositionPartially.png
    :alt: Close Position Partially
    :align: center

.. important::
  Users won't be able to partially close the position if they enable the *Instant orders placement* option in the *Chart settings → Trading* section.
  Also in this case, the ``amount`` property is not returned in the `Close Position`_ endpoint.

.. _reverse-position:

Reverse Position
~~~~~~~~~~~~~~~~~

Users can reverse positions from long to short or from short to long in three ways:

- Via the *Chart*.
- Via the :ref:`DOM panel <depth-of-market>`, by clicking the *Reverse* button.
- Via the *Account manager* panel, by right-clicking the position and selecting *Reverse Position*.

.. note::
  If you want to hide the *Reverse Position* option, set ``supportReversePosition: false`` in the `/accounts`_ endpoint.

Also, you can make the integration natively support the position reverse.
To do this, set ``supportNativeReversePosition: true`` in the `/accounts`_ endpoint.
In this case, TradingView sends requests to the `Modify Position`_ endpoint with the ``side`` parameter set.

If ``supportNativeReversePosition: false``, TradingView sends a market order with a double quantity and the opposite side of the position via the `Place Order`_ endpoint.

.. _trading-concepts-pipvalue:

Pip Value
.........

The main purpose of ``pipValue`` is to calculate risks in an :ref:`Order Ticket<trading-ui-orderticket>` (for 
those who use it). This parameter\'s value is specified in the account currency.

``pipValue`` is a cost of ``pipSize`` in the account currency. So, ``pipValue = pipSize`` when account currency and 
instrument currency match. ``pipSize = minTick`` for all instruments, except currency pairs. For Forex pairs it equals 
either the ``minTick`` or the ``minTick`` multiplied by ``10``. For Forex instruments, the ``pipValue`` size depends
on the rapidly changing currency cross rates. You should always send the actual value.

Besides `/instruments`_, ``pipValue`` can be sent via `/quotes`_ in the ``buyPipValue`` and ``sellPipValue`` fields. 
However, if you do not have support for different ``pipValue`` for buy and sell, you should pass the same values in 
both fields.

By default we use ``pipValue`` parameter to display profit/loss. If you provide ``unrealizedPl`` parameter in
`/positions`_, you should set ``supportPLUpdate`` flag in `/accounts`_ to ``false``. But the profit is 
fixed when the position is closed:

* at Bid — when Short position closed,
* at Ask — when Long position closed.
