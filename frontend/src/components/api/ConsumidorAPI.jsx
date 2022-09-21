import React, {useState,useEffect} from "react";
import API from './api';

export default() => {
    const [Titulo,setTitulo] = useState();

   
    useEffect(() => {
        API.get("/?format=json").then((response) => setTitulo(response.data))
    });
    console.log(typeof(Titulo))
    return(
        <div>
            {Titulo?.NomeTarefa}
        </div>
    )
}