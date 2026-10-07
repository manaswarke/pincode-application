<html>
          <head>
                    <title> Pincode Info App </title>
                    <style> 
                            * {
                                   font-size: 50px;
                                   text-align:center;
                            
                            }
                            body {
                                   background-color:lightyellow;
                            }
                            .fc {
                                   border: solid;
                                   width:60%;
                                   margin:auto;
                                   padding:1%;
                                   border-radius:30px;
                            }
                     </style>
          </head>
          <body>
                     <h1>Pincode Info App</h1>
                     <div class="fc">
                     <form method = "POST">
                           <input type="number"
                                   name="pc"
                                   placeholder="Enter Pincode"
                                   required
                                   min="1"
                      />
                      <br/><br/>
                      <input type="submit"
                               value="Find Info"
                           />
                     </form>    
                     </div>
                     <h2>
                           {{ msg }}
                     </h2>
          </body>
</html>
 