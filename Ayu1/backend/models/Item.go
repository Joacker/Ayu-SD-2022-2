package models

import "gorm.io/gorm"

type Item2 struct {
	gorm.Model

	Id       int     `json:"Id"`       // ID is the primary key
	Name     string  `json:"Name"`     // Title is the item title
	Price    float64 `json:"Price"`    // Done is the item done status
	Category string  `json:"Category"` // Category is the item category
	Count    int     `json:"Count"`    // Count is the item count
}
