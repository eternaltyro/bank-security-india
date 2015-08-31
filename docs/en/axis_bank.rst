.. 
   Copyright (c) 2015 ~eternaltyro

   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.3
   or any later version published by the Free Software Foundation;
   with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
   A copy of the license is included in the section entitled "GNU
   Free Documentation License".
   
   Inspired from Rodolphe Breard

AXIS Bank
=========

.. note::
   This used to be called UTI bank. It's a private sector bank with a modern Internet Banking interface. 

.. warning::
   None.

.. include:: ../notes.txt

Configuration SSL/TLS
---------------------

 - `Qualys SSL Labs`_: :note_a:`A`

.. note::
   Uses SSLv3;
   Uses RC4;
   Forward secrecy not enabled;

**Chip and PIN**

 - :note_a:`Chip and PIN cards offered`;

Authentication
--------------

 - :note_c:`Minimum Password Length: 8` ;
 - :note_c:`Maximum Password Length: 28` ;
 - :note_c:`Right click allowed`;
 - :note_e:`Copy Paste disabled`;
 - :note_c:`Virtual Keyboard provided`;

.. note::
   While pasting from clipboard into the password field is not allowed in the primary Internet Banking site,
   the payment-gateway site DOES allow pasting passwords into the input box. 

Mobile Application
------------------

Link: `Android application`_

**Permissions for Android**

* Device & app history

  - :note_c:`device status and history`

* Identity

  - :note_c:`find accounts on device`

* Calendar

  - :note_e:`read calendar events plus confidential information`
  - :note_f:`add or modify calendar events and send emails to guests without owners' knowledge`

* Contacts

  - :note_e:`read your contacts`

* Location

  - :note_e:`network based location`
  - :note_e:`GPS based location`

* SMS

  - :note_c:`Send SMS messages`

* Phone

  - :note_c:`Directly call phone numbers`
  - :note_e:`read call log`

* Photos / Media / Files

  - :note_c:`test access to protected storage`
  - :note_c:`modify or delete SD card contents`

* Camera

  - :note_e:`take pictures and videos`

* Wi-Fi connection information

  - :note_b:`view Wi-Fi connections`

* Device ID & call information

  - :note_c:`Read phone status and identity`
  
* Other 

  - :note_c:`run at startup`
  - :note_d:`control flashlight`
  - :note_c:`prevent phone from sleeping`
  - :note_b:`view network connections`
  - :note_c:`read Google service configuration`
  - :note_b:`full network access`
  - :note_b:`connect and disconnect from WiFi`
  - :note_d:`control vibration`


.. _Qualys SSL Labs: https://www.ssllabs.com/ssltest/analyze.html?d=www.axisbank.co.in
.. _Android application: https://play.google.com/store/apps/details?id=com.axis.mobile
.. _Mobile applications: http://www.axisbank.com/personal/speed-banking/axis-mobile/axis-mobile.aspx
