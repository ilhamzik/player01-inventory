# Nama: Muhammad Ilham Zikri - 2206083533

# Kelas: PBP F

## Link Aplikasi untuk tugas 2
[player01-inventory by ilhamzik](https://player01-inventory.adaptable.app/main/)

## Jawaban dari soal esai yang diberikan

### pertanyaan nomor 1 - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Pertama-tama saya membuat project Django yang baru karena soal meminta kita untuk itu dan tidak boleh memakai project yang kita buat saat tutorial, caranya:
    - Saya mengaktifkan virtual environment Django dengan cara mengirim kode "python -m venv env" dan "env\Scripts\activate" pada terminal.
    - Lalu saya mengikuti langkah dari tutorial yaitu membuat file requirements.txt yang akan diisi oleh dependencies yang saya perlukan(dan akan diinstall).
    - Lalu saya jalankan command "pip install -r requirements.txt" untuk meminta proses instalasi dependencies yang sudah saya cantumkan untuk dijalani.
    - Pada file settings.py, saya memperbolehkan semua orang untuk menjadi host dengan memberi "*"
    - tidak lupa menambah .gitignore agar file yang tidak perlu bisa diabaikan
- Selanjutnya saya membuat aplikasi bernama 'main' dengan menjalankan command "python manage.py startapp main"
- Lalu, saya membuat folder baru bernama 'templates' yang selanjutnya saya isi dengan 'main.html' sebagai penampil aplikasi nantinya.
- Selanjutnya saya mengatur alur url agar file yang ada bisa saling terhubung. caranya dengan menambah file baru yaitu urls.py di dalam folder main dan menambahkan 'path('', show_main, name='show_main)'
- Lalu, pada file urls.py yang berada pada folder player01_inventory menambahkan path baru yaitu 'main' pada url patterns.
- Nah, setelah set up awal, barulah saya bisa mengikuti instruksi soal yang meminta kami membuat atribut tertentu pada model. saya menambah atribut pada models.py sesuai dengan ketentuan soal dan ditambahkan sedikit.
- Selanjutnya, pindah ke views.py dan buat function yang mewakilkan atribut-atribut pada models.py tadi agar bisa di return pada main.html nantinya untuk ditampilkan secara statis.
- Setelah selesai dengan file dan isinya, kita bisa melakukan push ke repository github.
- Saat github sudah menerima kiriman update file tadi, kita bisa melakukan deploy di adaptable dengan cara menghubungkan repository github kita.

### pertanyaan nomor 2 - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src="/Assets//bagan.jpg">

### pertanyaan nomor 3 - Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment membantu kita dalam mengisolasi suatu project dan membuat depedencies yang kita pakai untuk project tersebut tidak tercampur dengan project lain (mungkin terjadi). Sebenarnya masih bisa membuat aplikasi web basis Django tanpa virtual environment. tetapi, akan beresiko karena project tak terisolasi.

### pertanyaan nomor 4 - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC atau Model-View-Controller merupakan arsitektur yang membagi tiga komponennya menjadi model, view, dan controller.    
- MVT atau Model-View-Template merupakan arsitektur yang memisahkan komponen utama dari sebuah aplikasi.
- MVVM atau Model-View-ViewModel merupakan arsitektur yang memisahkan antara logika dan model melalui ViewModel.

Perbedaan mencolok pada ketiga aplikasi tersebut adalah kegunaan dan fokus kerjanya. MVC lebih terfokus pada pengendalian alur kerja aplikasi, MVT menggunakan sebuah template untuk menggabungkan data dan tampilan, dan MVVM lebih fokus terhadap pemisahan antara tampilan, logika, dan data.