.. links
.. _`Depth Of Market`: https://www.tradingview.com/support/solutions/43000516459-depth-of-market-dom/

Glossary
========

.. glossary::
   :sorted:

   :abbr:`BATS (Better Alternative Trading System)`
      BATS exchange based in Kansas City that provides all of its trading data for free. Their data is often very
      similar to the data from the exchanges, but there can be differences. 

   Mapping symbol
      The mapping between the names of the broker’s instruments and TradingView instruments. This mapping solves the
      problem of TradingView and broker symbol names mimatching.

   Sandbox
      The sandbox is a fully functional copy of the TradingView website located at 
      `<https://beta-rest.tradingview.com>`_.
   
   Order
      Instructions to a broker to purchase (buy order) or sell (sell order) assets on a trader's behalf. When an order 
      is placed, it follows a process of order execution.
   
   Position
      Positions are on two main types. The amount of assets that is owned (:term:`long position`) or the amount of 
      debt (:term:`short position`). A trader takes a position when makes a purchase through a buy order or if sells
      short assets.
   
   Long position
      A position gain when there is an increase in price and lose when there is a decrease. It involves owning a 
      security. A long position formed as a result of buying a symbol.

   Short position
      A position formed as a result of a short sale that hasn't yet been covered. It profits when the security falls
      in price. A short often involves securities that are borrowed and then sold, to be bought back hopefully at a 
      lower price.

   :abbr:`DOM (Depth Of Market)`
      `Depth Of Market`_, known as Order Book, shows data streamed from the broker which supports Level 2 data.
      DOM shows the number of open buy and sell orders at different prices for a security.

   Limit order
      An order to buy or sell when a given or better price is reached.

   Stop order
      An order to buy or sell at the market price as soon as it reaches a certain level.

   Stop-Limit
      An order to buy or sell at a definitive price or better. But only after reaching a set price value. Essentially,
      it's a combination of a :term:`Stop oder` and a :term:`Limit order`.

   Stop-Loss
      An order that is used to limit losses. It is triggered to close a position at a given price value when it moves
      towards losses.

   Take-Profit
      A type of :term:`Limit order` that specifies the exact price at which to close out an open position for a profit. 
      If the price of the security does not reach the limit price, the Take-Profit order does not get filled. 

   :abbr:`OCO (Order-Cancels-Order)`
      Order-Cancels-Order, also known as One-Cancels-the-Other. A pair of conditional orders. If one order executes, 
      then the other is automatically cancelled.
   
   :abbr:`OSO (Order-Sends-Order)`
      *Order-Sends-Order* also know as Order-Triggers-Other/One-Triggers-Other (OTO). A pair of conditional orders. If 
      the primary order executes, a secondary order is automatically entered.
