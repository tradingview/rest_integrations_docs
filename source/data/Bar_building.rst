.. links
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

Bar building
------------

The API must support 1-minute resolution of the historical data. Daily resolution must be provided only if automatic 
building from 1-minute resolution data produces incorrect results. By default we expect to get daily resolutions from
the data feed. If you don't provide them, set ``has-daily`` flag in response to `/symbol_info`_ to ``false``.

Daily bars are built from lower resolution (1-minute typically) or taken from the API if they are available. Daily bar 
time matches the start of the 1st session of the day.

We build intermediate resolutions ourselves. Intermediate resolution bars are affected by ``session-regular`` and 
``timezone`` in the `/symbol_info`_.  The time of the first bar of every resolution matches with the beginning of the 
session.

The transition to summer/winter time is carried out automatically according to the specified timezone in 
`/symbol_info`_.
