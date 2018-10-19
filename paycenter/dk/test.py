# -*- coding: utf-8 -*-
from dk.agreepay import *
from dk.readconf import *
a=apreepay()
b=readconf()
a.url=b.getConfig('rrcp-bgtwfront-api','url')
a.placeorder()
