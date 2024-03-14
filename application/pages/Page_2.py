import streamlit as st
import pandas as pd

# dataframes
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# widgets
st.text_input("Your name", key="name")

name = st.session_state.name
name

# checkboxes

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       data=[[3,7,2],[6,2,9]],
       columns=['a', 'b', 'c'])

    chart_data

    # selection + sidebar
        
    option = st.sidebar.selectbox(
        'Which number do you like best?',
        chart_data['a'])

    'You selected: ', option

    # columns

    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    with left_column:
        if st.button('Press me!'):
            st.write('Why hello there')
        if st.button('Clear'):
            st.empty()


    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")


    # progress

    import time 
        
    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(10):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress((i + 1)*10)
        time.sleep(0.1)

    '...and now we\'re done!'

# add a streamlit slider from 0 to 100

x = st.slider('x', max_value=999) 
