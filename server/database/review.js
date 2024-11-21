/* jshint esversion: 6 */
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Dealerships schema
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

// Reviews schema
const reviews = new Schema({
  id: {
    type: Number,
    required: true,
  },
  name: {
    type: String,
    required: true
  },
  dealership: {
    type: Number,
    required: true,
  },
  review: {
    type: String,
    required: true
  },
  purchase: {
    type: Boolean,
    required: true
  },
  purchase_date: {
    type: String,
    required: true
  },
  car_make: {
    type: String,
    required: true
  },
  car_model: {
    type: String,
    required: true
  },
  car_year: {
    type: Number,
    required: true
  },
});

// Export both models
module.exports = {
  Dealership: mongoose.model('dealerships', dealerships),
  Review: mongoose.model('reviews', reviews)
};
