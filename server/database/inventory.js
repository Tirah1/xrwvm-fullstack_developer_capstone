/* jshint esversion: 6 */
const mongoose = require('mongoose');

const Schema = mongoose.Schema;

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

module.exports = mongoose.model('dealerships', dealerships);

const { Int32 } = require('mongodb');
const mongoose = require('mongoose');

const Schema = mongoose.Schema;

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
bodyType: {
    type: String,
    required: true
  },
year: {
    type: Number,
    required: true
  },
mileage: {
    type: Number,
    required: true
  }
});

module.exports = mongoose.model('cars', cars);
