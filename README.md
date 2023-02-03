# Simple twitter clone

- This is a simple twitter clone allow people to
  register, login logout, post images and text

  登録、ログイン、ログアウト、画像やテキストを投稿するこ とができるシンプルな Twitter クローン

- Used django template

  Django テンプレートを使用しました

- scalable

  スケーラブル

- Don't use superUser to login application, instead register an new user, other wise encounter a bug

  superUser を使用してログインする代わりに、新しいユーザーの登録を行ってください。そうしないと setting page のバグあります

- run `python -m pip install Pillow` if not installed already

# テスト　 C

たとえば、二つのテイブルがあります。

```
id |   name
----+-----------
  1 | fruit
  2 | vegetable
  3 | drink
(3 rows)

id |  name  | price | genre_id
----+--------+-------+----------
  1 | apple  |    10 |        1
  2 | potato |     5 |        2
  3 | coke   |     8 |        3
  5 | orange |    20 |        1
  6 | onion  |     5 |        2
  7 | coffee |    16 |        3
(6 rows)
```

このクエリを使う

```
SELECT genre.name, AVG(item.price) as avg_price
FROM item
JOIN genre ON item.genre_id = genre.id
GROUP BY genre.name, genre.id
ORDER BY genre.id;
```

- genre.name と item.price の平均値を選択して
- item テーブルからデータを取得します
- item テーブルと genre テーブルを結合,Forginkey をつかいます,item.genre_id = genre.id
- GROUP BY を使う、平均値を表現できます
- ORDER BY id 順番

結果：

```
   name    |      avg_price
-----------+---------------------
 fruit     | 15.0000000000000000
 vegetable |  5.0000000000000000
 drink     | 12.0000000000000000
(3 rows)
```

```
idカラム以外はインデックスを貼っていません。貼っておいた方が良いインデックスがもしあれば教えてください。こちらも理由をつけて回答してください
```

`WHERE, JOIN, aggregate function `
ようく使うのカラム、indexes は使うべき。パフォーマンスがあがります。
だが、大きな database,カラムが多いの場、毎回更新、INSERT,DELETE の場、indexes は更新します。だからパフォーマンスが下がります。それとも、index は空間、memory 必要です、それもパフォーマンス、影響を与えるの可能があります。
