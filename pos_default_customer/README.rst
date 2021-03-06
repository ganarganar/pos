==============================
Point Of Sale Default Customer
==============================

.. |badge1| image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://raster.shields.io/badge/github-ganarganar%2Fpos-lightgray.png?logo=github
    :target: https://github.com/ganarganar/pos/tree/13.0/pos_default_customer
    :alt: ganarganar/pos

|badge1| |badge2| |badge3|

This module saves time by setting a default partner for POS orders (f.e. "Consumidor Final Anónimo").

**Table of contents**

.. contents::
   :local:

Configuration
=============

To set the default partner:

#. Go to *Point of sale > Dashboard*.
#. Go the point of sale that you want to configure, click the three vertical dots, and then "Settings".
#. Under the "PoS Interface" section you can select the partner on the option "Default customer".

Usage
=====

#. Go to *Point of sale > Dashboard*.
#. Start a new POS session in any point of sale.
#. The selected customer will be set automatically.

Known issues / Roadmap
======================

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ganarganar/pos/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ganarganar/pos/issues/new?body=module:%20pos_default_customer%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Ganar Ganar

Contributors
~~~~~~~~~~~~

* `Ganar Ganar <https://ganargan.ar/>`_:

  * Lucas Soto <lsoto@ganargan.ar>
  * Leandro Ramírez <lramirez@ganargan.ar>

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

This module is part of the `ganarganar/pos <https://github.com/ganarganar/pos/tree/13.0/pos_default_customer>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
