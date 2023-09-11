import scipy.io

# Anna tiedoston polku
mat_file_path = 'tiedosto.mat'

# Lue .mat-tiedosto
mat_data = scipy.io.loadmat(mat_file_path)

# Tarkista, mitä muuttujia tiedostossa on
# Esimerkiksi, jos datavektori on nimellä "data", voit käyttää seuraavaa:
if 'data' in mat_data:
    data_vector = mat_data['data']
    print("Data-vektori:")
    print(data_vector)
else:
    print("Tiedostossa ei ole 'data'-muuttujaa.")