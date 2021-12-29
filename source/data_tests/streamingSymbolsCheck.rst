streamingSymbolsCheck
---------------------

Checking that the symbol, for which the tick came, exists in the symbol info. And also checking that ticks are 
available for each symbol in the symbol info. Ticks can arrive quite rare for some symbols, so you may need to 
increase the running time of this test. It can be achieved by using ``--symbols-duration`` parameter, described above.
