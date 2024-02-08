import streamlit as st
st.title("Hello World")
#title recommeded to be used once

st.header("Header")
st.subheader("SubHeader")

#text 
st.text("this is a text written under subheader")

#emojis and html 
st.markdown("""# h1 tag\n## h2 tag \n
            ### h3 tag\n:moon:\n:anger:<br>
            <h1>hello""",True)

#latex for mathematical expressions
st.latex(r""" \begin{pmatrix}
            3  & -10 & 2 \\
            -1 &   7 & 4 \\
            5  &   0 & 1
        \end{pmatrix}
        \begin{pmatrix}
            x\\ y\\ z
        \end{pmatrix}
        =
        \begin{pmatrix}
           3x-10y+2z \\
           -x+7y+4z \\
           5x+z
        \end{pmatrix}s
""")

#write
st.write("saksham","angirash","sharma")
st.write("#hi")
st.write(st)
st.write(sum)