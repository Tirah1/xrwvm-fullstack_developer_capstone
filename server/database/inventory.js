/* jshint esversion: 6 */
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Dealerships Schema
const dealerships = new Schema({
  id: {
    type: Number,
    required: true,
  },
  city: {
    type: String,
    required: true
  },
  state: {
    type: String,
    required: true
  },
  address: {
    type: String,
    required: true
  },
  zip: {
    type: String,
    required: true
  },
  lat: {
    type: String,
    required: true
  },
  long: {
    type: String,
    required: true
  },
  short_name: {
    type: String,
  },
  full_name: {
    type: String,
    required: true
  }
});

// Cars Schema
const cars = new Schema({
  dealer_id: {
    type: Number,
    required: true
  },
  make: {
    type: String,
    required: true
  },
  model: {
    type: String,
    required: true
  },
  year: {
    type: Number,
    required: true
  },
  price: {
    type: Number,
    required: true
  },
  mileage: {
    type: Number,
    required: true
  },
  color: {
    type: String,
  },
  vin: {
    type: String,
    required: true,
    unique: true
  }
});

// Export the models
const Dealership = mongoose.model('Dealership', dealerships);
const Car = mongoose.model('Car', cars);

module.exports = { Dealership, Car };
