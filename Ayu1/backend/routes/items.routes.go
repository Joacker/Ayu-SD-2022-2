package routes

import (
	"encoding/json"
	"net/http"

	"github.com/Joacker/Ayu1/backend/db"
	"github.com/Joacker/Ayu1/backend/models"
)

func GetItemsHandler(w http.ResponseWriter, r *http.Request) {
	db.DBConnection()

	db.DB.AutoMigrate(models.Items{})
	db.DB.Find(&models.Items{})
	json.NewEncoder(w).Encode(models.Items{})

}

func GetItemHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Get Item"))
}
