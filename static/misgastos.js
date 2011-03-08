
function Agregar(url){
    document.location.href=url;
}
function editar(url){
    document.location.href=url;
}

function get_buttons(url){
return    buttons = {
        "Si": function(){
        document.location.href=url;  
        },
        "Cancelar": function(){
            $(this).dialog("close");
        }
    }


}

function borrar(url){
    buttons = {
        "Si": function(){
        document.location.href=url;  
        },
        "Cancelar": function(){
            $(this).dialog("close");
        }
    }

    $("#del").dialog("option",'buttons', buttons);
    $("#del").dialog("open");
 
}

function volver(url) {
    document.location.href=url;
}

$(document).ready(function(){
    $("#del").dialog( {
        autoOpen:false,
        title:"Borrar"
    });

    $("#change_month_number").dialog({
            autoOpen:false,title:"Cambiar Numero de meses a mostrar"});
});

function change_number_months(url){
    buttons = {
        "Si": function(){
            $.get(url,{ "number":$("#id_number_month").val()});
            location.reload();
        },
        "No": function(){
            $(this).dialog("close");
        }
    }



    $("#change_month_number").dialog("option","buttons",buttons);
    $("#change_month_number").dialog("open");
}
