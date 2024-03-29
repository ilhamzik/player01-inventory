# Nama: Muhammad Ilham Zikri - 2206083533

# Kelas: PBP F

## Link Aplikasi untuk tugas 2
[player01-inventory by ilhamzik](https://player01-inventory.adaptable.app/main/)


<details>
<summary><b>Tugas 2</b></summary>

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

</details>

<details>
<summary><b>Tugas 3</b></summary>

### Perbedaan antara Form POST dan Form GET dalam Django

- **Form POST**: Data dikirim sebagai bagian dari permintaan HTTP POST. Biasanya digunakan ketika Anda ingin mengirim data yang sensitif, seperti kata sandi atau informasi pribadi. Data ini tidak terlihat di URL, dan dapat menyimpan data yang lebih besar. Menggunakan POST dalam Django biasanya digunakan untuk mengirim data yang akan diolah atau disimpan di server.

- **Form GET**: Data dikirim sebagai bagian dari URL dalam string query. Ini digunakan ketika Anda ingin berbagi data dengan mudah atau saat Anda ingin data yang dikirim dapat dilihat oleh pengguna atau disimpan di bookmark. Ini cocok untuk pencarian atau filter, tetapi data biasanya terbatas pada ukuran URL dan mungkin tidak cocok untuk data yang besar atau sensitif.

### Perbedaan antara XML, JSON, dan HTML dalam Konteks Pengiriman Data

- **XML (eXtensible Markup Language)**: XML adalah format untuk mendefinisikan data yang dapat disesuaikan dengan tag dan atribut sendiri. Biasanya digunakan untuk pertukaran data antar aplikasi yang berbeda atau untuk konfigurasi. Tidak memiliki format bawaan untuk representasi data yang lebih sederhana dibandingkan JSON. 

- **JSON (JavaScript Object Notation)**: JSON adalah format yang ringkas dan mudah dibaca untuk pertukaran data. Biasanya digunakan dalam pengembangan web modern dan API karena ringan dan mudah diuraikan oleh JavaScript. JSON sangat populer dalam pertukaran data antar aplikasi web karena kemampuannya yang baik dalam merepresentasikan data struktur beranak dan berulang.

- **HTML (HyperText Markup Language)**: HTML adalah bahasa markup yang digunakan untuk membuat konten web. Berbeda dengan XML dan JSON, HTML tidak digunakan untuk pertukaran data, melainkan untuk menampilkan konten di browser web. HTML memiliki struktur khusus untuk mengatur tampilan halaman web, sementara XML dan JSON lebih tentang representasi data.

### Mengapa JSON Sering Digunakan dalam Pertukaran Data antara Aplikasi Web Modern

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan:

- **Ringkas dan Mudah Dibaca**: JSON memiliki format yang ringkas dan mudah dibaca, yang membuatnya ideal untuk pertukaran data antar aplikasi web.

- **Kompatibel dengan JavaScript**: JSON adalah bagian integral dari JavaScript, sehingga mudah diuraikan dan digunakan oleh aplikasi web yang dibuat dengan JavaScript.

- **Mudah Diproses**: JSON memiliki struktur yang mudah diproses oleh berbagai bahasa pemrograman, sehingga dapat digunakan secara efisien dalam berbagai teknologi dan platform.

- **Dukungan untuk Struktur Data yang Kompleks**: JSON mendukung representasi struktur data yang kompleks, termasuk objek bersarang dan larik, yang sering digunakan dalam aplikasi web modern.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#### 1. Buat File `forms.py`

Pertama, kita akan membuat file `forms.py` yang akan berfungsi sebagai badan input dari pengguna. File ini akan berisi variabel `model` yang sesuai dengan model yang sudah ada dalam file `models.py`.

#### 2. Modifikasi `views.py`

Kemudian, pada file `views.py`, kita akan menambahkan fungsi baru bernama `create_product` untuk membuat produk berdasarkan input yang diberikan oleh pengguna. Selain itu, kita akan mengubah bagian `show_main` di dalam file `views.py` agar dapat menyimpan setiap produk yang ditambahkan.

#### 3. Buat File `create_product.html`

Selanjutnya, kita akan membuat file `create_product.html` sebagai tampilan untuk menginputkan produk. File ini akan memiliki tombol yang akan mengarahkan pengguna ke halaman input produk. Ketika produk telah ditambahkan, pengguna akan kembali ke layar utama dengan tampilan produk yang telah diinputkan.

#### 4. Routing

Selanjutnya, kita akan melakukan routing untuk fungsi-fungsi yang telah dibuat sebelumnya. Pada file `urls.py`, tambahkan import yang diperlukan, lalu tambahkan path-path baru untuk memanggil fungsi-fungsi tersebut melalui URL. Berikut contohnya:

```python
from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/int:id/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/int:id/', views.show_json_by_id, name='show_json_by_id'),
    # ...
]
```


Selanjutnya, inilah hasil screenshot saya pada postman
-html
<img src="/Assets//html.jpg">
-xml
<img src="/Assets//xml.jpg">
-xml by id
<img src="/Assets//xml by id.jpg">
-json
<img src="/Assets//json.jpg">
-json by id
<img src="/Assets//json by id.jpg">

</details>

<details>
<summary><b>Tugas 4</b></summary>

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
- **Definisi:** Django UserCreationForm adalah formulir bawaan yang disediakan oleh Django untuk membuat formulir pendaftaran pengguna. Formulir ini mempermudah pengembang dalam menciptakan halaman pendaftaran pengguna yang meminta informasi seperti nama pengguna, kata sandi, dan alamat email. 
- **Kelebihan:** Formulir ini mudah digunakan, terintegrasi dengan baik dalam sistem otentikasi Django, serta mengelola validasi data pendaftaran dengan baik. Selain itu, formulir ini dapat disesuaikan sesuai kebutuhan aplikasi Anda.
- **Kekurangan:** Batas utama adalah keterbatasan dalam penyesuaian desain. Jika Anda membutuhkan informasi tambahan selain yang disediakan dalam formulir ini, Anda perlu memodifikasinya atau membuat formulir pendaftaran khusus.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
**Autentikasi** adalah langkah verifikasi identitas pengguna, seperti memastikan bahwa nama pengguna dan kata sandi yang dimasukkan sesuai dengan yang terdaftar di sistem. Ini adalah tahap awal untuk memeriksa apakah pengguna adalah yang mereka klaim.
**Otorisasi** adalah tentang mengontrol hak akses pengguna setelah mereka berhasil terautentikasi. Ini menentukan tindakan atau sumber daya apa yang dapat diakses atau dikelola oleh pengguna yang telah terautentikasi.
- **Mengapa keduanya penting:** Autentikasi memastikan bahwa hanya pengguna yang sah yang diberikan akses ke aplikasi, sementara otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan sesuai dengan hak akses yang telah ditetapkan untuk mereka.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
**Cookies** adalah data kecil yang disimpan di perangkat klien (biasanya di browser). Mereka digunakan untuk menyimpan informasi sesi atau preferensi pengguna saat berinteraksi dengan situs web. Cookies memungkinkan server web untuk mengenali pengguna ketika mereka kembali ke situs.
- Django menggunakan cookies secara default untuk mengelola sesi pengguna. Dalam setiap interaksi dengan situs web Django, informasi sesi seperti ID sesi disimpan dalam cookie di perangkat pengguna. Ini memungkinkan Django untuk menjaga keberlanjutan sesi antar permintaan dan memberikan pengalaman yang personal kepada pengguna.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
**Keamanan secara default**: Saat diimplementasikan dengan baik, penggunaan cookies dalam pengembangan web aman secara default. Django, sebagai kerangka kerja yang solid, telah menerapkan langkah-langkah keamanan untuk melindungi cookies dan data sesi pengguna.
**Risiko Potensial**: Risiko utama terkait penggunaan cookies adalah serangan seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF), yang dapat memanfaatkan cookies jika tidak diatasi dengan benar. Oleh karena itu, pengembang harus memastikan aplikasi mereka mengikuti praktik keamanan yang baik, termasuk menghindari penyimpanan informasi sensitif dalam cookies dan mengamankan cookies dengan atribut seperti HttpOnly dan Secure.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- pertama-tama tentu saya mengimplementasikan fungsi registrasi, login, dan logout (dan bonus yaitu update amount dan delete item). Hal ini saya mulai dengan cara mengimport hal-hal yang diperlukan untuk membuat fungsi-fungsi tersebut pada views, seperti redirect, UserCreationForm, messages, authenticate, login, logout, dan Http404.

- setelah itu, saya pindah ke direktori templates yang berada pada direktori main untuk membuat file html baru yang menampilkan halaman register bernama register.html . file ini saya isi dengan form registrasi yang akan menerima input user dan mengirimkannya melalui POST.

- selanjutnya, saya membuat file html baru untuk tampilan login pengguna bernama login.html . File ini akan menerima input username dan login user, lalu mengirimkan ke POST dan menampilkan pesan apabila login gagal. Saya juga menaruh tombol yang menghubungkan ke halaman registrasi yang sudah saya hubungkan URLnya.

- tidak lupa juga untuk menambahkan tombol logout pada main.html.

- saya juga memodifikasi beberapa bagian untuk menyelesaikan soal bonus. seperti memodifikasi tampilan-tampilan pada file html yang saya miliki (menambah tombol-tombol).

- setelah itu juga saya mencoba berjalannya aplikasi saya, saya membuat beberapa dummy user dan dummy data(sesuai yang diminta soal).

- selanjutnya saya menghubungkan user yang saya punya dengan item-item yang didaftarkan mereka. caranya adalah dengan mengimport user pada models.py . hal itu membuat saya bisa mengautentikasi user serta memberinya hak untuk memodifikasi inventorynya. saya menambahkan kode `` user = models.ForeignKey(User, on_delete=models.CASCADE) `` yang memungkinkan saya untuk menghapus model dengan foreign key tsb.

- saya juga menambahkan sesuatu dalam fungsi create_file dalam views.py . saya mengisinya dengan : 
     product = form.save(commit=False)
     product.user = request.user
     product.save()
saya sedikit mengubah fungsi itu untuk memungkinkan saya dalam menghubungkan user yang sedang login dengan data dari form.

- tidak lupa juga saya lakukan migrations

- selanjutnya saya membuat tampilan yang memberikan keterangan tambahan dari pengguna seperti last login. saya mengimport datetime pada views.py lalu memodifikasi login_user dengan set cookie yang akan saya buat yaitu last login. tidak lupa menambahkannya sebagai context di show_main. nah, pada fungsi logout saya menghapus cookie last login tersebut.

- tidak lupa juga menambahkannya pada main.html untuk ditampilkan.

</details>

<details>
<summary><b>Tugas 5</b></summary>

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
- Elemen Selector
Manfaat: Selector ini digunakan untuk memilih semua elemen dengan tipe tertentu pada halaman web. Misalnya, jika kita menggunakan p sebagai selector, maka semua elemen <p> pada halaman web akan dipilih. 
kapan menggunakannya: Saat ingin menggunakan gaya yang sama ke semua elemen dengan jenis tertentu.
- Class Selector
Manfaat: Selector ini memungkinkan kita memilih elemen dengan nama kelas tertentu. Class selectors berguna ketika kita ingin menerapkan gaya tertentu pada beberapa elemen yang memiliki kelas yang sama.
Kapan menggunakannya: Saat ingin memberikan gaya yang sama pada beberapa elemen dengan karakteristik atau fungsi yang serupa, tanpa memperhatikan tipe elemennya.
- Type Selector
Manfaat: digunakan untuk menargetkan elemen HTML berdasarkan nama tag-nya.
Kapan menggunakannya: ketika kita ingin menerapkan gaya pada semua instansi elemen HTML tertentu di halaman. 

2. Jelaskan HTML5 Tag yang kamu ketahui.
- header: Digunakan untuk mendefinisikan bagian kepala dokumen atau bagian atas halaman web.
- nav: Menunjukkan bagian dari dokumen yang berisi tautan navigasi, seperti menu.
- main: Menandai konten utama halaman yang unik dan tidak berulang. Hanya boleh ada satu elemen main dalam satu halaman.

3. Jelaskan perbedaan antara margin dan padding.
- Margin: Margin adalah ruang di luar batas elemen. Ini menciptakan jarak antara elemen tersebut dan elemen lain.
- Padding: Padding adalah ruang di dalam batas elemen, antara batas elemen dan kontennya.
Perbedaan utama adalah bahwa margin menciptakan ruang di luar elemen (di antara elemen tersebut dan elemen lainnya), sedangkan padding menciptakan ruang di dalam elemen (antara konten elemen dan batasnya). 

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS adalah framework CSS utility-first yang memberikan kendali tinggi kepada pengembang dalam desain tata letak. Dibandingkan dengan Bootstrap, Tailwind memungkinkan pengguna untuk membuat tampilan yang sangat disesuaikan dengan menggabungkan kelas-kelas utilitas yang spesifik. Tailwind cocok untuk proyek yang memerlukan kreativitas tinggi dan kebebasan desain. Di sisi lain, Bootstrap menyediakan komponen UI yang sudah dirancang dengan baik, membuatnya cpcok untuk proyek dengan batasan waktu dan membutuhkan desain responsif yang cepat dan mudah tanpa banyak konfigurasi. Penggunaan keduanya tergantung pada tingkat kontrol dan fleksibilitas yang diinginkan oleh pengembang dalam proyek mereka.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama, saya mencari tau tentang bootstrap melalui link referensi pada naskah tutorial.
Setelah itu, saya mencoba untuk melihat-lihat referensi website serta cara mereka membuat tampilan seperti itu.
Lalu, saya modifikasi tampilan saya dengan modal riset yang sudah saya lakukan sedemikian rupa.
</details>

<details>
<summary><b>Tugas 6</b></summary>

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming melibatkan eksekusi kode secara berurutan, satu per satu, dengan menunggu setiap operasi selesai sebelum melanjutkan ke operasi berikutnya. Sebaliknya, asynchronous programming memungkinkan beberapa operasi berjalan bersamaan tanpa menunggu operasi selesai, meningkatkan efisiensi dan responsivitas program terhadap input eksternal.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming mengartikan pendekatan di mana program merespons kejadian atau event yang terjadi, seperti klik mouse atau pengiriman data melalui AJAX. Program menantikan kejadian tersebut dan memberikan respons dengan menjalankan fungsi atau aksi yang sesuai.
Contoh implementasinya dalam tugas ini adalah menggunakan event-driven untuk menanggapi klik tombol "Delete" pada item dalam aplikasi web. Ketika tombol "Delete" ditekan, program akan merespons event tersebut dengan menjalankan fungsi AJAX untuk menghapus item tanpa memuat ulang halaman secara keseluruhan.

3. Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronous programming pada AJAX memungkinkan operasi jaringan berjalan tanpa menghentikan eksekusi program utama, meningkatkan responsivitas aplikasi dengan memungkinkannya melanjutkan tugas lainnya selama operasi jaringan berlangsung.

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API adalah bagian dari standar web modern, lebih ringan, promise-based, dan direkomendasikan untuk aplikasi web modern. jQuery adalah pustaka populer dengan antarmuka yang mudah dan kompatibilitas browser yang baik. Pilihan tergantung pada kebutuhan proyek, dengan Fetch API disarankan untuk proyek-proyek baru karena kelebihannya dalam kecepatan dan responsivitas. Namun, jQuery tetap relevan untuk proyek dengan kebutuhan kompatibilitas tinggi terhadap browser lama.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama-tama membuat fungsi get_item_json pada views.py untuk mengambil data dalam bentuk JSON. lalu membuat fungsi untuk menambahkan produk menggunakan AJAX dimulai dengan mengimport csrf_exempt dan membuat fungsi baru bernama add_item_ajax.
- Nah, pada main.html kita ambil item dengan fetch API dengan menambahkan tag block script di akhir kode HTML dan membuat fungsi asynchronous getItems.
- Membuat fungsi asynchronous refreshProducts() pada blok script untuk memunculkan cards menggunakan AJAX dan merefresh data dari item serta mengupdate informasi jumlah item yang tersimpan secara asynchronous.
- lalu membuat fungsi pada bagian script untuk menambahkan Item (onclick).
- Membuat fungsi untuk menghapus item menggunakan AJAX pada views.py bernama delete_item_ajax yang memiliki parameter berupa id dari item yang akan dihapus dan menambahkan fungsi deleteProduct(id) pada bagian script di main.html untuk menghapus item dengan AJAX
- Menambahkan button pada cards untuk menghapus item menggunakan AJAX pada main.html dan menambahkan atribut onclick="deleteItem(${item.pk})" untuk memanggil fungsi deleteItem saat button di click.
- terakhir, melakukan perintah collecstatic dengan melakukan mapping untuk output file static ke directory yang sesuai dengan memodifikasi bagian STATIC_URL dan STATIC_ROOT pada settings.py. lalu menjalankan perintah collectstatic pada terminal :
</details>