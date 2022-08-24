package routes

import "net/http"

func GetItemsHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Get Items"))
}

func GetItemHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Get Item"))
}
