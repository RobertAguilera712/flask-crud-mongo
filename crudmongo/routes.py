from flask import render_template, url_for, flash, redirect, request
from crudmongo.forms import PetForm
from crudmongo import app, mongo
from bson.objectid import ObjectId


@app.route('/', methods=['GET', 'POST'])
def home():
    form = PetForm()
    pets = mongo.db.pets.find()
    action = url_for('home')
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get('name')
            species = request.form.get('species')
            breed = request.form.get('breed')
            pet = {"name": name, "species": species, "breed": breed}
            mongo.db.pets.insert_one(pet)
            flash('The pet has been saved', 'success')
            return redirect(url_for('home'))
    return render_template('index.html', form=form, pets=pets, action=action)

@app.route('/modify/<string:id>', methods=['GET', 'POST'])
def modify(id):
    form = PetForm()
    pet = mongo.db.pets.find_one({"_id": ObjectId(id)})
    pets = mongo.db.pets.find()
    action = url_for('modify', id=id)
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get('name')
            species = request.form.get('species')
            breed = request.form.get('breed')
            pet = {"name": name, "species": species, "breed": breed}
            mongo.db.pets.update_one({"_id": ObjectId(id)}, {"$set": pet})
            flash('The pet has been modified', 'warning')
            return redirect(url_for('home'))
    form.name.data = pet['name']
    form.species.data = pet['species']
    form.breed.data = pet['breed']
    return render_template('index.html', form=form, pets=pets, action=action)
       
       
@app.route('/delete', methods=['POST'])
def delete():
    id = request.form.get('id')
    mongo.db.pets.delete_one({"_id": ObjectId(id)})
    flash('The pet has been deleted', 'danger')
    return redirect(url_for('home'))