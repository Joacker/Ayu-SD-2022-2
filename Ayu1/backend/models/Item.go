package models

import "gorm.io/gorm"

type Items struct {
	gorm.Model

	Id       int     `gorm:"not null"` // ID is the primary key
	Name     string  `gorm:"not null"` // Title is the item title
	Price    float64 // Done is the item done status
	Category string  // Category is the item category
	Count    int     // Count is the item count
}
