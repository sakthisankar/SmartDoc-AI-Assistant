import streamlit as st
from App import main
import time


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SmartDoc AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* =========================================================
MAIN BACKGROUND
========================================================= */

.stApp {
    background: #f5f7fb;
}

/* Remove top spacing */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 1400px;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background: #ffffff !important;
    width: 320px !important;
    border-right: 1px solid #e5e7eb;
}

section[data-testid="stSidebar"] > div {
    background: #ffffff !important;
}

/* =========================================================
TOP LOGO AREA
========================================================= */

.logo-container {
    background: linear-gradient(90deg, #4f6df5, #5d7cff);
    padding: 22px;
    margin: -1rem -1rem 20px -1rem;
}

.logo-title {
    color: white;
    font-size: 34px;
    font-weight: 800;
    display: flex;
    align-items: center;
    gap: 12px;
}

/* =========================================================
SIDEBAR HEADINGS
========================================================= */

.sidebar-heading {
    font-size: 15px;
    font-weight: 800;
    color: #4f6df5;
    letter-spacing: 1.5px;
    margin-top: 25px;
    margin-bottom: 14px;
}

/* Divider */
.divider {
    height: 0.5px;
    background: #e5e7eb;
    margin-top: 18px;
    margin-bottom: 18px;
}

/* =========================================================
UPLOAD BOX
========================================================= */

section[data-testid="stFileUploader"] {
    background: #ffffff;
    padding: 16px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.03);
}

/* Upload Label */
section[data-testid="stFileUploader"] label {
    color: #374151 !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

/* Upload Button */
section[data-testid="stFileUploader"] button {
    background: #ffffff !important;
    color: #111827 !important;
    border: 1px dashed #cbd5e1 !important;
    border-radius: 14px !important;
    font-weight: 600 !important;
    height: 58px !important;
}

/* Upload Text */
section[data-testid="stFileUploader"] small,
section[data-testid="stFileUploader"] span,
section[data-testid="stFileUploader"] p {
    color: #6b7280 !important;
}

/* Uploaded file card */
.uploadedFile {
    border: 1px solid #e5e7eb !important;
    border-radius: 14px !important;
    background: #ffffff !important;
}

/* =========================================================
SIDEBAR LIST
========================================================= */

.sidebar-list {
    color: #111827;
    font-size: 16px;
    line-height: 1.1;
    font-weight: 350;
}

/* Sidebar Text */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {
    color: #111827;
}

/* =========================================================
HEADER
========================================================= */

.main-title {
    text-align: center;
    font-size: 64px;
    font-weight: 800;
    color: #111827;
    margin-top: 25px;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 22px;
    font-weight: 500;
    margin-bottom: 15px;
}

.author {
    text-align: center;
    color: #4f6df5;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 40px;
}

/* =========================================================
CHAT UI
========================================================= */

/* User Bubble */
.user-message {
    background: #eef2ff;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #dbe4ff;
    margin-left: 120px;
    margin-bottom: 20px;
    font-size: 16px;
    color: #111827;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.03);
}

/* AI Bubble */
.bot-message {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    margin-right: 120px;
    margin-bottom: 30px;
    font-size: 16px;
    line-height: 1.9;
    color: #111827;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.04);
}

/* Chat Labels */
.chat-label {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* =========================================================
CHAT INPUT
========================================================= */

.stChatInputContainer {
    background: white !important;
    border-top: 1px solid #e5e7eb;
}

/* =========================================================
FOOTER
========================================================= */

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
    font-size: 14px;
}

/* =========================================================
SCROLLBAR
========================================================= */

::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-thumb {
    background: #d1d5db;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="logo-container">
            <div class="logo-title">
                SmartDoc AI
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-heading">
        📁 DOCUMENTS
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload PDF Document",
        type=["pdf"]
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="sidebar-heading">
        ✨ FEATURES
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-list">
        🔍 Semantic Search<br>
        🧠 FAISS Vector Retrieval<br>
        🤖 GPT-Powered Answers<br>
        ⚡ Low Latency Querying<br>
        🛡️ Enterprise AI Assistant<br>
        💬 Context-Aware Responses
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="sidebar-heading">
        🧠 TECH STACK
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-list">
        ⚙️ OpenAI API<br>
        ⚙️ LangChain<br>
        ⚙️ FAISS<br>
        ⚙️ Streamlit<br>
        ⚙️ Python
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-title">
    🤖 SmartDoc AI
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Enterprise Document Intelligence Platform powered by RAG + OpenAI
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="author">
    Built by Sakthi Sankar | Intelligent Document Intelligence Platform
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">
                <div class="chat-label">👤 You</div>
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="bot-message">
                <div class="chat-label">🤖 SmartDoc AI</div>
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# CHAT INPUT
# =========================================================

if uploaded_file is not None:

    question = st.chat_input(
        "Ask anything about your document..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.spinner("Analyzing document with AI..."):

            time.sleep(1)

            answer = main(uploaded_file, question)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()

else:

    st.info("📄 Upload a PDF document to begin intelligent querying.")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
    Built️ by Sakthi Sankar | SmartDoc AI
    </div>
    """,
    unsafe_allow_html=True
)
