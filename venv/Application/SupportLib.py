class AnalyzerResult:
    """
        Analysis will be shown via this object
    """
    def __init__(self):
        self.retCode = ColorResult.RED
        self.Info = "Defult Return"

class HelperFunctions:
    """
        Global funcitons are kept here
    """
    def ConvretFractionToNumber(self, fractionLimit):
        if fractionLimit is FractionLimits:
            return fractionLimit/10;
        else:
            raise RuntimeError("Input fraction number is not valid in this application")
