#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from libfinance.api.calendar import get_all_trading_dates, public_api, get_trading_dates



pubic_returns = public_api()

all_trading_dates = get_all_trading_dates()


start_date = "2024-01-01"
end_date = "2024-02-27"

trading_dates = get_trading_dates(start_date, end_date)
print(trading_dates)
