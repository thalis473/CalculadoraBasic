from flask import Flask,render_template,request

app = Flask(__name__,template_folder="./src/views")

@app.route("/",methods=["GET","POST"])
def home():
    if (request.method =="GET"):
        return render_template("index.html")
    else:
        if(request.form["input1"] != "" and request.form["input2"] != ""):
            num1=request.form["input1"]
            num2=request.form["input2"]
            condicionais=request.form["condicionais"]
        # cálculos
            soma = int(num1) + int(num2)
            subt = int(num1) - int(num2)
            mult = int(num1) * int(num2)
            divi=int(num1) / int(num2)

            if(condicionais == "soma"):    
               return str(soma)
            elif(condicionais == "subt"):
               return str(subt)
            elif(condicionais == "mult"):
               return str(mult)
            else:
                return str(divi)
        else:
            return "<h1>Favor, preencha todos os campos do formulario!<h1>"

@app.errorhandler(404)
def note_foud(erro):
    return render_template("erro.html")

app.run(port=8080, debug=True)