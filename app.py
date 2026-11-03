

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Rectangle, Circle
import math

st.set_page_config(
    page_title="Bé vui học phân số",
    page_icon="🍕",
    layout="wide"
)

# ==========================
# GIAO DIỆN
# ==========================

st.markdown("""
<style>
.stApp {
    background-color: #FFF9F0;
}
h1 {
    color: #7952C7;
    text-align: center;
}
.question {
    background: white;
    padding: 20px;
    border-radius: 18px;
}
.stButton button {
    border-radius: 12px;
    background-color: #8B65D6;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🍕 BÉ VUI HỌC PHÂN SỐ")
st.markdown(
    "<h3 style='text-align:center;color:#E68A35'>"
    "🎮 Quiz Toán lớp 4 - Chinh phục phân số!"
    "</h3>",
    unsafe_allow_html=True
)

st.write("Hãy quan sát hình ảnh và chọn đáp án đúng nhé! 🌟")

# ==========================
# VẼ HÌNH PHÂN SỐ
# ==========================

def draw_fraction(kind, total, colored):

    fig, ax = plt.subplots(figsize=(5, 3.5))
    fig.patch.set_facecolor("#FFF9F0")
    ax.set_facecolor("#FFF9F0")

    colors = [
        "#FF7B89", "#FFD166", "#70C1B3",
        "#A78BFA", "#FF9F43", "#65A9F5",
        "#F28482", "#84DCC6", "#F6BD60",
        "#B8A1E3"
    ]

    if kind == "circle":
        for i in range(total):
            start = 90 - i * 360 / total
            end = 90 - (i + 1) * 360 / total

            color = colors[i % len(colors)] if i < colored else "#FFFFFF"

            ax.add_patch(
                Wedge(
                    (0, 0), 1,
                    end, start,
                    facecolor=color,
                    edgecolor="#70452B",
                    linewidth=2
                )
            )

        ax.add_patch(
            Circle((0, 0), 1, fill=False,
                   edgecolor="#70452B", linewidth=3)
        )

        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)

    elif kind == "bar":

        width = 1.8 / total

        for i in range(total):
            color = colors[i % len(colors)] if i < colored else "#FFFFFF"

            ax.add_patch(
                Rectangle(
                    (i * width, 0),
                    width, 0.8,
                    facecolor=color,
                    edgecolor="#70452B",
                    linewidth=2
                )
            )

        ax.set_xlim(-0.1, 1.9)
        ax.set_ylim(-0.2, 1.1)

    ax.axis("off")
    plt.tight_layout()

    return fig


# ==========================
# NGÂN HÀNG 10 CÂU HỎI
# ==========================

questions = [
    {
        "question": "🍕 Phân số nào chỉ phần bánh pizza đã tô màu?",
        "kind": "circle",
        "total": 4,
        "colored": 1,
        "options": ["1/4", "3/4", "1/3", "2/4"],
        "answer": "1/4",
        "explain": "Có 1 phần được tô màu trong tổng số 4 phần bằng nhau."
    },
    {
        "question": "🍰 Phân số nào chỉ phần bánh chưa tô màu?",
        "kind": "circle",
        "total": 8,
        "colored": 3,
        "options": ["3/8", "5/8", "4/8", "8/3"],
        "answer": "5/8",
        "explain": "Có 5 phần chưa tô màu trên tổng số 8 phần."
    },
    {
        "question": "🍫 Có bao nhiêu phần chocolate được tô màu?",
        "kind": "bar",
        "total": 6,
        "colored": 4,
        "options": ["2/6", "4/6", "6/4", "4/2"],
        "answer": "4/6",
        "explain": "Có 4 phần tô màu trong 6 phần bằng nhau."
    },
    {
        "question": "🍉 Phân số nào biểu thị phần đã tô màu?",
        "kind": "circle",
        "total": 5,
        "colored": 2,
        "options": ["2/5", "3/5", "5/2", "2/3"],
        "answer": "2/5",
        "explain": "Có 2 phần tô màu trên tổng số 5 phần."
    },
    {
        "question": "🎂 Mẫu số của phân số chỉ phần tô màu là bao nhiêu?",
        "kind": "circle",
        "total": 10,
        "colored": 7,
        "options": ["7", "3", "10", "17"],
        "answer": "10",
        "explain": "Mẫu số cho biết hình được chia thành 10 phần bằng nhau."
    },
    {
        "question": "🍕 Tử số của phân số chỉ phần được tô màu là bao nhiêu?",
        "kind": "circle",
        "total": 8,
        "colored": 3,
        "options": ["3", "5", "8", "11"],
        "answer": "3",
        "explain": "Tử số cho biết có 3 phần được tô màu."
    },
    {
        "question": "🍫 Phân số nào chỉ phần chocolate chưa tô màu?",
        "kind": "bar",
        "total": 5,
        "colored": 2,
        "options": ["2/5", "3/5", "5/2", "1/5"],
        "answer": "3/5",
        "explain": "Có 3 phần chưa tô màu trên tổng số 5 phần."
    },
    {
        "question": "🍰 Hình được chia thành 6 phần, tô màu 6 phần. Phân số là?",
        "kind": "circle",
        "total": 6,
        "colored": 6,
        "options": ["1/6", "5/6", "6/6", "6/5"],
        "answer": "6/6",
        "explain": "Cả 6 phần đều được tô màu nên phân số là 6/6."
    },
    {
        "question": "🍉 Hình nào biểu diễn 3 phần được tô màu trong 4 phần?",
        "kind": "circle",
        "total": 4,
        "colored": 3,
        "options": ["1/4", "2/4", "3/4", "4/4"],
        "answer": "3/4",
        "explain": "Có 3 phần được tô màu trong tổng số 4 phần."
    },
    {
        "question": "🌟 Hình được chia thành 8 phần, có 4 phần tô màu. Phân số là?",
        "kind": "bar",
        "total": 8,
        "colored": 4,
        "options": ["4/8", "8/4", "3/8", "5/8"],
        "answer": "4/8",
        "explain": "Có 4 phần tô màu trên tổng số 8 phần bằng nhau."
    }
]

# ==========================
# KHỞI TẠO TRÒ CHƠI
# ==========================

if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.done = False
    st.session_state.selected = None

# ==========================
# HIỂN THỊ KẾT QUẢ
# ==========================

if st.session_state.done:

    st.balloons()

    st.title("🏆 CHÚC MỪNG BẠN!")

    st.subheader(
        f"Bạn đạt {st.session_state.score}/100 điểm"
    )

    if st.session_state.score == 100:
        st.success("🌟 Xuất sắc! Bạn là siêu sao phân số!")
    elif st.session_state.score >= 70:
        st.success("👏 Rất tốt! Bạn đã hiểu về phân số.")
    elif st.session_state.score >= 50:
        st.info("💪 Khá tốt! Hãy cố gắng thêm nhé.")
    else:
        st.warning("📚 Bạn hãy luyện tập thêm nhé!")

    if st.button("🔄 CHƠI LẠI"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.done = False
        st.session_state.selected = None
        st.rerun()

# ==========================
# HIỂN THỊ CÂU HỎI
# ==========================

else:

    index = st.session_state.index
    q = questions[index]

    st.progress((index + 1) / len(questions))

    col1, col2 = st.columns(2)

    with col1:
        st.metric("⭐ Điểm số", st.session_state.score)

    with col2:
        st.metric("📝 Câu hỏi", f"{index + 1}/10")

    st.markdown("---")

    st.subheader(q["question"])

    # Hình minh họa
    fig = draw_fraction(
        q["kind"],
        q["total"],
        q["colored"]
    )

    st.pyplot(fig)
    plt.close(fig)

    st.write("👇 Hãy chọn đáp án đúng:")

    selected = st.radio(
        "Đáp án",
        q["options"],
        key=f"answer_{index}",
        index=None
    )

    if st.button("✅ KIỂM TRA ĐÁP ÁN"):

        if selected is None:
            st.warning("Bạn hãy chọn một đáp án nhé!")
        elif st.session_state.selected is None:

            st.session_state.selected = selected

            if selected == q["answer"]:
                st.session_state.score += 10
                st.success("🎉 Chính xác! Bạn được cộng 10 điểm!")
            else:
                st.error(
                    f"Chưa chính xác! Đáp án đúng là {q['answer']}"
                )

            st.info("💡 " + q["explain"])

    if st.session_state.selected is not None:

        if st.button("➡️ CÂU TIẾP THEO"):

            if index < len(questions) - 1:
                st.session_state.index += 1
                st.session_state.selected = None
            else:
                st.session_state.done = True

            st.rerun()

    st.markdown("---")
    st.caption("🌈 Cố gắng hoàn thành 10 câu hỏi để trở thành siêu sao phân số!")
