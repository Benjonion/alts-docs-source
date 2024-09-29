Constrains (Core)
-------------------------------------------

.. py:module:: alts.core.data.constrains
   :synopsis: Constrains dimensions and values of queries and results.

   .. autoclass:: QueryConstrain(count, shape, ranges)
      .. automethod:: matches_shape(shape)
      .. automethod:: constrains_met(queries)
      .. automethod:: add_queries(queries)
      .. automethod:: last_queries() -> queries
      .. automethod:: queries_from_norm_pos(norm_pos) -> queries
      .. automethod:: queries_from_index(indexes)
      .. automethod:: all_queries() -> ranges
