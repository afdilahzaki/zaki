from django.shortcuts import render, redirect 
from .models import Mahasiswa
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def blog_pribadi(request):
    return render(request, 'mahasiswa/blog.html')

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})

def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
     }
    return render(request, 'mahasiswa/index.html', context)

def tambah_mahasiswa(request):    
    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']
        programstudi = request.POST['programstudi']
        angkatan = request.POST['angkatan']

        # Validasi semua field wajib diisi
        if not nim or not nama or not programstudi or not angkatan:
            messages.error(request, 'Semua field wajib diisi!')
            return redirect('tambah_mahasiswa')

        # Cek apakah NIM sudah terdaftar
        if Mahasiswa.objects.filter(nim=nim).exists():
            messages.error(request, f'NIM {nim} sudah terdaftar!')
            return redirect('tambah_mahasiswa')

        # Simpan data baru
        Mahasiswa.objects.create(
            nim=nim, 
            nama=nama, 
            programstudi=programstudi, 
            angkatan=angkatan
        )

        messages.success(request, 'Mahasiswa berhasil ditambahkan!')
        return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/tambah.html')

def edit_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    if request.method == 'POST':
        mhs.nim = request.POST['nim']
        mhs.nama = request.POST['nama']
        mhs.programstudi = request.POST['programstudi']
        mhs.angkatan = request.POST['angkatan']
        mhs.save()
        return redirect('daftar_mahasiswa')
    return render(request, 'mahasiswa/edit.html', {'mhs': mhs})

def hapus_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    mhs.delete()
    return redirect('daftar_mahasiswa')
