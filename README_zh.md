# libfinance
\[ [English](README.md) | 中文 \]

`libfinance`是一个python函数库，用以更方便的获取金融数据。她的目标是为学术研究人员，研究者，开发者提供研究环境和生产环境下的高质量的金融数据。

# 安装

方法1: 通过python的包管理器pip的方式安装libfinance

``` {.sourceCode .bash}
$ pip install libfinance
```

方法2: 源代码的安装(以开发者的模式)
~~~
git clone https://github.com/StateOfTheArt-quant/libfinance.git
cd libfinance
pip install -e .
~~~

# quick-start

~~~
from libfinance import get_trading_dates, get_price

trading_dates = get_trading_dates(start_date="2023-12-25", end_date="2024-01-11")
print(trading_dates)


DatetimeIndex(['2023-12-25', '2023-12-26', '2023-12-27', '2023-12-28',
               '2023-12-29', '2024-01-02', '2024-01-03', '2024-01-04',
               '2024-01-05', '2024-01-08', '2024-01-09', '2024-01-10',
               '2024-01-11'],
              dtype='datetime64[ns]', freq=None)
              



data = get_price(order_book_ids=["000001.XSHE","600000.XSHG"], start_date="2024-03-01", end_date="2024-03-11")
print(data)
        
                           open   high    low  close       volume
order_book_id datetime                                           
000001.XSHE   2024-03-01  10.59  10.60  10.43  10.49  182810290.0
              2024-03-04  10.45  10.50  10.32  10.33  165592954.0
              2024-03-05  10.30  10.47  10.26  10.43  181731907.0
              2024-03-06  10.40  10.45  10.33  10.33  134564016.0
              2024-03-07  10.33  10.64  10.33  10.38  201616589.0
              2024-03-08  10.35  10.44  10.30  10.38  111397428.0
              2024-03-11  10.38  10.47  10.34  10.47  121067298.0
600000.XSHG   2024-03-01   7.13   7.16   7.10   7.11   29431801.0
              2024-03-04   7.12   7.12   7.05   7.07   27855963.0
              2024-03-05   7.05   7.18   7.04   7.16   41756232.0
              2024-03-06   7.17   7.22   7.12   7.12   25918749.0
              2024-03-07   7.12   7.20   7.11   7.14   24690348.0
              2024-03-08   7.12   7.17   7.11   7.12   19861794.0
              2024-03-11   7.13   7.17   7.06   7.11   26195498.0
~~~

# 文档

更多的信息以及函数说明及用例见 [Documentation](https://libfinance.readthedocs.io/zh/latest/)


# 加入我们的社区
通过微信公众号-群入口的方式加入[libfinance](https://github.com/StateOfTheArt-quant/libfinance)获取更多以及及时的信息:

<div>
    <img alt="ds" src="/docs/source/_static/img/code.png" width="600" height="220">
</div>