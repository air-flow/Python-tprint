# Python-tprint

SQL 結果をテーブル表記で出力する

Python、ライブラリ、コマンドラインユーティリティで表形式のデータをプリティプリントします。

ライブラリの主な使用例は次のとおりです。

SQL の結果をそのまま印字する：MySQL や Oracle、PostgreSQL に SQL を実行した結果を編集することなく関数呼び出しで印字する。

自由な表示形式を選択できる：様々な RDBMS の SQL 表示結果と同じ表形式の出力

SQL を CUI や GUI で操作したときと同じように見える：スマートな列の配置、構成可能な数値の書式設定、小数点による配置

## Library usage

このモジュールは tprint、リストのリストまたは別の表形式のデータ型を最初の引数として受け取り、適切にフォーマットされたプレーンテキストテーブルを出力する関数を 1 つだけ提供します。

### Test Stage

[データ生成と結果表示プログラム](https://github.com/air-flow/Python-tprint/blob/main/src/tutorial/mysql.py)

#### 期待するデータ

**_pymysql_**[^1] ライブラリで _**MySQL**_[^2] に対して **SELECT** クエリの結果の形式。

[^1]: https://pypi.org/project/PyMySQL/
[^2]: https://www.mysql.com/jp/

_cursorclass_ で _pymysql.cursors.DictCursor_ を指定している。

※このデータは Python で自動生成している。だが形式は間違っていない。

```python
[{'crrent_datetime_date_time_today_': '2020/10/23', 'id': 1, 'name': 'a'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 2, 'name': 'abcd'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 3, 'name': 'ab'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 4, 'name': 'ab'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 5, 'name': 'ab'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 6, 'name': 'abc'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 7, 'name': 'ab'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 8, 'name': 'abc'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 9, 'name': 'abcde'},
 {'crrent_datetime_date_time_today_': '2020/10/23', 'id': 10, 'name': 'abc'}]

```

#### 出力する結果

テスト段階では、MySQL に対してコマンドラインから出力した SQL の SELECT 結果と同じになるようにしている。

各列で、各列の最大の文字数に合わせて右寄せするようにしている。

列名も含めた最大の文字数に合わせている。
この例では、の最大文字数を下記の表にまとめている。

|               列                |           最大文字列            | 最大文字数 |
| :-----------------------------: | :-----------------------------: | :--------: |
|               id                |               10                |     2      |
|              name               |              abcde              |     5      |
| crrent_datetime_date_time_today | crrent_datetime_date_time_today |     31     |

```python

#RESULT
+--------------------------------------------+
| id|  name| crrent_datetime_date_time_today_|
+--------------------------------------------+
|  1|    ab|                       2020/10/23|
|  2|     a|                       2020/10/23|
|  3|     a|                       2020/10/23|
|  4|    ab|                       2020/10/23|
|  5| abcde|                       2020/10/23|
|  6| abcde|                       2020/10/23|
|  7|   abc|                       2020/10/23|
|  8|     a|                       2020/10/23|
|  9|    ab|                       2020/10/23|
| 10|    ab|                       2020/10/23|
+--------------------------------------------+
```

## 参考

[tabulate](https://pypi.org/project/tabulate/)
