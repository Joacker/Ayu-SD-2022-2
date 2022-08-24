package main

import (
	"fmt"
	"net/http"

	"github.com/Joacker/Ayu1/backend/routes"
	"github.com/gorilla/mux"
)

func main() {

	r := mux.NewRouter()
	r.HandleFunc("/", routes.HomeHandler)
	r.HandleFunc("/items", routes.GetItemsHandler).Methods("GET")
	r.HandleFunc("/items/{Id}", routes.GetItemsHandler).Methods("GET")

	fmt.Println("Hello World 3")
	http.ListenAndServe(":3000", r)

}
