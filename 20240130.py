st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')


# 시각화 선택 구현
    chart_type = st.sidebar.radio("Select chart type", ("Candlestick", "Line"))
    candlestick = go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])
    line = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close')
    if chart_type == "Candlestick":
        fig = go.Figure(candlestick) # 차트 재정의
    elif chart_type == "Line":
        fig = go.Figure(line)
    else:
        pass
    fig.update_layout(title=f"{ticker} Stock {chart_type} Chart", xaxis_title="Date", yaxis_title="Price")
    # Plot the figure
    st.plotly_chart(fig)
    st.markdown("<hr>", unsafe_allow_html=True)
    # 테이블 보여주기 구현
    num_row = st.sidebar.number_input('Number of Rows', min_value=1, max_value=len(data))
    st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set_index('Date'), use_container_width=True) # 역순 : 최근 날짜 데이터 먼저 보여줌