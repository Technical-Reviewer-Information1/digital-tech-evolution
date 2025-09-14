import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# スクリーンタイム評価基準の出典:
# 1. Reid Health (2024). "How Much Screen Time is Too Much for Adults?"
#    推奨: 労働時間外のスクリーンタイムは2時間以下
# 2. PMC研究論文 (2024). "The hazards of excessive screen time: Impacts on physical health, mental health, and overall well-being"
#    PMC Article: PMC10852174. 6時間以上の使用でうつ病リスク増加
# 3. Stanford Longevity Center (2024). "What Excessive Screen Time Does to the Adult Brain"
#    18-25歳成人における過度のスクリーンタイムが脳の皮質を薄くする影響を確認

st.set_page_config(
    page_title="情報技術の発達",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    st.title("情報技術の発達（pp.225-226）")
    st.caption("Created by Dit-Lab.(Daiki ITO)")
    st.caption("Supported by Tomoaki ATSUMI")
    
    st.markdown("---")
    
    # ステップ1: はじめに
    st.header("🌟 ステップ1: はじめに - 未来技術の世界へようこそ！")
    
    st.markdown("""
    **インターネットやAI、VRなどの情報技術は、私たちの生活を日々、驚くほど豊かにしてくれています。
    このエキスポでは、最新技術がどのようなものか、そして技術の発展によって生まれる新しい課題は何かを、
    一緒に体験していきましょう！**
    """)
    
    # 情報技術の発展の可視化
    st.subheader("📈 インターネット利用者数の推移")
    
    # 確かなデータに基づくインターネット利用者数推移（世界）
    internet_data = {
        '年': [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023],
        'インターネット利用者数(億人)': [0.003, 0.16, 3.61, 10.18, 20.78, 32.36, 46.48, 54.00]
    }
    
    df = pd.DataFrame(internet_data)
    fig = px.line(df, x='年', y='インターネット利用者数(億人)', 
                  title='世界のインターネット利用者数の推移',
                  markers=True)
    fig.update_traces(line=dict(color='#1f77b4', width=3),
                     marker=dict(size=8, color='#1f77b4'))
    fig.update_layout(
        xaxis_title="年",
        yaxis_title="インターネット利用者数（億人）",
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.caption("📊 出典: ITU（国際電気通信連合）World Telecommunication/ICT Indicators Database 2023")
    
    st.markdown("---")
    
    # ステップ2: VR/AR/MR体験ゾーン
    st.header("🥽 ステップ2: 体験ゾーン① - 現実を超えるテクノロジー (VR/AR/MR)")
    st.markdown("**似ているようで全く違う、3つの「現実」技術。それぞれの世界をのぞいてみましょう。**")
    
    tab1, tab2, tab3 = st.tabs(["🌐 VR (仮想現実)", "📱 AR (拡張現実)", "🔮 MR (複合現実)"])
    
    with tab1:
        st.subheader("VR (仮想現実) - 完全に別の世界へダイブ！")
        st.markdown("**シナリオ:** あなたは今、VRゴーグルを装着して、飛行機のパイロットになるための訓練をしています。")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("### 🎮 VR体験の想像")
            st.markdown("""
            **VRゴーグルを装着すると...**
            
            🕶️ 視界が完全にCGの世界に切り替わります
            
            ✈️ コックピットの中にいるような感覚
            
            📊 計器類が立体的に見え、手で操作できます
            
            🌤️ 窓の外には雲と青空が広がっています
            
            🎯 頭を動かすと360度見回すことができます
            
            **この没入感がVRの最大の特徴です！**
            """)
        
        with col2:
            st.markdown("### 📚 VRの解説")
            st.info("""
            **VR (Virtual Reality)** は、専用のゴーグルなどを使い、目の前すべてをCGなどの仮想的な空間に置き換える技術です。
            ゲームやフライトシミュレーターなどで、圧倒的な没入感を体験できます。
            
            **主な用途:**
            - ゲーム・エンターテインメント
            - 教育・訓練シミュレーション
            - 医療・リハビリテーション
            - 建築・設計の検証
            """)
    
    with tab2:
        st.subheader("AR (拡張現実) - 現実世界に情報をプラス！")
        st.markdown("**シナリオ:** あなたは今、スマホのカメラを自分の机に向けています。「AR起動」ボタンを押してみてください。")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("### 📱 AR体験シミュレーション")
            
            # AR起動前の状態
            if "ar_activated" not in st.session_state:
                st.session_state.ar_activated = False
            
            st.markdown("**現在のカメラ映像:** 📷")
            if not st.session_state.ar_activated:
                st.markdown("```\n🏢 机の上\n📚📝✏️\n```")
                if st.button("AR起動！", key="ar_start"):
                    st.session_state.ar_activated = True
                    st.rerun()
            else:
                st.markdown("```\n🏢 机の上\n📚📝✏️\n🦄✨ <- AR追加オブジェクト\n🎯 情報タグ\n```")
                st.success("ARが起動されました！現実の机の上にデジタル情報が重ね合わされています！")
                if st.button("ARを終了", key="ar_stop"):
                    st.session_state.ar_activated = False
                    st.rerun()
        
        with col2:
            st.markdown("### 📚 ARの解説")
            st.info("""
            **AR (Augmented Reality)** は、スマホのカメラなどを通じて、現実の風景の上に文字やキャラクターなどのデジタル情報を重ねて表示する技術です。
            
            **主な用途:**
            - スマホアプリ（ポケモンGO等）
            - ナビゲーション
            - ショッピング（試着体験）
            - 教育（教科書の拡張）
            - 工業（作業支援）
            """)
    
    with tab3:
        st.subheader("MR (複合現実) - 現実と仮想が手を取り合う！")
        st.markdown("**シナリオ:** あなたは今、未来の建築家。MRゴーグルをかけると、目の前の空っぽの空間に、これから建てる家の完成イメージが立体的に現れます。")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("### 🏗️ MR建築の想像")
            st.markdown("""
            **MRゴーグルをかけると...**
            
            🥽 現実の空間が見えたまま、建物の3Dモデルが重なって見えます
            
            🏠 建物の設計図が立体的に浮かび上がります
            
            👋 手で建物の周りを回り込んで見ることができます
            
            📐 実際のサイズ感で建物の大きさを確認できます
            
            🔧 手でドアや窓の位置を変更することも可能です
            
            👥 他の人と同じMR空間を共有して話し合えます
            
            **現実と仮想が融合するのがMRの特徴です！**
            """)
        
        with col2:
            st.markdown("### 📚 MRの解説")
            st.info("""
            **MR (Mixed Reality)** は、ARをさらに進化させ、現実空間に仮想の物体をまるでそこにあるかのように表示し、回り込んだり、手で操作したりもできる技術です。
            
            **主な用途:**
            - 医療手術支援
            - 製造業での設計検証
            - 建築・都市計画
            - 教育（解剖学等）
            - リモート協業
            """)
    
    st.markdown("---")
    
    # ステップ3: デジタルデバイド
    st.header("⚖️ ステップ3: 社会課題ゾーン② -「デジタルデバイド」を考える")
    st.markdown("**便利さの裏側にある「格差」とは？**")
    st.markdown("""
    情報技術は便利ですが、誰もが同じようにその恩恵を受けられるわけではありません。
    この情報格差をデジタルデバイドと言います。
    """)
    
    st.subheader("🏛️ シナリオ: オンライン行政サービス")
    st.markdown("""
    **ある町で、行政サービスの手続きが「スマートフォンアプリからのオンライン申請のみ」になりました。
    このとき、困ってしまう可能性がある人は誰だと思いますか？**
    """)
    
    options = [
        "A: スマホの操作に慣れていない高齢者",
        "B: スマホやインターネット回線を契約する経済的余裕がない人", 
        "C: 山間部など、インターネット環境が整備されていない地域に住む人"
    ]
    
    selected = st.multiselect("オンライン申請で困る可能性がある人は？（複数選択可）", options)
    
    if st.button("回答を確認", key="digital_divide_check"):
        if len(selected) == 3:
            st.success("✅ 正解です！")
        else:
            st.warning("すべての選択肢が正解です。もう一度考えてみてください。")
        
        st.markdown("""
        ### 📖 解説
        **答えは、A・B・Cのすべてです。**
        
        このように、**スキル**、**経済**、**環境**など、様々な要因によって情報技術を使える人と使えない人の間に、
        情報の量や社会参加の機会の**格差（デバイド）**が生まれてしまうことが、現代社会の大きな課題となっています。
        """)
        
        # デジタルデバイドの要因を可視化
        st.subheader("📊 日本におけるインターネット利用率の格差")
        
        # 総務省の統計データに基づく（2022年通信利用動向調査）
        divide_data = {
            '項目': ['20代', '60代', '世帯年収200万円未満', '世帯年収1000万円以上', '都市部', '地方'],
            '利用率(%)': [98.5, 76.0, 72.3, 96.8, 88.9, 82.1],
            'カテゴリ': ['年齢', '年齢', '経済', '経済', '地域', '地域']
        }
        
        df_divide = pd.DataFrame(divide_data)
        fig = px.bar(df_divide, x='項目', y='利用率(%)', color='カテゴリ',
                     title='インターネット利用率の格差（2022年）',
                     color_discrete_map={'年齢': '#FF6B6B', '経済': '#4ECDC4', '地域': '#45B7D1'})
        
        fig.update_layout(
            xaxis_title="属性",
            yaxis_title="インターネット利用率（%）",
            yaxis=dict(range=[0, 100])
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.caption("📊 出典: 総務省「令和4年通信利用動向調査」")
    
    st.markdown("---")
    
    # ステップ4: 健康チェック
    st.header("💪 ステップ4: 健康ゾーン③ - テクノロジーと上手に付き合うために")
    st.markdown("**あなたの「スクリーンタイム」は健康的？**")
    st.markdown("""
    便利なスマホやPCも、長時間使い続けると心身に不調をきたすことがあります。
    これを**VDT症候群**と言います。あなたの習慣をチェックしてみましょう。
    """)
    
    st.subheader("🔍 健康チェックリスト")
    
    check1 = st.checkbox("1時間に1回は画面から目を離し、休憩している")
    check2 = st.checkbox("画面の明るさを、部屋の明るさに合わせて調整している") 
    check3 = st.checkbox("猫背にならないよう、正しい姿勢を意識している")
    
    # スクリーンタイム入力
    st.subheader("📱 1日のスクリーンタイムを入力してください")
    screen_time = st.slider("1日のスマホ・PC使用時間（時間）", 0, 16, 6)
    
    if st.button("健康状態を診断", key="health_check"):
        score = sum([check1, check2, check3])
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # 総合評価（チェックリストとスクリーンタイム両方を考慮）
            # 出典: Reid Health研究, PMC論文 (2024) - 成人の非労働時間スクリーンタイム推奨値
            # 2時間以下: 健康的範囲, 6時間以上: うつ病リスク増加
            screen_score = 0
            if screen_time <= 2:
                screen_score = 3
                screen_msg = "📱 スクリーンタイム: 健康的な範囲です（推奨: ≤2時間/日）"
                screen_color = "info"
            elif screen_time <= 6:
                screen_score = 2
                screen_msg = "📱 スクリーンタイム: 注意が必要です。メンタルヘルスへの影響に注意"
                screen_color = "warning"
            else:
                screen_score = 1
                screen_msg = "📱 スクリーンタイム: 危険域です。うつ病リスクが高まります（研究: 6時間以上）"
                screen_color = "error"
            
            # 総合スコア計算
            total_score = score + screen_score
            
            if total_score >= 5:
                st.success("🟢 優秀！とても健康的にテクノロジーと付き合えています！")
            elif total_score >= 4:
                st.warning("🟡 まずまず。もう少し気を付けるとより良くなります。")
            else:
                st.error("🔴 要注意！テクノロジーの使い方を見直しましょう。")
            
            # スクリーンタイム評価を適切な色で表示
            if screen_color == "info":
                st.info(screen_msg)
            elif screen_color == "warning":
                st.warning(screen_msg)
            else:
                st.error(screen_msg)
        
        with col2:
            # 健康度の可視化（修正された計算）
            health_score = (total_score / 6) * 100
            
            fig = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = health_score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "テクノロジー健康度"},
                delta = {'reference': 75},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "lightgreen"},
                    'steps': [
                        {'range': [0, 50], 'color': "lightgray"},
                        {'range': [50, 75], 'color': "yellow"},
                        {'range': [75, 100], 'color': "green"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90}}
            ))
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        ### 💡 アドバイス
        テクノロジーは私たちの生活を豊かにしてくれますが、健康を第一に、上手に付き合っていくことが大切です。
        
        **VDT症候群の予防法:**
        - 20-20-20ルール: 20分ごとに20秒間、20フィート（約6m）先を見る
        - 適切な画面の明るさと距離を保つ
        - 正しい姿勢を保つ
        - 定期的な休憩とストレッチ
        """)
    
    st.markdown("---")
    
    # 学習まとめ
    st.header("🎓 学習まとめ")
    
    st.subheader("🔮 未来への展望")
    st.markdown("""
    **情報技術の発展によって、私たちの社会はどのように変わっていくでしょうか？**
    
    **ポジティブな変化:**
    - より豊かな体験と学習機会
    - 地理的制約を超えたコミュニケーション
    - 効率的な社会システム
    
    **課題として取り組むべきこと:**
    - デジタルデバイドの解消
    - プライバシーとセキュリティの確保
    - 健康的な技術利用の促進
    
    **みなさんも、技術の恩恵を受けながら、
    より良い社会づくりに参加していきましょう！**
    """)
    
    st.markdown("---")
    st.markdown("### 🙏 お疲れ様でした！")

if __name__ == "__main__":
    main()
