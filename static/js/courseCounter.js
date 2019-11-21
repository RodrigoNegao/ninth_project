$(document).ready(function(){

    var counter = 2;

    $("#addButton").click(function () {

    if(counter>4){
            alert("Apenas 4 Cursos");
            return false;
    }

    var newTextBoxDiv = $(document.createElement('div'))
         .attr("id", 'TextBoxDivC' + counter);

    newTextBoxDiv.attr("class", "form-row");

      var text1 = '<div class="form-group col-sm-2"><label>Curso '+ counter +': </label>' +
          '<input class="form-control" type="text" name="course' + counter +
          '" id="textbox' + counter + '" value="" ></div>'+'<div class="form-group col-sm-3"><label>Instituição '+ counter +' : </label>' +
      '<input class="form-control" type="text" name="cInstitution'+ counter + '" placeholder=""></div>'+
      '<div class="form-group col-sm-3"><label>Ano de Conclusão '+ counter + ':</label>'+'<input type="text" class="form-control" name="cyearFinish'+ counter +'" placeholder=""></div>'+
      '<div class="form-group col-sm-2"><label>Carga Hororária '+ counter + ':</label>'+'<input type="text" class="form-control" name="studyTime'+ counter + '" placeholder=""></div>';

    newTextBoxDiv.after().html(text1);

    newTextBoxDiv.appendTo("#TextBoxesGroup");


    counter++;
     });

     $("#removeButton").click(function () {
    if(counter==1){
          alert("Precisa ficar apenas um");
          return false;
       }

    counter--;

        $("#TextBoxDivC" + counter).remove();

     });

  });
