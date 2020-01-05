===========================
 Multiwebsite in Sec.Rules
===========================

Allows to use ``website_id`` (current website) in ``domain_force`` field of Record Rules (``ir.rule``), e.g.:

* ``[('website_ids', 'in', [website_id])]``
* ``[('website_id', '=', website_id)]``


Example of usage:

* Show a blog on specific websites only (TODO: add link to the module)
* Show an event on specific websites only (TODO: add link to the module)
* Show a product on specific websites only (TODO: add link to the module)

Known issues
============

* This module redefines ``ir.rule`` ``_compute_domain`` base method and may be not compatible with others that redefine the method too.

Odoo 12.0+
==========

We hope this feature will be built-in since Odoo 12.0 at least: https://github.com/odoo/odoo/pull/22743

Credits
=======

Contributors
------------
* `Mediterranean Apps  <mediterranean.apps@gmail.com>`__

Sponsors
--------
* `Mediterranean Apps  <mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps  <mediterranean.apps@gmail.com>`__

    