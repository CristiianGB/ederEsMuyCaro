import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);
  
  return (
    <div className="text-center mt-5">
		{ store.products?store.products.map((product, i) => (
	 		<div className="card" key={product.product_id} style={{width: "18rem"}}>
	 		<img className="card-img-top" src="..." alt="Card image cap"/>
	 		<div className="card-body">
	 			 <h5 className="card-title">{product.product_name}</h5>
	 		  <p className="card-text">price: {product.product_price}€</p>
	 		  <a href="#" className="btn btn-primary">Go somewhere</a>
	 		</div>
	   </div>
	 	)):"ederesunbombong"
	 	
	}
    </div>
  );
};
