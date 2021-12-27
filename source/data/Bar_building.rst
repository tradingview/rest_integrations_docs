.. links
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

Bar building
------------

Broker\'s feed must support 1-minute resolutions to build bars. If it is imposible to build daily resolutions from 
1-minute, set ``has-daily`` flag to ``true`` and send daily resolutions to the `/symbol_info`_.

Daily bars are being built as follows: data is taken unchanged from the feed. If the feed doesn\'t provide them, daily 
bars are built from ticks, that are inside all sessions of the current day. The daily bar has a bar start time, which 
coincides with the start time of the 1st session on a specific day, and the business day to which it belongs.

We build intemediate resolutions ourselves. Intermediate resolution bars are affected by ``session-regular`` and 
``timezone`` in the `/symbol_info`_. These resolutions are cut from the beggining of the session in the local 
``timezone`` of the exchange.

The transition to summer/winter time is carried out automatically according to the specified timezone in 
`/symbol_info`_.