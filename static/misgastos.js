
function Agregar(url){
    document.location.href=url;
}
function editar(url){
    document.location.href=url;
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

});