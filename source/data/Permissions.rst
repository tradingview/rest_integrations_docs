.. links:
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions

.. _permissions-endpoint:

Permissions
-------------

The `/permissions`_ endpoint gets a list of groups allowed for a user.

When permissions are needed
............................

Use `/permissions`_ when you need to restrict access to the market data for specific users.
For example, restrictions can be made depending on the users location or their subscription plan.

.. note:: 
  If all users have the same access on market data, you don't need to implement `/permissions`_.

There are four types how restrictions on market data can be implemented:

+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Type                        | Description                                                                                                                                 | Implementation required  |
+=============================+=============================================================================================================================================+==========================+
| No restrictions             | Any user can view the data.                                                                                                                 | No                       |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Hidden from the search bar  | Symbols don't appear in the search results unless a user logs into their broker account.                                                    | Yes                      |
|                             | However, any user can open the chart by entering the full symbol name (i.e., EXCHNAME:SYM1SYM2).                                            |                          |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Available only after login  | Symbol data and direct symbol search are unavailable unless a user logs into their broker account.                                          | Yes                      |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Available on subscriptions  | The subscribed users log into their broker account and get real-time data even from those exchanges that require fee-paying in TradingView. | Yes                      |
| from the broker's side      | This type prevents users from paying twice: on the broker's and TradingView's platforms.                                                    |                          |
+-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+

.. important::
  Choose the restriction type you want to implement and notify your TradingView manager as soon as you decide on exchanges and symbols that you will use.
  After that, we highly recommend not switching from one restriction type to another as it requires time-consuming and resource-intensive activities.

How restrictions work
......................

When a user logs into their broker account,
TradingView requests `/permissions`_ to receive a list of groups the user subscribed to.
The user gains access to one or more groups depending on the list received.

How to implement
.................

Before implementing the `/permissions`_ endpoint, you need to:

1. Choose the way you want to `restrict access to the market data <#types-of-the-market-data-restrictions>`__.
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
