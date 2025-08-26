## UKBB、EGA、NIHのMTAの条文対応表と統合条文の作成

### プロンプトの全体構成

#### 1. 役割と目的の定義
あなたは、複数のMTA（Material Transfer Agreement）を比較・分析し、統合する専門家です。目的は、UKBB, EGA, NIHの3つのMTAから共通項と相違点を抽出し、それらを網羅した汎用的な「統合条文」を作成することです。

#### 2. 入力ファイル定義
*   UKBB: `mta_ukbb.md`
*   EGA: `mta_ega.md`
*   NIH: `mta_nih.md`
* 　入力ファイルが読み込まれていない場合は、そのことを指摘して処理を中止してください。

#### 3. 用語統一の事前定義
統合条文の作成に先立ち、以下の**統一用語対応表**をすべての処理の前提として使用してください。これにより、出力の一貫性を確保します。

| 統合用語 | UKBB | EGA | NIH |
| :--- | :--- | :--- | :--- |
| **Data** | Materials | Data | dataset(s) |
| **Applicant** | Applicant | User Institution | Requester |
| **Principal Investigator (PI)** | Applicant PI | User | PI |
| **Approved Researchers** | Applicant Researchers | Authorised Personnel | Approved Users |
| **Approved Research Project** | Approved Research Project | Project | approved research project |
| **Data Provider** | UK Biobank | Data Producers | NIH, Submitting Investigator(s) |
| **Intellectual Property (IP)** | Intellectual Property Rights (IPRs) | intellectual property | intellectual property (IP) |
| **Breach**|	breach|	breach|	Policy Compliance Violations|
| **Termination**|	terminate|	terminate|	terminate, Project Close-out|
| **Publication of Findings** |	publication of Findings|	Publications	Dissemination of Research Findings|
| **Data Derivatives**|	Results Data, Other Data|	material derived from these Data|	Data Derivatives|


#### 4. 処理ステップの詳細化

**ステップ0: 入力ファイルの確認と宣言**
*   処理を開始する前に、指定された3つの入力ファイル（mta_ukbb.md, mta_ega.md, mta_nih.md）を正常に読み込めたことを確認し、「3つのMTAファイルを正常に読み込みました。処理を開始します。」と宣言してください。

**ステップ1: 条文の構造化と主要コンセプトのマッピング**
*   以下の表記は条文間の親子関係を表現しています。その階層構造を理解して解析してください。以下のMTAの階層構造についてを参照してください。
    * 箇条書きのmarkdown構造、インデント（字下げ）
    * 条文番号（例: 1.1は1の子要素）
    * コロンで終了している条文のその子階層
*   UKBBの第２階層の各条文（例：1.1）を１論理単位としてEGA, NIHとのマッピング処理を行なってください。
*   親条文（例: 1.2）が複数の子条文（例: 1.2.1, 1.2.2）を持つ場合、親条文と子条文1, 親条文と子条文2というように意味を崩さずに独立した文章に分割して考えてください。下記例のように、親条文の文意（主語、動詞など）を各子条文に補完して、一つの独立した条文として処理してください。
　　*  階層構造の処理例:
       *  入力: 1.2 UK Biobank warrants...: 1.2.1 it is entitled...
       *  AIが解釈すべき完全な文章: UK Biobank warrants that it is entitled...
*   UKBBの各条文が持つ中心的な法的意味を分析し、「主要コンセプトリスト」から最も関連性の高いキーワードを内部的なタグとして**原則1個（ただし、主要なコンセプトが複数存在する場合は、重要度順に複数）**付与してください。
*   マッピングを行う際は、以下の視点を考慮し、どれかに一致する場合はタグを付与してください。
    *   直接的対応: 条文の目的と内容がほぼ一致するもの。
    *   間接的対応: ある行為を規定する条文（例: 利用目的の制限）と、その違反時の罰則を規定する条文（例: 違反時の契約解除）など、論理的に関連するもの。
    *   概念的対応: 条文の文言は異なるが、背景にある法的・倫理的原則（例: データ利用の透明性確保）が共通するもの。
*  「主要コンセプトリスト」付与できない場合は、新しいコンセプトを追加してください。
*   次に、EGAとNIHの全条文をスキャンし、同じタグが付与されうる関連性の高い条文をUKBBとマッピングしてください。これにより、網羅的かつ体系的な対応付けを行います。
*   マッピング結果を内部的に保持してください。

**MTAの階層構造について**
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

**主要コンセプトリスト**

*  1. 契約の基本事項
    *   **1.1. Data/Materialsの提供:** 提供の合意、範囲、期間に関する規定。
    *   **1.2. 提供者の保証と免責:** 提供者が保証する事項（例：提供権限）と、保証しない事項（例：データの品質、"as is"原則）。
    *   **1.3. 契約期間と終了:** 契約の有効期間、更新、終了手続き、終了後のデータ破棄に関する規定。
    *   **1.4. 料金:** データアクセスに伴う費用に関する規定。
*  2. 利用者の責務と利用条件
    *   **2.1. 利用目的・範囲の制限:** 承認された研究プロジェクト、研究目的に限定する規定。
    *   **2.2. 利用者の限定:** 承認された研究者（PI、共同研究者等）に利用を限定する規定。
    *   **2.3. 第三者への共有・移転の禁止:** 承認されていない第三者へのデータ共有、販売、譲渡等を禁止する規定。
    *   **2.4. 法令・倫理遵守:** 関連法規、ガイドライン、倫理委員会の承認等を遵守する義務。
    *   **2.5. 参加者の非特定化:** 研究参加者を特定しようとする行為の禁止。
*  3. データセキュリティとコンプライアンス
    *   **3.1. データセキュリティ:** 適切なセキュリティ基準の維持、インシデント発生時の報告義務。
    *   **3.2. 秘密保持:** データや関連情報の機密性を保持する義務。
    *   **3.3. 監査・報告:** 定期的な進捗報告（年次報告等）の義務や、提供者による監査の権利。
    *   **3.4. 契約違反時の措置:** 契約違反が認められた場合のアクセス停止、データ破棄要求などの罰則規定。
*  4. 研究成果の取り扱い
    *   **4.1. 成果の公開と謝辞:** 研究成果の公表義務、謝辞の記載方法に関する規定。
    *   **4.2. 知的財産権（IP）:** 元データ、生成データ、発明に関する知的財産権の帰属やライセンスに関する規定。
*  5. 一般条項
    *   **5.1. 責任の制限:** 契約違反等によって生じる損害賠償責任の上限に関する規定。
    *   **5.2. 下請け・委託:** 第三者への処理委託（クラウド利用等）に関する条件や手続き。
    *   **5.3. 紛争解決:** 当事者間で紛争が生じた場合の解決手続き（協議、調停、裁判管轄等）。
    *   **5.4. その他:** 通知方法、不可抗力、完全合意条項など。

**ステップ2: 比較分析と統合条文の作成**
*   ステップ1のマッピング結果に基づき、UKBBの条文順に一行ずつ最後まで処理を行います。
*   **対応する条文が存在する場合:**
    *   **コンセプト** UKBB, EGA, NIH間で共有する主要コンセプトのカテゴリを記述してください。
    *   **一致点** 直接的対応、間接的対応、概念的一致の観点から一致する内容を記述してください。
    *   **不一致点** 直接的対応、間接的対応、概念的一致の観点から一致しない内容を記述してください。
    *   **統合条文**
        *   なるべく原文の表記を尊重してください。
        *   共通する内容は、最も包括的または標準的と思われる表現にまとめてください。なるべく原文の表記を尊重してください。
        *   不一致点のうち、補完しあえる内容（例: EGAの手続きとNIHの例外規定）は、追記する形で一つの条文に統合してください。
        *   方針が根本的に矛盾・対立する内容（例: 知的財産の扱い）は、統合せず `{案1: [MTA Aの趣旨], 案2: [MTA Bの趣旨]}` の形式で併記してください。
        *  色分けと日本語訳の手順: 統合条文（「外国統合英」および「外国統合日」）を作成する際は、以下の手順を厳密に守ってください。
          *  まず、英語の統合条文（「外国統合英」）を生成します。
          *  次に、その英語条文に対して、以下の色分けルールを適用し、HTMLの<span style='color: ...'>タグで文言を囲みます。以下の優先順位で色をつけます。
               * 由来元の文言（最優先）
                  * UKBB由来の文言: color: black;
                  * EGA由来の文言: color: blue;
                  * NIH由来の文言: color: green;
                  * 統合して文言を変更しても文意が変わらない場合は、MTAの色（black, blue, green）を適用すること。
               * 統一用語：汎用化・再構成部分（赤）とせず、文脈上ベースとなったMTAの色を適用してください。
               * 残りの部分：color: red; 以下のルールで着色してください。
                 *  <span style='color: red;'>AIが独自に追加した語句</span>: <span style='color: red;'>複数のMTAの文脈を自然につなぐためにAIが補った接続詞、関係詞、またはどのMTAにも直接の由来がない一般的な表現（例: "agrees to", "shall ensure that"など）は赤色で示します。</span>
                 * <span style='color: red;'>ただし、以下の場合は由来元の色を維持してください。</span>
                 * <span style='color: red;'>統一用語対応表にある用語（これは赤色にしません）。</span>
                 * <span style='color: red;'>単数形・複数形の変更、冠詞の追加・削除、動詞の時制変更など、文法的な整合性を取るための軽微な調整。</span>
                 構造の再編: 複数の条文から要素を抜き出して新しい一文を構成した場合の文の骨格部分。
                 *  接続詞・冠詞・時制の変更: 文脈を自然にするための and, or, the, a, shall be, agrees to などの補完や変更。
                 *  概念の抽象化: 複数のMTAの表現をまとめるための上位概念的な言葉の選択。（例：「Findings, publications, reports」を「Research Results」とするなど）
                 *  単数形・複数形の変更、冠詞の追加・削除、動詞の時制変更など、軽微な文法的調整は、由来元の色を維持してください。
               * <span style='color: red;'>日本語訳の色分けは、英語の<span>構造に忠実に従うことを基本としますが、日本語として不自然になる場合は、意味のまとまりを優先して柔軟に色を適用してください。翻訳の自然さが最も重要です。</span>
    *   **統合手順：** 以下のいずれかのパターンを参考に、どのような論理で条文を構築したかを明確に説明してください。
        * 【最大公約数パターン】: 3つのMTAに共通する中核的な原則を抽出し、それを基本条文としました。（例：免責条項）
        * 【積み上げパターン】: MTA Aの基本的な規定を骨子とし、そこにMTA Bの具体的な手続きやMTA Cの例外規定を追記・補完する形で、より網羅的な条文を構築しました。（例：データ利用目的）
        * 【最厳格ルール採用パターン】: 各MTAの規定の中で、利用者の義務や禁止事項が最も厳しいものを採用して統合しました。（例：第三者提供の禁止）
        * 【選択肢パターン】: 知的財産権の扱いのように、各MTAの方針が根本的に対立し、一つの条文に統合することが不可能なため、{案1: [MTA Aの趣旨], 案2: [MTA Bの趣旨]}の形式で併記しました。
        * 【単独ルール採用パターン】: あるMTAにしか存在しない特有の規定だが、汎用的なMTAにおいても有益または重要であると考えられるため、そのMTAの条文を基に統合条文を作成しました。（例：UKBBの生成データ分類、NIHの透明性確保のための研究概要公開）
*   **対応する条文が存在しない場合:**
    *   UKBBのMTAの条文を統合条文として記載し、「一致点」「不一致点」は「他MTAに直接対応する条文なし」などと記述してください。
    *   統一用語に置き換えてください。

**ステップ3: 残存条文の処理**
*   UKBBの全条文を処理した後、まだどの条文にも対応付けられていないEGAおよびNIHの条文を抽出し、テーブルの末尾に追加してください。
*   EGAとNIHの間でもステップ2と同様に対応関係を抽出してください。

**ステップ4: 出力**
*   最終結果を**単一の完全なHTMLコードブロック**として出力してください。
*   出力に「外国統合MTA/DTA」という名前をつけて、以降の質問で参照できるようにしてください。
*   太字と指定された場合は、<strong>タグで囲ってください。
*   テーブルの各列の定義は以下の通りです。

|列名|値の内容|言語|
|---|---|---|
|統合No.|外国統合MTA条文|英語|
|統合題名英|統合条文題名|英語|
|統合題名日|統合条文題名|日本語|
|統合英|統合条文|英語|
|統合日|統合条文|日本語|
|統合手順|統合手順|日本語|
|コンセプト|対応する条文間で共有する主要コンセプト|
|一致点|対応する条文の一致点|日本語|
|不一致点|対応する条文の不一致点|日本語|
|UKBB No.|UKBB条文番号|英語|
|UKBB英|UKBB原文|英語|
|UKBB日|UKBB原文|日本語|
|EGA No.|EGA条文番号|英語|
|EGA英|EGA原文|英語|
|EGA日|EGA原文|日本語|
|NIH No.|NIH条文番号|英語|
|NIH英|NIH原文|英語|
|NIH日|NIH原文|日本語|

* 統合No.について
　* 由来に応じてプレフィックスをつけ、その後に条文番号を続けます
    * UKBBが存在する場合、I-<UKBB条文番号>
    * UKBBが存在せずEGAが存在する場合、I-E<UKBB条文番号>
    * NIHだけが存在する場合、I-N<NIH条文番号>
  * 条文番号が２桁になるように１桁の場合は先頭に0をつけます。
    * I-1.1 → I-01.01
    * I-E1 → I-E01
    * I-17.1 → I-17.01
    * I-1.1.2 → I-01.01.02
* 統合条文題名は、統合条文の内容を10文字程度でタイトルをつけてください。
* UKBB No., EGA No., NIH No. について
  * 条文番号の格桁が２桁になるように１桁の場合は先頭に0をつけます。以下が例です
    * 1.1 → 01.01
    * 17.1 → 17.01
    * 1.1.2 → 01.01.02
* 原文の色は以下の通りにしてください。
  * UKBB原文: color: black;
  * EGA原文: color: blue;
  * NIH原文: color: green;
*   原文を表示する条文中で、特定の国・地域に固有の法律、規制、機関名（例: Human Tissue Act 2004, NIH, EU embargo）に関する文書は太字にしてください。
*   複数の条文が１つのセルに入る場合は、先頭に条文番号を書き、次の文との間に改行を入れてください。
*   最終出力前に、プロンプトの指示（特に、全条文の網羅、色分け、HTML形式など）がすべて満たされているか自己チェックしてください。

## 最終出力前のチェックリスト
以下のすべての項目が「はい」であることを確認してから、最終的なHTMLテーブルを出力してください。
* [ ] バッファサイズの上限を超えてしまって３つのファイルを原文通りに記憶できないなどの理由で入力内容を割愛していませんか。
* [ ] 表はHTML形式で出力されていますか？
* [ ] UKBBの第2階層の条文（1.1から17.10まで）が、それぞれ独立した行としてすべて出力されていますか？（条文のまとめや省略はありませんか？）
* [ ] UKBBの条文をすべて処理した後、UKBBに対応しなかったEGAおよびNIHの単独条文が、テーブルの末尾に追加されていますか？
* [ ] 列の色分けルールは守られていますか？
   *   UKBB由来の文言は黒色ですか？
   *   EGA由来の文言（例: 'moratorium period'）は青色で反映されていますか？
   *   NIH由来の文言（例: 'indemnify', 'IRB permission'）は緑色で反映されていますか？
* [ ] 内容が競合し統合できない条文は、「外国統合英」列で{案1, 案2}の形式で併記されていますか？
* [ ] 「一致点」「不一致点」の列は、具体的かつ明確な言葉で記述されていますか？
* [ ] 生成されるHTMLは非常に長くなることが予想されます。決して出力を分割したり、途中で要約したりせず、必ず一度の応答で、単一の完全なHTMLコードブロックとして全てを出力してください。

以上、よろしくお願いいたします。