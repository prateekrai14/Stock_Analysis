from tkinter import *
from SupportEnum import *

class ShareHolding:

    """Range: 0 to 100
	    Default AcceptableLimit 80
	    Default NotAcceptableLimit 30"""

    def __init__(self, root, good=80, bad=30):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)


    def isValidLimits(self):

        retcode = True
        returnStr = ""

        if not self.AcceptableLimit.get().isdecimal() or not self.NotAcceptableLimit.get().isdecimal():
            returnStr = " Only Decemial Number are allowed."
            retcode = False

        else:
            if ((int(self.AcceptableLimit.get()) >= 100) or (int(self.NotAcceptableLimit.get()) <= 0)):
                retcode = False
                returnStr += " Valid Range is > 0 and < 100."

            if (int(self.NotAcceptableLimit.get()) > int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Not Acceptable limit cannot be greater than Acceptable Limit."

            if (int(self.NotAcceptableLimit.get()) == int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Not Acceptable limit and Acceptable Limit cannot be equal."

        return retcode, returnStr


class PledgeShareHoldingLimits:

    """Range: 0 to 100
	    Default AcceptableLimit 0
	    Default NotAcceptableLimit 6"""

    def __init__(self, root, good=0, bad=6):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):

        retcode = True
        returnStr = ""

        if not self.AcceptableLimit.get().isdecimal() or not self.NotAcceptableLimit.get().isdecimal():
            returnStr = " Only Decemial Number are allowed."
            retcode = False

        else:
            if ((int(self.NotAcceptableLimit.get()) >= 100) or (int(self.AcceptableLimit.get()) < 0)):
                retcode = False
                returnStr += " Valid Range is >= 0 and < 100."

            if (int(self.AcceptableLimit.get()) > int(self.NotAcceptableLimit.get())):
                retcode = False
                returnStr += " Not Acceptable limit cannot be greater than Acceptable Limit."

            if (int(self.NotAcceptableLimit.get()) == int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Not Acceptable limit and Acceptable Limit cannot be equal."

        return retcode, returnStr

class SalesGrowthLimits:

    """Range: 0 to 100
	    Default AcceptableLimit 10
	    Default NotAcceptableLimit 0"""

    def __init__(self, root, good=10, bad=0):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):

        retcode = True
        returnStr = ""

        if not self.AcceptableLimit.get().isdecimal() or not self.NotAcceptableLimit.get().isdecimal():
            returnStr = " Only Decemial Number are allowed."
            retcode = False

        else:
            if ((int(self.AcceptableLimit.get()) > 100) or (int(self.NotAcceptableLimit.get()) < 0)):
                retcode = False
                returnStr += " Valid Range is >= 0 and =< 100."

            if (int(self.NotAcceptableLimit.get()) > int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Acceptable limit cannot be greater then Not Acceptable Limit."

            if (int(self.NotAcceptableLimit.get()) == int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Not Acceptable limit and Acceptable Limit cannot be equal."

        return retcode, returnStr



class ProfitGrowthLimits:

    """Range: 0 to 100
	    Default AcceptableLimit 10
	    Default NotAcceptableLimit 0"""

    def __init__(self, root, good=10, bad=0):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):

        retcode = True
        returnStr = ""

        if not self.AcceptableLimit.get().isdecimal() or not self.NotAcceptableLimit.get().isdecimal():
            returnStr = " Only Decemial Number are allowed."
            retcode = False

        else:
            if ((int(self.AcceptableLimit.get()) > 100) or (int(self.NotAcceptableLimit.get()) < 0)):
                retcode = False
                returnStr += " Valid Range is >= 0 and =< 100."

            if (int(self.NotAcceptableLimit.get()) > int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Acceptable limit cannot be greater then Not Acceptable Limit."

            if (int(self.NotAcceptableLimit.get()) == int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Not Acceptable limit and Acceptable Limit cannot be equal."

        return retcode, returnStr

class EquityCapitalLimits:

    """Range: 1 to 1000
	    Default AcceptableLimit 10
	    Default NotAcceptableLimit 200"""

    def __init__(self, root, good=10, bad=200):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):

        retcode = True
        returnStr = ""

        if not self.AcceptableLimit.get().isdecimal() or not self.NotAcceptableLimit.get().isdecimal():
            returnStr = " Only Decemial Number are allowed."
            retcode = False

        else:
            if ((int(self.AcceptableLimit.get()) <= 0) or (int(self.NotAcceptableLimit.get()) > 1000)):
                retcode = False
                returnStr += " Valid Range is > 0 and <= 1000."

            if (int(self.NotAcceptableLimit.get()) < int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Acceptable limit cannot be greater then Not Acceptable Limit."

            if (int(self.NotAcceptableLimit.get()) == int(self.AcceptableLimit.get())):
                retcode = False
                returnStr += " Not Acceptable limit and Acceptable Limit cannot be equal."

        return retcode, returnStr

###################################### For Further Use and Enhance ######################################
class AssestLiabilityRatio:
    """Range: POINT9 to ONEPOINT9
        Default AcceptableLimit ONEPOINT2
        Default NotAcceptableLimit POINT9"""

    def __init__(self, root, good=FractionLimits.ONEPOINT2, bad=FractionLimits.POINT9):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):
        return False if (int(self.AcceptableLimit.get()) >= int(self.NotAcceptableLimit.get())) else True

class PERatio:

    """Range: POINT9 to ONEPOINT9
    Default AcceptableLimit POINT9
    Default NotAcceptableLimit ONEPOINT3"""
    def __init__(self, root, good=FractionLimits.POINT9, bad=FractionLimits.ONEPOINT3):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):
        return False if (int(self.AcceptableLimit.get()) >= int(self.NotAcceptableLimit.get())) else True


class ProfitByRevenueLimits:
    """Range: 0 to 100
	    Default AcceptableLimit 10
	    Default NotAcceptableLimit 1"""

    def __init__(self, root, good=10, bad=1):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):
	    return False if ((int(self.AcceptableLimit.get()) >= 100) or
	                     (int(self.NotAcceptableLimit.get()) <= 0) or
	                     (int(self.NotAcceptableLimit.get()) >= int(self.AcceptableLimit.get()))) else True

class RevenueByMarketCapLimits:
    """Range: 0 to 100
	    Default AcceptableLimit 25
	    Default NotAcceptableLimit 5"""

    def __init__(self, root, good=25, bad=5):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isValidLimits(self):
        return False if ((int(self.AcceptableLimit.get()) >= 100) or
                         (int(self.NotAcceptableLimit.get()) <= 0) or
                         (int(self.NotAcceptableLimit.get()) >= int(self.AcceptableLimit.get()))) else True

class PriceToBookLimits:
    """Range: 1 to 100
	    Default AcceptableLimit 2
	    Default NotAcceptableLimit 10"""

    def __init__(self, root, good=2, bad=10):
        self.AcceptableLimit = StringVar(root, value=good)
        self.NotAcceptableLimit = StringVar(root, value=bad)

    def isVAlidLimits():
        return False if ((int(self.AcceptableLimit.get()) > 100) or (int(self.NotAcceptableLimit.get()) <= int(self.AcceptableLimit.get()))) else True