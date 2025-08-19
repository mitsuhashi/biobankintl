## 比較表から統合したUKBB-EGA-NIH条文を作成するプロンプト

### 入力について
UKBB, EGA, NIHのMTAの条文を比較した比較表です。以下のどれかがアップロードされます。
comp_ukbb_ega_nih_gemini_1-3.md
comp_ukbb_ega_nih_gemini_4-6.md
comp_ukbb_ega_nih_gemini_7-9.md
comp_ukbb_ega_nih_gemini_10-12.md
comp_ukbb_ega_nih_gemini_13-15.md
comp_ukbb_ega_nih_gemini_16-17.md
markdown形式の箇条書きです。

### 処理の内容について
比較表の対応関係をMTAの形式に変換してください。
対応するUKBB, EGA, NIHの条文のUNIONをとり冗長性を排除してください。
UK BiobankやEGA, NIHとなっている表記を「国際対応BB」としてください。

### 出力形式について

統合MTAを以下の形式で出力してください。出力形式は以下のとおりです。
UKBB条文に１つに対して必ず１つ、以下の形式の出力を出力してください。

* 冗長性を排除したUNION条文（英）
  * 冗長性を排除したUNION条文（日）
  * UNION条文（英）
　　* UNION条文（日）
　* 基になったUKBBの条文（英）
　　* 基になったUKBBの条文（日）
　* 基になったEGAの条文（英）
　　* 基になったEGAの条文（日）
  * 基になったNIHの条文（英）
　　* 基になったNIHの条文（日）

UKBBになくEGAに含まれる文言については、UNION条文と冗長性を排除したUNION条文を太字にしてください。
UKBBになくNIHに含まれる文言については、UNION条文と冗長性を排除したUNION条文を斜体にしてください。
条文（英）と条文（日）はそれぞれ英語、日本語で表記する意味です。
基になったUKBBの条文、UNION条文、冗長性を排除したUNION条文の先頭には必ずUKBBの条文番号をつけてください。

なお、基になったEGAとNIHの条文が存在しない場合は以下の出力にしてください。

* 冗長性を排除したUKBBの条文（英）
  * 冗長性を排除したUKBBの条文（日）
  * 基になったUKBBの条文（英）
　　* 基になったUKBBの条文（日）
