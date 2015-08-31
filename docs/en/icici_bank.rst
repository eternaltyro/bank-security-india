.. 
   Copyright (c) 2015 ~eternaltyro

   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.3
   or any later version published by the Free Software Foundation;
   with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
   A copy of the license is included in the section entitled "GNU
   Free Documentation License".
   
   Inspired from Rodolphe Breard

ICICI Bank
==========

.. note::
   None.

.. warning::
   None.

.. include:: ../notes.txt

Configuration SSL/TLS
---------------------

 - `Qualys SSL Labs`_: :note_c:`C`

.. note::
   Uses RC4; 
   Forward Secrecy not enabled. 

**Chip and PIN**

All cards have Chip and PIN.


Authentification
----------------

 - :note_e:`Minimum Password Length: 6` ;
 - :note_c:`Maximum Password Length: 28` ;
 - :note_e:`Maximum Password Length Limited to 28 characters` ;


Mobile Application
------------------

Link: `Android application`_

**Permissions for Android**

* Device & app history

  - :note_f:`retrieve running apps`

* Identity

  - :note_f:`find accounts on device`
  - :note_f:`add or remove accounts`

* Contacts

  - :note_c:`read your contacts`

* SMS

  - :note_c:`Read your text messages`
  - :note_c:`Send SMS messages`

* Phone

  - :note_e:`read call log`

* Photos / Media / Files

  - :note_c:`modify or delete SD card contents`
  - :note_c:`read contents of SD card`

* Wi-Fi connection information

  - :note_b:`view Wi-Fi connections`

* Device ID & call information

  - :note_c:`Read phone status and identity`
  
* Other 

  - :note_c:`receive data from Internet`
  - :note_c:`create accounts and set passwords`
  - :note_c:`prevent phone from sleeping`
  - :note_c:`use accounts on device`
  - :note_c:`set an alarm`
  - :note_c:`view network connections`
  - :note_c:`full network access`
  - :note_c:`control vibration`


.. _Qualys SSL Labs: https://www.ssllabs.com/ssltest/analyze.html?d=infinity.icicibank.com
.. _Android application: https://play.google.com/store/apps/details?id=com.csam.icici.bank.imobile 
.. _Mobile applications: http://www.icicibank.com/mobile-banking/index.page
