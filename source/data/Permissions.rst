.. links:
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions

.. _permissions-endpoint:

Permissions
-------------

The `/permissions`_ endpoint gets a list of groups allowed for a user.
Use this endpoint when you want to restrict access to the market data or hide data for specific users.
For example, such restrictions can be made depending on the users' location or subscription plan.

How to restrict access to market data
.......................................

How you restrict access depends on whether you use :ref:`symbol mapping <symbol-mapping>` or not,
in other words, whether you use `TradingView data <#integration-includes-data-available-on-tradingview>`__ available from a third-party source or `not <#integration-includes-broker-s-data-only>`__.

Integration includes data available on TradingView
###################################################

When :ref:`mapping symbols <symbol-mapping>` to existing TradingView data, there may be cases,
when real-time data requires payment on the TradingView platform.
To prevent users from paying twice: on the broker's and TradingView's platforms,
TradingView can provide real-time data to verified users of your integration.
In this case, you need to implement the `/permissions`_ endpoint.

.. important::
  TradingView will provide you with the group names that needs to be returned in the `/permissions`_ response.

Integration includes broker's data only
########################################

If you use only your own market data in the integration, you can choose one of the two types for data visibility.

+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Type                        | Description                                                                                                                                 | `/permissions`_ required |
+=============================+=============================================================================================================================================+==========================+
| No restrictions             | Any user can view data and find it via Symbol Search.                                                                                       | No                       |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Hidden from Symbol Search   | Symbols don't appear in Symbol Search until allowed to a user via the `/permissions`_ endpoint.                                             | Yes                      |
|                             | However, any user can open the Chart by entering the full symbol name (i.e., EXCHANGE:SYM1SYM2).                                            |                          |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+

How restrictions work
......................

When a user logs into their broker account,
TradingView requests `/permissions`_ to receive a list of groups the user subscribed to.
The user gains access to one or more groups depending on the list received.

How to implement
.................

Before implementing the `/permissions`_ endpoint, you need to:

1. Choose how you want to restrict your data and let your TradingView manager know about it. After that, we highly recommend not switching from one restriction type to another, as it requires time-consuming and resource-intensive actions.
2. Unless you settle on having no data restrictions, implement the `/groups`_ endpoint, which gets a list of symbols with different access levels.

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
