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
比較表の内容からUKBB, EGA, NIHのUNIONをとった統合MTAを作成してください。

### 出力形式について

まず、入力した比較表の最後の条文をそのまま出力してください。

その次に統合MTAを以下の形式で出力してください。出力形式は以下のとおりです。

・条文（英）
　・条文（日）
　・基になったUKBBの条文（英）
　　・基になったUKBBの条文（日）
　・基になったEGAの条文（英）
　　・ 基になったEGAの条文（日）
  ・基になったNIHの条文（英）
　　・基になったNIHの条文（日）

また、UKBBになく、EGAまたはNIHに記載されている内容に該当する場所を条文（英）と条文（日）でハイライトしてください。
条文、基になった条文の先頭には必ず条文番号をつけてください。
