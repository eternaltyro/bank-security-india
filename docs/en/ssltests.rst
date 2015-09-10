.. 
   Copyright (c) 2015 ~eternaltyro
   
   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.3
   or any later version published by the Free Software Foundation;
   with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
   A copy of the license is included in the section entitled "GNU
   Free Documentation License".

   Inspired heavily from Rodolphe Breard's Bank-a-geeks project.

.. 
   TODO: Punjab national bank
   TODO: OTP (delivery mode? App / SMS)
   TODO: Mobile app login mode (PIN/ password)

.. note::
   This page documents the SSL quality for different banks. It also details the attacks the sites are vulnerable to.

Bank Security India
==========================

.. include:: ../notes.txt


.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * -
     - GRADE
     - RC4 / MD5
     - ATTACKS
     - SSLv3 / SSLv2
     - Forward Secrecy
     - COMMENTS
   
   * - :doc:`Allahabad Bank <allahabad_bank>`
     - :note_c:`C`
     - | :note_d:`RC4-SHA;`
       | :note_d:`RC4-MD5`
     - :note_na:`None`
     - :note_na:`Good`
     - :note_d:`No`
     - :note_na:`www.allbankonline.in`
   
   * - :doc:`Andhra Bank <andhra_bank>`
     - :note_c:`C`
     - | :note_na:`RC4-SHA;`
       | :note_d:`RC4-MD5`
     - | :note_d:`BREACH;`
       | :note_f:`POODLE`
     - :note_na:`SSLv3`
     - :note_na:`No`
     - | :note_f:`TLSv1.2 / TLSv1.1 not supported;`
       | :note_na:`www.onlineandhrabank.net.in;`
       | :note_d:`Weak signature`

   * - :doc:`Axis Bank <axis_bank>`
     - :note_c:`C`
     - :note_d:`RC4-SHA`
     - | :note_d:`BEAST?;`
       | :note_f:`POODLE`
     - :note_c:`SSLv3`
     - :note_d:`No`
     - | :note_na:`axisbank.co.in;`
       | :note_a:`TLS_FALLBACK_SCSV supported`
       | :note_na:`(against downgrade attacks)`

   * - :doc:`Bank of Baroda <bank_of_baroda>`
     - :note_f:`F`/:note_c:`C`
     - | :note_d:`RC4-SHA;`
       | :note_d:`RC4-MD5?`
     - | :note_d:`BREACH?(www);`
       | :note_f:`POODLE`
     - | :note_f:`SSLv2 on www;`
       | :note_f:`SSLv3;`
     - :note_d:`No` [#bobifwd]_
     - | :note_f:`TLSv1.2 / TLSv1.1 not supported;`
       | :note_na:`www.bobibanking.com / intl.bobibanking.com`
   
   * - :doc:`Bank of India <bank_of_india>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Bank of Maharashtra <maharashtra_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Bharatiya Mahila Bank <mahila_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Canara Bank <canara_bank>`
     - :note_a:`A-`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Catholic Syrian Bank <catholic_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Central Bank of India <central_bank>`
     - :note_c:`C`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`City Union Bank <cub_bank>`
     - :note_b:`B`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Corporation Bank <corporation_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Dena Bank <dena_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Development Credit Bank <devcred_bank>`
     - :note_a:`A-`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Dhanlaxmi Bank <dhanlaxmi_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Federal Bank <federal_bank>`
     - :note_b:`B`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`HDFC Bank <hdfc_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`ICICI Bank <icici_bank>`
     - :note_c:`C`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`IDBI Bank <idbi_bank>`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Indian Bank <indian_bank>`
     - :note_c:`C`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Indian Overseas Bank <iob_bank>`
     - :note_b:`B`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Indusind Bank <indusind_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`ING Vysya Bank <ingvysya_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Jammu and Kashmir Bank <jammukashmir_bank>`
     - :note_na:`?`
     - :note_c:`C`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Karnataka Bank <karnataka_bank>`
     - :note_na:`?`
     - :note_b:`B`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Karur Vysya Bank <karurvysya_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Kotak Mahindra Bank <kotak_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
   
   * - :doc:`Lakshmi Vilas Bank <lakshmivilas_bank>`
     - :note_na:`?`
     - :note_b:`B`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Nainital Bank <nainital_bank>`
     - :note_na:`?`
     - :note_f:`F by script`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Oriental Bank of Commerce <obc_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Punjab and Sind Bank <punjabsind_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Ratnakar Bank <ratnakar_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`South Indian Bank <southindian_bank>`
     - :note_na:`?`
     - :note_b:`B`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`State Bank of India <sbi_bank>` [#statebanks]_
     - :note_na:`?`
     - :note_c:`C` [#onlinesbi]_
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Syndicate Bank <syndicate_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`TamilNad Mercantile Bank <tmb_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`UCO Bank <uco_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Union Bank of India <union_bank>`
     - :note_na:`?`
     - :note_f:`F`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Vijaya Bank <vijaya_bank>`
     - :note_na:`?`
     - :note_c:`C`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`

   * - :doc:`Yes bank <yes_bank>`
     - :note_na:`?`
     - :note_c:`C`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`
     - :note_na:`?`


.. [#bobifwd] PFS offered only on www site only with very modern browsers. (0xc013; 0xc014)
.. [#statebanks] Includes State Bank of *

.. toctree::
   :hidden:

   allahabad_bank
   andhra_bank
   axis_bank
   bank_of_baroda
   bank_of_india
   maharashtra_bank
   mahila_bank
   canara_bank
   catholic_bank
   central_bank
   cub_bank
   corporation_bank
   dena_bank
   devcred_bank
   dhanlaxmi_bank
   federal_bank
   hdfc_bank
   icici_bank
   idbi_bank
   indian_bank
   iob_bank
   indusind_bank
   ingvysya_bank
   jammukashmir_bank
   karnataka_bank
   karurvysya_bank
   kotak_bank
   lakshmivilas_bank
   nainital_bank
   obc_bank
   punjabsind_bank
   ratnakar_bank
   southindian_bank
   sbi_bank
   syndicate_bank
   tmb_bank
   uco_bank
   union_bank
   vijaya_bank
   yes_bank
   

notes
-----

 - :note_a:`A` : No Complaints ;
 - :note_b:`B` : Good, but could be better ;
 - :note_c:`C`/:note_d:`D` : Bad. Medium risk. ;
 - :note_e:`E`/:note_f:`F` : Worst. High risk practices.


Criteria
---------

**SSL/TLS Configuration**

For the quality of configuration when it comes to TLS/SSL, I used Qualys SSL Labs SSL checks. I click on the netbanking link for the respective banks and then when I see the login screen, I simply copied the domain.tld into the SSL labs check page and got the resultant rating and any warnings / errors. 

Interestingly, during my experiments, I came across atleast one major bank site, that had requested that SSL Labs do not test their site. Seems like a big glass of security by obscurity. [#obscurenotsecure]_ Bruce Schneier also says this:

  Smart security engineers open their systems to public scrutiny, because that’s how they improve. The truly awful engineers will not only hide their bad designs behind secrecy, but try to belittle any negative security results. Get ready for Rapiscan to claim that the researchers had old software, and the new software has fixed all these problems. Or that they’re only theoretical. Or that the researchers themselves are the problem. We’ve seen it all before.

For those sites that Qualys won't test, I used a neat SSL test script called testssl.sh [#testssl]_

I'm looking for insecure ciphers (MD5, RC4), vulnerable protocols (SSLv3) and similar poor security parameters in the SSL certificates. 

Protocols:
Offered Ciphers:
Attacks:
Forward Secrecy:
Weak signatures: (SHA1)

.. [#testssl] https://github.com/drwetter/testssl.sh 
