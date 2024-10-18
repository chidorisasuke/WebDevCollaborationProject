# app/routes.py
from flask import request, render_template, redirect, url_for, flash
from app import app

@app.route('/')
def index():
    return render_template('index.html')


#For static result
# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about_new.html', members=member_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    return "Form submitted successfully!"

'''
Metode "GET" digunakan untuk mengambil data dari server. Permintaan "GET" digunakan ketika ingin mengambil atau membaca informasi dari server, seperti membuka halaman web atau mengambil data dari server. Permintaan "GET" mengirimkan data dalam URL dan umumnya tidak digunakan untuk mengirim data sensitif seperti kata sandi.

Metode "POST" digunakan untuk mengirim data ke server untuk diproses. Ini adalah metode yang umum digunakan ketika ingin mengirim data dari formulir HTML atau permintaan yang memerlukan perubahan pada server, seperti mengirim komentar atau mengirim pesanan belanjaan. Data dikirim dalam badan permintaan (request body) dan umumnya digunakan untuk mengirim data sensitif.
'''

@app.route('/edit/<int:member_id>', methods=['GET', 'POST'])
def edit(member_id):
    if request.method == 'POST':
        updated_name = request.form.get('name')
        updated_university = request.form.get('university')
        updated_domicile = request.form.get('domicile')
        updated_email = request.form.get('email')

        # Update the member data
        member_data[member_id] = {
            'name': updated_name,
            'university': updated_university,
            'domicile': updated_domicile,
            'email': updated_email
        }
        
        flash(f'Anggota dengan ID {member_id} berhasil diperbarui!', 'success')
        return redirect(url_for('about'))
    
    member = member_data.get(member_id)
    
    return render_template('edit.html', member=member)
        
member_data = {
    1: {
        'name': 'Rayhan Gading',
        'university': 'Universitas pembangunan nasional "veteran" jawa timur X',
        'domicile': 'Surabaya',
        'email': 'rayhangading2@gmail.com'
    },
    2: {
        'name': 'Robert William',
        'university': 'Universitas Padjadjaran',
        'domicile': 'Sumedang',
        'email': 'robertw0112@gmail.com'
    },
    3: {
        'name': 'Siti Arwiyah',
        'university': 'Universitas Terbuka',
        'domicile': 'Bogor',
        'email': 'sitiarwiyah94@gmail.com'
    },
    4: {
        'name': 'Wildan Miladji',
        'university': 'Universitas Sangga Buana',
        'domicile': 'Bandung',
        'email': 'wildanmiladji53@gmail.com'
    },
    5: {
        'name': 'Yahya Bachtiar',
        'university': 'Universitas Airlangga',
        'domicile': 'Surabaya',
        'email': 'yahyabachtiar03@gmail.com'
    }
}