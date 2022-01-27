.. Helpful doc https://devguide.python.org/documenting/#restructuredtext-primer

.. links
.. _`TradingView Web Platform`: https://www.tradingview.com/chart/
.. _`REST Web API`: https://www.tradingview.com/rest-api-spec/

Broker Integration Manual
#########################

.. toctree::
   :hidden:
   :maxdepth: 1

   Integration_overview
   trading/index
   trading_tests/index
   data
   FAQ
   Glossary

This API lets brokers build a bridge to connect their backend systems to the TradingView interface, so that broker
partners then can be supported on the `TradingView Web Platform`_.

The integration is very straightforward. The broker builds a `REST Web API`_ on its own servers based on our
specification so that it can be connected to TradingView. TradingView provides a sandbox and required technical
assistance to get your TradingView Web Platform integration started.

Documentation structure
-----------------------

:doc:`Integration overview <Integration_overview>`
  This section will help you understand the structure of the integration and point out which parts you need to pay
  attention to and which ones you may not implement.

:doc:`Trading integration <trading/index>`
  Here you can read about the features of the trading integration. It is also describes the relationship between UI and
  API implementation.

:doc:`Trading integration tests <trading_tests/index>`
  Here you can find a description of the conformational tests that should be passed successfully before placing a 
  broker integration to the sandbox.

.. :doc:`Data integration <data/index>`
..   Here you can read about data integration. This section helps you manipulate data permissions, set up a list of 
..   instruments and stream of price.

.. :doc:`Data integration tests <data_tests/index>`
..   Here you can find a description of the tests that should be passed during the data integration phase.

:doc:`FAQ <FAQ>`
  There are short answers for simple questions and links to sections that answer complex questions.

:doc:`Glossary <Glossary>`
  Here collected are explanations of the meanings of terms and acronyms.
