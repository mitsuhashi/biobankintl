## UKBB、EGA、NIHのMTAの条文対応表と統合条文の作成

### プロンプトをfixするまでテストランについて

* まずはテストランモードを実施してください。
* ステップ１及び２ともUKBBの1.1から3.9までについて実施してください。
* 改良すべきプロンプトの修正案を出力してください。

### 処理の概要

#### ステップ１. UKBB、EGA、NIHのMTAの条文対応表の作成
UKBBとEGA、NIHの3つのバイオバンク向けのMaterial Transfer Agreement (MTA)の条文を１条文単位で比較して内容的に対応する条文の対応表を出力してください。

#### ステップ2. 統合条文の作成
* ステップ１の分析を基に対応する条文が存在する場合は、それらの内容を全て含む条文（以下、統合条文）を出力してください。

#### その他
* バッファサイズの上限を超えてしまって３つのファイルを原文通りに記憶できないなどの理由で内容を変更する必要が場合はその旨を出力してください(Gemini Pro 2.5ではないはず）。
* プロンプトの指示に対してどのように対応したかを説明してください。
* プロンプトの内容について質問がある場合は質問してください。プロンプトを書き換えます。

### 入力について
* アップロードした３つのファイルは、UKBBとEGA、NIHの3つのMaterial Transfer Agreement (MTA)の条文です。バイオバンク名とアップロードしたファイル名の対応は以下のとおりです。
  * UKBB: mta_ukbb.md
  * EGA: mta_ega.md
  * NIH: mta_nih.md
* 各ファイルはmarkdown形式の箇条書きです。

#### MTAの階層構造について
* 箇条書きの構造と条文番号が階層関係を表現しています。例えば、1.1 は 1の子要素です。
* 条文がコロンで終了している条文は、その子階層と関係があることを考慮して条文の意味を理解してください。以下が階層構造の例です。
  *   1.2 UK Biobank warrants to the Applicant that for the purposes of this MTA:
      *   1.2.1 it is entitled to supply the Materials to the Applicant;
      *   1.2.2 consent to take part in UK Biobank has been obtained from the Participants and further, consent under the Human Tissue Act 2004, has been obtained from the relevant Participants; and
      *   1.2.3 the use of the Materials for the Approved Research Project falls within UK Biobank's generic Research Tissue Bank (RTB) approval from the NHS North West REC, available here.
  *   **6. The User Institution agrees that the Data Producers, and all other parties involved in the creation, funding or protection of these Data:**
      *   a) make no warranty or representation, express or implied as to the accuracy, quality or comprehensiveness of these Data;
      *   b) exclude to the fullest extent permitted by law all liability for actions, claims, proceedings, demands, losses (including but not limited to loss of profit), costs, awards damages and payments made by the Recipient that may arise (whether directly or indirectly) in any way whatsoever from the Recipients use of these Data or from the unavailability of, or break in access to, these Data for whatever reason and;
      *   c) bear no responsibility for the further analysis or interpretation of these Data.
*   **2. Cost Jor No Cost**
    *   a. Registry is making the Data available to Researcher at no cost to Researcher. [If payment is desired, it may be beneficial to add payment terms, e.g., invoicing procedure, payment due dates].
    *   b. Researcher bears all costs and expenses incurred by Researcher to access and use the Data, and conduct the Research.
* 条文番号は一意になるようにつけてください。上の例の場合、1.2.1はそのままで一意ですが、2番目と3番目の例は 6.a, 2.aのように親階層の番号を先頭につけてください。

###　処理内容について

#### ステップ１. UKBB、EGA、NIHのMTAの条文対応表の作成
* UKBBの第２階層の条文（例：1.1 UK Biobank ...）を1.1から１条ずつ読み込み、内容的に対応するEGA、NIHの条文を探してください。
* 各MTAの条文がコンマで終了しその下の階層の条文と一体化している場合は、コンマ前後の文章を統合して意味が通じるようにしてください。
* UKBBの条文に対して複数のEGA, NIHの条文が対応する場合は１対応ずつ出力してください。
* 対応関係が存在する場合は、対応する条文の一致点と不一致点をそれぞれ出力してください。
* UKBBの条文に対応するEGA, NIHの条文が存在しない時はUKBBの条文だけを出力してください。
* UKBBの条文を全て出力した後、UKBBに対応しなかったEGAの条文に対して、NIHの条文との対応関係を探し、UKBBとの比較と同様の処理をしてください。
* EGAの条文を全て出力した後、UKBBにもEGAにも対応しなかったNIHの条文との対応関係を出力してください。
* UKBB, EGA, NIHの条文は原文通り全て出力してください。
* UKBB, EGA, NIHの条文には英国やEU、米国の法制度などのローカルな内容と考えられる記述を赤字にしてください。

#### ステップ2. 統合条文の作成
* 対応するUKBB, EGA、NIHの条文の内容を含む統合条文を作成してください。
* UKBB、EGA、NIHの条文で表記が違うが同じ意味の語句（主語や目的語など）を同じ表記に揃えてください。統合条文用の語句は提案してください。
* UKBB、EGA、NIHで、統一した語句の対応表を出力してください。
* 不一致点があり統合できない場合は、{条文案1, 条文案2...}のようにカッコ書きで列挙してください。
* 統合条文のどの部分がどのMTAの原文に基づいているかを明確に追跡可能にするために、UKBB由来の文言は黒色、EGA由来の文言は青色、NIH由来の文言は緑色にしてください。由来がはっきりしない場合は赤色にしてください。


###　出力について

#### 

* 出力表はHTMLで出力してください。
* 出力表の行は以下の内容を出力してください。列名はヘッダ行の値です。
* 各列指定した言語で出力してください。
* UKBBの条文番号順→EGAの条文番号順→NIHの条文順に出力してください。

|列名|値の内容|言語|
|---|---|---|---|
|外国統合No.|外国統合MTA条文|英語|
|外国統合英|統合条文|英語|
|外国統合日|統合条文|日本語|
|統合手順|統合手順|日本語|
|UKBB No.|UKBB条文番号|英語|
|UKBB英|UKBB原文|英語|
|UKBB日|UKBB原文|日本語|
|EGA No.|EGA条文番号|英語|
|EGA英|UKBB原文|英語|
|EGA日|UKBB原文|日本語|
|NIH No.|EGA条文番号|英語|
|NIH英|UKBB原文|英語|
|NIH日|UKBB原文|日本語|
|一致点|対応する条文の一致点|日本語|
|不一致点|対応する条文不一致点|日本語|

## 最終出力前のチェックリスト
以下のすべての項目が「はい」であることを確認してから、最終的なHTMLテーブルを出力してください。
[ ] バッファサイズの上限を超えてしまって３つのファイルを原文通りに記憶できないなどの理由で入力内容を割愛していませんか。
[ ] 表はHTML形式で出力されていますか？
[ ] ヘッダー行は指定された14列（外国統合No., 外国統合英, ... 不一致点）をすべて含んでいますか？
[ ] UKBBの第2階層の条文（1.1から17.10まで）が、それぞれ独立した行としてすべて出力されていますか？（条文のまとめや省略はありませんか？）
[ ] UKBBの条文をすべて処理した後、UKBBに対応しなかったEGAおよびNIHの単独条文が、テーブルの末尾に追加されていますか？
[ ] 「外国統合英」列の色分けルールは守られていますか？
[ ] UKBB由来の文言は黒色ですか？
[ ] EGA由来の特徴的な文言（例: 'moratorium period'）は青色で反映されていますか？
[ ] NIH由来の特徴的な文言（例: 'indemnify', 'IRB permission'）は緑色で反映されていますか？
[ ] 複数のMTAに共通する概念や、統合のために新しく構成した文言は赤色ですか？
[ ] 内容が競合し統合できない条文は、「外国統合英」列で{案1, 案2}の形式で併記されていますか？
[ ] すべての条文について、日本語訳の列（外国統合日, UKBB日, EGA日, NIH日）は埋まっていますか？（対応なしの場合は除く）
[ ] 「一致点」「不一致点」の列は、具体的かつ明確な言葉で記述されていますか？
[ ] 出力は途中で途切れることなく、単一の完全なHTMLコードブロックとして生成されていますか？

以上、よろしくお願いいたします。