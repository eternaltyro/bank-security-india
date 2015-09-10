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

.. list-table::
   :stub-columns: 1

   * - GRADE
     - :note_f:`F`

   * - ATTACKS
     - POODLE; BEAST; FREAK;

   * - RC4 / MD5
     - RC4-SHA; RC4-MD5

   * - SSLv2
     - :note_f:`Offered`

   * - SSLv3
     - :note_f:`Offered`

   * - TLSv1.2
     - :note_f:`Nope`

   * - PFS
     - :note_f:`Nope`

.. Caution::
   This thing is a disaster!
   Offers SSLv2 AND SSLv3;
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
