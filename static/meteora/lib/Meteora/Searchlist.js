
var Searchlist=new Class({'Implements':[Control],'__bindEvents':function(){var elements=$(this.dataForm).getElements('input, select, textarea, button');elements.each(function(el){var name=el.nodeName.toLowerCase();var eventName=null;switch(name){case'select':eventName='change';break;case'input':case'textarea':if(el.type&&el.type.match(/checkbox|radio/)){eventName='change';}else{eventName='keyup';}
break;}
this.addListener(el,eventName,this.__elementSearch);}.bind(this));},'__elementSearch':function(e){if(e.keyCode==13){if(this.__timeOut){window.clearTimeout(this.__timeOut);}
this.search();}else{this.timedSearch();}},'__buildComponents':function(){this.components={searchList:Widget.div({'class':'m-searchlist'}),items:Widget.ul()}
this.components.searchList.hide();this.components.searchList.appendChild(this.components.items);this.components.searchList.parent=this;this.dataForm.__searchList=this;if(this.options.attachTo){$(this.options.attachTo).appendChild(this.components.searchList);}else{$(this.components.searchList).clonePosition(this.dataForm,{setHeight:false,setWidth:true,offsetTop:this.dataForm.offsetHeight});this.dataForm.appendChild(this.components.searchList);}
this.__bindEvents();},'__populateList':function(json){this.components.searchList.hide();this.components.items.dumpChildren();try{var json=this.fromJSON(json);if($type(json)=='object'){var i=0;for(var index in json){if(index!='jsonRpc'){var content=json[index];var li=Widget.li({'class':i%2?'odd':'even'},Widget.fromHTML(content));this.components.items.appendChild(li);if(this.options.rowClick){var callback=this.options.rowClick.bind(index);}else{var callback=this.$events.onClick[0].bind(this,{'index':index,'content':content});}
li.addEvent('click',callback);i++;}}}}catch(e){var li=Widget.li(null,json);this.components.items.appendChild(li);}
this.components.searchList.show();},'initialize':function(dataForm,options){this.dataForm=$(dataForm);this.dataForm.parent=this;this.dataForm.onsubmit=function(){return false};this.components={};this.options={'onClick':function(){}}
this.setOptions(options);if(this.options.rowClick){this.options.onClick=this.options.rowClick;}
this.__buildComponents();this.search();},'timedSearch':function(){if(this.__timeOut){window.clearTimeout(this.__timeOut);}
this.__timeOut=window.setTimeout(function(){this.search()}.bind(this),500);},'search':function(){new Request({'url':this.dataForm.action,'loading':this.components.searchList,'method':this.dataForm.method,'data':this.dataForm.toQueryString(),'onComplete':this.__populateList.bind(this)}).send();}});