# -*- coding: utf-8 -*-
"""
Created on 2018/9/20

@author: gaoan
"""
import threading
import platform
from enum import Enum, unique
from .quote_keys import QuoteChangeKey
from .fundamental_fields import Valuation, Income, Balance, CashFlow, BalanceSheetRatio, Growth, \
    Leverage, Profitability

python_version = platform.python_version()

if python_version.startswith("3"):
    PYTHON_VERSION_3 = True
else:
    PYTHON_VERSION_3 = False

OPEN_API_SDK_VERSION = "2.0"

THREAD_LOCAL = threading.local()


@unique
class Market(Enum):
    """Enum for market """
    
    ALL = 'ALL'
    US = 'US'  # 美股
    HK = 'HK'  # 港股
    CN = 'CN'  # A股


@unique
class TradingSession(Enum):
    PreMarket = 'PreMarket'  # 盘前
    Regular = 'Regular'  # 盘中
    AfterHours = 'AfterHours'  # 盘后


@unique
class SecurityType(Enum):
    """Enum for sec_type """
    
    ALL = 'ALL'
    STK = 'STK'  # 股票
    OPT = 'OPT'  # 期权
    WAR = 'WAR'  # 窝轮
    IOPT = 'IOPT'  # 权证(牛熊证)
    FUT = 'FUT'  # 期货
    FOP = 'FOP'  # 期货期权
    CASH = 'CASH'  # 外汇


@unique
class Currency(Enum):
    """Enum for currency """
    
    ALL = 'ALL'
    USD = 'USD'  # 美元
    HKD = 'HKD'  # 港币
    CNH = 'CNH'  # 离岸人民币


@unique
class Language(Enum):
    zh_CN = 'zh_CN'  # 简体中文
    zh_TW = 'zh_TW'  # 繁体中文
    en_US = 'en_US'  # 英文


@unique
class QuoteRight(Enum):
    BR = 'br'  # 前复权
    NR = 'nr'  # 不复权


@unique
class TimelinePeriod(Enum):
    DAY = 'day'  # 当天分时
    FIVE_DAYS = '5day'  # 5日分时


@unique
class BarPeriod(Enum):
    DAY = 'day'  # 日K
    WEEK = 'week'  # 周K
    MONTH = 'month'  # 月K
    YEAR = 'year'  # 年K
    ONE_MINUTE = '1min'  # 1分钟
    THREE_MINUTES = '3min'  # 3分钟
    FIVE_MINUTES = '5min'  # 5分钟
    TEN_MINUTES = '10min'  # 10分钟
    FIFTEEN_MINUTES = '15min'  # 15分钟
    HALF_HOUR = '30min'  # 30分钟
    FORTY_FIVE_MINUTES = '45min'  # 45分钟
    ONE_HOUR = '60min'  # 60分钟
    TWO_HOURS = '2hour'  # 2小时
    THREE_HOURS = '3hour'  # 3小时
    FOUR_HOURS = '4hour'  # 4小时
    SIX_HOURS = '6hour'  # 6小时


class OrderStatus(Enum):
    PENDING_NEW = 'PendingNew'
    NEW = 'Initial'
    HELD = 'Submitted'
    PARTIALLY_FILLED = 'Submitted'
    FILLED = 'Filled'
    CANCELLED = 'Cancelled'
    PENDING_CANCEL = 'PendingCancel'
    REJECTED = 'Inactive'
    EXPIRED = 'Invalid'


@unique
class FinancialReportPeriodType(Enum):
    """
    财报类型
    """
    ANNUAL = 'Annual'  # 年报
    QUARTERLY = 'Quarterly'  # 季报
    LTM = 'LTM'  # 最近四个季度


@unique
class CorporateActionType(Enum):
    """
    公司行动类型
    """
    SPLIT = 'split'  # 拆合股
    DIVIDEND = 'dividend'  # 分红
