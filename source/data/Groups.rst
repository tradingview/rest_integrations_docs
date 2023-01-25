.. links
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

Groups
------

The `/groups`_ endpoint gets a list of possible symbol groups for users.
Groups are sets of symbols of the same type.

Implementing `/groups`_ is needed in two cases:

- If you plan to add different types of instruments, for example, one group is for Forex, the other one is for Crypto, etc.
- If you plan to restrict users from accessing certain symbols depending on their location or subscription plan.

.. important::
  Plan your symbol grouping carefully.
  Groups cannot be deleted, you can only remove all the symbols from them.

Group limitations
...................

There are several limitations on groups that you need to consider:

- Each integration can only contain up to 10 symbol groups.
- Each symbol group can contain up to 10,000 symbols in it. 
- You cannot put the same symbol into two different groups.

How to use
.............

If you decide to split symbols into groups, the requests to `/symbol_info`_ should be processed with the ``group`` parameter.
If the ``group`` parameter isn't specified, you should return an error.

If you don't want to split symbols into groups, you API must ignore all the parameters in the query to `/symbol_info`_.
For example, your API must return the same symbols both for a request with ``"group": "example_group"`` (for any group) and for a request without ``group``.

Examples
.........

An example of division into groups for the Crypto brokers:

.. code-block:: json

  {
    "s": "ok",
    "d": {
      "groups": [
        {
          "id": "broker_spots"
        },
        {
          "id": "broker_futures"
        },
        {
          "id": "broker_swaps"
        }
      ]
    }
  }

An example of division into groups for the Forex and CFD brokers:

.. code-block:: json

  {
    "s": "ok",
    "d": {
      "groups": [
        {
          "id": "broker_forex"
        },
        {
          "id": "broker_commodities"
        },
        {
          "id": "broker_cfd"
        },
        {
          "id": "broker_indices"
        }
      ]
    }
  }

Adding groups after release
............................

To add new symbol groups after release, implement the groups and add them into the staging environment.
After that, notify the TradingView team.

.. note:: 
  New group testing takes 1−2 weeks.
