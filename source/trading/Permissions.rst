.. links:
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions

.. _permissions-endpoint:

Permissions
-------------

You can restrict access to market data or hide symbols for some users.
There are several cases when it might be needed:

- Symbols can be hidden depending on the users' location. For example, users from Spain will be able to see symbols that are hidden from Italian users.
- Symbols can be hidden from the *Symbol Search* bar. However, any user can open a chart by entering a full symbol name (i.e., EXCHANGE:SYM1SYM2).
- Symbols can only be displayed after users log into their brokerage account.
- If the broker uses data provided by TradingView, the broker's users may also need to pay for the TradingView subscription to get real-time data. This may happen in the following cases:

  - The broker doesn't cover the real-time data subscription for users.
  - The real-time data provision is not subject to local compliance requirements.

  To prevent users from paying twice: on the broker's and TradingView's ends, TradingView can provide real-time data to verified integration users.

In the cases described above, you need to implement the `/permissions`_ endpoint that gets a list of groups allowed for a user.

.. note::
  You don't need to implement `/permissions`_ if you don't plan to hide any data.

How restrictions work
......................

When a user logs into their broker account,
TradingView requests `/permissions`_ to receive a list of the groups the user subscribed to.
The user gets access to one or more groups depending on the list received.
Refer to the :ref:`Groups <groups-endpoint>` article for more information about groups.

Prerequisites
...............

Before implementing `/permissions`_:

1. Choose how you want to restrict access to the market data.
2. Decide whether you plan to use :ref:`symbol mapping <symbol-mapping>` or not, in other words, whether you plan to use TradingView data available from a third-party source or your own data only.
3. Let the TradingView team know about your plans. After that, we highly recommend not switching from one restriction case to another, as it requires time-consuming and resource-intensive actions.
4. If you choose to use data provided by TradingView, the team will provide you with the group names that need to be returned in the `/permissions`_ response. Otherwise, the group names must be the ones that you create using the `/groups`_ endpoint.

How to implement permissions
.............................

When you finish with the steps described in the `Prerequisites <#prerequisites>`__ section, implement the `/permissions`_ endpoint.
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
