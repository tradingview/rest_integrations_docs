.. links
.. _/accounts: https://www.tradingview.com/rest-api-spec/#operation/getAccounts
.. _/config: https://www.tradingview.com/rest-api-spec/#operation/getConfiguration
.. _/state: https://www.tradingview.com/rest-api-spec/#operation/getState
.. _`TradingView REST API`: https://www.tradingview.com/rest-api-spec

.. todo
   - Protect position
   - Depth Of Market (DOM)
   - Account Manager
   - Chart trading

UI elements
-----------

.. contents:: :local:
   :depth: 3

Account Summary Row
...................
The ``Account Summary Row`` is a line that is always displayed after login into the integration. It contains the most 
important information about the current state of the subaccount currently selected by the user. 

| By default, ``Account Summary Row`` displays the values of the `/state`_ request into three fields:

* ``balance`` into the *Account Balance*,
* ``equity`` into the *Equity*,
* ``unrealizedPL`` into the *Profit*.

The ``Account Summary Row`` allows you to display other required broker information after configuration.
You can configure it at the broker or subaccount level. Setting at the broker level will allow displaying the same 
information for all subaccounts. Setting at the subaccount level will display information for the user-selected account. 
In this case, the information it can be different for different subaccounts.

For custom configuration of the ``Account Summary Row`` follow the steps below.

#. Enable the ``supportCustomAccountSummaryRow`` flag in the `/config`_ request.
#. Configure the ``Account Summary Row`` fields in the `/config`_ request in the
   ``accountSummaryRow`` object if you need to configure it at the broker level.
#. Configure the ``Account Summary Row`` fields in the `/accounts`_ request inside the ``ui`` object 
   in the ``accountSummaryRow`` object if you need to configure it at the account level.
   The account-level setting has a higher priority and will be applied if there is a configuration at both levels.
#. In the `/state`_ request in the ``accountSummaryRowData`` object, send the values for ``Account Summary Row``. 
   The order and size of the sent array must match the order and size of the array specified in the configuration.

If the display area of the ``Account Summary Row`` is undersized, the elements will be hidden sequentially, 
starting with the very first. This can happen on low-resolution screens. Therefore, arrange information in order of 
increasing importance.

Account Summary Tab
...................
The ``Account Summary Tab`` displays the fields received by `/state`_ request as a set of tables. By default, one 
table is displayed. It uses the fields ``balance``, ``unrealizedPL``, and ``equity`` (if sent, the filed is optional).

The information displayed in the ``Account Summary Tab`` can be flexibly configured at the broker or subaccount level.
The settings made at the broker level will be displayed the same for all subaccounts. Setting at the subaccount level 
will allow displaying information for the account selected by the user, and the information may be different for 
different subaccounts.

* At the broker level, the ``accountManager`` object is returned in the `/config`_ request.
* At the account level, the ``accountManager`` object is returned in the `/accounts`_ request inside the ``ui`` object.

In both cases, it contains an array of table objects. The columns of the table are defined within each such array.

Regardless of the configuration level, values for the tables are returned in the `/state`_ query in the ``amData`` 
object. The ``amData`` object is an array of tables. It contains a nested array of strings with a nested array of 
columns as string values. This object must be the same size as the object defined in the configuration.

Orders tickets
..............

Durations
~~~~~~~~~
`TradingView REST API`_ allows you to configure the duration (or *Time In Force*) separately for each of the 
supported order types. By default, any item from the duration list will be shown in the *Order Ticket* only for 
*Limit*, *Stop*, *Stop-Limit* orders. If this list should be different from the default for any Durations elements, 
you must submit it for this item in the ``supportedOrderTypes`` field. ``supportedOrderTypes`` must be an array 
of order types for which this duration will be available.