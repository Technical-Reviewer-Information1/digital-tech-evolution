import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="未来技術体験エキスポ",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    st.title("未来技術 体験エキスポ 🚀")
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
    st.subheader("📈 情報技術の発展タイムライン")
    
    timeline_data = {
        '年': [1969, 1989, 1995, 2004, 2007, 2012, 2016, 2020, 2022],
        '技術': ['ARPANET', 'World Wide Web', 'インターネット普及', 'SNS(Facebook)', 'iPhone', 'VR(Oculus)', 'AI(深層学習)', '5G通信', 'ChatGPT'],
        'ユーザー数(億人)': [0.001, 0.01, 0.15, 1, 10, 0.1, 2, 50, 1]
    }
    
    df = pd.DataFrame(timeline_data)
    fig = px.scatter(df, x='年', y='ユーザー数(億人)', 
                     size='ユーザー数(億人)', hover_name='技術',
                     title='情報技術の発展とユーザー数の推移',
                     log_y=True)
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # ステップ2: VR/AR/MR体験ゾーン
    st.header("🥽 ステップ2: 体験ゾーン① - 現実を超えるテクノロジー (VR/AR/MR)")
    st.markdown("**似ているようで全く違う、3つの「現実」技術。それぞれの世界をのぞいてみましょう。**")
    
    tab1, tab2, tab3 = st.tabs(["🌐 VR (仮想現実)", "📱 AR (拡張現実)", "🔮 MR (複合現実)"])
    
    with tab1:
        st.subheader("VR (仮想現実) - 完全に別の世界へダイブ！")
        st.markdown("**シナリオ:** あなたは今、VRゴーグルを装着して、飛行機のパイロットになるための訓練をしています。")
        
        # VR体験シミュレーション
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("### 🎮 VR体験シミュレーション")
            if st.button("VR体験を開始", key="vr_start"):
                st.success("VRゴーグルを装着しました！")
                st.markdown("**体験中...**")
                
                # 360度視点のシミュレーション
                import numpy as np
                theta = np.linspace(0, 2*np.pi, 100)
                r = np.random.random(100) * 10 + 5
                
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=r,
                    theta=theta * 180/np.pi,
                    mode='markers',
                    name='VR空間内オブジェクト',
                    marker=dict(size=8, color='blue')
                ))
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(visible=True, range=[0, 15])
                    ),
                    title="VR空間の360度ビュー（シミュレーション）"
                )
                st.plotly_chart(fig, use_container_width=True)
        
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
            st.markdown("### 🏗️ MR建築シミュレーション")
            
            # MRのインタラクティブ要素
            building_type = st.selectbox("建築する建物の種類を選択:", 
                                       ["一戸建て住宅", "マンション", "オフィスビル", "学校"])
            
            if st.button("MR建築プレビューを開始", key="mr_start"):
                st.success(f"{building_type}のMRモデルを現実空間に投影中...")
                
                # 3D建築物の簡易可視化
                import numpy as np
                
                x = np.random.random(50) * 10
                y = np.random.random(50) * 10
                z = np.random.random(50) * 5
                
                fig = go.Figure(data=[go.Scatter3d(
                    x=x, y=y, z=z,
                    mode='markers',
                    marker=dict(
                        size=8,
                        color=z,
                        colorscale='Viridis',
                        opacity=0.8
                    ),
                    name=f'{building_type} MRモデル'
                )])
                
                fig.update_layout(
                    title=f"{building_type} - MR 3Dプレビュー",
                    scene=dict(
                        xaxis_title="X座標(m)",
                        yaxis_title="Y座標(m)",
                        zaxis_title="高さ(m)"
                    )
                )
                st.plotly_chart(fig, use_container_width=True)
        
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
        factors = ['スキル格差', '経済格差', '地域格差', '年齢格差', '言語格差']
        impact = [85, 78, 65, 72, 45]
        
        fig = go.Figure([go.Bar(x=factors, y=impact, 
                               marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])])
        fig.update_layout(
            title="デジタルデバイドの主な要因と影響度",
            xaxis_title="格差の種類",
            yaxis_title="社会への影響度（%）"
        )
        st.plotly_chart(fig, use_container_width=True)
    
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
            if score == 3:
                st.success("🟢 優秀！とても健康的にテクノロジーと付き合えています！")
            elif score == 2:
                st.warning("🟡 まずまず。もう少し気を付けるとより良くなります。")
            else:
                st.error("🔴 要注意！テクノロジーの使い方を見直しましょう。")
            
            # スクリーンタイム評価
            if screen_time <= 3:
                st.info("📱 スクリーンタイム: 健康的な範囲です")
            elif screen_time <= 6:
                st.warning("📱 スクリーンタイム: 平均的ですが、休憩を忘れずに")
            else:
                st.error("📱 スクリーンタイム: 長すぎです。意識的に減らしましょう")
        
        with col2:
            # 健康度の可視化
            health_score = (score * 25) + (25 if screen_time <= 6 else 0)
            
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
    
    # 追加の工夫: 学習進捗とまとめ
    st.header("🎓 学習まとめ")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 今日学んだこと")
        learning_topics = {
            '技術': ['VR', 'AR', 'MR', 'デジタルデバイド', 'VDT症候群'],
            '理解度': [95, 88, 92, 85, 90]
        }
        
        df_learning = pd.DataFrame(learning_topics)
        fig = px.bar(df_learning, x='技術', y='理解度', 
                     title='学習項目別理解度',
                     color='理解度',
                     color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
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
    st.balloons()

if __name__ == "__main__":
    main()