$(document).ready(function(){

    var counter = 2;

    $("#addButton3").click(function () {

    if(counter>4){
            alert("Apenas 4 Formações");
            return false;
    }

    var newTextBoxDiv3 = $(document.createElement('div'))
         .attr("id", 'TextBoxDiv' + counter);

    newTextBoxDiv3.attr("class", "form-row");

      var text3 = '<div class="form-group col-sm-4"><label>Empresa '+ counter +' : </label>' +
          '<input type="text" class="form-control" name="company'+ counter +'" placeholder=""></div>'+
      '<div class="form-group col-sm-2"><label>Cargo '+ counter +':</label><input type="text" class="form-control" name="function'+ counter +'" placeholder=""></div>'+
      '<div class="form-group col-sm-2"><label>Periodo '+ counter +':</label><input type="text" class="form-control" name="worktime'+ counter +'" placeholder=""></div>'+
      '<div class="w-100"></div>'+
      '<div class="form-group col-sm-6"><label>Funções exercida no Cargo '+ counter +':(Opcional)</label><input type="text" class="form-control" name="functionDescribe'+ counter +'" placeholder="" maxlength="50"></div>';

    newTextBoxDiv3.after().html(text3);

    newTextBoxDiv3.appendTo("#TextBoxesGroup3");


    counter++;
     });

     $("#removeButton3").click(function () {
    if(counter==2){
          alert("Precisa ficar apenas um");
          return false;
       }

    counter--;

        $("#TextBoxDiv" + counter).remove();

     });

  });
