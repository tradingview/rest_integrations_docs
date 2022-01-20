.. links
.. _`/symbol_info`: https://www.tradingview.com/rest-api-spec/#operation/getSymbolInfo

symbolsResponseFieldsCorrectness
--------------------------------
Response fields correctness

Status code
  ``200`` status is expected.

Content type
  The ``Content-Type`` header is checked, it must contain ``application/json``.

Fields format
  Checking response fields according to the `/symbol_info`_ specification.

  * ``s`` equals ``ok``;
  * ``symbol`` is an array of strings;
  * ``description`` is an array of strings;
  * ``exchange-listed`` is required, not null, is an UPPERCASE string or an array of UPPERCASE strings;
  * ``exchange-traded`` is required, not null, is an UPPERCASE string or an array of UPPERCASE strings;
  * ``minmovement`` is required, not null, is an integer or an array of integers;
  * ``pricescale`` is required, not null, is an integer or an array of integers, is the power of ten;
  * ``currency`` is required, not null, is a string or an array of strings;
  * ``type`` is required, not null, is a string or an array; must be one of the following: ``stock``, ``fund``, 
    ``dr``, ``right``, ``bond``, ``warrant``, ``structured``, ``index``, ``forex``, ``futures``, ``crypto``;
  * ``timezone`` is required, not null, is a string or an array of strings, correct if in IANA Time Zone database 
    format;
  * ``session`` is required, not null, is a string or an array of strings, must be correct (for example, ``24x7``);
  * ``ticker`` is optional (if not available, then symbols is used), is a string or an array of strings, the name of 
    the ticker does not contain commas;
  * ``minmov2`` is optional, not null, an integer or an array of integers;
  * ``fractional`` is optional, bool or an array of bools;
  * ``has-intraday`` is optional, bool or an array of bools;
  * ``has-no-volume`` is optional, bool or an array of bools;
  * ``has-daily`` is optional, bool or an array of bools;
  * ``has-weekly-and-monthly`` is optional, bool or an array of bools;
  * ``supported-resolutions`` is optional, not null, an array of strings or an array of arrays of strings;
  * ``intraday-multipliers`` is optional, not null, an array of strings or an array of arrays of strings;
  * ``pointvalue`` is optional, not null, a float or an array of floats;
  * ``root`` is null, a string or an array of strings;
  * ``root-description`` is null, a string or an array of strings;
  * ``bar-source`` is optional, a string or an array of strings, must be one of the following: ``bid``, ``ask``, 
    ``mid``, ``trade``; bar-transform is optional, a string or an array of strings, must be one of the following: 
    ``none``, ``openprev``, ``prevopen``.
