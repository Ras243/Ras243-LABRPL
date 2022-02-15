mahasiswa = {
    'nama' : 'Nurrasuli',
    'asal' : 'Pasangkayu'
}

print('Nama awal : ',mahasiswa.get('nama'))
mahasiswa['nama'] = "Rascoding"
print(f"Nama akhir : {mahasiswa.get('nama')}")