.. 
   Copyright (c) 2015 ~eternaltyro

   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.3
   or any later version published by the Free Software Foundation;
   with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
   A copy of the license is included in the section entitled "GNU
   Free Documentation License".
   
   Inspired from Rodolphe Breard

HDFC Bank
=========

.. note::
   None.

.. warning::
   None.

.. include:: ../notes.txt

Configuration SSL/TLS
---------------------

 - `Qualys SSL Labs`_: :note_f:`F`

.. warning::
   Server vulnerable to POODLE attack.
   
.. note::
   Uses RC4; 
   Forward Secrecy not supported; 

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

* Identity

  - :note_f:`find accounts on device`

* Location

  - :note_c:`approximate location (network based)`
  - :note_c:`precise location (GPS based)`

* SMS

  - :note_c:`Read your text messages`
  - :note_c:`edit your text messages`
  - :note_c:`Receive SMS messages`

* Phone

  - :note_e:`directly call phone numbers`

* Photos / Media / Files

  - :note_c:`modify or delete SD card contents`
  - :note_c:`read contents of SD card`

* Wi-Fi connection information

  - :note_b:`view Wi-Fi connections`

* Other 

  - :note_c:`receive data from Internet`
  - :note_c:`run at startup`
  - :note_c:`prevent phone from sleeping`
  - :note_c:`view network connections`
  - :note_c:`full network access`

.. _Qualys SSL Labs: https://www.ssllabs.com/ssltest/analyze.html?d=netbanking.hdfcbank.com&latest
.. _Android application: https://play.google.com/store/apps/details?id=com.snapwork.hdfc
.. _Mobile applications: http://hdfcbank.com/personal/ways-to-bank/bank-with-your-phone/mobilebanking
