.. links:
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions

.. _permissions-endpoint:

Permissions
--------------

The `/permissions`_ endpoint gets a list of groups allowed for a user.

When to implement /permissions
................................

Use `/permissions`_ when you need to restrict access to some symbol groups for specific users, 
for example, when users pay for market data subscriptions. 
This endpoint prevents users from paying twice: on the brokerage and on the TradingView platform.

In this case, when a user logs into their broker account, 
TradingView requests `/permissions`_ to receive a list of groups the user subscribed to. 
The user gains access to one or more groups depending on the list received.

.. note::
   If all users have the same set of instruments, `/permissions`_ is not required.

How to group permissions
.........................

Before implementing `/permissions`_, implement the `/groups`_ endpoint first. 
It gets a list of symbols with different access levels.

.. note::
   Learn more about :ref:`Groups <groups-endpoint>`.

Response example
.................

The response will contain an object with an array of groups.

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
