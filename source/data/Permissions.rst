.. links:
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions

.. _permissions-endpoint:

Permissions
-------------

The `/permissions`_ endpoint gets a list of groups allowed for a user.

This endpoint is used when you want to restrict access to the market data or simply hide data for specific users.
For example, such restrictions can be made depending on the users location or their subscription plan.

The ways how you can restrict access depend on whether you use :ref:`symbol mapping <symbol-mapping>` or not,
in other words, whether you use TradingView data available from a third-party source or not.

.. important::
  Choose the restriction type you want to implement and notify your TradingView manager as soon as you decide on exchanges and symbols that you will use.
  After that, we highly recommend not switching from one restriction type to another as it requires time-consuming and resource-intensive activities.

Integration includes broker's data only
........................................

If you use your own market data only in the integration, you can choose one of the two types for data visibility.

+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Type                        | Description                                                                                                                                 | `/permissions`_ required |
+=============================+=============================================================================================================================================+==========================+
| No restrictions             | Any user can view data and find it via Symbol Search.                                                                                       | No                       |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Hidden from Symbol Search   | Symbols don't appear in Symbol Search until allowed to a user via the `/permissions` endpoint.                                              | Yes                      |
|                             | However, any user can open the Chart by entering the full symbol name (i.e., EXCHANGE:SYM1SYM2).                                            |                          |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+

Integration includes data available on TradingView
...................................................

When :ref:`mapping symbols <symbol-mapping>` onto existing TradingView data, there may be cases,
when real-time data requires fee-paying on the TradingView platform.
To prevent users from paying twice: on the broker's and TradingView's platforms,
TradingView can provide real-time data to verified users of your integration.
In this case, you need to implement the `/permissions` endpoint.

.. important::
  TradingView will provide you with the group names that needs to be returned in the `/permissions`_ response.

How restrictions work
......................

When a user logs into their broker account,
TradingView requests `/permissions`_ to receive a list of groups the user subscribed to.
The user gains access to one or more groups depending on the list received.

How to implement
.................

Before implementing the `/permissions`_ endpoint, you need to:

1. Choose the way you want to restrict access to the market data.
2. Notify your TradingView manager about it.
3. Unless you settle on having no data restrictions, implement the `/groups`_ endpoint, which gets a list of symbols with different access levels.

.. note::
  Learn more about :ref:`Groups <groups-endpoint>`.

When you finish with the steps above, implement the `/permissions`_ endpoint.
Its response must contain an object with an array of groups.

.. code:: json

  {
    "s": "ok",
    "d": {
      "groups": [
        "broker_futures",
        "broker_stocks",
        "broker_forex"
      ]
    }
  }
