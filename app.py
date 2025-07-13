import streamlit as st
import math
import pandas as pd
import plotly.express as px

# 🎨 Konfigurasi halaman
st.set_page_config(page_title="📦 EOQ Calculator", layout="wide")

# 🚀 Judul Aplikasi
st.title("📦 EOQ Calculator — Economic Order Quantity")
st.markdown("""
Selamat datang di aplikasi EOQ!  

EOQ adalah metode matematika untuk menentukan jumlah pemesanan optimal yang meminimalkan total biaya persediaan, yaitu biaya pemesanan dan biaya penyimpanan.
Dengan EOQ, perusahaan dapat membuat keputusan yang efisien & ekonomis dalam mengelola persediaan barang.

💼 Tentukan jumlah pemesanan optimal untuk meminimalkan total biaya persediaan.

---
""")

# 📖 Tampilkan Rumus EOQ
st.subheader("📐 Rumus EOQ")
st.latex(r"""
EOQ = \sqrt{\frac{2DS}{H}}
""")
st.markdown("""
di mana:  
- \(D\) = Permintaan tahunan  
- \(S\) = Biaya pemesanan per order  
- \(H\) = Biaya penyimpanan per unit per tahun
""")

# 📋 Sidebar: Input
with st.sidebar:
    st.header("📝 Input Parameter")
    D = st.number_input("📈 Permintaan Tahunan (unit)", min_value=1.0, value=1000.0)
    S = st.number_input("💰 Biaya Pemesanan per Order (Rp)", min_value=0.0, value=50000.0)
    H = st.number_input("🏠 Biaya Penyimpanan/unit/tahun (Rp)", min_value=0.0, value=2000.0)
    st.markdown("---")
    st.caption("💡 Isi nilai di atas lalu lihat hasilnya!")

# 🧮 Perhitungan EOQ
EOQ = math.sqrt((2 * D * S) / H)
jumlah_pesanan = D / EOQ
total_biaya = (D / EOQ) * S + (EOQ / 2) * H

# 📊 Output
st.subheader("📊 Hasil Perhitungan")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔷 EOQ (unit)", f"{EOQ:.2f}")
with col2:
    st.metric("🔷 Jumlah Pesanan per Tahun", f"{jumlah_pesanan:.2f}")
with col3:
    st.metric("🔷 Total Biaya Persediaan (Rp)", f"{total_biaya:,.2f}")

st.markdown("---")

# 📈 Grafik Biaya Total
order_quantities = [i for i in range(1, int(EOQ*2))]
costs = [(D/q)*S + (q/2)*H for q in order_quantities]

df = pd.DataFrame({
    "Order Quantity": order_quantities,
    "Total Cost": costs
})

fig = px.line(df, x="Order Quantity", y="Total Cost", 
              title="📉 Kurva Total Biaya Persediaan",
              labels={"Order Quantity": "Jumlah Order (X)", "Total Cost": "Total Biaya (Rp) (Y)"},
              color_discrete_sequence=["#4a90e2"])
fig.update_layout(
    plot_bgcolor="#f0f8ff",
    paper_bgcolor="#f9f9f9",
    font_color="#333"
)
fig.add_vline(x=EOQ, line_dash="dash", line_color="red",
              annotation_text=f"EOQ ≈ {EOQ:.0f}", annotation_position="top right")

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
- Sumbu X (Horizontal) : jumlah order, ini menunjukan jumlah unit yang dipesan per siklus

- Sumbu Y (Vertikal) : Total Biaya (Rp), Ini menunjukan total biaya persediaan untuk masing-masing jumlah order

- Kurva Biru = Total biaya persediaan yang berubah sesuai dengan jumlah unit per pemesanan

Jumlah order terlalu kecil => biaya pemesanan tinggi

Jumlah order terlalu besar => biaya penyimpanan tinggi

- Garis putus-putus merah : meunjukan titik minimum dari kurva biaya => EOQ
""")

st.markdown("""
---
### 📖 Tentang EOQ
EOQ membantu perusahaan untuk meminimalkan biaya total persediaan dengan menentukan jumlah pemesanan optimal.

📦 Contoh Kasus EOQ

🔷 Sebuah perusahaan toko buku menjual kertas cetak untuk percetakan.

🔷 Data tahunan:

- Permintaan tahunan (D) = 12.000 unit

- Biaya pemesanan per order (S) = Rp 50.000

- Biaya penyimpanan per unit per tahun (H) = Rp 2.000



🧮 Tanpa EOQ:
Jika perusahaan memesan kertas 1.000 unit sekali pesan, berarti dalam setahun mereka harus pesan:

12.000/1.000=12 kali

- Total biaya pemesanan = 12 × 50.000 = 𝑅𝑝.600.000

- Rata-rata persediaan = 1.000/2 = 500 unit

- Total biaya penyimpanan = 500 × 2.000 = Rp1.000.000  

- Total biaya = Rp 600.000 + Rp 1.000.000 = Rp 1.600.000



Rumus EOQ
""")

st.latex(r"""EOQ = \sqrt{\frac{2DS}{H}}""")

st.latex(r"""EOQ = \sqrt{\frac{2 x 12.000 x 50.000}{2.000} = \sqrt{\frac{600.000} = 774,6}}""")

st.markdown("""
            EOQ optimal ≈ 775 unit per pesanan

Berarti dalam setahun mereka akan pesan: 12.000/775≈15.5≈16 kali

- Total biaya pemesanan = 16 × 50.000=Rp800.000

- Rata-rata persediaan = 775/2 ≈ 388 unit

- Total biaya penyimpanan = 388 × 2.000 ≈ Rp776.000

-  Total biaya = Rp 800.000 + Rp 776.000 ≈ Rp 1.576.000


📉 Perbandingan:

Strategi :
- pesan 1.000 unit tiap kali total biaya persediaan: Rp.1.600.000

- pesan dengan  EOQ (775): Rp.1.576.000


Dengan EOQ perusahaan menghemat biaya sekitar Rp.24.000 per tahun di banding jika asal memesan 1.000 unit.
""")



st.caption("📄 Oleh: Mohamad Sony hidayatullah | 📧 sonyhidayatullah55@gmail.com | 🔗 SonSyntax")
