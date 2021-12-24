.. links
.. _`/groups`: https://www.tradingview.com/rest-api-spec/#operation/getGroups
.. _`/permissions`: https://www.tradingview.com/rest-api-spec/#operation/getPermissions
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

Groups
------

The group is a set of symbols with the same permission. Implementing of the `/groups`_ is only necessary if you use 
symbol groups to restrict access to the instruments. The `/groups`_ allow you to specify a list of groups. The 
`/permissions`_ specifies which groups are available to a particular user. After logging into broker\'s account, the 
user gets access to one or several groups (it depends on `/permissions`_).

.. important::
  Please plan your symbol grouping carefully. Groups cannot be deleted, you can only remove all the symbols from 
  there.

If a broker has many various groups of instruments, we recommend split them into groups. So, the requests to the 
`/symbol_info`_ should be processed with the ``group`` parameter. If the ``group`` parameter isn't specifies in the 
`/symbol_info`_ request, you should return an error.

If a broker has many various groups of instruments, we recommend split them into groups. So, the requests to the 
`/symbol_info`_ should be processed with the group parameter. If the group parameter isn\'t specified in the 
`/symbol_info`_ request, you should return an error.

.. tip:: 
  Each integration is limited to have up to 10 symbol groups. Each symbol group is limited to have up to 10K symbols in 
  it. You cannot put the same symbol into 2 different groups.

.. _groups-division:

If there is no division into gruops, API must ignore all the parameters in the query to the `/symbol_info`_. For
example, API must return the same symbols both for a request with the ``"group": "XXX"`` (for any group) and for a
request without this parameter.

If there is no division into gruops, API must ignore all the parameters in the query to the `/symbol_info`_. For 
example, API must return the same symbols both for a request with the ``"group": "XXX"`` (for any group) and for a 
request without this parameter.

An example of division into groups for Cypto exchanges:

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

An example of division into groups for the Forex and CFD exchanges:

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
