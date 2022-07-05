from enum import IntEnum, unique

@unique
class FractionLimits(IntEnum):
    ZERO = 0
    POINT1 = 1
    POINT2 = 2
    POINT3 = 3
    POINT4 = 4
    POINT5 = 5
    POINT6 = 6
    POINT7 = 7
    POINT8 = 8
    POINT9 = 9
    ONE = 10
    ONEPOINT1 = 11
    ONEPOINT2 = 12
    ONEPOINT3 = 13
    ONEPOINT4 = 14
    ONEPOINT5 = 15
    ONEPOINT6 = 16
    ONEPOINT7 = 17
    ONEPOINT8 = 18
    ONEPOINT9 = 19

@unique
class ColorResult(IntEnum):
    GREEN = 0
    DARKGREEN = 1
    YELLOW = 2
    RED = 3

@unique
class ANNUALENTITIES(IntEnum):
    COMPANY_NAME = 0
    FACE_VALUE=1
    YEAR_MONTH=2
    TOTAL_EQUITY=3
    BOOK_VALUE=4
    SALES=5
    NET_PROFIT=6
    EPS=7
    ANUALIZED_DIVIDENT=8
    DIV_RATIO=9

@unique
class QUATERENTITIES(IntEnum):
    QSALES = 12
    QNET_PROFIT=13

@unique
class YEAR2DATEENTITIES(IntEnum):
    YSALES = 15
    YSALE_GROWTH=16
    YNET_PROFIT=17
    YNET_PROFIT_GROWTH=18

@unique
class SHAREHOLDINGS(IntEnum):
    PROMOTOR_HOLDINGS = 19
    PLEDGED=20
    INSTITUTE_HOLDINGS=21

@unique
class MARKETDATA(IntEnum):
    MARKET_CAP = 23
    PRICES=24
    YEAR_HIGH_LOW=25
    PE = 27
    SECTOR=28