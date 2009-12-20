
function Agregar(url){
    document.location.href=url;
}
function editar(url){
    document.location.href=url;
}
function borrar(url){
  Dialog.question(
  'Are you sure?',
  {
    'title': 'Borrar',
    'onYes': function(dialog) {
    document.location.href=url;  
      dialog.close();
    },
    'onNo': function(dialog) {
      dialog.close();
    }
  }
);
    
}

function volver(url) {
    document.location.href=url;
}

