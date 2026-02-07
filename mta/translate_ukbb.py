
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# 日本語フォントの登録
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

# PDF生成の設定
filename = "UK_Biobank_MTA_Full_Japanese.pdf"
doc = SimpleDocTemplate(filename, pagesize=A4,
                        rightMargin=50, leftMargin=50,
                        topMargin=50, bottomMargin=50)

styles = getSampleStyleSheet()
# スタイルの定義
style_normal = ParagraphStyle(name='JapaneseNormal', parent=styles['Normal'], fontName='HeiseiKakuGo-W5', fontSize=9, leading=13, alignment=TA_JUSTIFY)
style_title = ParagraphStyle(name='JapaneseTitle', parent=styles['Title'], fontName='HeiseiKakuGo-W5', fontSize=16, leading=20, spaceAfter=20)
style_h1 = ParagraphStyle(name='JapaneseHeading1', parent=styles['Heading1'], fontName='HeiseiKakuGo-W5', fontSize=11, leading=15, spaceBefore=12, spaceAfter=6)
style_h2 = ParagraphStyle(name='JapaneseHeading2', parent=styles['Heading2'], fontName='HeiseiKakuGo-W5', fontSize=10, leading=13, spaceBefore=6, spaceAfter=3, leftIndent=10)
style_h3 = ParagraphStyle(name='JapaneseHeading3', parent=style_normal, fontName='HeiseiKakuGo-W5', fontSize=9, leading=13, leftIndent=20)
style_list = ParagraphStyle(name='JapaneseList', parent=style_normal, leftIndent=20)
style_center = ParagraphStyle(name='JapaneseCenter', parent=style_normal, alignment=TA_CENTER)

story = []

# --- Page 1 ---
story.append(Paragraph("新規申請者 MTA – データのみ (2023)", style_normal))
story.append(Paragraph("ACCESS_031_F 26/10/2023 v1.4", style_normal))
story.append(Spacer(1, 24))

story.append(Paragraph("試料提供契約 (Material Transfer Agreement)", style_title))

story.append(Paragraph("拝啓", style_normal))
story.append(Spacer(1, 6))
story.append(Paragraph("<b>申請者 殿：</b>", style_normal))
story.append(Paragraph("<b>申請参照番号：</b>", style_normal))
story.append(Spacer(1, 12))

p1_text = """
UKバイオバンク・リミテッド（以下「<b>UKバイオバンク</b>」）は、UKバイオバンクのリソースを使用するための貴殿の申請を承認できることを嬉しく思います。
本申請に対するUKバイオバンクの承認は90日間有効であり、その間に申請者はアクセス利用料（Access Charges）を支払い、本試料提供契約（以下「<b>MTA</b>」）を締結する必要があります。
これらはアクセスが付与される前の最終段階です。これらの手順が90日以内に申請者によって行われない場合、申請者はアクセスを再申請する必要があります。
<br/><br/>
<b>当事者</b><br/>
本契約は、UKバイオバンクと申請者（以下、各々を「<b>当事者</b>」、総称して「<b>両当事者</b>」）との間の合意です。
申請者PI（主任研究者）はMTAの当事者ではありませんが、UKバイオバンクは、申請者のUKバイオバンクおよびUKバイオバンク参加者に対する義務を十分に認識させるため、
申請者PIに対し、本MTAの規定を「読み、理解した」ことを確認する署名を求めています。
申請者は、本承認済み研究プロジェクトに関与する申請者PIおよびすべての申請者研究員の行為に対して責任を負うものとしますが、
共同研究機関（Collaborator Institution(s)）、主任共同研究者（Lead Collaborator(s)）、または共同研究者（Collaborator Researcher(s)）の行為に対しては責任を負いません。
<br/><br/>
<b>契約の構成</b><br/>
本MTAは発効日に発効します。本申請/承認済み研究プロジェクトに関して以前のバージョンのMTAに同意している場合、
以前のバージョンは発効日をもって自動的に終了し、本MTAに置き換えられます。
<br/><br/>
<b>標準条件および付属書</b><br/>
UKバイオバンクの標準MTAの内容およびそれに含まれる条件は、交渉不可能です。
本MTAには、添付の申請者利用規約（そこで言及されている文書および/または資料を含む）、申請書の内容（該当する場合）、および以下の付属書が組み込まれます。
<br/>• 付属書1（データ処理の記述およびUK補遺）
<br/>• 付属書2（セキュリティ対策）
<br/>• 付属書3（申請者年次プロジェクト報告書テンプレート）および
<br/>• 付属書4（承認済み研究プロジェクト – 申請者が利用可能となる本試料の概要）
<br/><br/>
本MTAで使用される定義は、15〜16ページに記載されています。
<br/><br/>
<b>支払い</b><br/>
支払われるべきアクセス利用料は、申請書の支払いセクションに記載されています。これにより、付加価値税（VAT）が含まれた請求書を作成することができます
（適切な場合。申請者が英国外に拠点を置く場合、VATは含まれません）。これらのアクセス利用料の概要は付属書4にも記載されています。
<br/><br/>
支払いは、銀行振込またはSage Payを通じて、以下の宛先に英ポンド（GBP）で行う必要があります。
<br/><br/>
<b>銀行:</b> Barclays Bank PLC
<br/><b>口座名:</b> UK Biobank Limited
<br/><b>口座番号:</b> 33069427
<br/><b>ソートコード:</b> 20-24-41
<br/><b>IBAN:</b> GB78 BARC 2024 4133 0694 27
"""
story.append(Paragraph(p1_text, style_normal))
story.append(Spacer(1, 12))
story.append(Paragraph("敬具", style_normal))
story.append(Spacer(1, 12))
story.append(Paragraph("<b>UKバイオバンクを代表して</b><br/>Jonathan Sellors<br/>General Counsel & Company Secretary", style_normal))
story.append(PageBreak())

# --- Terms and Conditions (Pages 2-14) ---
story.append(Paragraph("申請者利用規約", style_title))

# Clause 1
story.append(Paragraph("1. UKバイオバンクによる本試料の提供", style_h1))
story.append(Paragraph("1.1 UKバイオバンクは、本MTAの規定に従い、本MTAに定める期間および方法で申請者に本試料を提供することに同意する。", style_normal))
story.append(Paragraph("1.2 UKバイオバンクは、本MTAの目的において以下を申請者に保証する：", style_normal))
story.append(Paragraph("1.2.1 申請者に本試料を提供する権利を有していること。", style_h2))
story.append(Paragraph("1.2.2 UKバイオバンクへの参加に関する同意が参加者から得られており、さらに2004年ヒト組織法に基づく同意が関連する参加者から得られていること。および", style_h2))
story.append(Paragraph("1.2.3 承認済み研究プロジェクトのための本試料の使用が、NHS North West RECからのUKバイオバンクの包括的な研究組織バンク（RTB）承認の範囲内であること（こちらで入手可能）。", style_h2))
story.append(Paragraph("1.3 申請者は、本試料が、満足のいく品質、特定の目的または用途への適合性、または本試料の使用が第三者の権利を侵害しないことに関するいかなる保証もなく、「現状有姿（as is）」で提供されることに同意する。本MTAに明示的に記載されている場合を除き、制定法、コモンロー、その他による明示または黙示を問わず、すべての保証、条件、規約は、法律で認められる最大限の範囲で除外される。", style_normal))

# Clause 2
story.append(Paragraph("2. 申請者による本試料の使用", style_h1))
story.append(Paragraph("2.1 申請者は、本試料について以下に同意する：", style_normal))
story.append(Paragraph("2.1.1 本MTAの条件に従ってのみ使用すること。", style_h2))
story.append(Paragraph("2.1.2 許可された目的のために承認済み研究プロジェクトを実施するためにのみ使用すること。", style_h2))
story.append(Paragraph("2.1.3 禁止された兵器（生物兵器を含む）に関連する目的で使用してはならず、そのような目的で使用されることが意図されている、またはその可能性が高いことが判明または疑われる場合は譲渡してはならない。", style_h2))
story.append(Paragraph("2.1.4 その行為が禁輸措置の条件に違反することになる場合、国連、EU、英国、またはOSCEの禁輸措置の対象となる仕向地に譲渡してはならない。および", style_h2))
story.append(Paragraph("2.1.5 申請者機関によって、および申請者内の個人レベルで、申請者PI、申請者研究員、および関連会社および第三者処理業者（申請者によって指名されたもの）によってのみ使用されること。", style_h2))
story.append(Paragraph("2.2 申請者は、本試料を共有、サブライセンス、開示、譲渡、販売、贈与、または他の人物や許可されていない第三者に提供してはならない。", style_normal))
story.append(Paragraph("2.3 本MTAの他の規定を損なうことなく、条項2.1または2.2の規定に対する実際の違反または予期される違反があった場合、UKバイオバンクは本契約を直ちに終了し、UKバイオバンクが提供した本試料の即時返却または破棄を要求する権利を有する。", style_normal))
story.append(Paragraph("2.4 申請者は、申請者PI、申請者研究員、および関連会社および第三者処理業者が、本MTAの条件およびデータ保護法を認識し、遵守することを保証しなければならない。申請者PI、申請者研究員、関連会社、または第三者処理業者の作為または不作為は、当該申請者が完全な責任と義務を負う当該申請者の作為とみなされる。", style_normal))
story.append(Paragraph("2.5 本MTAは、申請者に明示的に付与された権利のみを付与する。疑義を避けるために付言すると、本MTAのいかなる規定も、UKバイオバンクが同じ本試料（またはUKバイオバンクのリソース内の他のデータおよび/またはサンプル）を、アクセス手続（UKバイオバンクのウェブサイトで入手可能、随時更新される）に従って別の第三者に提供すること、またはUKバイオバンクのその他の運営目的のために提供することを妨げるものではない。", style_normal))
story.append(Paragraph("2.6 申請者に提供される本試料に関して：", style_normal))
story.append(Paragraph("2.6.1 UKバイオバンクは本試料の所有者であり、本試料の知的財産権の所有者である。および", style_h2))
story.append(Paragraph("2.6.2 UKバイオバンクはこれにより、本MTAの条件に従い、許可された目的のために本試料を使用するための、取消可能、全世界的、ロイヤリティフリー、非独占的、譲渡不可のライセンス（ただし所有権は含まない）を、期間中申請者に付与する。", style_h2))

# Clause 3
story.append(Paragraph("3. 申請者によるデータの生成", style_h1))
story.append(Paragraph("<i>承認済み研究プロジェクト中の申請者による、または申請者に代わるデータの生成</i>", style_normal))
story.append(Paragraph("3.1 承認済み研究プロジェクトの実施において申請者が生成したデータは、以下のカテゴリに該当するとみなされる：", style_normal))
story.append(Paragraph("3.1.1 結果データ（Results Data）: 知見（Findings）の基礎となり、他の有能な研究者が知見を生成できるようにするデータおよび方法論（例えば、SAS/R/Stataスクリプト）。", style_h2))
story.append(Paragraph("3.1.2 知見（Findings）: 承認済み研究プロジェクトの結果として申請者が生成した知見。および/または", style_h2))
story.append(Paragraph("3.1.3 その他のデータ（Other Data）: 上記の2つのカテゴリのいずれにも該当しない、申請者が生成したその他すべてのデータ。", style_h2))
story.append(Paragraph("<i>生成されたデータの所有権</i>", style_normal))
story.append(Paragraph("3.2 条項3.3に規定されている場合を除き、申請者は知見、結果データ、およびその他のデータの知的財産権（IPR）を所有するものとする。申請者はこれにより、知見、結果データ、およびその他のデータを使用、複製、配布、出版、保存、およびその他の方法で普及させるための、恒久的、取消不能、全世界的、全額払込済み、ロイヤリティフリー、完全にサブライセンス可能な非独占的ライセンスをUKバイオバンクに付与する。", style_normal))
story.append(Paragraph("3.3 本MTAのいかなる規定も、本試料の知的財産権を申請者に譲渡するように作用するものではない。知見、結果データ、またはその他のデータに本試料が組み込まれている限りにおいて、それらの本試料の知的財産権はUKバイオバンクの財産であり続け、申請者には帰属しない。", style_normal))
story.append(Paragraph("3.4 申請者はUKバイオバンクに対し、UKバイオバンクによる申請者の知見および結果データの受領および使用が、第三者の既存の知的財産権を含む権利を侵害しないことを確認する。このような確認は以下とする：", style_normal))
story.append(Paragraph("3.4.1 知見の公表または結果データのUKバイオバンクへの返却の時点でそれぞれ行われたとみなされる。および", style_h2))
story.append(Paragraph("3.4.2 申請者の最善の知識と確信に基づき、合理的かつ勤勉な調査を行った上で提供される（ただし、この義務の範囲には、申請者が外部の特許調査を行う要件は含まれない）。", style_h2))
story.append(Paragraph("<i>申請者が行った発明/開発に対する権利</i>", style_normal))
story.append(Paragraph("3.5 条項3.7の制限を常に条件として、UKバイオバンクは、本試料、結果データ、知見、またはその他のデータを使用した結果として申請者が行った発明（「<b>申請者生成発明</b>」）に関連する知的財産権に対する権利またはライセンスを持たないことを確認する。", style_normal))
story.append(Paragraph("3.6 しかしながら、申請者は、UKバイオバンクのリソースが、(a) 50万人のUK参加者の善意と貢献、(b) 慈善および公的資金（特にWellcomeおよび医学研究評議会から）、(c) 公的リソース（UKの健康記録データなど）の使用、(d) 公益に資する健康関連研究の実施を促進するという明確な目的で設立されたことの組み合わせを使用して作成されたことを認める。UKバイオバンクもまた、申請者によってリソースの強化に対してなされている貢献（特に、承認済み研究プロジェクトの知見および結果データの生成および他の研究者への利用可能性の形での）を認める。", style_normal))
story.append(Paragraph("3.7 具体的な義務に関しては、上記の条項3.6の確認を考慮し、申請者は（そして本条項は本MTAの重要な規定である）、以下を行わず、また試みないことに同意する：", style_normal))
story.append(Paragraph("3.7.1 以下の特許請求の範囲を持つ特許を出願すること。または", style_h2))
story.append(Paragraph("3.7.2 以下の知的財産権を主張または行使しようとすること：", style_h2))
story.append(Paragraph("本試料内の遺伝子型-表現型データ、または承認済み研究プロジェクトの過程で申請者によって（またはその代理で）生成された遺伝子型-表現型データ（そのような遺伝子型-表現型データが結果データ、知見、またはその他のデータの形式であるかどうかにかかわらず）。上記を制限することなく、両当事者は、本条項3.7が、申請者が薬物、治療法、診断、その他の技術または治療法における知的財産権の特許取得または行使を禁止するものではないことに同意する。ただし、これにより、UKバイオバンクのリソースを使用して申請者が特定したバイオマーカーデータを含む、申請者が生成したデータ（条項3.1で定義）を、承認された研究者が使用することを許可するUKバイオバンクの能力が制限されないことを条件とする。", style_normal))
story.append(Paragraph("<i>付与される権利の制限</i>", style_normal))
story.append(Paragraph("3.8 UKバイオバンクは、(i) 本MTAに基づいて申請者に付与された本試料に対する権利のいずれかをサブライセンスする申請者の権利、および/または (ii) 本試料のいずれかを出版または配布する申請者の権利（ただし、申請者の知見の出版物に相応の量の裏付けデータを含める唯一の目的を除く。これには参加者レベルデータを含めてはならない。これには、関連する出版社が合理的に要求する特定の結果データの相応の公開が含まれる場合がある）を（直接的または間接的に）明示的に除外する。", style_normal))
story.append(Paragraph("3.9 疑義を避けるために付言すると、本MTAに基づいて申請者に付与された本試料を使用する権利は、許可された目的のためのみである。", style_normal))

# Clause 4
story.append(Paragraph("4. 申請者からの確認事項", style_h1))
story.append(Paragraph("<i>一般</i>", style_normal))
story.append(Paragraph("4.1 申請者は、本試料を使用して実施されるすべての作業が、以下に準拠して実施されることをUKバイオバンクに確認する：", style_normal))
story.append(Paragraph("4.1.1 適用されるすべての法律、規制、ガイドライン、および承認（2004年ヒト組織法、データ保護法、および研究倫理委員会（または承認済み研究プロジェクトが実施される法域における該当する同等の機関）から必要な承認を含むがこれらに限定されない）。および", style_h2))
story.append(Paragraph("4.1.2 適用されるすべての貿易制限および輸出管理（(i) 英国、(ii) 米国、(iii) 欧州連合およびその加盟国、(iv) 国連、または (v) その他の政府によって随時管理、制定、または施行される制裁、すなわち貿易、経済、および金融制裁法、規制、禁輸措置、および制限措置（いずれの場合も法的拘束力を持つ）を含むがこれらに限定されない）。", style_h2))
story.append(Paragraph("<i>セキュリティ</i>", style_normal))
story.append(Paragraph("4.2 申請者は、価値のある独自の機密/秘密データの保存に合理的に期待される基準で、安全なネットワークシステムに本試料を保持するものとする。さらに、申請者は、本試料を偶発的または不法な破壊、紛失、改ざん、不正開示、またはアクセス（以下「<b>データセキュリティインシデント</b>」）から保護するために、付属書2（セキュリティ対策）に定められた適切な技術的および組織的措置を実施する義務を負う。本MTAに署名することにより、申請者PIは、本試料を保護するために付属書2に定められたセキュリティ対策が講じられていることを確認する。", style_normal))
story.append(Paragraph("4.3 申請者は、本試料に影響を与える合理的に疑われる「ニアミス」または実際のデータセキュリティインシデントを認識した後、遅滞なく（いかなる場合でも24時間以内に）UKバイオバンクに通知するものとする。当該通知は、DPO@ukbiobank.ac.uk宛に電子メールで送信し、写しをaccess@ukbiobank.ac.ukに送信しなければならない。", style_normal))
story.append(Paragraph("4.3.1 申請者は、情報が不完全である、または関連する調査が進行中であることを理由に、当該通知を遅らせてはならない。さらに、申請者は、法律で義務付けられている場合を除き、UKバイオバンクの事前の書面による明示的な同意なしに、当該データセキュリティインシデントについて外部への発表、監督当局または規制当局への通知を行ってはならない。", style_h2))
story.append(Paragraph("4.3.2 両当事者は、データセキュリティインシデントの処理を容易にするために、互いに協力し、合理的な支援を提供するものとする。", style_h2))
story.append(Paragraph("<i>参加者による同意の撤回</i>", style_normal))
story.append(Paragraph("4.4 申請者は、UKバイオバンクが申請者に通知する参加者による「それ以上の使用禁止（no further use）」の撤回について、（UKバイオバンクのウェブサイトに記載されている参加者の撤回オプションに従って）迅速かつ適切に対処することを確認する。", style_normal))
story.append(Paragraph("<i>参加者の特定</i>", style_normal))
story.append(Paragraph("4.5 申請者は、以下を行うこと（または試みること）を明示的に禁止される：", style_normal))
story.append(Paragraph("4.5.1 参加者を（直接的または間接的に）特定するために、提供された本試料を開発、リンク、またはリエンジニアリングすること。", style_h2))
story.append(Paragraph("4.5.2 UKバイオバンクが提供した本試料から参加者を特定すること。または", style_h2))
story.append(Paragraph("4.5.3 参加者に接触すること。", style_h2))
story.append(Paragraph("4.6 申請者が誤って参加者を特定した場合、直ちにUKバイオバンクに通知し、その経緯を（合理的な詳細をもって）説明しなければならない。当該通知は、DPO@ukbiobank.ac.uk宛に電子メールで送信し、写しをaccess@ukbiobank.ac.ukに送信しなければならない。", style_normal))
story.append(Paragraph("4.7 条項4.6の目的を除き、申請者は以下を行ってはならない：", style_normal))
story.append(Paragraph("4.7.1 当該参加者の身元を他の人物と共有すること。または", style_h2))
story.append(Paragraph("4.7.2 参加者自身に接触を試みること。", style_h2))
story.append(Paragraph("4.8 本MTAの他の規定を損なうことなく、条項4.1、4.2、および4.4から4.7までの規定に対する実際の違反または予期される違反があった場合、UKバイオバンクは本契約を直ちに終了し、UKバイオバンクが提供した本試料の即時返却または破棄を要求する権利を有する。", style_normal))

# Clause 5
story.append(Paragraph("5. 一般向け要約の公開、年次報告書の提出、および知見の返却と公開", style_h1))
story.append(Paragraph("<i>UKバイオバンクのウェブサイトでの要約の公開</i>", style_normal))
story.append(Paragraph("5.1 申請者が承認済み研究プロジェクトのために本試料を受領した後、UKバイオバンクは以下の情報をウェブサイトで公開する権利を有する：", style_normal))
story.append(Paragraph("5.1.1 申請書に含まれる承認済み研究プロジェクトの一般向け要約（UKバイオバンクが機密扱いとすることに合意した資料を除く）。および", style_h2))
story.append(Paragraph("5.1.2 申請者の概要詳細。", style_h2))
story.append(Paragraph("<i>年次プロジェクト報告書</i>", style_normal))
story.append(Paragraph("5.2 期間中、申請者はUKバイオバンクに対し、以下を提供するものとする：", style_normal))
story.append(Paragraph("5.2.1 付属書3に添付された様式（またはUKバイオバンクが随時要求するその他の様式）で、承認済み研究プロジェクトの進捗状況を合理的な詳細で記載した（要約セクションを含む）報告書を、年次ベース（発効日から）で提出すること。これには、申請者が作成した知見で、その合理的見解において以下に該当するものが含まれるものとする：", style_normal))
story.append(Paragraph("(a) 公開済みまたは公開待ちであるもの。", style_h3))
story.append(Paragraph("(b) 公開された特許で開示されているもの。または", style_h3))
story.append(Paragraph("(c) その他（医学研究の文脈において）重要であるもの。および", style_h3))
story.append(Paragraph("5.2.2 クレームが申請者生成発明をカバーしている、またはカバーすることを意図している特許の要約（および要求された場合は出願の写し）を、公開から2ヶ月以内に提出すること。", style_h2))
story.append(Paragraph("5.3 年次プロジェクト報告書に関して、UKバイオバンクは：", style_normal))
story.append(Paragraph("5.3.1 年次プロジェクト報告書の要約セクションを公開する能力を有するものとする。ただし、特許権の出願が必要な項目については、申請者（以下の条項5.7を参照）が合理的な期間、機密性を保持することを条件とする。および", style_h2))
story.append(Paragraph("5.3.2 年次プロジェクト報告書から生じる合理的な質問を申請者に尋ねる機会を有するものとし、申請者は適時にそのような質問に回答するものとする。", style_h2))
story.append(Paragraph("5.4 年次プロジェクト報告書、またはUKバイオバンクに提供されたその他の情報もしくはデータに、適用される輸出管理の対象となる技術またはデータが含まれている場合、年次プロジェクト報告書、情報、またはデータのUKバイオバンクへの送信を許可するために必要な輸出ライセンスを取得することは申請者の責任である。申請者は、年次プロジェクト報告書、情報、またはデータが輸出ライセンスに基づいて送信されることを、少なくとも1週間前にUKバイオバンクに通知し、UKバイオバンクにライセンス条件の詳細と、年次プロジェクト報告書、情報、またはデータに含まれる技術の管理理由を提供しなければならない。", style_normal))
story.append(Paragraph("5.5 年次プロジェクト報告書が所定の期間、方法、および形式でUKバイオバンクに受領されない場合、本MTAに基づく申請者の権利は停止され、申請者（および共同研究者）は、年次プロジェクト報告書が正式かつ適切に提供されるまで、さらなるデータのダウンロード（新しいデータフィールドまたは既存のデータフィールドの更新に関して）またはリサーチ・アクセス・プラットフォームを介した既存のデータへのアクセスができなくなる。UKバイオバンクからの督促にもかかわらず、年次プロジェクト報告書が発効日の関連する記念日から3ヶ月後も未提出のままである場合、UKバイオバンクは、申請者に終了の書面による通知を行うことにより本MTAを終了し、および/または申請者機関（または申請者PI）がUKバイオバンクからのさらなる本試料の申請またはアクセスを行うことを防ぐ権利を有する。", style_normal))
story.append(Paragraph("<i>知見の公開</i>", style_normal))
story.append(Paragraph("5.6 申請者は、承認済み研究プロジェクトの完了日から6ヶ月以内に、以下のいずれかの方法で知見を公開（およびUKバイオバンクにそのリンクを提供）するために「あらゆる合理的な努力（All Reasonable Endeavours）」を払うものとする：", style_normal))
story.append(Paragraph("5.6.1 学術誌において。または", style_h2))
story.append(Paragraph("5.6.2 オープンソースの出版サイトにおいて。", style_h2))
story.append(Paragraph("5.7 UKバイオバンクは、申請者が合理的な研究開発慣行に従って、合理的な期間、当該知見を機密として保持できることを認め、これに同意する。疑義を避けるために付言すると、申請者は、特許保護が求められている（かつ特許がまだ公開されていない）知見に関して機密性を保持する権利を有する。", style_normal))
story.append(Paragraph("5.8 当該知見が一般に公開された場合、UKバイオバンクは、当該知見の基礎となる結果データが速やかにUKバイオバンクに返却されるか、またはその他の方法で利用可能にされることを要求する。UKバイオバンクはまた、結果データが、他の研究者が結果データを解釈および理解するために合理的に必要な文書とともに、適切かつ理解可能な形式（特に他の研究者にとって）で返却されることを要求する。", style_normal))
story.append(Paragraph("5.9 知見の公開後6ヶ月以内に、関連する申請者は、条項5.8に定められた形式でUKバイオバンクに結果データを提供するものとする（あるいは、UKバイオバンクと関連する申請者は、結果データが他の研究者に公開され、および/または一般に公開されることを条件として、関連する申請者が結果データを保持することに合意する場合がある）。", style_normal))
story.append(Paragraph("5.10 UKバイオバンクは、本条項に定められた期限の延長に関する書面による要請（適切な説明を含む）を合理的に検討するものとする。", style_normal))
story.append(Paragraph("5.11 申請者は、期間（およびその後の延長期間）の最初の3年以内に、承認済み研究プロジェクトに関連する相応のレベルの知見を公開するために「あらゆる合理的な努力」を払うものとする。これが不可能な場合、申請者はUKバイオバンクに対し、なぜ不可能なのかについての合理的な説明と、いつ公開が期待できるかの見積もりを提供するものとする。", style_normal))
story.append(Paragraph("<i>UKバイオバンクへの通知</i>", style_normal))
story.append(Paragraph("5.12 付属書4に別段の記載がない限り、申請者は知見の報告についてUKバイオバンクの承認を得る必要はない。それにもかかわらず、申請者は、あらゆる形式（例：論文ジャーナル、オンラインレポート、会議の要旨）での最初の一般発表または出版の予定日の少なくとも2週間前に、知見の報告書およびプレスリリースの写しをUKバイオバンクに提供しなければならない。申請者は、まずAMSにそのような文書をアップロードするものとする。これが不可能な場合、申請者はそのような文書をaccess@ukbiobank.ac.ukに電子メールで送信するものとする。", style_normal))
story.append(Paragraph("5.13 しかしながら、上記の条項5.12の規定にかかわらず、申請者は、その知見の報告が論争を引き起こしたり、その他の点で重大な公衆の注目を集める可能性が高い場合、事前に（書面で）速やかにUKバイオバンクに通知する必要がある。このような状況において、UKバイオバンクは、申請者が検討するために、適切と判断する報告書に関する勧告、留保、または提案を行う権利（およびそれを公開する権利）を留保する。", style_normal))
story.append(Paragraph("<i>UKバイオバンクへのクレジット</i>", style_normal))
story.append(Paragraph("5.14 UKバイオバンクは、「UK Biobank」という用語が、すべての出版物のタイトルおよび/または要約に含まれることを要求する。", style_normal))
story.append(Paragraph("5.15 UKバイオバンクは、UKバイオバンクのデータを使用した知見のすべての出版物に、以下のクレジットを含めることを要求する。これは、当該出版物の「謝辞（Acknowledgements）」に組み込まれるべきである：", style_normal))
story.append(Paragraph("「This research has been conducted using the UK Biobank Resource under application number [ ].」（本研究は、申請番号[ ]の下、UKバイオバンクのリソースを使用して実施されました。）", style_h2))
story.append(Paragraph("5.16 UKバイオバンクへのこの謝辞は、可能であれば、参照検索ツール（PubMed、MEDLINE、および/またはDOI参照など）にリンクされるべきである。", style_normal))

# Clause 6
story.append(Paragraph("6. 料金", style_h1))
story.append(Paragraph("6.1 申請者は、UKバイオバンクへの申請書の支払いセクションに記載されているアクセス利用料を、銀行振込またはSage Payにより、英ポンド（GBP）で支払うことに同意する。アクセス利用料はVAT抜きの金額で記載されている。申請者は、アクセス利用料に加えて、適用されるVATを支払うものとする。", style_normal))
story.append(Paragraph("6.2 アクセス利用料を支払う際、申請者は請求書番号および/または申請参照番号を支払いの参照として引用し、送金通知をcreditcontrol@ukbiobank.ac.ukに送信するものとする。", style_normal))
story.append(Paragraph("6.3 本MTAに基づいてUKバイオバンクが申請者に付与する権利は、アクセス利用料（および適用されるVAT）が支払われることを条件とする。したがって、疑義を避けるために付言すると、アクセス利用料（および適用されるVAT）が全額受領されるまで、本試料は申請者に提供されない。", style_normal))
story.append(Paragraph("6.4 申請者が本MTAを受領してから90日以内にアクセス利用料（および適用されるVAT）の支払いが行われない場合、申請者はUKバイオバンクのリソースおよび本試料へのアクセスを再申請する必要がある。", style_normal))

# Clause 7
story.append(Paragraph("7. 年次確認および監査", style_h1))
story.append(Paragraph("7.1 期間中、UKバイオバンクは、申請者PIに対し、承認済み研究プロジェクトがMTA（および付属書）の規定に準拠し続けていることを年次ベースで確認することを要求する。具体的には、申請者PIは、付属書3に添付された様式の年次プロジェクト報告書の一部として、UKバイオバンクにそのような確認を提供するものとする。年次プロジェクト報告書が所定の期間、方法、および形式でUKバイオバンクに受領されない場合、UKバイオバンクは上記の条項5.5に定められた権利を留保する。", style_normal))
story.append(Paragraph("7.2 UKバイオバンクがデータセキュリティインシデントまたはその他の重大なインシデントが発生したと合理的に信じる状況において、UKバイオバンクは、申請者に通知した上で、本MTAの規定の遵守を確認または調査するために、自らまたは適切な第三者を通じて以下を行うことができる：", style_normal))
story.append(Paragraph("7.2.1 本試料のセキュリティ、保管、またはその他の手配を確認するために監査（対面またはリモート）を実施することを選択する。および", style_h2))
story.append(Paragraph("7.2.2 UKバイオバンクが随時合理的に要求する、承認済み研究プロジェクトおよび/またはその進捗状況に関する追加情報を要求する。", style_h2))
story.append(Paragraph("7.3 UKバイオバンクは、関連する申請者の手順およびプロセス内に重大な不履行が発見されない限り、そのような監査の費用を負担するものとする。重大な不履行が発見された場合、関連する申請者は、UKバイオバンクおよび関連する第三者の合理的な費用を払い戻す義務を負う。", style_normal))
story.append(Paragraph("7.4 UKバイオバンクは、その監査権が年に1回を超えて行使されないこと、および申請者に合理的な通知（データセキュリティインシデントまたはその他の重大なインシデントの場合は即時となる場合がある）を提供することを条件とすることを確認する。可能な限り、UKバイオバンクは、他の関連当事者とのサイト訪問および監査を調整することに同意する。", style_normal))

# Clause 8
story.append(Paragraph("8. 機密保持", style_h1))
story.append(Paragraph("8.1 条項8.2の例外を条件として、UKバイオバンクは、申請者によって書面で開示され、機密であるとマークされた情報（「<b>申請者の機密情報</b>」）を機密として保持し、いかなる人物にも開示してはならない。", style_normal))
story.append(Paragraph("8.2 UKバイオバンクは、本MTAによって明示的に許可されている場合、または以下の場合に申請者の機密情報を開示することができる：", style_normal))
story.append(Paragraph("8.2.1 法律により、政府機関もしくはその他の規制当局により、または管轄権を有する裁判所もしくはその他の当局により開示が要求される場合。", style_h2))
story.append(Paragraph("8.2.2 当該申請者による開示の前にUKバイオバンクが知っていたことが（申請者が合理的に満足するように）UKバイオバンクによって示される場合。", style_h2))
story.append(Paragraph("8.2.3 開示に制限を課さなかった第三者によってUKバイオバンクに合法的に開示された場合。", style_h2))
story.append(Paragraph("8.2.4 情報が（または入る）公知の事実となった場合（UKバイオバンクによる本条項の違反によるものを除く）。または", style_h2))
story.append(Paragraph("8.2.5 UKバイオバンクと申請者が合理的に行動し、そのような情報が些細な、あるいは明白なものであることに同意する場合、またはそのような開示が許可されることに書面で同意する場合。", style_h2))

# Clause 9
story.append(Paragraph("9. データ保護", style_h1))
story.append(Paragraph("<i>当事者の関係</i>", style_normal))
story.append(Paragraph("9.1 両当事者は、UKバイオバンクと申請者が、本MTAに従って処理される参加者レベルデータに関して独立した管理者（Controllers）であり、申請者が許可された目的のために厳格に参加者レベルデータを処理することを認める。いかなる場合も、両当事者は参加者レベルデータを共同管理者（Joint Controllers）として処理してはならない。", style_normal))
story.append(Paragraph("9.2 各当事者は、データ保護法の下で管理者として適用される義務を遵守することについて、個別に責任を負うものとする。", style_normal))
story.append(Paragraph("<i>協力</i>", style_normal))
story.append(Paragraph("9.3 申請者、申請者PI、または申請者研究員が、参加者レベルデータの処理に関連して、参加者、規制当局、またはその他の第三者から通信、問い合わせ、または苦情（「<b>コレスポンデンス</b>」）を受け取った場合、その詳細をUKバイオバンクに速やかに通知するものとする。いかなる状況においても、申請者、申請者PI、または申請者研究員は以下を行うものとする：(i) コレスポンデンスに応答する前にUKバイオバンクの書面による承認（応答の内容の承認を含む）を得ること。および (ii) データ保護法に従い、UKバイオバンクがコレスポンデンスに直接応答することを許可すること。", style_normal))
story.append(Paragraph("<i>申請者が英国外に所在する場合</i>", style_normal))
story.append(Paragraph("9.4 UKバイオバンクが英国外の申請者に対し、データ保護法に従って適切なレベルの保護を保証していると指定されていない地域に参加者レベルデータを移転する場合、両当事者は、UK補遺（UK Addendum）が参照により自動的に本MTAに組み込まれ、本MTAの付属書1のパートBに記載されているように完了したものとみなされることに同意する。", style_normal))
story.append(Paragraph("9.5 MTAとUK補遺の間に矛盾がある場合、UK補遺が優先する。", style_normal))
story.append(Paragraph("<i>申請者による国際移転</i>", style_normal))
story.append(Paragraph("9.6 申請者は、データ保護法に準拠した移転を確実にするために必要な措置を講じない限り、英国外の地域（または条項9.4が適用される場合、その後の地域で処理が行われる場合）で参加者レベルデータを処理（または参加者レベルデータの処理を許可）してはならない。", style_normal))

# Clause 10
story.append(Paragraph("10. 責任の制限", style_h1))
story.append(Paragraph("10.1 両当事者は以下に同意する：", style_normal))
story.append(Paragraph("10.1.1 条項10.2、10.3、および10.4に従い、本MTAに基づく、および/または承認済み研究プロジェクトに関連するUKバイオバンクの最大累積責任は、承認済み研究プロジェクトに関連して申請者がUKバイオバンクに支払った、または支払うべきアクセス利用料（申請者に請求されているか否かを問わない）に限定される。および", style_h2))
story.append(Paragraph("10.1.2 条項10.2、10.3、および10.5に従い、本MTAに基づく、および/または承認済み研究プロジェクトに関連する申請者の最大累積責任は、承認済み研究プロジェクトに関連して申請者がUKバイオバンクに支払った、または支払うべきアクセス利用料（申請者に請求されているか否かを問わない）に限定される。", style_h2))
story.append(Paragraph("10.2 上記の条項10.1にかかわらず、UKバイオバンクは申請者に対し、また申請者はUKバイオバンクに対し、以下の責任を負わない：", style_normal))
story.append(Paragraph("10.2.1 利益の損失（直接的、間接的、または結果的を問わない）。", style_h2))
story.append(Paragraph("10.2.2 使用の損失、収益の損失、生産の損失、またはビジネスの損失（いずれの場合も直接的、間接的、または結果的を問わない）。", style_h2))
story.append(Paragraph("10.2.3 信用の損失、評判の損失、または機会の損失（いずれの場合も直接的、間接的、または結果的を問わない）。", style_h2))
story.append(Paragraph("10.2.4 予想される節約の損失またはマージンの損失（いずれの場合も直接的、間接的、または結果的を問わない）。", style_h2))
story.append(Paragraph("10.2.5 データまたはソフトウェアの使用または価値の損失（いずれの場合も直接的、間接的、または結果的を問わない）。または", style_h2))
story.append(Paragraph("10.2.6 間接的または結果的な損失。", style_h2))
story.append(Paragraph("10.3 本MTAのいかなる規定も、以下を含むがこれらに限定されない、法的に制限できない責任を除外または制限するように作用するものではない：", style_normal))
story.append(Paragraph("10.3.1 過失によって引き起こされた死亡または人身傷害。", style_h2))
story.append(Paragraph("10.3.2 詐欺または詐欺的不実表示。および", style_h2))
story.append(Paragraph("10.3.3 法律により責任を除外または制限すること、または除外または制限を試みることが許可されていない事項。", style_h2))
story.append(Paragraph("10.4 疑義を避けるために付言すると、UKバイオバンクは、申請者が本試料を使用して直接的または間接的に開発した知見、製品、テスト、または治療法について、いかなる責任（製品関連の責任を含むがこれに限定されない）も負わない。", style_normal))
story.append(Paragraph("10.5 本MTAのいかなる規定も、以下から生じる損失、損害、費用、または経費に対する申請者のUKバイオバンクへの責任を除外または制限するように作用するものではない：", style_normal))
story.append(Paragraph("10.5.1 条項9（データ保護）および条項14.5から14.10（第三者処理業者）の不遵守。", style_h2))
story.append(Paragraph("10.5.2 条項2.2の違反、または申請者が許可されていない人物または第三者に本試料（知的財産権を含む）をサブライセンス、配布、またはその他の方法で共有する状況。", style_h2))
story.append(Paragraph("10.5.3 条項4.5および4.7に記載された状況。および", style_h2))
story.append(Paragraph("10.5.4 申請者によって引き起こされたデータセキュリティインシデント。", style_h2))

# Clause 11
story.append(Paragraph("11. 期間", style_h1))
story.append(Paragraph("11.1 本MTAの期間は発効日に開始し、条項12に従って早期に終了するか、法律に従って終了しない限り（NHSイングランドとの健康リンクデータの提供に関する関連枠組みまたはその他の契約の終了など、UKバイオバンクのデータライセンス権が制限または終了する場合を含む）、完了日に終了するものとする。", style_normal))
story.append(Paragraph("11.2 本MTAの期間は、承認済み研究プロジェクトの最終年度に、申請者によって（かつUKバイオバンクの合意を得て）、以下の1年単位の増分で延長される場合がある：", style_normal))
story.append(Paragraph("11.2.1 最小1年間。", style_h2))
story.append(Paragraph("11.2.2 2年間。または", style_h2))
story.append(Paragraph("11.2.3 最大3年間。", style_h2))
story.append(Paragraph("これは、延長要求の理由を（合理的な詳細とともに）記載したUKバイオバンクへの申請および関連する追加アクセス利用料の支払いを条件とする。", style_normal))
story.append(Paragraph("11.3 疑義を避けるために付言すると、上記の条項11.2に記載された延長は累積的に適用できる（該当するアクセス利用料を条件とする）。例えば、承認済み研究プロジェクトの期間を3年から6年にするために3年の延長が付与され、その後さらに3年から9年に延長されるなどである。", style_normal))

# Clause 12
story.append(Paragraph("12. 終了および終了の結果", style_h1))
story.append(Paragraph("12.1 UKバイオバンクは、申請者が以下の場合、申請者に書面で通知することにより、直ちに本MTAを終了する権利を有する：", style_normal))
story.append(Paragraph("12.1.1 本MTAの重要な規定の違反または本MTAの重大な違反を犯し、是正可能な違反の場合、違反の詳細を記し是正を求める書面による通知を受け取ってから10日以内に同違反を是正しない場合。または", style_h2))
story.append(Paragraph("12.1.2 事業の停止、停止する可能性が高い、または停止すると脅かす場合、または支払不能事由（Insolvency Event）に陥る場合、または重大かつ不利な規制上の判断を受ける場合。", style_h2))
story.append(Paragraph("12.2 上記の条項11.1に基づくMTAの満了時、または条項12.1に基づく、もしくは法律に基づくUKバイオバンクによる本MTAの終了時（NHSイングランドとの健康リンクデータの提供に関する関連枠組みまたはその他の契約の終了など、UKバイオバンクのデータライセンス権が制限または終了する場合を含む）：", style_normal))
story.append(Paragraph("12.2.1 本MTAに基づいて申請者に付与された権利およびすべてのライセンスは自動的に終了する。および", style_h2))
story.append(Paragraph("12.2.2 申請者は本試料を破棄するか、恒久的にアクセス不能にし、これが行われたことをaccess@ukbiobank.ac.ukに書面で確認するものとする。疑義を避けるために付言すると、本MTAの規定が遵守されていることを条件として、申請者は結果データまたはその他のデータを破棄する必要はない。", style_h2))
story.append(Paragraph("12.3 前述を損なうことなく、またUKバイオバンクが有するその他の権利または救済手段を損なうことなく、条項12.1に基づいてUKバイオバンクが本MTAを終了する権利を有する違反があった場合、UKバイオバンクは以下の措置を講じることができる：", style_normal))
story.append(Paragraph("12.3.1 申請者PI、申請者研究員、および申請者機関のその他の研究者が、無期限にUKバイオバンクのリソース内のさらなる本試料にアクセスすることを禁止する。および/または", style_h2))
story.append(Paragraph("12.3.2 デフォルトした申請者機関内の関連人事担当者、デフォルトした申請者PIの資金提供者、および/または統治機関またはその他の関連規制機関に通知することを選択する。", style_h2))
story.append(Paragraph("12.4 理由の如何を問わず本MTAが終了した場合でも、条項2、3、4、5、7、8、9、10、12、13、14、16、および17の規定は、それぞれの条件に従って引き続き有効である。", style_normal))
story.append(Paragraph("12.5 本MTAの終了または満了は、終了または満了の時点で発生している当事者の権利および義務に影響を与えない。", style_normal))

# Clause 13
story.append(Paragraph("13. 通知", style_h1))
story.append(Paragraph("13.1 本MTAに基づいて要求される通知は書面で行うものとし、以下のいずれかとする：", style_normal))
story.append(Paragraph("13.1.1 以下に記載されたアドレスに電子メールで送信する。または", style_h2))
story.append(Paragraph("13.1.2 （電子メールの送信に失敗した場合）UKバイオバンクまたは申請者の登録住所に郵便で送付する。", style_h2))
story.append(Paragraph("13.2 通知は以下の場合に受領されたとみなされる：", style_normal))
story.append(Paragraph("13.2.1 電子メールで送信された場合、受信者の電子メールサーバーでの受領時（または、この時間が受領地の営業時間外にあたる場合、営業時間が再開した時）。または", style_h2))
story.append(Paragraph("13.2.2 郵便で送信された場合、受領地の営業日であれば配達日（または営業日でない場合は翌営業日）。", style_h2))
story.append(Paragraph("13.3 UKバイオバンクへの通知は、access@ukbiobank.ac.ukのアクセスチームに送信するものとする。申請者への通知は、関連する申請者および申請者PIに電子メールで送信される。", style_normal))

# Clause 14
story.append(Paragraph("14. 関連会社、譲渡および下請け", style_h1))
story.append(Paragraph("<i>関連会社</i>", style_normal))
story.append(Paragraph("14.1 承認済み研究プロジェクトのために本MTAに基づいて申請者に付与される権利には、以下の条件の下、申請者の関連会社が含まれる：", style_normal))
story.append(Paragraph("14.1.1 MTAの条項7.1に従って年次ベースでUKバイオバンクに提出される年次プロジェクト報告書において、各関連会社の最新の詳細を提供すること。", style_h2))
story.append(Paragraph("14.1.2 各関連会社の行為、不履行、および不作為について、それらが申請者自身のものであるかのように、UKバイオバンクに対して完全な責任と義務を負い続けること。および", style_h2))
story.append(Paragraph("14.1.3 各関連会社が本MTAの条件を遵守することを保証すること。", style_h2))
story.append(Paragraph("<i>譲渡</i>", style_normal))
story.append(Paragraph("14.2 UKバイオバンクも申請者も、他方当事者の書面による事前の承認（不当に保留または遅延されてはならない）を得ることなく、本MTAまたは本契約に基づく権利もしくは義務を譲渡する権利を有しない。", style_normal))
story.append(Paragraph("<i>下請け</i>", style_normal))
story.append(Paragraph("14.3 条項14.5に定められた状況を除き、申請者は、UKバイオバンクの事前の書面による同意（不当に保留されてはならない）を得ることなく、本MTAに基づく義務の履行またはその一部を下請けに出してはならない。", style_normal))
story.append(Paragraph("14.4 条項14.3に基づいて同意が付与された場合、関連する申請者は、下請け業者の行為、不履行、および不作為について、それらが申請者自身のものであるかのように責任を負うものとし、同意が付与されたことによって、関連する申請者が本MTAに基づく義務から免除されることはない。", style_normal))
story.append(Paragraph("<i>第三者処理業者</i>", style_normal))
story.append(Paragraph("14.5 UKバイオバンクは、申請者が、許可された目的のために厳密に、かつデータ計算および分析の個別の要素に関連してのみ本試料を処理するために、第三者処理業者に下請けに出すことができることを認め、これに同意する（かかる処理業者を「<b>第三者処理業者</b>」という）。申請者は、条項14.6から14.10までに定められた条件に厳密に従って遵守し、第三者処理業者に従事させなければならない。", style_normal))
story.append(Paragraph("14.6 申請者は、第三者処理業者が共同研究者（Collaborator）ではなく、許可された目的（「<b>プロセッサータスク</b>」）に関連するデータ計算および分析の個別の要素の目的でのみ従事することを保証する。", style_normal))
story.append(Paragraph("14.7 第三者処理業者に従事させる前に、申請者は以下の評価を実施し、文書化しなければならない：", style_normal))
story.append(Paragraph("14.7.1 第三者処理業者が承認済み研究プロジェクトの研究目的の進捗に必要であるかどうか。", style_h2))
story.append(Paragraph("14.7.2 過去のデータセキュリティおよび過去のデータ使用/活動に関する出所に照らして、第三者処理業者がデータの適切な受領者であるかどうか（例えば、Cambridge Analyticaは資格がない）。および", style_h2))
story.append(Paragraph("14.7.3 第三者処理業者が、データ保護法の要件を満たす方法で本試料を処理することを十分保証できるかどうか。", style_h2))
story.append(Paragraph("14.8 申請者は以下を行うものとする：", style_normal))
story.append(Paragraph("14.8.1 第三者処理業者のすべての行為、不履行、および不作為について、それらが申請者自身のものであるかのように、UKバイオバンクに対して完全な責任を負い続けること。", style_h2))
story.append(Paragraph("14.8.2 第三者処理業者がプロセッサータスクを実行するために厳密に必要な本試料のみを第三者処理業者に提供すること。", style_h2))
story.append(Paragraph("14.8.3 MTAの条項7.1に従って年次ベースでUKバイオバンクに提出される年次プロジェクト報告書において、各第三者処理業者およびプロセッサータスクの詳細を提供すること。および", style_h2))
story.append(Paragraph("14.8.4 本試料のデータ転送または処理が行われる前に、第三者処理業者との間で書面による契約が締結されていることに基づいてのみ、第三者処理業者に従事させること。かかる契約には、とりわけ以下を含める必要がある：", style_h2))
story.append(Paragraph("(a) プロセッサータスクの明確な定義と範囲。これには、申請者の文書化された指示に従ってのみデータを処理する合意を含む。", style_h3))
story.append(Paragraph("(b) 第三者処理業者に対し、プロセッサータスクのみを実施することを許可し、明示的に許可されない限りその他の行為を行わないこと。", style_h3))
story.append(Paragraph("(c) 本MTAに定められたセキュリティ基準（最小限として）に従って本試料を保存、処理、使用し、データセキュリティインシデントから本試料を保護するための適切な技術的および組織的セキュリティ対策を実施すること。", style_h3))
story.append(Paragraph("(d) プロセッサータスクが完了したら、本試料（およびプロセッサータスクの結果として生成されたデータ）を削除（または恒久的にアクセス不能に）すること。", style_h3))
story.append(Paragraph("(e) 第三者処理業者が、本試料（またはそこから派生したデータ）または承認済み研究プロジェクトの一環として申請者が作成または行ったこと（UKバイオバンクと申請者間のMTAの対象となるもの）のいずれに対しても、（直接的または間接的に）権利を持たないことを確認すること。", style_h3))
story.append(Paragraph("(f) 第三者処理業者が本MTAの関連規定と同等の規定に拘束されることを確認すること。これには、a) 本試料（またはそこから派生したデータ）を第三者に譲渡しないこと、および b) 参加者を再特定する試みを行わないことを含むがこれらに限定されない。", style_h3))
story.append(Paragraph("(g) 第三者処理業者が、データ保護法の要件を満たす方法で本試料を処理することを十分保証すること。および", style_h3))
story.append(Paragraph("(h) 重大な問題（第三者処理業者による上記の規定の違反を含む）が発生した場合、申請者が第三者処理業者との契約を直ちに終了する無制限かつ一方的な権利を有すること。", style_h3))
story.append(Paragraph("14.9 申請者は、条項14.5から14.10までの遵守を確保するために、第三者処理業者の活動を合理的なレビュー下に置かなければならない。", style_normal))
story.append(Paragraph("14.10 UKバイオバンクが第三者処理業者の身元または活動に関して懸念を表明した場合、申請者は速やかにその問題を調査し報告するものとする。UKバイオバンクは、合理的に必要な場合（および申請者との対話を条件として）、申請者に以下を要求することができる：", style_normal))
story.append(Paragraph("14.10.1 第三者処理業者を監査すること。および/または", style_h2))
story.append(Paragraph("14.10.2 第三者処理業者との契約を終了すること。", style_h2))

# Clause 15
story.append(Paragraph("15. 不可抗力", style_h1))
story.append(Paragraph("15.1 いずれかの当事者が不可抗力事象（Force Majeure Event）により本MTAに基づく義務の履行を妨げられ、阻害され、または遅延した場合、当該当事者は直ちに他方当事者にその開始日と不可抗力事象が本MTAに基づく義務の履行能力に与える影響を通知するものとする。当事者が相互に合意した場合、影響を受けた当事者の義務は、不可抗力事象が継続する間、停止される。", style_normal))
story.append(Paragraph("15.2 不可抗力事象の影響を受けた当事者は、不可抗力事象により妨げられ、阻害され、または遅延した義務の履行不履行または遅延について責任を負わない。ただし、当該当事者がその影響を最小限に抑えるためにあらゆる合理的な努力を払い、不可抗力事象の除去後できるだけ速やかに履行を再開することを条件とする。履行不能の期間が不可抗力事象の開始から90日を超える場合、影響を受けていない当事者は、他方当事者に書面で通知することにより、30日の通知期間をもって本MTAを終了するオプションを有する。", style_normal))
story.append(Paragraph("15.3 本条項15の規定は、いずれかの当事者が本MTAを終了するために有するその他の権利に影響を与えない。", style_normal))

# Clause 16
story.append(Paragraph("16. 紛争解決", style_h1))
story.append(Paragraph("16.1 紛争（Dispute）が発生した場合、両当事者は本条項16に定められた手順に従うものとする。", style_normal))
story.append(Paragraph("16.2 いずれかの当事者は、他方当事者に紛争の書面による通知を行い、その性質と完全な詳細（「<b>紛争通知</b>」）および関連する裏付け文書を設定することができる。紛争通知の送達から5営業日以内に、UKバイオバンクの代表者と申請者の代表者は、誠意を持って当該紛争を解決しようと試みるものとする。", style_normal))
story.append(Paragraph("16.3 何らかの理由で両当事者のそれぞれの代表者が紛争通知から10営業日以内に紛争を解決できない場合、紛争に関与するいずれかの当事者は、UKバイオバンクの主任研究者（Principal Investigator）および申請者の適切な上級役員（Senior Officer）による議論のためにそれを参照することができる。両当事者のこれらの上級代表者（またはそれぞれの指名者）は、紛争を解決する目的で、速やかに会議、電話、またはビデオ会議を手配するよう努めるものとする。", style_normal))
story.append(Paragraph("16.4 条項16.3に定められた紛争のエスカレーション後、UKバイオバンクの主任研究者および申請者の適切な上級役員が、エスカレーションされてから30営業日以内に何らかの理由で紛争を解決できない場合、両当事者は、効果的な紛争解決センター（CEDR）モデル調停手続きに従って、誠意を持って紛争を解決するための調停に入ることに同意する。紛争通知の送達から20営業日以内に両当事者間で別段の合意がない限り、調停人はCEDRによって指名されるものとする。調停を開始するには、当事者は他方当事者に書面で通知し、紛争を調停に付託しなければならない。", style_normal))
story.append(Paragraph("16.5 疑義を避けるために付言すると、法的問題ではなく、科学的または技術的な問題またはビジネス上の決定に関する紛争は、解決のために上級代表者に留まるものとする。", style_normal))
story.append(Paragraph("16.6 紛争が調停開始から10営業日以内に解決されない場合、または両当事者が書面で合意するその他の期間内に解決されない場合、いずれかの当事者は本MTAの条項17.10に従って訴訟手続きを発行することができる。", style_normal))
story.append(Paragraph("16.7 本条項16のいかなる規定も、イングランドおよびウェールズの裁判所において、権利および利益を保護するために暫定的/差し止めによる救済を求めることを妨げるものではない。ただし、そのような救済が調停を妨げたり停止したりしないことを条件とする。", style_normal))

# Clause 17
story.append(Paragraph("17. 一般", style_h1))
story.append(Paragraph("17.1 両当事者は、申請者がいつでも、また随時、UKバイオバンクに書面で通知することにより申請者PIを変更できることに同意する。ただし、申請者は、新しい申請者PIの身元/ステータスがUKバイオバンクのアクセス基準、アクセス手順、および本MTAの関連条件に準拠していることを保証しなければならない。", style_normal))
story.append(Paragraph("17.2 本MTAは、両当事者間の完全な合意を統治および構成し、本件に関する両当事者間の以前のすべての合意、約束、保証、保証、表明、および理解（口頭か書面かを問わない）に取って代わり、無効にする。さらに、各当事者は、本MTAに明示的に記載されている場合を除き、他方当事者またはその他の人物によってなされたいかなる声明、約束、保証、声明、保証、約束、または表明（無実か過失かを問わない）に依拠しておらず、それらに関して（契約違反に対する唯一の救済手段を除き）いかなる救済手段も有しないことを認め、同意する。", style_normal))
story.append(Paragraph("17.3 本MTAの規定といずれかの付属書の間に矛盾がある場合、関連する付属書の規定が適用される。", style_normal))
story.append(Paragraph("17.4 いずれかの当事者による、本契約に基づく権利または救済の行使または執行における放棄、遅延、または自制は、明示または黙示を問わず、放棄当事者が署名した書面に定められていない限り、かかる権利または救済の放棄を構成しない。", style_normal))
story.append(Paragraph("17.5 本MTAのいかなる規定も、本MTAの当事者ではない人物によって強制されることを意図しておらず、制定法その他に基づいて第三者に権利が付与されることもない。", style_normal))
story.append(Paragraph("17.6 本MTAのいかなる規定も、両当事者間にパートナーシップ、合弁事業、または代理関係を構築するものではない。", style_normal))
story.append(Paragraph("17.7 本MTAへのすべての変更は、合意され、書面で提示され、発効する前に両当事者を代表して署名されなければならない。", style_normal))
story.append(Paragraph("17.8 本MTAのいずれかの規定または部分規定が無効、違法、または執行不能であるか、そうなった場合、それは削除されたものとみなされるが、本MTAの残りの部分の有効性および執行可能性には影響しない。", style_normal))
story.append(Paragraph("17.9 条項17.8に基づいて本MTAのいずれかの規定または部分規定が削除されたとみなされる場合、両当事者は、元の規定の意図された商業的結果を可能な限り達成する代替規定に合意するために誠意を持って交渉するものとする。", style_normal))
story.append(Paragraph("17.10 本MTAおよびそれに起因または関連して生じる紛争または請求（契約外の紛争または請求を含む）は、イングランドおよびウェールズの法律に準拠し、同法に従って解釈されるものとする。上記の条項16に従い、両当事者は、イングランドの裁判所が、本MTAまたはその主題もしくは形成に起因または関連して生じる訴訟、訴訟手続き、または紛争に対して専属管轄権を有することに取消不能で同意する。", style_normal))
story.append(Spacer(1, 24))

story.append(Paragraph("本MTAは、両当事者の正当な権限を有する代表者によって締結される。", style_normal))
story.append(Spacer(1, 24))

# Signature block simulation
story.append(Paragraph("<b>UKバイオバンクを代表して:</b><br/>署名: ______________________<br/>氏名: ______________________<br/>役職: ______________________<br/>日付: ______________________", style_normal))
story.append(Spacer(1, 12))
story.append(Paragraph("<b>申請者機関を代表して:</b><br/>署名: ______________________<br/>氏名: ______________________<br/>役職: ______________________<br/>日付: ______________________", style_normal))
story.append(Paragraph("私は、申請者機関を代表して法的拘束力のある文書に署名する権限があることを確認します。", style_normal))
story.append(Spacer(1, 12))
story.append(Paragraph("私は、本承認済み研究プロジェクトの申請者主任研究者（Principal Investigator）であり、以下に署名することにより、本MTAの規定を読み、理解したことを確認します。<br/>署名: ______________________<br/>氏名: ______________________<br/>役職: ______________________<br/>日付: ______________________", style_normal))
story.append(PageBreak())

# --- Definitions (Pages 15-16) ---
story.append(Paragraph("定義", style_title))
definitions_text = """
<b>アクセス利用料（Access Charges）:</b> 本試料へのアクセス、および該当する場合は共同研究者が本試料へアクセスできるようにするために申請者が支払う料金（VATを含む場合がある）。付属書4に要約され、AMS上の申請書の支払いセクションに詳述されている。
<br/><br/>
<b>関連会社（Affiliate）:</b> 申請者を直接的または間接的に支配（Control）している、申請者に支配されている、または申請者と共通の支配下にある会社またはその他の事業体（申請者が会社である場合、当該申請者の子会社、親会社、持株会社、または当該親会社もしくは持株会社の子会社を含む）。かかる支配が存在する限りにおいて。
<br/><br/>
<b>あらゆる合理的な努力（All Reasonable Endeavours）:</b> 「あらゆる合理的な努力」を使用する義務を負う当事者に関して、記載された結果を達成するために合理的な行動方針を追求することを意味する。これには合理的な支出が必要になる場合があるが、結果を達成するために利用可能なあらゆる行動方針を追求することや、自らの運営上または商業上の利益の範囲外で行動することは要求されない。
<br/><br/>
<b>AMS:</b> 申請者がUKバイオバンクのリソースへのアクセスを申請および管理するために使用するオンラインのアクセス管理システム（Access Management System）。
<br/><br/>
<b>申請者（Applicant）または申請者機関（Applicant Institution）:</b> 承認済み研究プロジェクトに関してアクセス申請を行う組織（例：大学、企業、またはその他の識別可能な法的実体）。申請者PIが雇用されているか、または契約上付属している組織。
<br/><br/>
<b>申請者の機密情報（Applicant’s Confidential Information）:</b> 本MTAの条項8.1で定義される。
<br/><br/>
<b>申請者生成発明（Applicant-Generated Inventions）:</b> 本MTAの条項3.5で定義される。
<br/><br/>
<b>申請（Application）:</b> 承認済み研究プロジェクトに関連して使用するための本試料へのアクセスを求める、申請者PIおよびその機関によるUKバイオバンクへの申請。
<br/><br/>
<b>申請者主任研究者（Applicant Principal Investigator）または申請者PI（Applicant PI）:</b> 承認済み研究プロジェクトの主任研究者。
<br/><br/>
<b>申請者研究員（Applicant Researcher）:</b> 承認済み研究プロジェクトにおいて申請者PIと協力している申請者の研究者。
<br/><br/>
<b>承認済み研究プロジェクト（Approved Research Project）:</b> UKバイオバンクによって承認された研究プロジェクト（UKバイオバンクによる条件または規定を含む）。付属書4に記載されている。
<br/><br/>
<b>共同研究者（Collaborator）または共同研究機関（Collaborator Institution）:</b> 承認済み研究プロジェクトにおいて申請者PIと協力している主任共同研究者を雇用している組織（例：大学、企業、またはその他の識別可能な法的実体）。
<br/><br/>
<b>共同研究者（Collaborator Researcher）:</b> 承認済み研究プロジェクトにおいて共同研究機関で主任共同研究者と協力している研究者。
<br/><br/>
<b>完了日（Completion Date）:</b> 延長を含む、承認済み研究プロジェクトの終了日として付属書4に含まれる日付。
<br/><br/>
<b>支配（Control）:</b> 対象となる事業体の発行済株式またはその他の議決権の少なくとも50％を直接的または間接的に所有し、投票権を有するか、または事業体の業務を指示する権限を有すること（または、特定の法域において外国企業が所有することを許可される最大の上限がそれより少ない割合である場合はその割合）。「支配している」および「支配されている」も同様に解釈されるものとする。
<br/><br/>
<b>管理者（controller）、処理者（processor）、データ主体（data subject）、個人データ（personal data）、処理（processing）（および処理する（process））、特別な種類の個人データ（special categories of personal data）:</b> データ保護法で与えられた意味を持つ。
<br/><br/>
<b>データ保護法（Data Protection Legislation）:</b> 本MTAに基づく、または関連する当事者の個人データの処理に（全体または一部において）適用されるすべての法律を意味し、該当する場合以下を含む：(i) 2018年欧州連合（離脱）法（"UK GDPR"）のセクション3により英国法の一部を形成するGDPR。(ii) 2018年英国データ保護法。(iii) 2018年欧州連合（離脱）法セクション2により効力を有し続ける2003年プライバシーおよび電子通信（EC指令）規則。および (iv) 個人データの処理に適用される、英国で随時施行されているその他の法律（随時改正または代替される場合を含む）。
<br/><br/>
<b>データセキュリティインシデント（Data Security Incident）:</b> 本MTAの条項4.2で定義される。
<br/><br/>
<b>紛争（Dispute）:</b> 一方のUKバイオバンクと他方の申請者との間の、本MTAまたはその履行、有効性、もしくは執行可能性に起因または関連して生じるあらゆる紛争、論争、手続き、または請求（法的紛争を含む）。
<br/><br/>
<b>発効日（Effective Date）:</b> 本MTAがUKバイオバンクの権限ある署名者によって署名された日付。すでに申請者機関によって署名され、関連する申請者PIによって「読み、理解した」として署名されているものとする。
<br/><br/>
<b>知見（Findings）:</b> 本MTAの条項3.1.2で定義され、承認済み研究プロジェクトの結果として申請者によって得られた結論および結果の観点から文字通り発見されたものを意味する。明確にするために付言すると、知見には申請者生成発明は含まれず、UKバイオバンクの本試料ではないデータから得られた結果も含まれない。
<br/><br/>
<b>不可抗力事象（Force Majeure Event）:</b> 影響を受けた当事者の合理的な支配を超える行為、出来事、不作為、または事故に起因または帰属するあらゆる原因。これには、天災、戦争、暴動、市民騒乱、下請業者またはサプライヤーによる不履行、法律または政府の命令、規則、規制、または指示（適用されるすべての輸出管理および/または制裁措置を含む）の遵守、事故、工場または機械の故障、供給障害、伝染病、パンデミック、火災、洪水、または嵐が含まれるがこれらに限定されない。
<br/><br/>
<b>支払不能事由（Insolvency Event）:</b> ある人物が1986年支払不能法セクション123の意味において債務を支払うことができない場合（裁判所による決定を必要としない）、管財人、受財人、行政管財人、または資産の全部もしくは一部に対して任命された管理者がいる場合、債権者と一般的に和解に入る場合、または清算のために命令が出されるか決議が可決される場合（溶媒合併または溶媒再建のためのスキームの一部としての場合は除く）、またはいずれかの法域で類似もしくは同等のプロセスを受ける場合、または債権者の権利に影響を与えるその他の取り決めを受ける場合を意味する。
<br/><br/>
<b>知的財産権（Intellectual Property Rights）またはIPR:</b> 特許、商標およびサービスマーク、意匠権、著作権、データベース権、営業秘密、およびノウハウを含むがこれらに限定されない、既存および将来のすべての知的財産権。登録済みか否か、登録可能か否かを問わず、これらの登録および登録出願、ならびに更新、延長、継続、組み合わせ、または分割、および世界中のどこにおいても同等または類似の効果を持つ類似の性質の権利および保護形態をすべて含む。
<br/><br/>
<b>主任共同研究者（Lead Collaborator）:</b> 共同研究機関における主任研究者。
<br/><br/>
<b>責任（Liability）:</b> 契約、不法行為、不実表示、返還、制定法、その他にかかわらず、本MTAに起因または関連して生じる責任。これには、原因の如何を問わず（過失による場合を含む）、本MTAに基づく当事者の義務の違反、不履行、欠陥、または履行遅延に起因するものが含まれるがこれらに限定されない。
<br/><br/>
<b>本試料（Materials）:</b> 参加者レベルデータを含め、本MTAに基づいて、または関連してUKバイオバンクから申請者に提供される、付属書4に記載のデータ。
<br/><br/>
<b>MTA:</b> 本試料提供契約、申請者利用規約（そこで言及されている文書および/または資料を含む）、付属書、および該当する場合は申請者の申請書の内容。
<br/><br/>
<b>紛争通知（Notice of Dispute）:</b> 本MTAの条項16.2で定義される。
<br/><br/>
<b>その他のデータ（Other Data）:</b> 本MTAの条項3.1.3で定義される。
<br/><br/>
<b>参加者（Participant(s)）:</b> UKバイオバンクに参加する個人。
<br/><br/>
<b>参加者レベルデータ（Participant Level Data）:</b> 本試料に含まれる付属書1に記載された個人データ、および適用可能な生成データ（本MTAの条項3.1に記載）。
<br/><br/>
<b>許可された目的（Permitted Purpose）:</b> 承認されたプロジェクトの範囲および付属書4に記載された期間（本MTAの規定に従う）に従って承認済み研究プロジェクトを実施すること。
<br/><br/>
<b>結果データ（Results Data）:</b> 本MTAの条項3.1.1で定義される。
<br/><br/>
<b>期間（Term）:</b> 本MTAの条項11.1で定義される。
<br/><br/>
<b>第三者処理業者（Third-Party Processors）:</b> 本MTAの条項14.5で定義される。
<br/><br/>
<b>UK補遺（UK Addendum）:</b> 2018年データ保護法s.119A(1)に基づき英国情報コミッショナーによって発行された、EU委員会標準契約条項（Standard Contractual Clauses）に対する国際データ転送補遺を意味する。現在有効なものはhttps://ico.org.uk/media/for-organisations/documents/4019539/international-data-transfer-addendum.pdfで入手可能であり、随時英国情報コミッショナーによって修正または代替される場合がある。
<br/><br/>
<b>VAT:</b> 1994年付加価値税法（およびそのすべての修正および更新）に基づいて課金される付加価値税、または類似の代替税もしくは追加税。
"""
story.append(Paragraph(definitions_text, style_normal))
story.append(PageBreak())

# --- Annex 1 ---
story.append(Paragraph("付属書 1<br/>データ処理の記述 & UK補遺", style_title))
p17_intro = """
本付属書1は本MTAの一部を構成する。パートA（データ処理の記述）は、本MTAに記載された許可された目的（または当事者間で書面で合意されたその他の目的）のために厳密に処理するために、UKバイオバンクが申請者、申請者PI、および申請者研究員に開示する参加者レベルデータの種類を記述している。パートB（UK補遺）は、UK補遺がどのように完了したとみなされるか、およびUK補遺によって要求される追加情報を規定している。
<br/><br/>
<b>パート A - データ処理の記述</b>
"""
story.append(Paragraph(p17_intro, style_normal))
story.append(Spacer(1, 6))

annex1_text = """
<b>データ主体:</b> 参加者
<br/><br/>
<b>データのカテゴリ:</b> 処理される参加者レベルデータは、以下の個人データのカテゴリに関するものである：
<br/>• EIDs – 承認済み研究プロジェクトに固有のコード化された一意の仮名化識別子。および
<br/>• 出生地、幼少期および教育、雇用歴、婚姻状況、子供の数などの特別な種類のデータを含まない、ベースラインの質問票の回答およびインタビューから得られたデータ。
<br/><br/>
<b>特別な種類のデータ:</b> 処理される参加者レベルデータは、以下の特別な種類のデータに関するものである：
<br/>UKバイオバンクのリソースには、健康、遺伝的、およびバイオメトリックデータが含まれる。本試料に含まれるすべての特別な種類のデータは非識別化されている（直接的および間接的な識別子は削除されている）。
<br/><br/>
特別な種類のデータの種類には以下が含まれる場合がある：
<br/>• 身長、体重、血圧などの参加者の表現型の測定値（参加者あたり約2,000の表現型。詳細はこちらを参照：http://biobank.ndph.ox.ac.uk/showcase/schema.cgi?id=1）
<br/>• 参加者のゲノムの測定値。これには遺伝子型、エクソームシーケンス、および全シーケンスデータが含まれる。
<br/>• 参加者のサンプルの分析によって作成されたバイオマーカー。これには一般的なバイオマーカー（コレステロールなど）、感染症マーカー、プロテオミクスおよびメタボロミクスマーカーが含まれる。
<br/>• 頭部、心臓、身体のMRIスキャン、および超音波とDEXAの結果としての画像データ（最大100,000人の参加者について）。
<br/>• 病院記録、プライマリケア記録、死亡およびがん登録、またはその他の臨床データソースを含む健康記録リンケージから得られたデータ。および
<br/>• 過去の病気/疾患歴、食事、認知および身体測定など、ベースライン/オンラインの質問票の回答およびインタビューから得られたその他の特別な種類のデータ。
<br/><br/>
<b>移転の目的:</b> 移転は、申請者が許可された目的を実施できるようにするために行われる。
<br/><br/>
<b>受領者:</b> 移転された参加者レベルデータは、以下の受領者または受領者のカテゴリにのみ開示される場合がある：
<br/>• 申請者内の許可された人員、すなわち申請者主任研究者および申請者研究員。
<br/>• MTAの関連規定の対象となる第三者処理業者。
<br/>• MTAの関連規定の対象となる関連会社。
<br/>• データ保護法に基づいて行動する法執行機関。
<br/>• データ保護法に基づいて行動する関連データ保護当局。および
<br/>• 監査人（UKバイオバンクまたは適切な第三者）。
<br/><br/>
<b>処理活動:</b> 参加者レベルデータは、以下の基本的な処理活動の対象となる：
<br/>• 許可された目的のためのリサーチ分析プラットフォーム内での参加者レベルデータへのアクセスおよび使用。
<br/>• UKバイオバンクによって承認された場合、申請者のシステム/ネットワークサーバーへの送信、利用可能化、および保存。ただし、WGS（全ゲノムシーケンス）またはWES（全エクソームシーケンス）ファイルは除外され、これらはリサーチ分析プラットフォームから送信またはダウンロードしてはならない。
<br/>• 第三者処理業者によるプロセッサータスクを含む研究業務。および
<br/>• リスク管理、コンプライアンス、法務、および監査機能。
<br/><br/>
<b>個人データを共有するためのUKバイオバンクの法的根拠:</b>
<br/>個人データ: 正当な利益（UK GDPR 第6条(1)(f)）
<br/>特別な種類のデータ: 科学的研究目的（UK GDPR 第9条(2)(j)）
<br/><br/>
<b>UKバイオバンクのDPOの連絡先詳細:</b> DPO@ukbiobank.ac.uk
<br/><br/>
<b>申請者のDPO（またはデータ保護目的のその他の連絡先）の連絡先詳細:</b>
<br/>氏名: ______________________
<br/>役職: ______________________
<br/>メールアドレス: ______________________
"""
story.append(Paragraph(annex1_text, style_normal))
story.append(PageBreak())

# Annex 1 Part B
p18_intro = """
<b>パート B – UK補遺</b>
<br/><br/>
本MTAの条項9.4が申請者に適用される場合、UK補遺は参照により自動的に本MTAに組み込まれ、以下のように完了したとみなされる：
<br/><br/>
1. UK補遺の表1において：
<br/>a) UK補遺の開始日は本契約の発効日とする。
<br/>b) UKバイオバンクが輸出者（Exporter）となり、申請者が輸入者（Importer）となる。および
<br/>c) 当事者の詳細および主要な連絡先は、以下に記載されたUKバイオバンクおよび申請者の詳細とする。
<br/><br/>
2. UK補遺の表2において、2番目のオプション（すなわち、承認されたEU SCCs。付属書情報を含み、本補遺の目的のために発効した承認されたEU SCCsの以下のモジュール、条項、またはオプション規定のみを含む）がチェックされたとみなされ、かつ：
<br/>a) モジュール1（管理者から管理者）が適用される（モジュール2（管理者から処理者）、3（処理者から処理者）、および4（処理者から管理者）は適用されない）。
<br/>b) オプション条項7（ドッキング条項）は適用されない。および
<br/>c) オプション条項11（オプション）は適用されない。
<br/><br/>
3. UK補遺の表3において：
<br/>a) 付属書1A（当事者リスト）: 以下の「当事者リスト」セクションに記載された情報で完了する。
<br/>b) 付属書1B（移転の記述）: 以下の「移転の記述」セクションに記載された情報で完了する。および
<br/>c) 付属書II: 本MTAの付属書2（セキュリティ対策）に記載された情報で完了する。
<br/><br/>
4. UK補遺の表4において：輸出者および輸入者のオプションがチェックされたとみなされる。
<br/><br/>
<b>当事者 / 輸出者 / 輸入者</b>
<br/><br/>
<b>当事者の詳細</b>
<br/><b>輸出者名:</b> UK Biobank Limited
<br/><b>住所:</b> Units 1 – 2 Spectrum Way, Stockport, Cheshire, SK3 0SA
<br/><b>会社番号:</b> 4978912
<br/><br/>
<b>輸入者名:</b> 本MTAの1ページ目で特定された申請者の完全な法的名称。
<br/><b>住所:</b> 申請者の登録住所。
<br/><br/>
<b>主要連絡先</b>
<br/><b>輸出者:</b> UK Biobank DPO (DPO@ukbiobank.ac.uk)
<br/><b>輸入者:</b> 本付属書1のパートAで特定された申請者の連絡先の役職および詳細。
<br/><br/>
<b>当事者リスト:</b> 上記で特定されたUKバイオバンクおよび申請者。
<br/><b>移転の記述:</b> 移転は、申請者が許可された目的を実施できるようにするために行われる。
"""
story.append(Paragraph(p18_intro, style_normal))
story.append(PageBreak())

# --- Annex 2 ---
story.append(Paragraph("付属書 2<br/>セキュリティ対策", style_title))
annex2_intro = """
UKバイオバンクは、UK GDPRに基づき、適切な組織的および技術的対策を講じて、本試料が安全に保存、検索、および使用されることを保証する法的義務を負っている。UKバイオバンクはまた、共有する本試料が適切なセキュリティで保護され続けることを保証するために合理的な措置を講じなければならない。
<br/><br/>
本付属書2は本MTAの一部を構成し、申請者機関が遵守しなければならないデータ保存、検索、および使用に関する適切なレベルのセキュリティ基準を表している。本付属書2は、UKバイオバンクによって随時更新される場合がある。
<br/><br/>
これらのセキュリティ対策の目的は、UKバイオバンクが提供する本試料が、個人データであるかのように扱われ、保護されることを保証することである。特に以下に関して：
<br/>• <b>機密性</b> – 本試料は、許可されたユーザーのみにアクセスを制限し、内部および外部の脅威による不正アクセスから本試料を保護するための組織的および技術的対策を講じて保護される。および
<br/>• <b>完全性</b> – 本試料は、実施される質の高い研究をサポートするために正確かつ完全なままである。
"""
story.append(Paragraph(annex2_intro, style_normal))

story.append(Paragraph("1. 情報セキュリティポリシー", style_h1))
story.append(Paragraph("1.1 申請者機関は、本MTAに従って処理する本試料を保護するために適用する技術的、管理的、および物理的なセキュリティ基準を規定した書面による情報セキュリティポリシーを策定し、維持しなければならない。", style_normal))
story.append(Paragraph("1.2 情報セキュリティポリシーは、不正および不法な処理、ならびに損傷または破壊から本試料を保護するために、申請者機関において適切な技術的および組織的セキュリティ対策の使用を義務付けるものとする。情報セキュリティポリシーは、最低限として本付属書2に定められたセキュリティ対策を詳述するものとする。さらに、実際の、または疑わしいデータセキュリティインシデントが発生した場合に講じられる措置を記述するものとする。", style_normal))
story.append(Paragraph("1.3 申請者機関は、その組織内で申請者機関が処理する本試料のセキュリティを確保し、申請者機関の情報セキュリティポリシーを見直し、維持し、更新する責任を持つ、十分なスキルを持つ個人を任命しなければならない。情報セキュリティポリシーは、申請者機関の内部ITおよびITセキュリティガバナンスと管理のための措置を定めるものとする。", style_normal))
story.append(Paragraph("1.4 情報セキュリティポリシーは、以下のことも定めるものとする：", style_normal))
story.append(Paragraph("1.4.1 本試料は、その存在期間を通じて、物理的な危害や劣化からの保存、および不正アクセスからのセキュリティを確保するために、その形式と感度に適した環境に保存されること。", style_h2))
story.append(Paragraph("1.4.2 ウイルス対策ソフトウェアや役割ベースのアクセス制御を含むがこれらに限定されない、データの機密性、完全性、および可用性を確保するための適切な制御が実施されること。", style_h2))
story.append(Paragraph("1.4.3 本試料の保存、アクセス、および分析に使用されるサーバー、クライアントデバイス、およびアプリケーションは、ベンダーがサポートするバージョンのオペレーティングシステム、ファームウェア、およびソフトウェアで展開され、例外がある場合は、適切な緩和策が記述され監査可能であるように文書化されること。および", style_h2))
story.append(Paragraph("1.4.4 暗号化が転送中（in transit）および保存時（at rest）に行われていること（以下の条項6.1に従って）。", style_h2))

story.append(Paragraph("2. トレーニング", style_h1))
story.append(Paragraph("2.1 申請者機関は、本試料にアクセスするすべての許可された個人が以下を確実にするものとする：", style_normal))
story.append(Paragraph("2.1.1 取り扱う本試料に対する責任を認識していること。および", style_h2))
story.append(Paragraph("2.1.2 少なくとも3年ごとに適切な情報セキュリティおよびデータ保護のトレーニングを受けること。このトレーニングプログラムには、現在の一般的な脅威と対応する適切な行動に関する情報が含まれるべきである。", style_h2))
story.append(Paragraph("2.2 申請者機関は、本試料にアクセスできるすべての個人について、最新のトレーニング記録を保持しなければならない。", style_normal))

story.append(Paragraph("3. 本試料へのアクセス", style_h1))
story.append(Paragraph("3.1 申請者機関は、処理する本試料へのアクセスを正当に許可された個人のみに制限する物理的および技術的なアクセス制御を実施しなければならない。アクセスログと監視を実施すべきである。", style_normal))
story.append(Paragraph("3.2 申請者機関は、正当に許可された個人のみが本試料へのアクセスを許可され、職務の遂行に必要な範囲でのみ許可されることを保証しなければならない。", style_normal))
story.append(Paragraph("3.3 申請者機関は、データ処理システムへのデータアクセス権限の付与、変更、または無効化に対する全体的な責任を持つシステム管理者を特定し、任命しなければならない。アクセス権限は定期的に見直されるべきである。", style_normal))
story.append(Paragraph("3.4 本試料にアクセスできる個人が退職するか、権限が削除された場合（例えば、役割の変更の結果として）、申請者機関は1週間以内にそのステータスが更新されることを保証しなければならない（例えば、アクセス制御リストを変更することによって）。", style_normal))
story.append(Paragraph("3.5 申請者機関は、サーバーデータ処理施設へのアクセスが正当に許可された個人のみに制限されることを保証し、そのようなサーバーデータ処理場所で物理的なセキュリティ対策（例えば、鍵、生体認証リーダー、またはその他の電子セキュリティ対策の使用）を実施しなければならない。", style_normal))
story.append(Paragraph("3.6 申請者機関は、本試料へのアクセスに関して適切な記録を保持しなければならない。", style_normal))

story.append(Paragraph("4. ユーザーアクセス制御", style_h1))
story.append(Paragraph("4.1 申請者機関は、本試料へのアクセスが上記のようにアクセス権限を通じて制御されることを保証しなければならない。ユーザー名またはユーザーアカウントと適切に安全なパスワードの使用が最低限必要である。追加の適切な制御には、パスワードレス技術の使用や多要素認証の使用が含まれる場合がある。", style_normal))
story.append(Paragraph("4.2 申請者機関は、許可された個人が同じユーザーアカウントを共有または使用しないことを保証しなければならず、例外がある場合は、適切な緩和策が記述され監査可能であるように文書化されなければならない。", style_normal))
story.append(Paragraph("4.3 ITシステムの許可されたユーザーを認証するために、多要素認証の使用が強く推奨される。", style_normal))

story.append(Paragraph("5. 技術的制御", style_h1))
story.append(Paragraph("5.1 申請者機関は、本試料を処理するために使用するすべてのラップトップ、デスクトップ、およびサーバーに、ファイアウォール、ウイルス対策、スパイウェア対策、およびその他のマルウェア対策ソフトウェアおよび技術を含む適切なエンドポイントセキュリティを実施しなければならない。", style_normal))
story.append(Paragraph("5.2 申請者機関は、ファイアウォール、ウイルス対策、スパイウェア対策、およびその他のマルウェア対策ソフトウェアおよび技術を定期的に更新し、当時の最新のウイルス、スパイウェア、およびその他のマルウェアの脅威から保護されるようにしなければならない。", style_normal))
story.append(Paragraph("5.3 申請者機関は、重要なソフトウェアおよびファームウェアの更新とパッチが合理的に迅速な期間内に適用されることを保証しなければならない。", style_normal))
story.append(Paragraph("5.4 申請者機関は、ファイアウォールおよびウイルス対策措置に加えて、侵入防止および検知システム（IPS/IDS）の使用を含む多くの方法を使用して外部からの攻撃を緩和し、適切な監視を実施しなければならない。", style_normal))
story.append(Paragraph("5.5 リモートアクセスが提供される場合、許可されたデバイスのみがITシステムにアクセスし、ブルートフォース攻撃に耐性があることを保証するための制御を実施しなければならない。", style_normal))
story.append(Paragraph("5.6 申請者機関は、脆弱性が発見され、合理的な期間内に対処されることを保証するためにあらゆる合理的な措置を講じなければならない。これらの措置には、内部脆弱性スキャンおよび独立した外部監査人（ペネトレーションテスト）の使用が含まれる場合がある。", style_normal))

story.append(Paragraph("6. データの保存と転送", style_h1))
story.append(Paragraph("6.1 物理的に安全でないストレージ（例：クライアントデバイス、ラップトップ、PC、容易に取り外せる小型デスクトップサーバーまたはその他の機器）に保持されるデータは、常に保存時（at rest）に暗号化されなければならない（本試料のバックアップコピーを含む）。物理的に安全なストレージ（例：安全な部屋にあるラックサーバー）に保持されるデータは、可能な場合は暗号化されるべきである。", style_normal))
story.append(Paragraph("6.2 データは、転送中にベストプラクティスを使用して暗号化されなければならない。安全でない、または時代遅れのプロトコルや暗号スイートは使用してはならない。", style_normal))
story.append(Paragraph("6.3 ポータブルメディア（例：USBまたはリムーバブルドライブ）の使用は積極的に推奨されないが、使用される場合、データは強力なパスワードまたはその他の秘密情報を使用して暗号化されなければならない。", style_normal))
story.append(Paragraph("6.4 申請者機関は、すべての許可された個人が、オンラインでのデータの保存と共有に関するUKバイオバンクの要件を認識していることを保証しなければならない。そのような要件には以下が含まれる：", style_normal))
story.append(Paragraph("6.4.1 参加者レベルデータを、許可されていない個人または許可されていない第三者と（直接的または間接的に）共有してはならない。", style_h2))
story.append(Paragraph("6.4.2 参加者レベルデータを、許可されていない個人または許可されていない第三者がアクセス可能なWebベースまたはその他のリポジトリに（直接的または間接的に）共有、保存、またはアップロードしてはならない。", style_h2))
story.append(Paragraph("6.4.3 本試料のクラウドおよびオンラインストレージは、以下の場合に許可される：", style_h2))
story.append(Paragraph("6.4.3.1 MTAの規定に従って使用される場合。", style_h3))
story.append(Paragraph("6.4.3.2 許可された個人のみが本試料にアクセスできる場合。", style_h3))
story.append(Paragraph("6.4.3.3 不正および不法な処理から本試料を保護するために適切なセキュリティ対策が講じられている場合。および", style_h3))
story.append(Paragraph("6.4.3.4 申請者機関が本試料に対して完全な責任を負う場合。", style_h3))
story.append(Paragraph("6.5 本試料は、MTAの満了または終了まで、本付属書2に従って申請者機関によって保持されるものとする。その後、本試料はMTAに従って申請者機関によって破棄されるか、または恒久的にアクセス不能にされるものとする。データの破棄または削除は恒久的であるべきであり、破棄または削除されたデータは復元可能であってはならない。", style_normal))
story.append(Paragraph("6.6 申請者機関は、要求があった場合、またはMTAの満了もしくは終了時にすべてのUKバイオバンクデータを削除できるように、情報資産登録簿を維持しなければならない。", style_normal))
story.append(PageBreak())

# --- Annex 3 ---
story.append(Paragraph("付属書 3<br/>年次プロジェクト報告書テンプレート", style_title))
annex3_text = """
本付属書3の目的は、申請者PIに対し、年次ベース（発効日の毎年の記念日）で完了しUKバイオバンクに提出する必要がある年次プロジェクト報告書フォームのテンプレートを提供することである。疑義を避けるために付言すると、申請者PIはMTAの締結時にこのフォームを完了する必要はない。
<br/><br/>
UKバイオバンクは、提出方法を含め、このフォームを随時更新する権利を留保する。フォームの最新版および提出手順は、UKバイオバンクのAMSおよびウェブサイトで入手可能である。
<br/><br/>
<b>申請者年次プロジェクト報告書</b>
<br/>
毎年、UKバイオバンクの研究プロジェクトの申請者主任研究者（PI）は、プロジェクトに関するいくつかの情報を提供し、試料提供契約（MTA）の条件を遵守していることを確認する必要がある。ヘルプについては、UKバイオバンクのウェブサイトにあるAMSユーザーガイドを参照されたい。期限内にこの報告書を提供しない場合（期限前にUKバイオバンクから督促があった後）、プロジェクトに取り組んでいるすべての研究者が、RAPを介してさらなるデータをダウンロードしたり、既存のデータにアクセスしたりすることができなくなる。RAPを介したさらなるデータのダウンロードおよび/または既存のデータへのアクセス能力は、報告書が提出されたときにプロジェクトに取り組んでいるすべての研究者に対して回復される。
<br/><br/>
<b>研究プロジェクト番号:</b> ______________________<br/>
<b>申請者機関:</b> ______________________<br/>
<b>報告完了日:</b> ______________________<br/>
<br/>
<b>1. すべての共同研究者は現在、AMSの共同研究者リストに名前が記載されているこの研究プロジェクトのUKバイオバンクデータにアクセスしていますか？</b><br/>
[ はい / いいえ ]<br/>
<i>いいえの場合、未登録の共同研究者にできるだけ早く登録を提出するよう依頼してください。登録承認後、共同研究者リストに追加できます。UKバイオバンクデータにアクセスしなくなった共同研究者は削除してください。</i>
<br/><br/>
<b>2. この研究プロジェクトでUKバイオバンクデータにアクセスしている関連会社の名前を提供してください。ない場合は、その旨を記載してください：</b><br/>
関連会社: ______________________
<br/><br/>
<b>3. この研究プロジェクトの下請け業者としてUKバイオバンクデータを処理する第三者処理業者の名前、および第三者処理業者があなたの代理で行うタスクの詳細を提供してください。ない場合は、その旨を記載してください：</b><br/>
第三者処理業者: ______________________<br/>
第三者処理業者のタスク: ______________________
<br/><br/>
<b>4. 研究プロジェクトの進捗状況と今後12ヶ月の計画の更新（要約セクションを含む）を提供してください：</b><br/>
これまでの進捗: ______________________<br/>
今後12ヶ月の計画: ______________________
<br/><br/>
<b>5. 研究成果（例：ウェブサイト、特許、GWAS要約統計の場所）の詳細を提供し、前回の年次プロジェクト報告書以降のこのプロジェクトからのすべての出版物（プレプリントおよび査読付き出版物を含む）をリストアップしてください。ない場合は、その旨を記載してください：</b><br/>
研究成果: ______________________<br/>
出版物: <i>(形式: 第一著者, 年, タイトル, ジャーナル, PMID, DOI, 論文/特許へのウェブリンク)</i>
<br/><br/>
<b>6. UKバイオバンクデータおよびこの研究プロジェクトに関連する作業に関連するコードやリソースを保存/共有するために、一般にアクセス可能なオンラインリポジトリを使用していますか？</b><br/>
[ はい / いいえ ]<br/>
はいの場合、使用しているオンラインリポジトリの詳細（GitHubなど）を提供してください：<br/>
パブリックアカウント詳細: <i>(名前とウェブサイトリンク)</i>
<br/><br/>
<b>7. 私は以下を確認します（'x'でマークしてください）：</b><br/>
[ ] 私は上記で特定された研究プロジェクトの申請者PIです。<br/>
[ ] 私は上記で特定された研究プロジェクトのために行われているすべての研究を認識しています。<br/>
[ ] 関連する試料提供契約（適用される修正および更新を含む）および付属書の規定が遵守されています。<br/>
[ ] UKバイオバンクの本試料を保護するために、ここに記載されたセキュリティ対策が、上記で特定された研究プロジェクトに対して実施されています。
"""
story.append(Paragraph(annex3_text, style_normal))
story.append(PageBreak())

# --- Annex 4 ---
story.append(Paragraph("付属書 4<br/>承認済み研究プロジェクト", style_title))
story.append(Paragraph("（ここに承認されたプロジェクトの詳細が記載されます）", style_normal))
story.append(Paragraph("※ 本付属書には、通常、具体的な研究プロジェクトの範囲、期間、および提供されるデータセットの詳細が記載されますが、本テンプレートでは空白となっています。", style_normal))

# Build PDF
doc.build(story)