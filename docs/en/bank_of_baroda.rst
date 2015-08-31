.. 
   Copyright (c) 2015 ~eternaltyro

   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.3
   or any later version published by the Free Software Foundation;
   with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
   A copy of the license is included in the section entitled "GNU
   Free Documentation License".
   
   Inspired from Rodolphe Breard

Bank of Baroda
==============

.. note::
   None.

.. warning::
   None.

.. include:: ../notes.txt

Configuration SSL/TLS
---------------------

 - `Qualys SSL Labs`_: :note_f:`F`

.. warning::
   Offers SSLv2;
   Offers SSLv3;
   Does not offer TLSv1.2

.. note::
   Uses RC4; 
   Forward Secrecy not supported. 

**Chip and PIN**

All cards have Chip and PIN.


Authentification
----------------

 - :note_e:`Minimum Password Length: 6` ;
 - :note_c:`Maximum Password Length: 28` ;
 - :note_e:`Maximum Password Length Limited to 28 characters` ;


Mobile Application
------------------

.. Not provided

.. _Qualys SSL Labs: https://www.ssllabs.com/ssltest/analyze.html?d=bobibanking.com
