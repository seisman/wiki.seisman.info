Misc
====

Extensive and intensive conjugate quantities
--------------------------------------------

For a system described by N :ref:`extensive quantities <extensive_quantity>` :math:`e_k`
and N :ref:`intensive quantities <intensive_quantity>` :math:`i_k`.

The differential increase in energy :math:`U` per unit volume of the system
for a variation of :math:`e_k` is:

.. math::

    dU = \sum_k i_k d e_k

The Gibbs potential of the system is defined as:

.. math::

    G = U - \sum_k i_k e_k

And, the differential increase of Gibbos potential can be expressed as:

.. math::

    dG = dU - d\sum_k i_k e_k
       = \sum_k i_k d e_k - \sum e_k d i_k - \sum i_k d e_k
       = \sum e_k d i_k

Therefore, the intensive quantities :math:`i_k` can be defined as partial
derivatives of the energy :math:`U` with respect to their
extensive conjugate quantities :math:`e_k`:

.. math::

    i_k = \frac{\partial U}{\partial e_k}

The extensive quantities :math:`e_k` can be defined as partial derivatitives
of the Gibbos potential :math:`G` with respect to their intensive conjugate
quantities :math:`i_k`:

.. math::

    e_k = - \frac{\partial G}{\partial i_k}