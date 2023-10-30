# Simple json size stats with Python

#### Examples

Level 1 only:
```
$ ./main.py -l 1 sample.json 
Source file size: 100.6 Mb
JSON parse time: 1.3 sec

Transfer times:
 100 Mbps 8.4 sec
 1 Gigabit 0.8 sec
 10 Gigabit 0.1 sec

1 Gigabit transfer + parse time: 2.1 sec

  90.2 Mb - {root}
```

Level 2 only:
```
$ ./main.py -l 2 sample.json 
Source file size: 100.6 Mb
JSON parse time: 1.3 sec

Transfer times:
 100 Mbps 8.4 sec
 1 Gigabit 0.8 sec
 10 Gigabit 0.1 sec

1 Gigabit transfer + parse time: 2.1 sec

  90.2 Mb - {root}
  33.0 b      - {root/bnplBankInfo}
  17.0 b      - {root/bnplBaseFromBankInfo}
  50.0 b      - {root/helpingHand}
   6.0 b      - 'root/creditInformation'
  34.0 b      - {root/bnplInfo}
   7.0 b      - 'root/upsellByPromo'
   2.0 b      - [root/upsellActions]
   4.3 Kb     - [root/grouping]
  22.0 b      - {root/presentationFields}
 670.0 b      - {root/commonPayment}
   4.0 b      - 'root/freeDeliveryThreshold'
  88.0 b      - {root/deliveryDiscountMap}
  14.0 b      - 'root/freeDeliveryStatus'
  26.0 b      - 'root/freeDeliveryReason'
   1.0 b      - 'root/priceLeftForFreeDelivery'
   2.0 b      - [root/coinIdsToUse]
   6.0 Kb     - {root/totals}
   6.0 b      - 'root/useInternalPromocode'
  70.7 Kb     - [root/commonDeliveryOptions]
   2.4 Kb     - {root/cashback}
   6.0 b      - 'root/selectedCashbackOption'
   2.0 b      - 'root/cashbackBalance'
 116.9 Kb     - [root/cashbackOptionsProfiles]
 136.0 b      - [root/paymentOptions]
   7.0 b      - 'root/isPickupPromocodeSuitable'
  12.7 Kb     - [root/presets]
 206.0 b      - {root/buyer}
  46.0 b      - {root/costLimitInformation}
* 90.0 Mb     - [root/carts]
   5.0 b      - 'root/buyerCurrency'
```

Level 3 with pattern:
```
$ ./main.py -l 3 -p root/totals sample.json 
Source file size: 100.6 Mb
JSON parse time: 1.3 sec

Transfer times:
 100 Mbps 8.4 sec
 1 Gigabit 0.8 sec
 10 Gigabit 0.1 sec

1 Gigabit transfer + parse time: 2.1 sec

   6.0 Kb     - {root/totals}
 216.0 b          - [root/totals/conditionalPromos]
   5.7 Kb         - [root/totals/promos]
   1.0 b          - 'root/totals/servicesTotal'
   3.0 b          - 'root/totals/buyerDeliveryTotal'
   6.0 b          - 'root/totals/buyerTotal'
   6.0 b          - 'root/totals/buyerItemsTotal'
```
