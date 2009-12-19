
Fx.Scroll=new Class({Extends:Fx,options:{offset:{'x':0,'y':0},wheelStops:true},initialize:function(element,options){this.element=this.pass=$(element);arguments.callee.parent(options);var cancel=this.cancel.bind(this,false);if($type(this.element)!='element')this.element=$(this.element.getDocument().body);var stopper=this.element;if(this.options.wheelStops){this.addEvent('onStart',function(){stopper.addEvent('mousewheel',cancel);},true);this.addEvent('onComplete',function(){stopper.removeEvent('mousewheel',cancel);},true);}},set:function(){var now=Array.flatten(arguments);this.element.scrollTo(now[0],now[1]);},compute:function(from,to,delta){var now=[];(2).times(function(i){now.push(Fx.compute(from[i],to[i],delta));});return now;},start:function(x,y){if(!this.check(x,y))return this;var offsetSize=this.element.getSize(),scrollSize=this.element.getScrollSize(),scroll=this.element.getScroll(),values={'x':x,'y':y};for(var z in values){var max=scrollSize[z]-offsetSize[z];if($chk(values[z]))values[z]=($type(values[z])=='number')?values[z].limit(0,max):max;else values[z]=scroll[z];values[z]+=this.options.offset[z];}
return arguments.callee.parent([scroll.x,scroll.y],[values.x,values.y]);},toTop:function(){return this.start(false,0);},toLeft:function(){return this.start(0,false);},toRight:function(){return this.start('right',false);},toBottom:function(){return this.start(false,'bottom');},toElement:function(el){var position=$(el).getPosition(this.element);return this.start(position.x,position.y);}});