#! /usr/bin/env python
import os
from flask import Flask
from app import app
#app.run(debug=True,host="0.0.0.0",port=8080)

app.run(debug=True,
        host=os.getenv('IP', '0.0.0.0'), 
        port=int(os.getenv('PORT', 8080))
        )
         
