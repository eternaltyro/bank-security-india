.. 
   Copyright (c) 2015 ~eternaltyro

   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.3
   or any later version published by the Free Software Foundation;
   with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
   A copy of the license is included in the section entitled "GNU
   Free Documentation License".
   
   Inspired from Rodolphe Breard

AXIS BANK
=========

.. note::
   This used to be called UTI bank. It's a private sector bank with a modern Internet Banking interface. 

.. warning::
   None.

.. include:: ../notes.txt

Configuration SSL/TLS
---------------------

 - `Qualys SSL Labs`_: :note_a:`A`


**Chip and PIN**

All cards have Chip and PIN.


Authentification
----------------

 - :note_e:`Minimum Password Length: 6` ;
 - :note_c:`Maximum Password Length: 28` ;
 - :note_e:`Maximum Password Length Limited to 28 characters` ;
 - :note_e:`l'authentification par clé USB requière l'utilisation du plugin Java`;
 - :note_c:`l'authentification par OTP n'est pas un second facteur mais une méthode d'authentification à part entière` ;
 - :note_f:`l'utilisation de l'OTP requière l'application mobile dédiée`.


Mobile Application
------------------

Link: `Android application`_

**Permissions for Android**

* Device & app history

  - :note_f:``

* Identity

  - :note_f:`find accounts on device`

* Calendar

  - :note_e:`read calendar events plus confidential information`
  - :note_c:`add or modify calendar events and send emails to guests without owners' knowledge`

* Contacts

  - :note_c:`read your contacts`

* Location

  - :note_c:`network based location`
  - :note_c:`GPS based location`

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
  - :note_c:`control flashlight`
  - :note_c:`prevent phone from sleeping`
  - :note_c:`view network connections`
  - :note_c:`read Google service configuration`
  - :note_c:`full network access`
  - :note_c:`connect and disconnect from WiFi`
  - :note_c:`control vibration`


.. _Qualys SSL Labs: https://www.ssllabs.com/ssltest/analyze.html?d=www.axisbank.co.in
.. _Android application: https://play.google.com/store/apps/details?id=com.axis.mobile
.. _Mobile applications: http://www.axisbank.com/personal/speed-banking/axis-mobile/axis-mobile.aspx
