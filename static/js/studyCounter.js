$(document).ready(function(){

    var counter = 2;

    $("#addButton2").click(function () {

    if(counter>4){
            alert("Apenas 4 Formações");
            return false;
    }

    var newTextBoxDiv2 = $(document.createElement('div'))
         .attr("id", 'TextBoxDiv' + counter);

    newTextBoxDiv2.attr("class", "form-row");

      var text2 = '<div class="form-group col-sm-2"><label for="inputlevelStudy'+ counter +'">Ensino '+ counter +':</label>' +
          '<select id="inputlInstitution'+ counter +'" name="inputlevelStudy' + counter +
          '" class="form-control"><option selected></option><option value="Médio">Médio</option><option value="Superior">Superior</option><option value="Fundamental">Fundamental</option></select></div>' +
      '<div class="form-group col-sm-3"><label>Instituição'+ counter +':</label> <input type="text" class="form-control" name="lInstitution'+ counter + '"placeholder=""></div>'+
      '<div class="form-group col-sm-3"><label>Ano de Conclusão '+ counter +':</label><input type="text" class="form-control" name="lyearFinish'+ counter + '" placeholder=""></div>';

    newTextBoxDiv2.after().html(text2);

    newTextBoxDiv2.appendTo("#TextBoxesGroup2");


    counter++;
     });

     $("#removeButton2").click(function () {
    if(counter==2){
          alert("Precisa ficar apenas um");
          return false;
       }

    counter--;

        $("#TextBoxDiv" + counter).remove();

     });

  });
