package routes

import (
	"encoding/json"
	"net/http"

	"github.com/Joacker/Ayu1/backend/db"
	"github.com/Joacker/Ayu1/backend/models"
)

func GetItemsHandler(w http.ResponseWriter, r *http.Request) {
	db.DBConnection()
	var items []models.Items
	db.DB.AutoMigrate(items)
	db.DB.Find(&items)
	json.NewEncoder(w).Encode(&items)

}

func GetItemHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Get Item"))
}
