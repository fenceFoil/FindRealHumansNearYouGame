(function(t){function e(e){for(var a,r,o=e[0],l=e[1],c=e[2],p=0,h=[];p<o.length;p++)r=o[p],Object.prototype.hasOwnProperty.call(n,r)&&n[r]&&h.push(n[r][0]),n[r]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(t[a]=l[a]);u&&u(e);while(h.length)h.shift()();return i.push.apply(i,c||[]),s()}function s(){for(var t,e=0;e<i.length;e++){for(var s=i[e],a=!0,r=1;r<s.length;r++){var l=s[r];0!==n[l]&&(a=!1)}a&&(i.splice(e--,1),t=o(o.s=s[0]))}return t}var a={},n={app:0},i=[];function r(t){return o.p+"js/"+({about:"about"}[t]||t)+"."+{about:"f90ca52f"}[t]+".js"}function o(e){if(a[e])return a[e].exports;var s=a[e]={i:e,l:!1,exports:{}};return t[e].call(s.exports,s,s.exports,o),s.l=!0,s.exports}o.e=function(t){var e=[],s=n[t];if(0!==s)if(s)e.push(s[2]);else{var a=new Promise((function(e,a){s=n[t]=[e,a]}));e.push(s[2]=a);var i,l=document.createElement("script");l.charset="utf-8",l.timeout=120,o.nc&&l.setAttribute("nonce",o.nc),l.src=r(t);var c=new Error;i=function(e){l.onerror=l.onload=null,clearTimeout(p);var s=n[t];if(0!==s){if(s){var a=e&&("load"===e.type?"missing":e.type),i=e&&e.target&&e.target.src;c.message="Loading chunk "+t+" failed.\n("+a+": "+i+")",c.name="ChunkLoadError",c.type=a,c.request=i,s[1](c)}n[t]=void 0}};var p=setTimeout((function(){i({type:"timeout",target:l})}),12e4);l.onerror=l.onload=i,document.head.appendChild(l)}return Promise.all(e)},o.m=t,o.c=a,o.d=function(t,e,s){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:s})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var s=Object.create(null);if(o.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)o.d(s,a,function(e){return t[e]}.bind(null,a));return s},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/",o.oe=function(t){throw console.error(t),t};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],c=l.push.bind(l);l.push=e,l=l.slice();for(var p=0;p<l.length;p++)e(l[p]);var u=c;i.push([0,"chunk-vendors"]),s()})({0:function(t,e,s){t.exports=s("56d7")},"034f":function(t,e,s){"use strict";var a=s("85ec"),n=s.n(a);n.a},"2a37":function(t,e,s){"use strict";var a=s("5ccf"),n=s.n(a);n.a},"56d7":function(t,e,s){"use strict";s.r(e);s("e260"),s("e6cf"),s("cca6"),s("a79d");var a=s("2b0e"),n=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{attrs:{id:"overall"}},[s("div",{attrs:{id:"app"}},[s("router-view")],1)])},i=[],r=(s("034f"),s("2877")),o={},l=Object(r["a"])(o,n,i,!1,null,null,null),c=l.exports,p=(s("d3b7"),s("8c4f")),u=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"home"},[a("img",{staticStyle:{width:"400px",background:"#fffa4d"},attrs:{src:s("dfc9")}}),a("HelloWorld")],1)},h=[],d=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"hello"},[s("h1",[t._v("Create a profile now!!")]),s("button",{staticClass:"japanese",attrs:{onclick:"window.location.href = '#/profile';"}},[t._v("始まりましょうか")]),t._m(0),t._l(t.reviews,(function(e){return s("div",{key:e},[s("p",[t._v(t._s(e))])])}))],2)},f=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("h1",[t._v("The number 1 rated dating app for real humans."),s("br"),t._v("Just read the reviews of our very real and happy customers.")])}],m={name:"HelloWorld",props:{},data:function(){return{reviews:["The best dating app money can buy 10 out of 10","didnt find a human, only robots 0 out of 1"]}}},v=m,_=Object(r["a"])(v,d,f,!1,null,"5c275a20",null),w=_.exports,g={name:"home",components:{HelloWorld:w}},C=g,b=Object(r["a"])(C,u,h,!1,null,null,null),y=b.exports,x=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"profile"},[a("h1",{staticClass:"header-title"},[t._v("Enter a Name")]),a("div",{staticClass:"left-to-right-profile"},[t._v("👉")]),a("img",{staticClass:"logo anim",attrs:{src:s("dfc9")}}),a("img",{staticClass:"logo anim-1",attrs:{src:s("dfc9")}}),a("img",{staticClass:"logo anim-2",attrs:{src:s("dfc9")}}),a("img",{staticClass:"logo anim-3",attrs:{src:s("dfc9")}}),a("img",{staticClass:"logo anim-4",attrs:{src:s("dfc9")}}),a("form",{attrs:{id:"profile-name",align:"center",method:"post"}},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.name,expression:"name"}],attrs:{type:"text",placeholder:"Name"},domProps:{value:t.name},on:{input:function(e){e.target.composing||(t.name=e.target.value)}}}),a("div",{staticClass:"button"},[a("input",{attrs:{type:"button",value:"Submit"},on:{click:t.submit}})])])])},k=[],j=(s("b0c0"),s("96cf"),s("89ba")),O={name:"profile",data:function(){return{name:""}},components:{},methods:{submit:function(){var t=Object(j["a"])(regeneratorRuntime.mark((function t(){var e,s,a,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e="http://findrealhumansnearyou.com/create_profile",s=Math.floor(66666*Math.random()+1e4),t.next=4,fetch(e+"",{method:"POST",headers:{"Content-Type":"application/json;charset=utf-8"},body:JSON.stringify({name:this.name,picture:s})});case 4:return a=t.sent,t.next=7,a.json();case 7:n=t.sent,window.localStorage.setItem("playerID",n.playerID),window.localStorage.setItem("playerName",this.name),window.localStorage.setItem("playerPictureURL","https://www.thiswaifudoesnotexist.net/example-".concat(s,".jpg")),window.location.href="#/pickupline";case 12:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()}},S=O,E=(s("2a37"),Object(r["a"])(S,x,k,!1,null,null,null)),I=E.exports,P=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"results"},[s("h1",{staticClass:"header-title"},[t._v("This is teh result page")]),s("h1",{staticClass:"round-num"},[t._v("Round "+t._s(t.round))]),s("h1",t._l(t.hearts,(function(e){return s("span",{key:e},[s("span",{staticClass:"hearts",staticStyle:{color:"pink"}},[t._v("* ")])])})),0),s("h1",{staticClass:"implants"},[t._v("cybernetic implants")]),s("div",t._l(t.implants,(function(t){return s("span",{key:t,staticStyle:{"margin-right":"1em"}},[s("Implant")],1)})),0),t._l(t.pickuplines,(function(e){return s("div",{key:e},[t._m(0,!0),s("h1",{staticClass:"robo-pickuplines"},[t._v(t._s(e))])])})),t._m(1),s("h1",{staticClass:"dated"},[t._v("Your lovely Dates")]),t._l(t.dates,(function(t){return s("div",{key:t,staticClass:"dates-display"},[s("img",{staticClass:"waifu-thumbnail",attrs:{src:t}})])})),s("button",{on:{click:t.submit}},[t._v("Ready")])],2)},T=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("h1",{staticClass:"seperator"},[s("div",{staticClass:"asterisk left"},[t._v("*")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore middle"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("div",{staticClass:"asterisk right"},[t._v("*")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("h1",{staticClass:"seperator"},[s("div",{staticClass:"asterisk left"},[t._v("*")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore left"},[t._v("_")]),s("span",{staticClass:"pipe left"},[t._v("|")]),s("span",{staticClass:"underscore middle"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("span",{staticClass:"pipe right"},[t._v("|")]),s("span",{staticClass:"underscore right"},[t._v("_")]),s("div",{staticClass:"asterisk right"},[t._v("*")])])}],N=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("svg",{attrs:{height:"0%",viewBox:"0 -103 512 512",width:"0%",xmlns:"http://www.w3.org/2000/svg"}},[s("path",{attrs:{d:"m210.6875 90.054688h90.628906v95.058593h-90.628906zm0 0"}}),s("path",{attrs:{d:"m90.054688 90.054688h90.628906v95.058593h-90.628906zm0 0"}}),s("path",{attrs:{d:"m331.320312 90.054688h90.628907v95.058593h-90.628907zm0 0"}}),s("path",{attrs:{d:"m512 0h-512v275.164062h30.820312v30.035157h30.003907v-30.035157h30.046875v30.035157h30.003906v-30.035157h30.046875v30.035157h30.003906v-30.035157h30.046875v30.035157h30.003906v-30.035157h30.046876v30.035157h30.003906v-30.035157h30.046875v30.035157h30.003906v-30.035157h30.046875v30.035157h30.003906v-30.035157h30.046875v30.035157h30.003907v-30.035157h30.820312zm-451.949219 215.113281v-155.0625h391.898438v155.0625zm0 0"}})])},$=[],R={name:"Implant"},L=R,D=Object(r["a"])(L,N,$,!1,null,null,null),J=D.exports,z={name:"pickupline",data:function(){return{round:1,hearts:4,implants:2,pickuplines:["Hey I am a Robot. Plz beleive me","Just a hot single looking to become a hot mess."],dates:["https://www.thiswaifudoesnotexist.net/example-196646.jpg","https://www.thiswaifudoesnotexist.net/example-196647.jpg","https://www.thiswaifudoesnotexist.net/example-196647.jpg","https://www.thiswaifudoesnotexist.net/example-196647.jpg","https://www.thiswaifudoesnotexist.net/example-196647.jpg","https://www.thiswaifudoesnotexist.net/example-196647.jpg","https://www.thiswaifudoesnotexist.net/example-196647.jpg","https://www.thiswaifudoesnotexist.net/example-196647.jpg","https://www.thiswaifudoesnotexist.net/example-196627.jpg","https://www.thiswaifudoesnotexist.net/example-112647.jpg","https://www.thiswaifudoesnotexist.net/example-106647.jpg","https://www.thiswaifudoesnotexist.net/example-192647.jpg"]}},components:{Implant:J},methods:{submit:function(){window.location.href="#/pickupline"}}},M=z,H=Object(r["a"])(M,P,T,!1,null,null,null),W=H.exports,U=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"about"},[s("h1",{staticClass:"header-title"},[t._v(t._s(t.playerName))]),s("h1",{staticClass:"this-is-you japanese"},[t._v("これはあなたです")]),s("div",{staticClass:"left-right"},[t._v("👉")]),s("div",{staticClass:"left-right-reverse"},[t._v("👉")]),s("div",{staticClass:"left-to-right"},[t._v("👉")]),s("div",{staticClass:"picture"},[s("img",{staticClass:"waifu",attrs:{src:t.pictureURL}})]),s("h1",[t._v("Enter pickup line")]),s("div",{staticClass:"text"},[s("textarea",{directives:[{name:"model",rawName:"v-model",value:t.pickupline,expression:"pickupline"}],attrs:{rows:"4",cols:"50"},domProps:{value:t.pickupline},on:{input:function(e){e.target.composing||(t.pickupline=e.target.value)}}})]),s("div",{staticClass:"button"},[s("button",{attrs:{type:"button"},on:{click:t.submit}},[t._v("Submit")])])])},Y=[],q=(s("e25e"),{name:"pickupline",data:function(){return{pickupline:"",playerName:window.localStorage.getItem("playerName"),pictureURL:window.localStorage.getItem("playerPictureURL")}},components:{},methods:{submit:function(){var t=Object(j["a"])(regeneratorRuntime.mark((function t(){var e,s,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e="http://findrealhumansnearyou.com/",t.next=3,fetch(e+"get_pickup_completions",{method:"POST",headers:{"Content-Type":"application/json;charset=utf-8"},body:JSON.stringify({playerID:parseInt(window.localStorage.getItem("playerID")),humanWords:this.pickupline})});case 3:return s=t.sent,t.next=6,s.json();case 6:return a=t.sent,alert(a.options[0]),t.next=10,fetch(e+"commit_new_pickup",{method:"POST",headers:{"Content-Type":"application/json;charset=utf-8"},body:JSON.stringify({playerID:parseInt(window.localStorage.getItem("playerID")),humanWords:this.pickupline,botScreed:a.options[0]})});case 10:window.location.href="#/swipe";case 11:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()}}),A=q,B=Object(r["a"])(A,U,Y,!1,null,null,null),F=B.exports,G=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"about"},[s("h1",{staticClass:"header-title"},[t._v(t._s(t.prospects[t.index].name))]),s("h1",{staticClass:"this-is-not-you japanese"},[t._v("これはあなたじゃないです")]),s("div",{staticClass:"picture"},[s("img",{staticClass:"waifu",attrs:{src:t.prospects[t.index].src}})]),s("h1",[t._v(t._s(t.prospects[t.index].line))]),s("button",{staticClass:"button-2 japanese",attrs:{type:"submit"},on:{click:function(e){return t.submit("RIGHT")}}},[t._v("右")]),s("button",{staticClass:"button-1 japanese",attrs:{type:"submit"},on:{click:function(e){return t.submit("LEFT")}}},[t._v("左")])])},K=[],Q={name:"swipe",data:function(){return{index:0,prospects:[{name:"Name 1",src:"https://www.thiswaifudoesnotexist.net/example-196646.jpg",line:"Pickup Line 1"},{name:"Name 2",src:"https://www.thiswaifudoesnotexist.net/example-196647.jpg",line:"Pickup Line 2"}]}},components:{},methods:{submit:function(t){alert(t),this.index<this.prospects.length-1?this.index++:window.location.href="#/results"}}},V=Q,X=Object(r["a"])(V,G,K,!1,null,null,null),Z=X.exports,tt=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"about"},[s("h1",{staticClass:"header-title"},[t._v("Your Name")]),s("h1",{staticClass:"this-is-you japanese"},[t._v("これはあなたです")]),s("div",{staticClass:"left-right"},[t._v("👉")]),s("div",{staticClass:"left-right-reverse"},[t._v("👉")]),s("div",{staticClass:"left-to-right"},[t._v("👉")]),t._m(0),s("h1",[t._v("Enhance Your Pickup Line")]),t._l(t.endings,(function(e){return s("div",{key:e,staticClass:"text"},[s("div",{staticClass:"button"},[s("button",{attrs:{type:"button"},on:{click:function(s){return t.submit(e)}}},[t._v(t._s(e))])])])}))],2)},et=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"picture"},[s("img",{staticClass:"waifu",attrs:{src:"https://www.thiswaifudoesnotexist.net/example-196646.jpg"}})])}],st={name:"selectline",data:function(){return{pickupline:"",endings:["Ending 1","Ending 2"]}},components:{},methods:{submit:function(t){alert(t),window.location.href="#/swipe"}}},at=st,nt=Object(r["a"])(at,tt,et,!1,null,null,null),it=nt.exports;a["a"].use(p["a"]);var rt=[{path:"/",name:"home",component:y},{path:"/about",name:"about",component:function(){return s.e("about").then(s.bind(null,"f820"))}},{path:"/profile",name:"profile",component:I},{path:"/pickupline",name:"pickupline",component:F},{path:"/selectline",name:"selectline",component:it},{path:"/results",name:"results",component:W},{path:"/swipe",name:"swipe",component:Z}],ot=new p["a"]({routes:rt}),lt=ot;a["a"].config.productionTip=!1,new a["a"]({router:lt,render:function(t){return t(c)}}).$mount("#app")},"5ccf":function(t,e,s){},"85ec":function(t,e,s){},dfc9:function(t,e,s){t.exports=s.p+"img/logo-frhny.493de023.png"}});
//# sourceMappingURL=app.1aae6c43.js.map