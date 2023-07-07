.. links
.. _`Depth Of Market`: https://www.tradingview.com/support/solutions/43000516459-depth-of-market-dom/
.. _`can be differences`: https://www.tradingview.com/support/solutions/43000473924-why-might-my-us-stock-data-look-incorrect/
.. _`Cboe BZX`: http://markets.cboe.com/

Glossary
********

.. glossary::
   :sorted:

   :abbr:`BATS (Better Alternative Trading System)`
      The `Cboe BZX`_ exchange (formerly BATS) provides US stock data for free. Their data is often very
      similar to the data from the exchanges, but there `can be differences`_.

   Trading session
      The period of time that matches the primary daytime trading hours for a given exchange and locale.
      For Forex and Crypto exchanges, trading session is the last 24 hours.

   User session
      A time interval from a user's login to their logout.

   Mapping symbol
      The mapping between the names of the broker\'s instruments and TradingView instruments. This mapping solves the
      problem of TradingView and broker symbol names mismatching.

   Sandbox
      The sandbox is a fully functional copy of the TradingView website located at
      `<https://beta-rest.xstaging.tv>`_.

   Order
      Instructions to a broker to purchase (buy order) or sell (sell order) assets on a trader's behalf. When an order
      is placed, it follows a process of order execution.

   Position
      There are positions of two main types - the amount of assets which is owned (:term:`long position`), or the
      amount of debt (:term:`short position`). A trader takes a position when buys through a buy order, or if sells
      short assets.

   Long position
      A position gain when there is a price increase, and a position loss when there is a price decrease. It involves
      owning a security. A long position formed as a result of buying a symbol.

   Short position
      A position formed as a result of a short sale that hasn\'t yet been covered. It profits when the security falls in
      price. A short often involves securities that are borrowed and then sold, to be bought back at a lower price,
      hopefully.

   :abbr:`DOM (Depth Of Market)`
      `Depth Of Market`_, known as Order Book, shows data streamed from the broker which supports :term:`Level 2 data`.
      DOM shows the number of open buy and sell orders at different securities\' prices.

   Limit order
      An order to buy or sell when a given or better price is reached.

   Stop order
      An order to buy or sell at the market price as soon as it reaches a certain level.

   Stop-Limit
      An order to buy or sell at a definitive or a better price, but only after reaching a set price value. Essentially,
      it\'s a combination of a :term:`Stop oder` and a :term:`Limit order`.

   Stop-Loss
      An order that is used to limit losses. It is triggered to close a position at a given price value when it moves
      towards losses.

   Take-Profit
      A type of :term:`Limit order` that specifies the exact price at which to close out an open position for a profit.
      If the price of the security does not reach the limit price, the Take-Profit order does not get filled.

   :abbr:`OCO (Order-Cancels-Order)`
      Order-Cancels-Order, also known as One-Cancels-the-Other. A pair of conditional orders. If one order is executed,
      then the other is automatically cancelled.

   :abbr:`OSO (Order-Sends-Order)`
      Order-Sends-Order also know as Order-Triggers-Other/One-Triggers-Other (OTO). A pair of conditional orders. If
      the primary order is executed, a secondary order is automatically entered.

   minTick
      A minimum price movement.

   pipSize
      Size of 1 pip. For the Forex symbol usually equals ``minTick*10``. For example for EURUSD pair:
      ``minTick=0.00001`` and ``pipSize=0,0001``.

   :abbr:`OHLC (Open-High-Low-Close chart)`
      An OHLC chart is a type of bar chart that shows open, high, low, and closing prices for each period.

   Level 2 data
      Level 2 data shows the supply and demand of the price levels beyond or outside of the current price. This gives
      the user a visual display of the price range and associated liquidity at each price level.
