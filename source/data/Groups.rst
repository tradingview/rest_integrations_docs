.. links
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

Groups
------

The group is a set of symbols with the same type. Implementing of the `/groups`_ is only necessary if you use symbol 
groups to group symbols by type. The `/groups`_ allow you to specify a list of groups.

.. important::
  Please plan your symbol grouping carefully. Groups cannot be deleted, you can only remove all the symbols from 
  there.

If a broker has many various groups of instruments, we recommend split them into groups. So, the requests to the 
`/symbol_info`_ should be processed with the ``group`` parameter. If the ``group`` parameter isn\'t specified in the 
`/symbol_info`_ request, you should return an error.

.. tip:: 
  Each integration is limited by 10 symbol groups. Each symbol group can contain up to 10K symbols in it. You cannot 
  put the same symbol into 2 different groups.

.. _groups-division:

If there is no division into groups, API must ignore all the parameters in the query to the `/symbol_info`_. For
example, API must return the same symbols both for a request with the ``"group": "XXX"`` (for any group) and for a
request without this parameter.

An example of division into groups for Crypto brokers:

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

To add a new symbol group after release, implement the groups and add them into the staging environment.
After that, notify your TradingView manager.

.. note:: 
  New group testing takes 1−2 weeks.
