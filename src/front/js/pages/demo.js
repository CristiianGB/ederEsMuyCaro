import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Demo = () => {
	const { store, actions } = useContext(Context);
	const [price, setPrice] = useState("")
	const [name, setName] = useState("")

	
		
  return (
    <div className="container">
      <div>
        <input type="text" onChange={(e)=>{setName(e.target.value)}} value={name} placeholder="name"></input>
        <input type="text" onChange={(e)=>{setPrice(e.target.value)}} value={price} placeholder="price"></input>
		<button onClick={()=>{actions.createProducts(price, name)}}>create product</button>
      </div>
      <br />
      <Link to="/">
        <button className="btn btn-primary">Back home</button>
      </Link>
    </div>
  );
};
