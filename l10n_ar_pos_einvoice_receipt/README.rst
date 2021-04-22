==============================
Point Of Sale eInvoice Receipt
==============================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://raster.shields.io/badge/github-ganarganar%2Fpos-lightgray.png?logo=github
    :target: https://github.com/ganarganar/pos/tree/13.0/l10n_ar_pos_einvoice_receipt
    :alt: ganarganar/pos

|badge1| |badge2| |badge3|

This module modifies the way that the receipt is showed if the "Invoice" option is selected on the POS screen.

The modifications that this module does are aimed to make the receipts compliant with AFIP's RGs. This means that the receipts printed are legal electronic invoices.

Warning: (all, but especially) this module development is based on the Adhoc's argentinian localization, and probably would not work fine with other localizations around (f.e. Moldeo's one), as there are many diferences between one and other.

By the way, the QR RG is applied.

.. |receipt_example| image:: /l10n_ar_pos_einvoice_receipt/static/description/receipt_example.png
    :alt: Receipt example

Example receipt with all options enabled:

|receipt_example|

**Table of contents**

.. contents::
   :local:

Configuration
=============

To make the "Invoice" button enabled by default:

#. Go to *Point of sale > Dashboard*.
#. Go the point of sale that you want to configure, click the three vertical dots, and then "Settings".
#. Under the "Bills & Receipts" section you must check the option "Invoice by default".

To automatically download a copy of the generated invoice:

#. Go to *Point of sale > Dashboard*.
#. Go the point of sale that you want to configure, click the three vertical dots, and then "Settings".
#. Under the "Bills & Receipts" section you must check the option "PDF invoice download".

To show or hide the cashier info on the receipt:

#. Go to *Point of sale > Dashboard*.
#. Go the point of sale that you want to configure,click the three vertical dots, and then "Settings".
#. Under the "Bills & Receipts" section you must check the option "Show cashier info".

To show or hide the company contact info (phone number, website and e-mail) on the receipt:

#. Go to *Point of sale > Dashboard*.
#. Go the point of sale that you want to configure,click the three vertical dots, and then "Settings".
#. Under the "Bills & Receipts" section you must check the option "Show contact info".

To show or hide the invoice number on the receipt:

#. Go to *Point of sale > Dashboard*.
#. Go the point of sale that you want to configure,click the three vertical dots, and then "Settings".
#. Under the "Bills & Receipts" section you must check the option "Show invoice number".

To show or hide the customer's VAT data:

#. Go to *Point of sale > Dashboard*.
#. Go the point of sale that you want to configure,click the three vertical dots, and then "Settings".
#. Under the "Bills & Receipts" section you must check the option "Show customer VAT".

Usage
=====

#. Go to *Point of sale > Dashboard*.
#. Start a new POS session in any point of sale.
#. After starting a new sale, go to the payment screen and check "Invoice".
#. Validate.
#. An AFIP compliant receipt (and backend invoice) will be generated.

Known issues / Roadmap
======================

* Make the errors a bit more friendly to the users.
* Check that working offline doesn't generate a big mess with order sync.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ganarganar/pos/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ganarganar/pos/issues/new?body=module:%20l10n_ar_pos_einvoice_receipt%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Ganar Ganar
* Galup
* Pushnube

Contributors
~~~~~~~~~~~~

* `Ganar Ganar <https://ganargan.ar/>`_:

  * Lucas Soto <lsoto@ganargan.ar>
  * Leandro Ramírez <lramirez@ganargan.ar>

* `Galup <https://galup.com.ar/>`_:

  * Gabriela Rivero

* Iván Todorovich
* Mario Núñez

Maintainers
~~~~~~~~~~~

This module is maintained by Ganar Ganar.

.. image:: https://ganargan.ar/web/image?model=res.partner&id=1&field=image_128
   :alt: Ganar Ganar
   :target: https://ganargan.ar

.. |maintainer-sotolucas| image:: https://github.com/sotolucas.png?size=40px
    :target: https://github.com/sotolucas
    :alt: sotolucas

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-sotolucas| 

This module is part of the `ganarganar/pos <https://github.com/ganarganar/pos/tree/13.0/l10n_ar_pos_einvoice_receipt>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
