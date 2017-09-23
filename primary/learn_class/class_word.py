函数（e，t） {
    function o（e） {
        return“ [object Function]” === Object.prototype.toString.call（e）
    }函数r（e） {
        if（！d[e]）
        throw新的错误（“Module” + e + “未定义”）;
        var t = d[e];
        return t.module.status！ == a.INITIALIZED && n（e），t.module.exports
    }函数n） {
        var n = d[e]，i = n.module，f = i.exports，s = i.factory;
        if（i.parent = u，u = n，o（s）） {
            var c = s（r，f，i）;
            c！ == t && （i.exports = c）
        } else i.exports = d[e].factory;
        i.status = a.INITIALIZED
    }函数i（e，r，i） {
        if（d[e]）
        throw new Error（“Module” + e + “已经被定义了”）;
        if（“undefined” == typeof i && （i = r），！o（i） && i！Object（i））
        throw new Error（“factory of module” + e + “必须是一个对象或函数。”）;
        d[e] = {
            module： {
                id：e，exports： {}，uri：“”，依赖关系： []，parent：t，factory：i，status：a.DEFINED
            }
        }，e === f && n（e）
    }
    var a = {
        DEFINED：“模块刚刚定义”，INITIALIZED：“模块被编译并且module.exports可用。“
    };
    if（！e.define） {
        for（
        var u，d = {}，f = null，s = document.getElementsByTagName（”script“），c = 0，l = s.length;
        l > c && ！f;
        c++）f = s[c].getAttribute（“data - main”）;
        if（！f）
        throw new Error数据主要属性在脚本标签中。“）;
        e.define = i
    }
}（window）;
define（” / lib / jquery - 1.6.2“，
function（e，t） {
    return function（e，t）函数n（e，n，r） {
        if（r === t && 1 === e.nodeType） {
            var i = “data - ” + n.replace（q，“$ 1 - $ 2”）toLowerCase（）;
            if（r = e.getAttribute（i），“string” == typeof r） {
                try {
                    r = “true” === r？！0：“false” === r？！1：“null” = ？ == ř空：H.isNaN（R）I.test（R）H.parseJSON（R）：R：parseFloat（R）
                }赶上（O） {}
                H.data（E，N，R）
            } else r = t
        }
        return r
    }
    function r（e） {
        for（
        var t in e）
        if（“toJSON”！ == t）
        return！1;
        return！0
    }
    function i（e，n，r） {
        var i = n + “defer”，o = n + “queue”，a = n + “mark”，s = H.data（e，i，t，！0）;！s || “queue”！ == r && H。数据（E，O，T，！0） || “标记”！ == -[R && H.data（E，A，T，！0） || 的setTimeout（函数（） {
            H.data（E，O，T，！0） || H.data（e，a，t，！0） || （H.removeData（e，i，！0），s.resolve（））
        }，0）
    }
    function o（） {
        return！1
    }
    function a（） {
        return！0
    }函数s（e，n，r） {
        var i = H.extend（ {}，r[0]）;
        i.type = e，i.originalEvent = {}，i.liveFired = t，H.event.handle.call（n，i），i.isDefaultPrevented（） && r[0].preventDefault（）
    }函数l（e） {
        var t，n，r，i，o，A，S，L，U，C，F，D，p = []，H = []，M = H._data（此，“事件”）;！如果（e.liveFired == 此 && m && m.live && ！e.target.disabled && （！e.button || “click”！ == e.type）） {
            e.namespace && （f = new RegExp（“（ ^ |\\。）” + e.namespace.split（“。”）。连接（“\\。（？：。 * \\。）？”） + “（\\。 | $）”）），e.liveFired = this;
            var g = live.slice（0）;对于（S = 0;
            S < g.length;
            S++）O = G[s]时，o.origType.replace（G“”） === e.type h.push（？o.selector）：g.splice（S - ，1）;对于（i = H（e.target）.closest（H，e.currentTarget）中，l = 0，U = i.length;
            U > 升;升++）为（C = 1[1]，S = 0;
            S < g.length;
            S++）O = G[s]时，c.selector == o.selector || ˚F && f.test（o.namespace！） || ||c.elem.disabled（α = c.elem，R = NULL，（“的mouseenter” === o.preType || “鼠标离开” === o.preType） && （e.type = O.preType，R = H（e.relatedTarget）.closest（o.selector） [0]，R && H.contains（A，R） && （R = A））中，r && ř === 一个 || p.push（ {
                ELEM：一，handleObj：○，级别：c.level
            }））;对于（！L = 0，U = p.length;
            U > 升 && （I = p[1]，（正 && i.level > N）） && （e.currentTarget = i.elem，e.data = i.handleObj.data，e.handleObj = i.handleObj，D = i.handleObj.origHandler.apply（i.elem，自变量）中，d！ == ！1 && ！e.isPropagationStopped（） || （n = i.level，d === ！1 && （t = ！1），！e.isImmediatePropagationStopped（）））;
            l++）;
            return t
        }
    }函数u（e，t） {回报率（E && “ * ”！ == ê？e + “。”：“”） + t.replace（Q，“`”）replace（Z，“＆”）
    }函数c（e） {
        return！e || ！e.parentNode || 11 == =e.parentNode.nodeType
    }
    function f（e，t，n） {
        if（t = t || 0，H.isFunction（t））
        return H.grep（e，
        function（e，r） {
            var i = !!t.call（e，r，e）;
            return i === n
        }）;
        if（t.nodeType）
        return H.grep（e，
        function（e，r） {
            return e === t == =n
        }）;
        if（“string” == typeof t） {
            var r = H.grep（e，
            function（e） {
                return 1 === e.nodeType
            }）;
            if（fe.test（t））返回H.filter（t，r，！n）;
            t = H.filter（t，r）
        }返回H.grep（e，函数（e，r） {
            return H.inArray（e，t） > =0 === n
        }）
    }
    function d（e，t） {
        return H.nodeName（e，“table”）？e.getElementsByTagName（“tbody”） [0] || e.appendChild（e.ownerDocument.createElement“tbody”））：e
    }
    function p（e，t） {
        if（1 === t.nodeType && H.hasData（e）） {
            var n = H.expando，r = H.data（e），i = H.data（t，r）;
            if（r = r[n]） {
                var o = r.events;
                if（i = i[n] = H.extend（ {}，r），o） {
                    delete i对于（
                    var s in o）
                    for（
                    var s in o）
                    for。（
                    var s in o）
                    for。（
                    var s in o）
                    for [A][s]的.namespace？“”：“”） + O[A][s]的.namespace，邻 [A][s]的，邻 [A][s]的。数据）
                }
            }
        }
    }功能h（e，t） {
        var n;
        1 === t.nodeType && （t.clearAttributes && t.clearAttributes（），t.mer geAttributes && t.mergeAttributes（E）中，n = t.nodeName.toLowerCase（），“对象” === Ñt.outerHTML = e.outerHTML：？！“输入” == Ñ || “复选框” == 即键入 && “无线电”！ == e.type？“选项” === N 't.selected = e.defaultSelected :( “输入” ===ñ|| “textarea的” === N）&&（t.defaultValue = e.defaultValue）:( e.checked &&（t.defaultChecked = t.checked = e.checked），t.value！== e.value &&（t.value = e.value）），t.removeAttribute（H。在e？e.getElementsByTagName（“*”）中返回“getElementsByTagName”：e？e.querySelectorAll（“*”）中的“querySelectorAll”：[]} function g（e）{ （“checkbox”=== e.type ||“radio”=== e.type）&&（e.defaultChecked = e.checked）}函数y（e）{H.nodeName（e，“input”）？在e && H.grep（e.getElementsByTagName（“input”）中，g（e）：“getElementsByTagName”，g）}函数v（e，t）{t.src？H.ajax（{url：t.src，async： ！1，数据类型： “脚本”}）：H.globalEval（（t.text || t.textContent || t.innerHTML || “”）替换（CE，。 “/ * $ 0 * /”）），T .parentNode && t.parentNode.removeChild（t）}函数b（e，t，n）{var r =“width”=== t？e.offsetWidth：e.offsetHeight，i =“width”=== t？Pe ：Ie; return r> 0？（“border”！== n && H.each（i ，函数（）{N ||（R- = parseFloat（H.css（即， “填充” +此））|| 0）， “裕度” === N + R + = parseFloat（H.css（E，的n +此））|| 0：R- = parseFloat（H.css（即， “边界” + +此 “宽度”））|| 0}）中，r + “PX”）:( R = SE（E，T ，T），（0> [R ||空== R）&&（R = e.style [吨] || 0）中，r = parseFloat（R）|| 0，N && H.each（I，函数（）{ R + = parseFloat（H.css（即 “填充” +本））|| 0， “填充” == N &&（R + = parseFloat（H.css（即， “边界” +这+ “宽度”））！| | 0），“margin”== = n &&（r + = parseFloat（H.css（e，n + this））|| 0）}），r +“px”）}函数x（e）{return function对于（var r，i，o，a = t.toLowerCase（）），if（“string”！= typeof t &&（n = t，t =“*”），H.isFunction（n） （泽）中，s = 0，L =则为a.length;升>取值; S ++）R = A [s]时，O = / ^ \ + /测试（R），邻&&（R = r.substr（1） ||“*”），i = e [r] = e [r] || []，i [o？“unshift”：“push”]（n）}}函数T（e，n，r，i ，o，a）{o = o || n.dataTypes [0]，a = a || {}，a [o] =！0; for（var s，l = e [o]，u = C =升l.length：0，F = E ===室温; C>û&&（F ||小号！）;ü++）S =升[U]（N，R，i）中， “串” ==类型s &&（！f || a [s]？s = t：（n.dataTypes.unshift（s），s = T（e，n，r，i，s，a）））; return！f && s ||一个[“*”] ||（s = T（e，n，r，i，“*”，a）），s}函数w（​​e，t，n，r）{if（H.isArray ））H.each（T，函数（T，I）{N || We.test（e）中R（E，I）：瓦特 （n + |）“，i，n，r）}）; else if（n || null = =（t +“”“！！function function function function function function function function function function function function function function function function function function function function function function function function function function function function function function function function function N（e，n，r）{var i，o，a，s，l = e.contents，u = e.dataTypes，c = e.responseFields; for（o in c）o在r &&（n [ O]] = R [O]）;对于（; “*” === U [0];）u.shift（）中，i ===吨&&（I = e.mimeType || n.getResponseHeader（“内容如果（i）for（o in l）if（l [o] && l [o] .test（i））{u.unshift（o）; break} if（u [0] in r ）a = u [0]; else {for（o in r）{if（！u [0] || e.converters [o +“”+ u [0]]）{a = o; break} （s = o）} a = a || s} return a？（a！== u [0] && u.unshift（a），r [a]）：void 0}函数C（e，n）{e .dataFilter &&（n = e.dataFilter（n，e.dataType））; var r，i，o，a，s，l，u，c，f = e.dataTypes，d = {}，p = f.length ，h = f [0]; for（r = 1; p> r; r ++）{if（1 === r）for（i in e.converters）“string”== typeof i &&（d [i.toLowerCase （）] = e.converters [i]）; if（a = h，h = f [r]，“*”=== h）h = a; else if（“*”！== a && a！ h）{if（s = a +“”+ h，l = d [s] || d [“*”+ h]，！l）{c = t; for（u in d）if（o = split（“”），（o [0] === a ||“*”=== o [0]）&&（c = d [o [1] +“”+ h]））{u = [u]，u ===！0？l = c：c ===！0 &&（l = u）; break}} l || c || H.error（“无转换 从“+ s.replace（”“，”到“）），l！==！0 &&（n = l？l（n）：c（u（n）））}} return n} function E（） try {return new e.XMLHttpRequest} catch（t）{}}函数S（）{try {return new e.ActiveXObject（“Microsoft.XMLHTTP”）} catch（t）{}}函数A（）{return setTimeout k（0），ht = H.now（）}函数k（）{ht = t}函数D（e，t）{var n = {}; return H.each（vt.concat.apply vt.slice（0，t）），function（）{n [this] = e}），n}函数F（e）{if（！mt [e]）{var t = L.body，n = H （ “<” + E + “>”）appendTo（T）中，r = n.css（ “显示器”）;。n.remove（），（ “无” ===  -  [R || “” === R） &&（英尺||（英尺= L.createElement（ “IFRAME”），ft.frameBorder = ft.width = ft.height = 0），t.appendChild（英尺），DT && ft.createElement ||（DT =（英尺contentWindow || ft.contentDocument）.document，dt.write（（“CSS1Compat”=== L.compatMode？“<！doctype html>”：“”）+“<html> <body>”），dt.close （））中，n = dt.createElement（e）中，dt.body.appendChild（N）中，r = H.css（N， “显示器”），t.removeChild（FT）），MT [E] = R} return mt [e]}函数j（e）{return H.isWindow（e）？e：9 === e.nodeType？e.defaultView || e.parentWindow：！1} var L = e.document，M = e.navigator，O = e.location，H = function（）{function n（）{if（！s.is 准备）{try {L.documentElement.doScroll（“left”）} catch（e）{return void setTimeout（n，1）} s.ready（）}} var r，i，o，a，s = function e，t）{return new s.fn.init（e，t，r）}，l = e.jQuery，u = e。$，c = / ^（？：[^ <] * \ W] +>）[^>] * $ |＃（[\ W \  - ] *）$）/，F = / \ S /峰，d = / ^ \ S + / p = / \ S + $ /， H = / \ D / M = / ^ <（\ W +）\ S * \ /？>（：<？\ / \ 1>）$ /，G = / ^ [\]，：{} \ S ] * $ /，Y = / \\（？：[ “\\\ / bfnrt] | U [0-9A-FA-F] {4}）/ G，v = /”[^“\\\ñ \ R] *“|真|假|空|  -  \ D +？（？：\。\ D *）（？：[EE] [+ \  - ] \ D +？）/ G，b = /（？ ：^ |：|，）（？：\ s * \ [）+ / g，x = /（webkit）[\ /]（[\ w。] +）/，T = /（opera） *版本）？[\ /]（[\ w。] +）/，w = /（msie）（[\ w。] +）/，N = /（mozilla）（？rv：（[\ w。] +））？/，C = /  - （[az]）/ gi，E =函数（e，t）{return t.toUpperCase（）}，S = M.userAgent，A = Object.prototype.toString，K = Object.prototype.hasOwnProperty，D = Array.prototype.push，F = Array.prototype.slice，J = String.prototype.trim，O = Array.prototype.indexOf，H = { }; return s.fn = s.prototype = {constructor：s，init：function（e，n，r）{var i，o，a，l; if（！e）return this; if（e.nodeType） return this.context = this [0] = e，this.length = 1，this; if（“body”=== e &&！n && L.body）return this.context = L，this [0] = L.body， this.selector = e，this.length = 1，this; if（“string”== typeof e）{if（i =“<”=== e.charAt（0）&&“>”=== e。的charAt（e.length-1）&& e.length> = 3 [空，即，空]：！c.exec（e）中，！我|| I [1] && N）返回否|| n.jquery！？ （n || r）.find（e）：this.constructor（n）.find（e）; if（i [1]）返回n = n instanceof s？n [0]：n，l = n？ .ownerDocument || N：？L，A = m.exec（e）所示，s.isPlainObject（n）的（E = [L.createElement（一个[1]）]，s.fn.attr.call（E ！中，n，0））：E = [l.createElement（A [1]）] :( A = s.buildFragment（[I [1]]，[1]）中，e =（a.cacheable S'。克隆（a.fragment）：a.fragment）.childNodes），s.merge（此，E）;如果（O = L.getElementById（I[2]），邻 && o.par entNode） {
            if（o.id！ == i[2]）
            return r.find（e）;
            this.length = 1，this[0] = o
        }
        return this.context = L，this.selector = e，this
    }
    return s.isFunction（e）？r.ready（e）: (e.selector！ == t && （this.selector = e.selector，this.context = e.context），s.makeArray（e，this）
}，选择器：“”，jquery：“1.6.2”，length：0，size：
function（） {
    return this.length
}，toArray：
function（） {
    return F.call（this，0）
}，get：
function（e） {
    return null == e？this.toArray（）：0 > e？this[this.length + e]：this[e]
}，pushStack：
function（e，t，n）r = this.constructor（）;
return s.isArray（e）？D.apply（r，e）：s.merge（r，e），r.prevObject = this，r.context = this.context，“find“ === t？r.selector = this.selector + （this.selector？”“：”“） + n：t && （r.selector = this.selector + ”。“ + t + ”（“ + n + ”）“），r
}，each：
function（e，t） {
    return s.each（this，e，t）
}，ready：
function（e） {
    return s.bindReady（），o.done（e），this
}
eq：
function（e） {
    return - 1 === e？this.slice（e）：this.slice（e， + e + 1）
}，first：
function（） {
    return this.eq（0）
}，最后：
function（） {
    return this.eq（ - 1）
}，slice：
function（） {
    return this.pushStack（F.apply（this，arguments），“slice”，F.call（arguments）.join，“））
}，map：
function（e） {
    return this.pushStack（s.map（this，
    function（t，n） {
        return e.call（t，n，t）
    }））
}，end：
function（） {
    return this.prevObject || this.constructor（null）
}，push：D，sort： []。sort，splice： []。splice
}，s.fn.init.prototype = s.fn，s。extend = s.fn.extend = function（） {
    var e，n，r，i，o，a，l = arguments[0] || {}，u = 1，c = arguments.length，f = ！1;
    for（“boolean” == typeof l && （f = l，l = arguments[1] || {}，u = 2），“object” == typeof l || s.isFunction（l） || ={}），c === u && （l = this， - u）;
    c > u;
    u++）
    if（null！ = （e = arguments[u]））
    for（n in e）r = N]，I = E[N]，L！ == 我 && （F && 我 && （s.isPlainObject（ⅰ） || （O = s.isArray（I）））？（O 2（O = ！1， = R && 小号？.isArray（R）R： []）：一个 = R && s.isPlainObject（R）R： {}，L[N] = s.extend（F，A，I））：我 == 吨 && （升 [n] = i））;
    return l
}，s.extend（ {
    noConflict：
    function（t） {
        return e。$ === s && （e。$ = u），t && e.jQuery === s && 的jQuery = 1）中，s
    }，的isReady：1，readyWait：1，holdReady：功能（E） {Ës.readyWait++：？s.ready（0）
    }，准备：功能（E） {如果（E = ==！0 && ！ - s.readyWait || e！ == ！0 && ！s.isReady） {
            if（！L.body）
            return setTimeout（s.ready，1）;
            if（s.isReady = ！0，è == 0 && -s.readyWait > 0）返回;！o.resolveWith（L， [S]），s.fn.tr igger && S（L）.trigger（“就绪”）解除绑定（“准备好了”）
        }
    }，bindReady：（！O）功能（） {
        {
            IF如果（O = s._Deferred（），“完成” === 大号.readyState）
            return setTimeout（s.ready，1）;
            if（L.addEventListener）L.addEventListener（“DOMContentLoaded”，a，！1），e.addEventListener（“load”，s.ready，！1）;
            else if（L.attachEvent） {
                L.attachEvent（“onreadystatechange”，a），e.attachEvent（“onload”，s.ready）;
                var t = ！1;
                try {
                    t = null == e.frameElement
                } catch r）的 {}
                L.documentElement.doScroll && 吨 && N（）
            }
        }
    }，isFunction：功能（E） {返回“功能” === s.type（E）
    }，IsArray的：Array.isArray || 函数（E） {返回“array” === s.type（e）
    }，isWindow：
    function（e） {
        return e && “object” == typeof e && “setInterval” in e
    }，isNaN：
    function（e） {
        return null == e | ||h.test（e） || isNaN（e）
    }，键入：
    function（e） {
        return null == e？String（e）：H[A.call（e）] || “object”
    }，isPlainObject：功能（E） {如果（E || “对象” == s.type（E） || ||e.nodeType s.isWindow（E）！）返回1;如果（e.constructor && ķ！.call（e，“constructor”） && ！k.call（e.constructor.prototype，“isPrototypeOf”））
        return！1;
        var n;
        for（n in e）;
        return n === t || k。呼叫（E，N）
    }，isEmptyObject：功能（E） {
        for（
        var t in e）
        return！1;
        return！0
    }，error：
    function（e） {
        throw e
    }，parseJSON：
    function（t） {
        return“string” == typeof t && t？（t = s.trim吨），e.JSON && e.JSON.parse e.JSON.parse（T）：g.test（t.replace（Y，“@”）？替换（v，“]”）代替（b“”。））？new Function（“
        return” + t）（）：void s.error（“Invalid JSON：” + t））：null
    }，parseXML：
    function（t，n，r） {
        return e.DOMParser？r = new DOMParser，n = r.parseFromString（t，“text / xml”））: (n = new ActiveXObject（“Microsoft.XMLDOM”），n.async = “false”，n.loadXML（t）r = n.documentElement，r && r.nodeName && “parsererror”！ == r.nodeName || s.error（“Invalid XML：” + t），n
    }，noop：
    function（） {}，globalEval：
    function（t）（t）e（e），（e）（e）（e）E（n），（），，，，，，，，，，，，，，，，，，，，，，，，，0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0，a = e.length，l = a === t || s.isFunction（e）;
    if（r）
    if（l） {
        for（i in e）
        if（n.apply（e[i]，r） === ！1）
        break
    } else for（;
    a > o && n.apply（e[o++]，r）！ == ！1;）;
    else if（l） {
        for（i in e）
        if（n。call（e[i]，i，e[i]） === ！1）
        break
    } else f或者（;
    a > o && n.call（e[o]，o，e[o++]）！ == ！1;）;
    return e
}，trim：j？
function（e） {
    return null == e？：（）（）（）（）（）（）（）（）e，t） {
        var n = t || [];
        if（null！ = e） {
            var r = s.type（e）;
            null == e.length || “string” === r || “函数“ === r || ”regexp“ === r || s.isWindow（e）？D.call（n，e）：s.merge（n，e）
        }
        return n
    }，inArray：
    function e（t） {
        if（O）
        return O.call（t，e）;
        for（
        var n = 0，r = t.length;
        r > n;
        n++）
        if（t[n] === e）对于（
        var o = n.length;
        o > ），对于（“n”），合并：
        function（e，n） {
            var r = e.length，i = 0;
            if（“number” == typeof n.length）i[i++] e[r++] = n[i];
            else for（;
            n[i]！ == t;）e[r++] = n[i++];
            return e.length = r，e
        }，grep：函数（e，t，n） {
            var r，i = [];
            n = !!n;
            for（
            var o = 0，a = e.length;
            a > o;
            o++）r = o]，o），n！ == r && i.push（e[o]）;
            return i
        }，map：
        function（e，n，r） {
            var i，o，a = []，l = 0，u = e.length，c = e instanceof s || u！ == t && “number” == typeof u && （u > 0 && e[0] && e[u - 1] || 0 === u || s.isArray e））;
            if（c）
            for（;
            u > l;
            l++）i = n（e[l]，l，r），null！ = i && （a[a.length] = i）;
            else for在e）i = n（e[o]，o，r），null！ = i && （a[a.length] = i）;
            return a.concat.apply（ []，a）
        }，g uid：1，proxy：
        function（e，n） {
            if（“string” == typeof n） {
                var r = e[n];
                n = e，e = r
            }
            if（！s.isFunction（e）
            return t;
            var i = F.call（arguments，2），o = function（） {
                return e.apply（n，i.concat（F.call（arguments）））
            };
            return o.guid = eguid = eguid || o.guid || s.guid++，o
        }，access：
        function（e，n，r，i，o，a） {
            var l = e.length;
            if（“object” == typeof n） {
                for（
                var u in n）s.access（e，u，n[u]，i，o，r）;
                return e
            }
            if（r！ == t） {
                i = ！a && i && s.isFunction）;对于（
                var c = 0;
                l > c;
                c++）o（e[c]，n，i？r.call（e[c]，c，o（e[c]，n）a）;
                return e
            }
            return l？o（e[0]，n）：t
        }，now：
        function（） {
            return（new Date）.getTime（）
        }，uaMatch：
        function（e） {
            e = toLowerCase（）;
            var t = x.exec（e） || T.exec（e） || w.exec（e） || e.indexOf（“compatible”） < 0 && N.exec（e） || [];
            return {
                browser：t[1] || “”，version：t[2] || “0”
            }
        }，sub：
        function（） {
            function e（t，n） {
                return new e.fn.init T，N）
            }
            s.extend（！0，E，这一点），e.superclass = 此，e.fn = e.prototype = 此（），e.​​fn.constructor = E，e.sub = this.sub，e.fn.init = function（n，r） {
                return r && r instanceof s && ！（r instanceof e） && （r = e（r）），s.fn.init.call（this，n，r，t）
            }，e.fn.init.prototype = e.fn;
            var t = e（L）;
            return e
        }，browser： {}
    }），s。each（“Boolean Number String Function Array Date RegExp Object”.split（“”），
    function（e，t） {
        H[“ [object” + t + “]”] = t.toLowerCase（）
    }），i = s.uaMatch（S），i.browser && （s.browser[i.browser] = ！0，s.browser.version = i.version），s.browser.webkit && （s.browser.safari = ！0），F。测试（“听”） && （D = / ^ [\ S \ XA0] + /p = / [\ S \ XA0] + $ /）中，r = S（L），L.addEventListenerθA = 函数（） {
        L.removeEventListener（“DOMContentLoaded”中，a，1！），s.ready（）
    }：L.attachEvent && （α = 函数（） {“完成” === L.readyState && （L.detachEvent（“的onreadystatechange“，a），s.ready（））
    }），s
}（），B = ”done fail isResolved isRejected promise then always pipe“.split（”“），P = [] _Deferred：
function（） {
    var e，t，n，r = []，i = {
        done：
        function（） {
            if（！n） {
                var t，o，a，s，l，u = arguments;
                forè && （L = E，E = 0），t = 0时，O = u.length;○ > 吨;吨++）一个 = U[T]，S = H.type（a）中，“阵列” === 小号？i.done.apply（i，a）：“
                function” === s && r.push（a）;
                l && i.resolveWith（l[0]，l[1]）
            }
            return this
        }，resolveWith：
        function（i，○） {如果（N && Ë && 吨） {
                O = ö || []，T = 1;！！尝试 {对于（;
                    R[0];。）r.shift（）应用（I，O）
                }最后 {
                    e = [i，o]，t = 0
                }
            }
            return this
        }，resolve：
        function（） {
            return i.resolveWi th（this，arguments），this
        }，isResolved：
        function（） {
            return！（！t && ！e）
        }，cancel：
        function（） {
            return n = 1，r = []，this
        }
    };
    return i
}
Deferred：
function（e） {
    var t，n = H._Deferred（），r = H._Deferred（）;
    return H.extend（n， {
        then：
        function（e，t） {
            return n.done（e）.fail（t），this
        }，always：
        function（） {
            return n.done.apply（n，arguments）.fail.apply（this，arguments）
        }，fail：r.done，rejectWith：r.resolveWith，reject：r.resolve，isRejected：r.isResolved，pipe：
        function（e，t） {
            return H.Deferred（
            function（r） {
                H.each（ {
                    done： [e，“resolve”]，fail： [t，“reject”]
                }，
                function（e，t） {
                    var i，o = t[0]，a = t[1];
                    n[e]（H.isFunction（o）？
                    function（） {
                        i = 应用（此，自变量）中，i && H.isFunction（i.promise）i.promise（），然后（r.resolve，r.reject）：：R[A]（i）
                    }其中：R A]）
                }）
            }）.promise（）
        }，promise：
        function（e） {
            if（null == e） {
                if（t）
                return t;
                t = e = {}
            }
            for（
            var r = B.length;
            r--;
            e[B[r]] = n[B[r]];
            return e
        }
    }），n.done（r.cancel）.fail（n.cancel），delete n.cancel，e && e.call（n，n），n
}，when：
function（e） {
    function t（e） {
        return function（t） {
            n[e] = arguments.length > 1？P.call（arguments，0）：t， - o | |a.resolveWith（a，P.call（n，0））
        }
    }
    var n = arguments，r = 0，I = n.length，O = I，A = 1 > =I && È && H.isFunction（e.promise）E：？H.Deferred（）;如果（I > 1） {对于（;
        I > -[R; R++）N[R] && H.isFunction（N[R].promise）N[R].promise（），然后（T（R？），a.reject）： - O;ø || a.resolveWith（一，n）
    } else a！ == e && a.resolveWith（a，i？ [e]： []）;
    return a.promise（）
}
}），H.support = function（） {
    var e，t，R，I，O，A，S，L，U，C，F，D，p，H，M，G = L.createElement（“DIV”）中，y = L.documentElement;若（g.setAttribute（”className“，”t“），g.innerHTML = ” < link / ><table ></ table> <a href='/a 'style='top: 1px;
    float: left;
    opacity: .55;
    '>一个</a> <input type ='checkbox '/>“，e = g.getElementsByTagName（”*“），t = g.getElementsByTagName（”a“）[0]，！e ||！e.length | ！| T）返回{}; N = L.createElement（ “选择”）中，r = n.appendChild（L.createElement（ “选项”））中，i = g.getElementsByTagName（ “输入”）[0]，一= {leadingWhitespace：3 === g.firstChild.nodeType，TBODY：！g.getElementsByTagName（ “TBODY”）的长度，htmlSerialize：!! g.getElementsByTagName（ “链接”）的长度，样式：/top/.test （t.getAttribute（ “风格”）），hrefNormalized： “/ A” === t.getAttribute（ “HREF”），不透明度：/ ^ $ 0.55 /测试（t.style.opacity），cssFloat：!! t.style.cssFloat，C heckOn： “在” === i.value，optSelected：r.selected，getSetAttribute： “T” == g.className，submitBubbles：0，changeBubbles：0，focusinBubbles：1，deleteExpando：0， noCloneEvent：0，inlineBlockNeedsLayout：1，shrinkWrapBlocks：1，reliableMarginRight：！（！0）！0}，i.checked = 0，a.noCloneChecked = i.cloneNode .checked，n.disabled = 0，一个.optDisabled =！r.disabled; try {delete g.test} catch（v）{a.deleteExpando =！1}！g.addEventListener && g.attachEvent && g.fireEvent &&（g.attachEvent（“onclick”，function（）{a。 noCloneEvent =！1}），g.cloneNode（！0）.fireEvent（ “点击”））中，i = L.createElement（ “输入”），i.value = “T”，i.setAttribute（ “类型”， “无线电”），a.radioValue = “T” === i.value，i.setAttribute（ “选中”， “选中”），g.appendChild（I）中，s = L.createDocumentFragment（），s.appendChild （g.firstChild），a.checkClone = s.cloneNode（！0）.cloneNode（！0）.lastChild.checked，g.innerHTML = “”，g.style.width = g.style.paddingLeft = “1像素” ，L = L.getElementsByTagName（ “正文”）[0]，C = L.createElement（L “DIV”？： “体”）中，f = {能见度： “隐藏”，宽度：0，高度：0，边界：0，余量：0}，升&& H.extend（F，{位置：“ABSOLU te，左：-1e3，top：-1e3}）; for（h in f）c.style [h] = f [h]; if（c.appendChild（g），u = l || y，u .insertBefore（c，u.firstChild），a.appendChecked = i.checked，a.boxModel = 2 === g.offsetWidth，g.style &&（g.style.display =“inline”中的“zoom”，g。 style.zoom = 1，a.inlineBlockNeedsLayout = 2 === g.offsetWidth，g.style.display =“”，g.innerHTML =“<div style ='width：4px;
    '> </ div>”，a .shrinkWrapBlocks = 2！== g.offsetWidth），g.innerHTML =“<table> <tr> <td style ='padding：0;
    border：0;
    display：none '> </ td> <td> /td></tr></table>",d=g.getElementsByTagName("td"),m=0===d[0].offsetHeight,d[0].style.display="",d [1] .style.display = “无”，a.reliableHiddenOffsets =米&& 0 === D [0] .offsetHeight，g.innerHTML = “”，L.defaultView && L.defaultView.getComputedStyle &&（O = L.createElement（“DIV “），o.style.width =” 0" ，o.style.marginRight = “0”，g.appendChild（○），a.reliableMarginRight = 0 ===（parseInt函数（（L.defaultView.getComputedStyle（邻， null）|| {marginRight：0}）。margin（R），{0}），c.innerHTML =“”，u.removeChild（c），g.attachEvent）for（h in {submit：1，change： 1，focusin：1}）p =“on”+ h，m = p in g，m ||（g.setAttribut e（p，“return;”），m =“function”== typeof g [p]），a [h +“Bubbles”] = m; return c = s = n = r = l = o = g = = null，a}（），H.boxModel = H.support.boxModel; var I = / ^（？：\ {。* \} | \ [。* \]）$ /，q = /（[az] ）（[AZ]）/克; H.extend（{缓存：{}，UUID：0，的expando： “jQuery的” +（H.fn.jquery +的Math.random（））。代替（/ \ D /克，“”），noData：{embed：！0，object：“clsid：D27CDB6E-AE6D-11cf-96B8-444553540000”，applet：！0}，hasData：function（e）{return e = e.nodeType？ .cache [E [H.expando]]：E [H.expando]，!!è&& R（E）}，数据：功能（E，N，R，I）{如果（H.acceptData（e））的{var o，a = H.expando，s =“string”== typeof n，l = e.nodeType，u = l？H.cache：e，c = 1？e [H.expando]：e [H .expando] && H.expando; if（c &&（！i ||！c || u [c] [a]）||！s || r！== t）return c ||（l？e [的expando] = C = ++ H.uuid：C = H.expando）中，u [C] ||（U [C] = {}，L ||（U并[c] .toJSON = H.noop））， （“object”== typeof n ||“function”== typeof n）&&（i？u [c] [a] = H.extend（u [c] [a]，n）：u [c] = H.extend（U [C]中，n）），邻= U [C]，我&&（O [α] ||（O [A] = {}），邻= O [A]）中，r！==吨&&（O [H.camelCase（N）] = R）， “事件” ==ñ||问题o [N] S 0 [H.camelCase（N）] ||问题o [N]：！？O：O [a] && o [a] .events}}，removeData：function（t，n，i）{if（H.acceptData（t））{var o = H.expando，a = t.nodeT ype，s = a？H.cache：t，l = a？t [H.expando]：H.expando; if（s [1]）{if（n）{var u = i？s [1] o]：s [l]; if（u &&（delete u [n]，！r（u）））return} if（！i ||（delete s [l] [o]，r（s [l]） ））{var c = s [l] [o]; H.support.deleteExpando || s！= e？delete s [l]：s [l] = null，c？（s [l] = {}， a ||（s [l] .toJSON = H.noop），s [l] [o] = c）：a &&（H.support.deleteExpando？delete t [H.expando]：t.removeAttribute？t.removeAttribute （H.expando）：t [H.expando] = null）}}}}，_ data：function（e，t，n）{return H.data（e，t，n，！0）}，acceptData：function （e）{if（e.nodeName）{var t = H.noData [e.nodeName.toLowerCase（）]; if（t）return！（t ===！0 || e.getAttribute（“classid” ！== t）}返回！0}}），H.fn.extend（{data：function（e，r）{var i = null; if（“undefined”== typeof e）{if（this.length && （i = H.data（this [0]），1 === this [0] .nodeType））for（var o，a = this [0] .attributes，s = 0，l = a.length; l >取值; S ++）O = A [S] .name和0 === o.indexOf（ “数据 - ”）&&（O = H.camelCase（o.substring（5））中，n（在此[0]， o，i [o]））; return i} if（“object”== typeof e）return this.each（function（）{H.data（this，e）}）; var u = e.split（“ 。“）; return u [1] = u [1]？”“+ u [1]：”“，r === t？（i = this.triggerHandler（”getData“+ u [1] + “！”，[U [0]]）中，i ===吨&& this.length &&（I = H.data（此[0]，E），i = N时（在此[0]，E，I））， i === t && u [1]？this.data（u [0]）：i）：this.each（function（）{var t = H（this），n = [u [0]，r]; t .triggerHandler（ “使用setData” + U [1] + “！”，N），H.data（此，E，R），t.triggerHandler（ “changeData” + U [1] + “！”，N）} ）}，removeData：function（e）{return this.each（function（）{H.removeData（this，e）}）}}），H.extend（{_ mark：function（e，n）{e && =（N || “FX”）+ “标记”，H.data（E，N，（H.data（E，N，T，！0）|| 0）1，！0））}，_取消标记：function（e，n，r）{if（e！==！0 &&（r = n，n = e，e =！1），n）{r = r ||“fx”; var o = r + ？标记”，一个= E 0：（！H.data（N，O，T，0）|| 1）-1;一个H.data（！N，O，A，0）:( H.removeData （N，O，0！），I（N，R， “标记”））}}，队列：功能（E，N，R）{如果（E）{N =（N || “FX”）+ “queue”; var i = H.data（e，n，t，！0）;返回r &&（！i || HisArray（r）？i = H.data（e，n，H.makeArray ），！0）：i.push（r）），i || []}}，出队：函数（e，t）{t = t ||“fx”; var n = ）中，r = n.shift（）; “INPROGRESS” ===ř&&（R = n.shift（））中，r &&（ “FX” ===吨&& n.unshift（ “INPROGRESS”），r.call（E，函数（）{H.dequeue（E，T）}）），n.length ||（H.removeData（E，T + “排队”，！0），I（E，T， “队列”））}} ），H.fn.extend（{队列：功能（E，N）{ 返回“string”！= typeof e &&（n = e，e =“fx”），n === t？Hqueue（this [0]，e）：this.each（function（）{var t =这个eque（e，n）;“fx”=== e &&“inprogress”！== t [0] && H.dequeue（this，e）}）}，dequeue：function（e）{return this.each （function（）{H.dequeue（this，e）}）}，delay：function（e，t）{return e = H.fx？H.fx.speeds [e] || e：e，t = t ||“fx”，this.queue（t，function（）{var n = this; setTimeout（function（）{H.dequeue（n，t）}，e）}）}，clearQueue：function（e）{返回this.queue（e ||“fx”，[]）}，promise：function（e，n）{function r（）{ -  l || o.resolveWith（a，[a]）}“string” ！= typeof e &&（n = e，e = t），e = e ||“fx”; for（var i，o = H.Deferred（），a = this，s = a.length，l = U = E + “推迟”，C = E + “队列” 中，f = E + “标记”; S  - ）（I = H.data（A [s]时，U，T，0！）||（H。数据（[s]时，C，T，！0）|| H.data（A [s]时，F，T，！0））&& H.data（一个[秒]中，u，H._Deferred（）， ！0））&&（l ++，i.done（r））; return r（），o.promise（）}}）; var _，R，W = / [\ n \ t \ r] / g，$ = / \ S + / Z = / \ R / G，X = / ^（?:按钮|输入）$ / I，V = / ^（?:按钮|输入|对象|选择| textarea的）$ / I， U = / ^一个（？：REA）？$ / I，J = / ^（?:自动对焦|自动播放|异步|检查|控件|推迟|禁用|隐|环|多个|开放|只读|所需|作用域| 选择）$ / i，Y = / \：| ^ on /; H.fn.extend（{attr：function（e，t）{return H.access（this，e，t，！0，H.attr） }，removeAttr：function（e）{return this.each（function（）{H.removeAttr（this，e）}）}，prop：function（e，t）{return H.access（this，e，t， ！0，H.prop）}，removeProp：function（e）{return e = H.propFix [e] || e，this.each（function（）{try {this [e] = t，delete this [e ]}，addClass：function（e）{var t，n，r，i，o，a，s; if（H.isFunction（e））return this.each（function t（e）=（e），（n），n = 0，R = this.length; R> N;在n ++）如果（ⅰ=此[n]的，1 === i.nodeType）如果（i.className || 1 == t.length）{对于（邻！ =“”+ i.className +“”，a = 0，s = t.length; s> a; a ++）〜o.indexOf（“”+ t [a] +“”）||（o + = t [a ] +;“）; i.className = H.trim（o）} else i.className = e; return this}，removeClass：function（e）{var n，r，i，o，a，s，l; if（HisFunction（e））返回this.each（function（t）{H（this）.removeClass（e.call（this，t，this.className））}）; if（e &&“string”==对于（n =（e ||“”），split（$），r = 0，i = this.length; i> r; r ++）if（o = this [r ]，1 === o.nodeType && o.cla ssName）if（e）{for（a =（“”+ o.className +“”）.replace（W，“”），s = 0，l = n.length; l> s; s ++）a = a。 replace（“”+ n [s] +“”，“”）; o.className = H.trim（a）} else o.className =“”; return this}，toggleClass：function（e，t）{var n = typeof e，r =“boolean”== typeof t; return this.each（H.isFunction（e）？function（n）{H（this）.toggleClass（e.call（this，n，this.className ，t），t）}：function（）{if（“string”=== n）for（var i，o = 0，a = H（this），s = t，l = e.split ;其中i = 1的[o ++]）S = R S：a.hasClass（i）中，[S “addClass”？： “removeClass”]！（ⅰ）;否则（ “未定义” ===ñ|| “布尔” === N）&&（this.className && H._data（此， “__的className __”，this.className），this.className = this.className ||ë=== 1 “！？”：H._data（此，” __className __“）}，hasClass：function（e）{for（var t =”“+ e +”“，n = 0，r = this.length; r> n; n ++）if（（ “”+ +这个[n] .className +“”）.replace（W，“”）.indexOf（t）>  -  1）return！0; return！1}，val：function（e）{var n， i = this [0]; if（！arguments.length）return i？（n = H.valHooks [i.nodeName.toLowerCase（）] || HvalHooks [i.type]，n &&“get”in n && r = n.get（i，“value”））！== t？r：（r = i.value，“string”== typeof r？r.replace（z，“”）：null == r？ “”：r））：t; var o = H.isFunction（e）; return this.each（function（r）{var i，a = H（this）; 1 === this.nodeType && ？e.call（this，r，a.val（））：e，null == i？i =“”：“number”== typeof i？i + =“”：H.isArray（i）&& = H.map（i，function（e）{return null == e？“”：e +“”}）），n = H.valHooks [this.nodeName.toLowerCase（）] || H.valHooks [this。类型]，n &&“set”在n && n.set（this，i，“value”）！== t ||（this.value = i））}）}}），H.extend（{valHooks：{option： {get：function（e）{var t = e.attributes.value; return！t || t.specified？e.value：e.text}}，选择：{get：function（e）{va rt，n = e.selectedIndex，r = []，i = e.options，o =“select-one”=== e.type; if（0> n）返回null; for（var a = o？n ：0，s = o？n + 1：i.length; s> a; a ++）{var l = i [a]; if（！（！l.selected ||（H.support.optDisabled？l.disabled ：空== l.getAttribute（ “无效”））|| l.parentNode.disabled && H.nodeName（l.parentNode “OPTGROUP”）））{如果（T = H（L）.VAL（），O）返回t; r.push（t）}} return o &&！r.length && i.length？H（i [n]）。val（）：r}，set：function（e，t）{var n = H.makeArray （t）; return H（e）.find（“option”）。each（function（）{this.selected = H.inArray（H（this）.val（），n）> = 0}），n。长度||（e.selectedIndex = -1）中，n}}}，attrFn：{VAL：0，CSS：0，HTML：0，文本：0，数据：0，宽度：0， height：！0，offset：！0}，attrFix：{tabindex：“tabIndex”}，attr：function（e，n，r，i）{var o = e.nodeType; if（！e || 3 == = o || 8 === o || 2 === o）return t; if（i && n in H.attrFn）return H（e）[n]（r）; if（！（e中的“getAttribute” ）返回H.prop（e，n，r）; var a，s，l = 1！== o ||！HisXMLDoc（e）; return l &&（n = H.attrFix [n] || n， S = H.attrHooks [n]的，S ||（J.TEST（N）S = R：？_ && “的className” == N &&（H.nodeName（即， “形式”）|| Y.test（N！ ））&&（S = _））），R ==牛逼空=== R（H.removeAttr（E，N），T）：？？s &&“S 等于s && l &&（a = s.set（e，r，n））！== t？a：（e.setAttribute（n，“”+ r），r）：s &&“get”in s && l && null！ （a = s.get（e，n））？a：（a = e.getAttribute（n），null === a？t：a）}，removeAttr：function（e，t）{var n; 1 === e.nodeType &&（T = H.attrFix [吨] ||吨，H.support.getSetAttribute？e.removeAttribute（吨）:( H.attr（E，T， “”），e.removeAttributeNode（E在e &&（e [n] =！1））}中的att .Hooks：{type：{set：函数（e，t）{if（X.test（e.nodeName）&& e.parentNode）H.error（“type property can not be changed”）; else if（！H.support.radioValue &&“radio”== = t && H.nodeName（e，“input”））{var n = e.value; return e.setAttribute（“type”，t），n &&（e.value = n），t}}}，tabIndex：{get ：function（e）{var n = e.getAttributeNode（“tabIndex”）; return n && n.specified？parseInt（n.value，10）：V.test（e.nodeName）|| U.test（e.nodeName） && e.href？0：t}}，value：{get：function（e，t）{return _ && H.nodeName（e，“button”）？_。get（e，t）：t in e？e.value ：null}，set：function（e，t，n）{return _ && H.nodeName（e，“button”）？_。set（e，t，n）：void（e.value = t）}}}， propFix：{tabindex属性 “的tabIndex” 只读 “readOnly的”， “对”：“HT mlFor “ ”阶级“： ”类名“，最大长度： ”最大长度“，CELLSPACING： ”CELLSPACING“，CELLPADDING： ”CELLPADDING“，行跨度： ”行跨度“，合并单元格： ”合并单元格“，USEMAP： ”USEMAP“ FRAMEBORDER：” frameBorder“，contenteditable：”contentEditable“}，prop：function（e，n，r）{var i = e.nodeType; if（！e || 3 === i || 8 === i || 2 = == i）return t; var o，a，s = 1！== i ||！HisXMLDoc（e）; return s &&（n = H.propFix [n] || n，a = H.propHooks [一个&&（o = a.set（e，r，n））中的r！== t？a &&“set”！== t？o：e [n] = r：a &&“get”in a＆ （o = a.get（e，n））！== t？o：e [n]}，propHooks：{}}），R = {get：function（e，n）{return H.prop ，n）？n.toLowerCase（）：t}，set：function（e，t，n）{var r; return t ===！1？H.removeAttr（e，n）:( r = H.propFix [n] || n，e在e &&（e [r] =！0），e.setAttribute（n，n.toLowerCase（））），n}}，H.support.getSetAttribute ||（H.attrFix = H.propFix，_ = H.attrHooks.name = H.attrHooks.title = H.valHooks.button = {get：function（e，n）{var r; return r = e.getAttributeNode（n），r &&“” ！== r.nodeValue？r.nodeValue：t}，set：function（e，t，n）{var r = e.getAttributeNode（n）; return r？（r.nodeValue = t，t）：void 0 }}，H.each（[ “宽度”， “高度”]，功能（E，T）{H.attrHooks [T] = H .extend（hattrHooks [t]，{set：function（e，n）{return“”=== n？（e.setAttribute（t，“auto”），n）：void 0}}）}） ），H.support.hrefNormalized || H.each（[的 “href”， “SRC”， “宽度”， “高度”]，功能（E，N）{H.attrHooks [N] = H.extend（H .attrHooks [n]，{get：function（e）{var r = e.getAttribute（n，2）; return null === r？t：r}}）}），H.support.style ||（ H.attrHooks.style = {get：function（e）{return e.style.cssText.toLowerCase（）|| t}，set：function（e，t）{return e.style.cssText =“”+ t} }），H.support.optSelected ||（H.propHooks.selected = H.extend（H.propHooks.selected，{get：function（e）{var t = e.parentNode; t &&（t.selectedIndex，t。 parentNode && t.parentNode.selectedIndex）}}）），H.support.checkOn || H.each（[ “无线电”， “复选框”]，函数（）{H.valHooks [此] = {得到：函数（e）中{return null === e.getAttribute（“value”）？“on”：e.value}}}），H.each（[“radio”，“checkbox”]，function（）{H.valHooks ] = H.extend（H.valHooks [this]，{set：function（e，t）{return H.isArray（t）？e.checked = H.inArray（H（e）.val（），t） > = 0：void 0}}）}）; var G = / \。（。*）$ /，K = / ^（？：textarea | input | select）$ / i，Q = / \ Z = / /g,ee=/[^\w\s.|`]/g ，e = {（e，n，r，i）{if（3！== e。 nodeType && 8！== e.nodeType）{if（r ===！1）r = o; else if（！r）return; var a，s; r.handler &&（a = r，r = a.handler） r.guid ||（r.guid = H.guid ++）; var l = H._data（e）; if（l）{var u = l.events，c = l.handle; u ||（l.events = u = {}），c ||（l.handle = c = function（e）{return“undefined”== typeof H || e && H.event.triggered === e.type？t：H.event。 handle.apply（c.elem，arguments）}），c.elem = e，n = n.split（“”）; for（var f，d，p = 0; f = n [p ++];）{s ？=一个H.extend（{}，A）：{处理程序：R，数据：I}？ -  “ ”f.indexOf（“。”）>图1（d = f.split（）中，f = D .shift（），s.namespace = d.slice（0）的.sort（）。加入（ “ ”））:( D = []，s.namespace =“”），s.type = F，S。 guid ||（s.guid = r.guid）; var h = u [f]，m = H.event.special [f] || {}; h ||（h = u [f] = []， m.setup && m.setup.call（E，I，D，C）== 1 ||（e.addEventListener e.addEventListener（F，C，1）：！？！e.attachEvent && e.attachEvent（ “接通” + F，C））），m.add &&（m.add.call（E，S），s.handler.guid ||（s.handler.guid = r.guid）），h.push（一个或多个），H .event.global并[f] = 0} E = NULL}}}，全球：{}，除去：功能（E，N，R，I）{如果（3 == e.nodeType && 8 ==ë！。节点类型）{R === 1 &&（R = 0）;！v （e），v = y && y.events; if（y && v）= a，y，...， if（n && n.type &&（r = n.handler，n = n.type），！n ||“string”== typeof n &&“。”=== n.charAt（0））{n = n ||“ “; for（s in v）H.event.remove（e，s + n）} else {for（n = n.split（”“）; s = n [g ++];）if（m = s，h = null，u = s.indexOf（“。”）<0，c = []，u ||（c = s.split（“。”），s = c.shift（），f = new RegExp “（？。？\\（：* \\）”）|（^ \\）+ H.map（c.slice（0）的.sort（），TE）。加入 “+”（\\ 。| $）“）），p = v [S]）如果（R）{对于（D = H.event.special [秒] || {}，L = 1 || 0;升<p.length &&（ H = p [1]，r.guid == h.guid ||（（U || f.test（h.namespace））&&（空==我&& p.splice（1  - ！，1）中，d。除去&& d.remove.call（E，H）），空== I））;升++）;！（0 === p.length ||空= I && 1 === p.length）&&（d.teardown && d.teardown （l = 0; l <p.length（e，c）！==！1 || H.removeEvent（e，s，y.handle），a = null，delete v [s] ;升++）H = p [1]，（U || f.test（h.namespace））&&（H.event.remove（E，M，h.handler，1），p.splice（L--， 1））; if（H.isEmptyObject（v））{var b = y.handle; b &&（b.elem = null），删除y.events，删除y.handle，H.isEmptyObject（y）&& H.removeData E，T，0）}}}}，自定义事件：{的getData：0，使用setData：0，changeData：0}，触发：乐趣 c（n，r，i，o）{var a，s = n.type || n，l = [];
如果（s.indexOf（ “！”）> = 0 &&（S = s.slice（0，-1）中，a =！0），s.indexOf（ “”）> = 0 &&（L = s.split（ “ ”），S = l.shift（），l.sort（））中，i &&！H.event.customEvent [秒] || H.event.global [S]）{如果（N =“ 对象”= = typeof n？n [H.expando]？n：new H.Event（s，n）：new H.Event（s），n.type = s，n.exclusive = a，n.namespace = l.join （“。”），n.namespace_re = new RegExp（“（^ | \\。）”+ l.join（“\\。（？？。* \\。）？”）+“（\\。 $）“），（o ||！i）&&（n.preventDefault（），n.stopPropagation（）），！i）return void H.each（H.cache，function（）{var e = H.expando ，T =此并[e];吨&& t.events && t.events [秒] && H.event.trigger（N，R，t.handle.elem）}）;！如果（3 == i.nodeType && 8 == i.nodeType ）{n.result = t，n.target = i，r = null！= r？H.makeArray（r）：[]，r.unshift（n）; var u = i，c = s.indexOf（“ ：“）<0？”on“+ s：”“; do {var f = H._data（u，”handle“）; n.currentTarget = u，f && f.apply（u，r），c && H.acceptData U）&& U [C] && U [C]。适用（U，R）===！1 &&（n.result =！1，n.preventDefault（））中，u = u.parentNode || || u.ownerDocumentü === n.target.ownerDocument && e} while（u &&！n.isPropagationStopped（））; if（！n.isDefaultPrevented（））{var d，p = H.event.special [s] || {}; if ！（p._default && p._default.call（i.ownerDocum 耳鼻喉科，N）！==！1 || “点击” ===小号&& H.nodeName（I， “A”）||！H.acceptData（I）））{尝试{C &&我[秒] &&（D = 1并[c]，D &&（ⅰ并[c] = NULL），H.event.triggered = S，I [S]（））}赶上（H）{}ð&&（ⅰ并[c] = D），H.event。 trigger = t}} return n.result}}}，handle：function（n）{n = H.event.fix（n || e.event）; var r =（（H._data（this，“events” ）|| {}）[n.type] || []）片（0）中，i = n.exclusive && n.namespace，O = Array.prototype.slice.call（参数，0）;！问题o [ 0] = n，n.currentTarget = this; for（var a = 0，s = r.length; s> a; a ++）{var l = r [a]; if（i || n.namespace_re.test l.namespace））{n.handler = l.handler，n.data = l.data，n.handleObj = l; var u = l.handler.apply（this，o）; if（u！== t && n.result = u，u ===！1 &&（n.preventDefault（），n.stopPropagation（））），n.isImmediatePropagationStopped（））break}} return n.result}，道具：“altKey attrChange attrName bubbles button可取消charCode clientX clientY ctrlKey currentTarget数据详细信息eventPhase fromElement处理程序keyCode layerX layerY metaKey newValue offsetX offsetY pageX pageY prevValue relatedNode relatedTarget screenX screenY shiftKey srcElement target toElement view wheelD elta which“.split（”“），fix：function（e）{if（e [H.expando]）return e; var n = e; e = H.Event（n）; for（var r，i = this.props.length; I;）R = this.props [ -  I]，E [R] = N [R];若（e.target ||（e.target = e.srcElement || L）， 3 === e.target.nodeType &&（e.target = e.target.parentNode）,! e.relatedTarget && e.fromElement &&（e.relatedTarget = e.fromElement === e.target?e.toElement:e.fromElement） ，null == e.pageX && null！= e.clientX）{var o = e.target.ownerDocument || L，a = o.documentElement，s = o.body; e.pageX = e.clientX +（a && a.scrollLeft | | S && s.scrollLeft || 0） - （一&& a.clientLeft ||小号&& s.clientLeft || 0），e.pageY = e.clientY +（一个&& a.scrollTop ||小号&& s.scrollTop || 0） - （一&& a.clientTop || s && s.clientTop || 0）} return null！= e.which || null == e.charCode && null == e.keyCode ||（e.which = null！= e.charCode？e.charCode：e.keyCode） ，e.metaKey && e.ctrlKey &&（e.metaKey = e.ctrlKey），e.which || e.button ===吨||（e.which = 1＆e.button 1：！？2＆e.button 3：4＆E。按钮2：0），E}，GUID：1E8，代理：H.proxy，特殊：{准备：{设置：H.bindReady，拆卸：H.noop}，住：{增加：功能（E）{H .event.add（此，U（e.origType，e.selector），H.extend（{}，E，{H andler：升，GUID：e.handler.guid}））}，除去：功能（E）{H.event.remove（此，U（e.origType，e.selector）中，e）}}，beforeunload：{设置：功能（例如，T，N）{H.isWindow（本）&&（this.onbeforeunload = N）}，拆解：功能（E，T）{this.onbeforeunload ===吨&&（this.onbeforeunload = NULL） ？}}}}，H.removeEvent = L.removeEventListener功能（例如，T，N）{e.removeEventListener && e.removeEventListener（T，N，1！）}：功能（例如，T，N）{e.detachEvent &&即detachEvent（“on”+ t，n）}，H.Event = function（e，t）{return this.preventDefault？（e && e.type？（this.originalEvent = e，this.type = e.type，this。 isDefaultPrevented = e.defaultPrevented || e.returnValue === 1 || e.getPreventDefault && e.getPreventDefault（）一个：！O）：this.type = E，T && H.extend（此，T），this.timeStamp = H .now（），void（this [H.expando] =！0））：new H.Event（e，t）}，H.Event.prototype = {preventDefault：function（）{this.isDefaultPrevented = a; var e = this.originalEvent; e &&（e.preventDefault？e.preventDefault（）：e.returnValue =！1）}，stopPropagation：function（）{this.isPropagationStopped = a; var e = this.originalEvent; e && stopPropagation && e.stopProp agate（），e.​​cancelBubble =！0）}，stopImmediatePropagation：function（）{this.isImmediatePropagationStopped = a，this.stopPropagation（）}，isDefaultPrevented：o，isPropagationStopped：o，isImmediatePropagationStopped：o}; var ne = function e）{var t = e.relatedTarget，n =！1，r = e.type; e.type = e.data，t！== this &&（t &&（n = H.contains（this，t）），n ||（H.event.handle.apply（此，自变量），e.type = R））}，再=函数（E）{e.type = e.data，H.event.handle.apply（此，参数）};如果（H.each（{的mouseenter： “鼠标悬停”，鼠标离开： “鼠标移开”}，功能（E，T）{H.event.special并[e] = {设置：函数（n）的{H。 event.add（此，T，N && n.selector重新：NE，E）}，拆解：功能（E）{H.event.remove（此，T，E && e.selector重新：NE）}}}）， H.support.submitBubbles ||（H.event.special.submit = {setup：function（e，t）{return H.nodeName（this，“form”）？！1：（H.event.add（this， “click.specialSubmit”，function（e）{var t = e.target，n = t.type;“submit”！== n &&“image”！== n ||！H（t）.closest（“form “）.length || s（”submit“，this，arguments）}），void H.event.add（this，”keypress.specialSubmit“，function（e）{var t = e.target，n = t。类型;” 文本 “！== N &&” 密码 “！== ||ň！H（t）的.closest（” 形式 “）。长度|| 13！== e.keyCode || S（” 提交”，这一点，参数） }}），teardown：function（e）{H.event.remove（this，“。specialSubmit”）}}），！H.support.changeBubbles）{var ie，oe = function（e）{var t = ？e.type中，n = e.value;返回 “无线电” ===吨|| “复选框” === T N = e.checked： “选择-多个” === T N = e.selectedIndex> -1？H.map（e.options，function（e）{return e.selected}）。join（“ - ”）：“”：H.nodeName（e，“select”）&&（n = e.selectedIndex ），n}，ae = function（e）{var n，r，i = e.target; K.test（i.nodeName）&&！i.readOnly &&（n = H._data（i，“_ change_data” R = OE（ⅰ），（ “事件的内容”！== e.type || “无线电”！== i.type）&& H._data（I， “_ change_data” 中，r）中，n！==吨&&ř！== N &&（零= N || R 1）&&（e.type = “变化”，e.liveFired = t时，H.event.trigger（E，参数[1] i）中，））}; H.event.special .change = {filters：{focusout：ae，beforedeactivate：ae，click：function（e）{var t = e.target，n = H.nodeName（t，“input”）？t.type：“”; “radio”=== n ||“checkbox”=== n || H.nodeName（t，“select”））&& ae.call（this，e）}，keydown：function（e）{var t = e ？.TARGET中，n = H.nodeName（T， “输入”）t.type： “”;（13 === e.keyCode && H.node！名称（T， “文本区域”）|| 32 === e.keyCode &&（ “复选框” ===Ñ|| “无线电” === n）的|| “选择-多个” === N）&& ae.call （this，e）}，beforeactivate：function（e）{var t = e.target; H._data（t，“_ change_data”，oe（t））}}，setup：function（e，t）{if “file”=== this.type）return！1; for（var n in ie）H.event.add（this，n +“。specialChange”，ie [n]）; return K.test（this.nodeName） }，teardown：function（e）{return H.event.remove（this，“。specialChange”），K.test（this.nodeName）}}，ie = H.event.special.change.filters，ie.focus = ie.beforeactivate} H.support.focusinBubbles || H.each（{focus：“focusin”，blur：“focusout”}，function（e，t）{function n（e）{var n = H.event。 fix（e）; n.type = t，n.originalEvent = {}，H.event.trigger（n，null，n.target），n.isDefaultPrevented（）&& e.preventDefault（）} var r = 0; H .event.special [T] = {设置：功能（）{0 ===  -  [R ++ && L.addEventListener（E，N，0！）}，拆解：函数（）{0 ===  -  R的&& L.removeEventListener （E，N，！0）}}}），H.each（[ “绑定”， “一个”]，功能（E，N）{H.fn [N] =函数（E，R，I）{ var o; if（“object”== typeof e）{for（var a in e）this [n]（a，r，e [a]，i）; return this} if（（2 === arguments。长度 || r ===！1）&&（i = r，r = t），“one”=== n？（o = function（e）{return H（this）.unbind（e，o），i 。适用（在此，自变量）}，o.guid = i.guid || H.guid ++）：O = I， “卸载” ===è&& “一个” == n）的this.one（E，R， i）; else for（var s = 0，l = this.length; l> s; s ++）H.event.add（this [s]，e，o，r）; return this}}），H.fn对于（var n = 0，r = this.length; r> n; n ++）的.extend（{unbind：function（e，t）{if（“object”！= typeof e || e.preventDefault））H.event代表：函数（e，t，n，r）{（e，t，n，r） return this.live（t，n，r，e）}，undelegate：function（e，t，n）{return 0 === arguments.length？this.unbind（“live”）：this.die（t， null，n，e）}，trigger：function（e，t）{return this.each（function（）{H.event.trigger（e，t，this）}）}，triggerHandler：function（e，t） {return this [0]？H.event.trigger（e，t，this [0]，！0）：void 0}，toggle：function（e）{var t = arguments，n = eguid || H .guid ++，r = 0，i = function（n）{var i =（H.data（this，“lastToggle”+ eguid）|| 0）％r; return H.data（this，“lastToggle” e.guid，I + 1），n.preventDefault（），T [1]。适用（在此，自变量）|| 1};！为（i.guid = N; R <t.length）吨[R ++ ] .guid = n; return this.click（i）}，hover：function（e，t）{return this.mouseenter（e）.mouseleave（t || e）}}）; var se = {focus：“focusin”模糊： “事件的内容”，的mouseenter： “鼠标悬停”，鼠标离开： “鼠标移出”}; H.each（[ “活”， “管芯”]，功能（E，N）{H.fn [N] =函数（例如，r，i，a）{var s，l，c，f，d = 0，p = a || this.selector，h = a？this：H（this.context）; if（“object”==如果（“die”=== n &&！e && a &&“。=” == a.charAt（0））return h.unbind（a），this; for（（r ===！1 || H.isFunction（r））&&（i = r || o，r = t） ，e =（e ||“”）split（“”）; null！=（s = e [d ++]）;）if（l = G.exec（s），c =“”，l &&（c = L [0]，S = s.replace（G “”））， “悬停”！== S）如果（F = S，SE [秒]（e.push（SE [S] + c）中， s + = c）：s =（se [s] || s）+ c，“live”=== n）for（var g = 0，y = h.length; y> g; g ++）H.event。 add（h [g]，“live”。+ u（s，p），{data：r，selector：p，handler：i，origType：s，origHandler：i，preType：f}）; else h.unbind （“live”）+ e（s，p），i）; else e.push（“mouseenter”+ c，“mouseleave”+ c）; return this}}），H.each（“blur focus focusin focusout load调整大小滚动卸载点击dblclick mousedown mouseup mousemove mouseover mouseout mo （e，t）{H.fn [t] =函数（e，n）{返回null == n &&（n = e，e =空），的arguments.length> 0 this.bind（T，E，N）：！this.trigger（T）}，H.attrFn &&（H.attrFn [T] = 0）}），函数（）{函数e（e，t，n，r，i，o）{for（var a = 0，s = r.length; s> a; a ++）{var l = r [a]; if（l）{var u = 1;！为（L = L并[e];升;）{如果（l.sizcache === N）【U = R [l.sizset];！断裂}如果（1 == l.nodeType || ø||（l.sizcache = N，l.sizset = a）中，l.nodeName.toLowerCase（）===吨）{U =升;破} L = L [E]}  -  [R [α] = U}对于（var a = 0，s = r.length; s> a; a ++）{var l = r [a]; if（l） {var u =！1; for（l = 1 [e]; l;）{if（l.sizcache === n）{u = r [l.sizset]; break} if（1 === nodeType）if（o ||（l.sizcache = n，l.sizset = a），“string”！= typeof t）{if（l === t）{u =！0; break}} else if c.filter（t，[l]）。length> 0）{u = l; break} l = 1 [e]} r [a] = u}}} var r = /（（？ ：\（[^（）] + \）| [^（）] +）+ \）| \ [（？：\ [[^ \ [\]] * \] | [ '“][ ^ '”] * ['“] | [ ^ \ [\]'”] +）+ \] | \\。| [^> +〜，（\ [\\] +）+ | [> +〜]）（\ s *，\ S *） - （（：|？\ r | \ n）的*）/ G，I = 0，O = Object.prototype.toString，A = 1，S = 0，L = / \！ \ / g，u = / \ W /; [0,0] .sort（function（）{return s =！1,0 }）; var c = function（e，t，n，i）{n = n || []，t = t || L; var a = t; if（1！== t.nodeType && 9！ .nodeType）return []; if（！e ||“string”！= typeof e）return n; var s，l，u，p，h，g，y，v，x =！0，T = c。 isXML（t），w = []，N = e; do if（r.exec（“”），s = r.exec（N），s &&（N = s [3]，w.push ]）中，s [2]））{p = S [3];}断裂而（一个或多个）;如果（w.length> 1个&& d.exec（E））如果（2 === w.length && f.relative [瓦特[0]] l = b（w [0] + w [1]，t）; else（l = f.relative [w [0]]？[t]：c（w.shift ）; w.length;）e = w.shift（），f.relative [e] &&（e + = w.shift（）），l = b（e，l）; else if（！i && w.length> 1 && 9 === t.nodeType && T！&& f.match.ID.test（W [0]）&&！f.match.ID.test（W [w.length-1]）&&（H = c.find（w.shift （），T，T），T = h.expr c.filter（h.expr，h.set）[0]：？h.set [0]），T）为（H = I {EXPR：瓦特.pop（），设置：M（i）}其中：c.find（w.pop（），1 == w.length || “〜” == W [0] && “+” ==瓦特！ [0] || t.parentNode吨：！t.parentNode，T），L = h.expr c.filter（h.expr，h.set）：？h.set，w.length> 0 U = M（L）：X = 1; w.length;）G = w.pop（）中，Y = G，f.relative [G] Y = w.pop（）：G = “”，空==？ y &&（y = t），f.relative [g]（u，y，T）; else u = w = []; if（u ||（u = 1），u || c.error e），“[object Array]”=== o.call（u））if（x）if（t && 1 === t.nodeType）for（v = 0; null！= u [v]; v ++）u [v] &&（u [v] ===！0 || 1 === u [v] .nodeType && c.contains（t，u [v]））&& n.push（l [v]）; else for v = 0; null！= u [v]; v ++）u [v] && 1 === u [v] .nodeType && n.push（l [v]）; else n.push.apply（n，u）; else m（u，n）;返回p &&（c（p，a，n，i），c.uniqueSort（n）），n}; c.uniqueSort = function（e）{if（y &&（a = s，e对于（var t = 1; t <e.length; t ++）e [t] === e [t-1] && e.splice（t  - ，1）;返回e }，c.matches = function（e，t）{return c（e，null，null，t）}，c.matchesSelector = function（e，t）{return c（t，null，null，[e]） .length> 0}，c.find = function（e，t，n）{var r; if（！e）return []; for（var i = 0，o = f.order.length; o> i; i ++）{var a，s = f.order [i]; if（a = f.leftMatch [s] .exec（e））{var u = a [1]; if（a.splice（1,1） ， “\\”！== u.substr（u.length-1）&&（一个[1] =（A [1] || “”）。代替（1， “”）中，r = f.find [ s]（a，t，n），null！= r））{e = e.replace（f.match [s]，“”）; break}}} return r ||（r =“undefined”！=类型t.getElementsByTagName？t.getElementsByTagName（“*”）：[]），{set：r，expr：e}}，c.filter = function（e，n，r，i）{for（var o，a ，s = e，l = []，u = n，d = n && n [0] && c.isXML（n [0]）; e && n.length;）{for（var p in f.filter）if（null！ （o = f.leftMatch [p] .exec（e））&& o [2]）{var h，m，g = f .filter [P]，Y = 0 [1];如果（！a = 1时，o.splice（1,1）， “\\” === y.substr（y.length-1））继续;如果（U ===升&&（L = []），f.preFilter [p]）如果（O = f.preFilter [p]（O型，U，R，L，I，D））{如果（O == =（0）=（0）for（var = 0; null！=（m = u [v]）; v ++）if（m）{h = g（m， o，v，u）; var b = i ^ !! h; r && null！= h？b？a =！0：u [v] =！1：b &&（l.push（m），a =！0） }如果（H ==吨！）{如果（R ||（U = 1时）中，e = e.replace（f.match [p]， “”）,!一个）返回[];破}}如果（ e === s）{if（null！= a）break; c.error（e）} s = e} return u}，c.error = function（e）{throw“语法错误，无法识别的表达式： e}; var f = c.selectors = {order：[“ID”，“NAME”，“TAG”]，匹配：{ID：/＃（（？：[\ w \ u00c0- \ uFFFF \ \\）+）/，CLASS：/ \（（：。？[\ W \ u00c0- \ uFFFF \  - ] | \\）+）/，NAME：/ \ [名称= ['“] * （（？： [\W\u00c0 - \uFFFF\ - ] | \\。） + ） [“'] * \] /，ATTR：/ \ [\ S *（（：[\ W \ u00c0- \ uFFFF？ \  - ] | \\）+）\ S *。（？：？（\ S =）\ S *（：（['“]？）\3 | （＃（： [\（ * 。？）？：W\u00c0 - \uFFFF\ - ] | \\） * ） | ） | ）\S * \] / ，TAG： / ^（（？： [\W\u00c0 - \uFFFF\ * \ - ] | \\） + ） / ，CHILD： / :(只 | 第n | 最后 | 第一）柴尔德（：\（\S * （即使 | 奇数 | （：？？？ [ + \ - ]\D + |（ ? :？？？？？ [ + \ - ]\D * ）N\S * （： [ + \ - ]\S * \D + ）））\S * \）） / ，POS： / :(第n | 当量 | GT | LT | 第一 | 最后 | 甚至 | 奇数）（？：\（（\D * ）\）？）（ = [ ^ \ - ] | $） / ，PS EUDO： / （（： [\w\u00c0 - \uFFFF\ - ] | \\） + ？）（？：？？\（（ ['“]）（（：\（[^ \）] + ？\）| [^ \（\）] *）+）\ 2 \））/}，leftMatch：{}，attrMap：{ “类”： “的className”， “为”： “htmlFor”}，attrHandle： {eref =（e）{return e.getAttribute（“href”）} ）{var n =“string”== typeof t，r = n &&！u.test（t），i = n &&！r; r &&（t = t.toLowerCase（））; for（var o，a = S = e.length; S> A; A ++）如果（O = E [A]）{对于（（O = o.previousSibling）&& 1 == o.nodeType;！）; E [α] = I || o && o.nodeName.toLowerCase（）=== t？o ||！1：o === t} i && c.filter（t，e，！0）}，“>”：function（e，t）{var n ，r =“string”== typeof t，i = 0，o = e.length; if（r &&！u.test（t））{for（t = t.toLowerCase（）; o> i; i ++）if （n = e [i]）{var a = n.parentNode; e [i] = a.nodeName.toLowerCase（）=== t？a：！1}} else {for（; o> i; i ++） N = E [I]中，n &&（E [I] = R n.parentNode：n.parentNode ===吨）;（！T，E，0）R && c.filter}} “”：函数（T， r，o）（r）=（r），（）（）=（） ，l（“parentNode”，r，s，t，a，o）}，“〜”：function（t，r，o）{var a，s = i ++，l = n;“string”！= typeof r || u.test（R）||（R = r.toLowerCase（）中，a = R，L = E），L（” 上一个sibling“，r，s，t，a，o）}}，find：{ID：function（e，t，n）{if（”undefined“！= typeof t.getElementById &&！n）{var r = getElementById（e [1]）; return r && r.parentNode？[r]：[]}}，NAME：function（e，t）{if（“undefined”！= typeof t.getElementsByName）{for（var n = ]中，R = t.getElementsByName（E [1]）中，i = 0，O = r.length;○> I;我++）R [I] .getAttribute（ “名称”）=== E [1] &&ñ。 push（r [i]）; return 0 === n.length？null：n}}，TAG：function（e，t）{return“undefined”！= typeof t.getElementsByTagName？t.getElementsByTagName（e [1 ]）：void 0}}，preFilter：{CLASS：function（e，t，n，r，i，o）{if（e =“”+ e [1] .replace（l，“”）+“” ，o）return e; for（var a，s = 0; null！=（a = t [s]）; s ++）a &&（i ^（a.className &&（“”+ a.className +“”）.replace / [\ t \ n \ r] / g，“”）.indexOf（e）> = 0）？n || r.push（a）：n &&（t [s] =！1））; return！1 }，ID：function（e）{return e [1] .replace（l，“”）}，TAG：function（e，t）{return e [1] .replace（l，“”）toLowerCase }，CHILD：功能（E）{如果（ “第n” === E [1]）{E [2] || c.error（E [0]）中，e [2] = E [2] .replace （/ ^ \ + | \ s * / g，“”）; var t = /（ - ？）（\ d *）（？：n（[+ \  - ]？\ d *））？/ “偶” === E [2] && “2N” || “奇” === E [2] && “2N + 1” ||！/ \ D /。测试（E [2]）&&“0N + “+ E [2] || e [2]）; e [2] = t [1] +（t [2] || 1）-0，e [3] = t [3] && c.error（e [0]）; return e [0] = i ++，e}，ATTR：function（e，t，n，r，i，o）{var a = e [1] = e [1] .replace（1， “”）;回复O && f.attrMap并[a] &&（E [1] = f.attrMap [A​​]）中，E [4] =（E [4] || E [5] ||！ “e”，“e”，“e”，“e”，“e”，“e” ，T，N，I，O）{如果（ “非” === E [1]）{如果（！（（r.exec（E [3]）|| “”）。长度> 1 || / ^ \ w / .test（e [3]）））{var a = c.filter（e [3]，t，n，！0 ^ o）; return n || i.push.apply（i，a ），！1} e [3] = c（e [3]，null，null，t）} else if（f.match.POS.test（e [0]）|| f.match.CHILD.test e {0}）返回！0;返回e}，POS：function（e）{return e.unshift（！0），e}}，filter：{enabled：function（e）{return e.disabled == =！1 &&“hidden”！== e.type}，disabled：function（e）{return e.disabled ===！0}，checked：function（e）{return e.checked ===！0}选择：function（e）{return e.parentNode && e.parentNode.selectedIndex，e.selected ===！0}，parent：function（e）{return !! e.firstChild}，empty：function（e）{return！ e.firstChild}，具有：功能（例如，T，N）{返回!! C（N [3]，E）。长度}，标题：功能（E）{返回/小时\ D / i.test（例如.nodeName）}，文本：函数（e）中 {var t = e.getAttribute（“type”），n = e.type; return“input”=== e.nodeName.toLowerCase（）&&“text”=== n &&（t === n || null ===吨）}，无线电：功能（E）{返回 “输入” === e.nodeName.toLowerCase（）&& “无线电” === e.type}，复选框：功能（E）{返回“输入“=== e.nodeName.toLowerCase（）&&” 复选框 “=== e.type}，文件：函数（E）{返回” 输入 “=== e.nodeName.toLowerCase（）&&” 文件“== = e.type}，password：function（e）{return“input”=== e.nodeName.toLowerCase（）&&“password”=== e.type}，submit：function（e）{var t = e .nodeName.toLowerCase（）;返回（ “输入” ===吨|| “键” ===吨）&& “提交” === e.type}，图像：功能（E）{返回 “输入”= == e.nodeName.toLowerCase（）&&“image”=== e.type}，reset：function（e）{var t = e.nodeName.toLowerCase（）; return（“input”=== t || “button”=== t）&&“reset”=== e.type}，button：function（e）{var t = e.nodeName.toLowerCase（）; return“input”=== t &&“button”= == e.type || “键” === T}，输入：功能（E）{返回/输入|选择| textarea的|按钮/ i.test（e.nodeName）}，焦点：功能（E）{ return e === e.ownerDocument.activeElement}}，setFilters：{first：function（e，t）{return 0 === t} ，最后：function（e，t，n，r）{return t === r.length-1}，even：function（e，t）{return t％2 === 0}，odd：function ，t）{return t％2 === 1}，lt：function（e，t，n）{return t <n [3] -0}，函数（e，t，n）{return t> n [3] -0}，nth：function（e，t，n）{return n [3] -0 === t}，eq：function（e，t，n）{return n [3] -0 == = t}}，filter：{PSEUDO：function（e，t，n，r）{var i = t [1]，o = f.filters [i]; if（o）return o（e，n ，T，R）;如果（ “包含” ===ⅰ）返回（e.textContent || || e.innerText c.getText（[E]）|| “”）的indexOf（T [3]）> = 0; if（“not”=== i）{for（var a = t [3]，s = 0，l = a.length; l> s; s ++）if（a [s] === e ）返回！1; return！0} c.error（i）}，CHILD：function（e，t）{var n = t [1]，r = e; switch（n）{case“only”第一 “：为（; R = r.previousSibling;）如果（1 === r.nodeType）返回1;如果！（” 第一 “=== n）的返回0; R = E;壳体！” 最后“： for（; r = r.nextSibling;）if（1 === r.nodeType）return！1; return！0; case“nth”：var i = t [2]，o = t [3]; if 1 === i && 0 === o）return！0; var a = t [0]，s = e.parentNode; if（s &&（s.sizcache！== a ||！e.nodeIndex））{var l = 0; for（r = s.firstChild; r; r = r.nextSibling）1 === r.nodeType &&（r.nodeIndex = ++ l）; s.sizcache = a} var u = e.nodeIndex-o ; return 0 === i？0 === u：u％i === 0 && u / i> = 0}}，ID：function（e，t）{return 1 === e.nodeType && e.getAttribute（“id”）=== t}，TAG：function（e，t ）{return“*”=== t && 1 === e.nodeType || e.nodeName.toLowerCase（）=== t}，CLASS：function（e，t）{return（“”+（e.className | | e.getAttribute（“class”））+“”）.indexOf（t）>  -  1}，ATTR：function（e，t）{var n = t [1]，r = f.attrHandle [n]？ ！？f.attrHandle [n]的（E）：空= E [N] E [N]：e.getAttribute（N）中，i = R + “”，O = T [2]中，a = T [4];返回null == r？“！=”=== o：“=”=== o？i === a：“* =”=== o？i.indexOf（a）> = 0：“〜 =“=== o？（”“+ i +”“）.indexOf（a）> = 0：a？”！=“=== o？i！== a：”^ =“=== o？ 0 === i.indexOf（一）： “$ =” ===Øi.substr（i.length-则为a.length）===？答： “| =” === O I === a || i.substr（0，a.length + 1）=== a +“ - ”：！1：i && r！==！1}，POS：function（e，t，n，r）{var i = t [2]，o = f.setFilters [i]; return o？o（e，n，t，r）：void 0}}}，d = f.match.POS，p = function（e，t） {return“\\”+（t-0 + 1）}; for（var h in f.match）f.match [h] = new RegExp（f.match [h] .source + /（？ [] * \]）（？！[^ \（] * \））/。source），f.leftMatch [h] = new RegExp（/（^（？：。| \ r | \ n）*？ /.source+f.match[h].source.replace(/\\(\d+)/g,p));var m = function（e，t）{return e = Array.prototype.slice.call（即，0），T？（t.push.apply（T，E），T）：电子}; {尝试Array.prototype.slice.call（L.documentElement.childNodes，0）[0]} .nodeType赶上（克）{M =函数（ e，t）{var n = 0，r = t || []; if（“[object Array]”=== o.call（e））Array.prototype.push.apply（r，e）; else对于（var i = e.length; i> n; n ++）r.push（e [n]）;对于（; e [n]; n ++）r的if（“number”== typeof e.length） push（e [n]）; return r}} var y，v; L.documentElement.compareDocumentPosition？y = function（e，t）{return e === t？（a =！0,0）比较文档位置&& t.compareDocumentPosition？4＆e.compareDocumentPosition（t）？ -  1：1：e.compareDocumentPosition？-1：1} :( y = function（e，t）{if（e === t）return a =！0， 0; if（e.sourceIndex && t.sourceIndex）return e.sourceIndex-t.sourceIndex; var n，r，i = []，o = []，s = e.parentNode，l = t.parentNode，u = s; if（s === l）return v（e，t）; if（！s）return-1; if（！l）return 1; for（; u;）i.unshift（u），u = u。 parentNode; for（u = l; u;）o.unshift（u），u = u.parentNode; n = i.length，r = o.length; for（var c = 0; n> c && r> c; c ++ ）if（i [c]！== o [c]）return v（i [c]，o [c]）; return c === n？v（e，o [c]， -  1） （i（c），t，1）}，v =函数（e，t，n）{if（e === t）return n; for（var r = e.nextSibling; r; {if（r === t）return-1; r = r.nextSibling} return 1}），c.getText = function（e）{for（var t，n =“”，r = 0; e [r ]; R ++）T = E [R]，3 === t.nodeType || 4 === t.nodeType N + = t.nodeValue：8 == t.nodeType &&（N + = c.getText（T？！ childNodes））; return n}，function（）{var e = L.createElement（“div”），n =“script”+（new Date）.getTime（），r = L.documentElement; e.innerHTML = <a name='"+n+"'/>“，r.insertBefore（e，r.firstChild），L.getElementById（n）&&（f.find.ID = function（e，n，r）{if “undefined”！= typeof n.getElementById &&！r）{var i = n.getElementById（e [1]）; return i？i.id === e [1] ||“undefined”！= typeof i.getAttributeNode && i .getAttributeNode（“id”）。nodeValue === e [1]？[i]：t：[]}}，f.filter.ID = function（e，t）{var n =“undefined”！= typeof e.getAttributeNode && e.getAttributeNode（“id”）; return 1 === e.nodeType && n && n.nodeValue === t}），r.removeChild（e），r = e = null}（），function（）{var e = L.createElement（ “DIV”）;。e.appendChild（L.createComment（ “”）），e.getElementsByTagName（ “*”）的长度> 0 &&（f.find.TAG =函数（E，T）{风险n = t.getElementsByTagName（e [1]）; if（“*”=== e [1]）{for（var r = []，i = 0; n [i]; i ++）1 === n [I] .nodeType && r.push（n [i]）; n = r} return n}），e.innerHTML =“<a href='#'> </a>”，e.firstChild &&“undefined”！= typeof e.firstChild .getAttribute &&“＃”！== e.firstChild.getAttribute（“href”）&&（f.attrHandle.href = function（e）{return e.getAttribute（“href”，2）}），e = null} ），L.querySelectorAll &&！function（）{var e = c，t = L.createElement（“div”），n =“__ sizzle __”; if（t.innerHTML =“<p class ='TEST '></ p > “,! t.querySelectorAll || 0！== t.querySelectorAll（”。TEST“）。长度）{C =函数（T，R，I，O）{如果（R = R || L，O！&& ！c.isXML（r））{var a = / ^（\ w + $）| ^ \。（[\ w \  - ] + $）| ^＃（[\ w \ t）; if（a &&（1 === r.nodeType || 9 === r.nodeType））{if（a [1]）return m（r.getElementsByTagName（t），i）; if（a [ 2] && f.find.CLASS && r.getElementsByClassName）return m（r.getElementsByClassName（a [2]），i）} if（9 === r.nodeType）{if（“body”=== t && r.body）return m（[r.body]，i）; if（a && a [3]）{var s = r.getElementById（a [3]）; if（！s ||！s.parentNode）return m（[]，i ）; if（s.id === a [3]）return m（[s]，i）} try {return m（r.querySelectorAll（t），i）} catch（l）{}} else if 1 === r.nodeType &&“object”！== r.nodeName.toLowerCase（））{var u = r，d = r.getAttribute（“id”），P = D || N，H = r.parentNode，G = / ^ \ S * [+〜] /测试（T）;·d P = p.replace（/' / 克，“\\$＆“）：r.setAttribute（”id“，p），g && h && （r = r.parentNode）;
    try {
        if（！g || h）
        return m（r.querySelectorAll（” [id = '“+ p + ]“+ t），i）} catch（y）{} finally {d || u.removeAttribute（”id“）}}} return e（t，r，i，o）}; for（var r in e ）c [r] = e [r]; t = null}}（），function（）{var e = L.documentElement，t = e.matchesSelector || e.mozMatchesSelector || e.webkitMatchesSelector || e.msMatchesSelector ; if（t）{var n =！t.call（L.createElement（“div”），“div”），r =！1; try {t.call（L.documentElement，“[test！=']：嘶嘶“！）
    }赶上（I） {
        R = 0
    } = c.matchesSelector功能（E，I） {如果（ⅰ = i.replace（ / \ = \S * （ [ ^ '” \]] * ）\ S * \] /克， “= '$ 1 ']”），！c.isXML（e））的尝试{如果（R ||！f.match.PSEUDO.test（ⅰ）&&！/！= / .test（i））{var o = t.call（e，i）; if（o ||！n || e.document && 11！== e.document.nodeType）return o}} catch（a）{}返回c（i，null，null，[e]）。length> 0}}}（），function（）{var e = L.createElement（“div”）; e.innerHTML =“<div class ='test e＆gt;（e.lastChildName = “e”，1！ == e.ge tElementsByClassName（“e”）。length && （f.order.splice（1, 0，“CLASS”），f.find.CLASS = function（e，t，n） {
            return“undefined” == typeof t.getElementsByClassName | |n？void 0：t.getElementsByClassName（e[1]）
        }，e = null））
    }（），L.documentElement.contains？c.contains = function（e，t） {
        return e！ == t && e.contains e.contains（T）：！0）
    }：？L.documentElement.compareDocumentPosition c.contains = 函数（E，T） {返回 !! （16 e.compareDocumentPosition（T））
    }：c.contains = function（） {
        return！1
    }，c.isXML = function（e） {
        var t = （e？e.ownerDocument || e：0）.documentElement;
        return t？“HTML”！ == t.nodeName：1
    };
    var b = function（e，t） {
        for（
        var n，r = []，i = “”，o = t.nodeType？ [t]：t;
        n = f.match.PSEUDO.exec e = e[e] e + “ * ”：e;
        for（
        var a = 0，s = o.length;
        s > a;
        a++）c（e，o[a]，r）;
        return c.filter（i，r）
    };
    H.find = c，H.expr = c.selectors，H.expr[“：”] = H.expr.filters，H.unique = c.uniqueSort，H.text = c.getText，H.isXMLDoc = c.isXML，H.contains = c.contains
}（）; VAR乐 = /直到$ /，UE = / ^（?:父母| prevUntil | prevAll）/，CE = /，/，FE = / ^ [^：＃\ [\] * $ /，DE = 阵列.prototype.slice，PE = H.expr.match.POS，he = {
    children：！0，contents：！0，next：！0，prev：！0
}; H.fn.extend（ {
    find：
    function（e） {
        var t，n，r = 这个;
        if（“string”！ = typeof e）
        return H（e）.filter（
        function（） {
            for（t = 0，n = r.length;
            n > t;
            t++）
            if（H.contains t），返回！0
        }）;
        var i，o，a，s = this.pushStack（“”，“find”，e）;
        for（t = 0，n = this.length;
        n > t;吨++）如果（ⅰ = s.length，H.find（E，此 [T]，S），在t > 0）为（O = I;○ < s.length;○++）用于：（a = 0;我（a） = （（（））（）（）（）（））;
        return this.filter（
        function（） {
            for（
            var e = 0，n = t.length;
            n > e;
            e++）
            if（H.contains（this，t[e]））
            return！0
        }）
    }，不是：
    function（e） {
        return this.pushStack（f（this，e，！1），“not”，e）
    }，filter：
    function（e） {
        return this.pushStack（f（this，e，0），“filter”，e）
    }，是：
    function（e） {
        return !! e && （“string” == typeof e？H.filter（e，this）.length > 0：this.filter（e）.length > 0）
    }，最接近：
    function（e，t） {
        var n，r，i = []，o = this[0];
        if（H.isArray（e）） {
            var a，s，l = {}，U = 1;如果（邻 && e.length） {对于（n = 0时，R = e.length;
                R > N;在n++）S = E[N]，L[S] || （L[s]的 = pe.test（s）？H（s，t || this.context）：s）;
                for（;
                o && o.ownerDocument && o！ == t;） {
                    for（s in l）a = l[s] a.jquery？一.index（o） > -1：H（o）.is（a）） && i.push（ {
                        selector：s，elem：o，level：u
                    }）;
                    o = o.parentNode，u++
                }
            }
            return i
        }
        var c = pe.test（e） || “string”！ = typeof e？H（e，t || this.context）：0;
        for（n = 0，r = this.length;
        r > n;
        n++）为（○ = 此 [N];
        O;） {如果（C c.index（O2） > -1：H.find.matchesSelector（邻，E）） {
                i.push（O）;破
            }如果（o = o.parentNode，！o || ！o.ownerDocument || o === t || 11 === o.nodeType）
            break
        }
        return i = i.length > 1？Hunique（i）：i，this.pushStack（i，“nearest”，e）
    }，index：
    function（e） {
        return e && “string”！ = typeof e？H.inArray（e.jquery？e[0]：e，this）：hinArray（this[0]，e？H（e）：this.parent（）。children（））
    }，add：
    function（e，t） {
        var n = “string” == typeof e？（e，t）：H.makeArray（e && e.nodeType？ [e]：e），r = H.merge（this.get（），n）;
        return this.pushStack（c（n[0]） || c（r[0]）？r：H.unique（r））
    }和andSelf：
    function（） {
        return this.add（this.prevObject）
    }
}），H.each（ {
    parent：
    function（e）
    var t = e.parentNode;
    return t && 11！ == t.nodeType？t：null
}，parents：
function（e） {
    return H.dir（e，“parentNode”）
}，parentsUntil：
function（e，t，n） {
    return H.dir（e，“parentNode”，n）
}，next：
function（e） {
    return H.nth（e，2，“nextSibling”）
}，prev：
function e） {
    return H.nth（e，2，“previousSibling”）
}，nextAll：
function（e） {
    return H.dir（e，“nextSibling”）
}，prevAll：
function（e） {
    return H.dir E，“previousSibling”）
}，nextUntil：
function（e，t，n） {
    return H.dir（e，“nextSibling”，n）
}，prevUntil：
function（e，t，n） {
    return H.dir（e，“previousSibling”，n）
}，兄弟姐妹：
function（e） {
    return Hsibling（e.parentNode.firstChild，e）
}，children：
function（e） {
    return Hsibling（e.firstChild）
}，contents：
function（e） {
    return H.nodeName（e，“iframe”）？e.contentDocument || e.contentWindow.document：H.makeArray（e.childNodes）
}
}，
function（e，t） {
    H.fn[e] = 函数（n，r） {
        var i = H.map（this，t，n），o = de.call（arguments）;
        return le.test（e） || （r = n），r && “string” = =typeof r && （i = H.filter（r，i）），i = this.length > 1 && ！he[e]？Hunique（i）：i，（this.length > 1 || ce.test R）） && ue.test（E） && （I = i.reverse（）），this.pushStack（I，E，o.join（“”））
    }
}），H.extend（ {滤波器：功能（e，t，n） {
        return n && （e = “：not（” + e + “）”），1 === t.length？H.find.matchesSelector（t[0]，e）？ [t[]]： []：H.find.matches（e，t）
    }，dir：
    function（e，n，r） {
        for（
        var i = []，o = e[n];
        o && 9！节点类型 && （R === 吨 || 1 == o.nodeType || H（O）。是（R）！）;）1 === o.nodeType && i.push（O），O = O[n]的;
        return i
    }，nth：
    function（e，t，n，r） {
        t = t || 1;
        for（
        var i = 0;
        e && （1！ == e.nodeType || ++i！）;
        E = E[N]）;换货政...rn e
    }，sibling：
    function（e，t） {
        for（
        var n = [];
        e;
        e = e.nextSibling）1 === e.nodeType && e！ == t && n.push（e）;
        return n
    }
}）;
var me = / jQuery \ d + =“（？：\ d + | null）”/g，ge = / ^ \ s + /，ye = / <（?! area | br | col | embed | hr | img |输入|链路|元| PARAM）（（\ w：] +）[^>] *）\ / > / GI，VE = / < （ [\瓦特：] + ） / ，是 = / <TBODY /I？，XE = / <|＆＃\ W +; /，碲 = / <（?:脚本|对象|嵌入|选项|风格）/I，我们 = /检查\ S *（：[^ =] | =？ \ S * .checked）/I，NE = / \ /（Java | ECMA）脚本 / I，CE = / ^ \ S * <（！？\ [CDATA \ [| \  -  \  - ）/，EE = {
    option： [1，“ < select multiple = 'multiple' > ”，“ < / select>”]，legend：[1，“<fieldset>”，“</fieldset > ”]，thead： [1，“ < TABLE > ”，“ < / TABLE>”]，TR：[2， “<TABLE> <TBODY>”， “</TBODY > </ TABLE>”]，TD：[3“，<TABLE> < TBODY> <TR> “ ”</TR > </ TBODY> </TABLE > “]，列： [2，” < TABLE > <TBODY > </ TBODY> <COLGROUP>“，”</COLGROUP > </table>"],area:[1,"<map>","</map > "],_default:[0,"",""]};Ee.optgroup=Ee.option,Ee.tbody= Ee.tfoot = Ee.colgroup = Ee.caption = Ee.thead，Ee.th = Ee.td，H.support.htmlSerialize ||（Ee._default = [1， “分区的<div>”，“</ DIV >“]），H.fn.extend（{text：function（e）{return HisFunction（e）？this.each（function（t））{var n = H（this）; n.text调用（这一点，T，N .text（）））}）：“object”！= typeof e && e！== t？this.empty（）。append（（this [0] && this [0] .ownerDocument || L）.createTextNode（e） ：（）（）（）（）（）H（this）.wrapAll（e.call（this，t））返回this.each ）}）; if（this [0]）{var t = H（e，this [0] .ownerDocument）.eq（0）.clone（！0）; this [0] .parentNode && t.insertBefore（this [0 ]），t.map（function（）{for（var e = this; e.firstChild && 1 === e.firstChild.nodeType;）e = e.firstChild; return e}）。append（this）} return this} ，wrapInner：function（e）{return this.each（H.isFunction（e）？function（t）{H（this）.wrapInner（e.call（this，t））}：function（）{var t = H（this），n = t.contents（）; n.length？n.wrapAll（e）：t.append（e）}）}，wrap：function（e）{return this.each（function（） H（this）.wrapAll（e）}）}，unwrap：function（）{return this.parent（）。each（function（）{H.nodeName（this，“body”）|| H（this）.replaceWith （this.childNodes）}）。end（）}，append：function（）{return this.domManip（arguments，！0，function（e）{1 === this.nodeType && this.appendChild（e）}）}， prepend：function（）{return this.domManip（arguments，！0，function（e ）{1 === this.nodeType && this.insertBefore（e，this.firstChild）}）}之前：function（）{if（this [0] && this [0] .parentNode）返回this.domManip（arguments，！1 ，function（e）{this.parentNode.insertBefore（e，this）}）; if（arguments.length）{var e = H（arguments [0]）; return e.push.apply（e，this.toArray ）），this.pushStack（e，“before”，arguments）}}之后：function（）{if（this [0] && this [0] .parentNode）返回this.domManip（arguments，！1，function（e ）{this.parentNode.insertBefore（e，this.nextSibling）}）; if（arguments.length）{var e = this.pushStack（this，“after”，arguments）; return e.push.apply（e，H （参数[0]）。toArray（）），e}}，remove：function（e，t）{for（var n，r = 0; null！=（n = this [r]）; r ++） è|| H.filter（E，[N]）。长度）&&（吨|| 1！== n.nodeType ||（H.cleanData（n.getElementsByTagName（ “*”）），H.cleanData（[ n）]），n.parentNode && n.parentNode.removeChild（n））; return this}，empty：function（）{for（var e，t = 0; null！=（e = this [t]）; t ++） for（1 === e.nodeType && H.cleanData（e.getElementsByTagName（“*”））; e.firstChild;）e.removeChild（e.firstChild）; return this}，clone：function（e，t）{return E = null == e？！1：e，t = null == t？e：t，this.map（function（）{return H.clone（this，e，t）}）}，html：function（e） {if（e === t）return this [0] && 1 === this [0] .nodeType？this [0] .innerHTML.replace（me，“”）：null; if（“string”！= typeof è|| Te.test（E）||！H.support.leadingWhitespace && ge.test（E）||的Ee [（ve.exec（E）|| [ “”， “”]）[1] .toLowerCase（） ]）HisFunction（e）？this.each（function（t）{var n = H（this）; n.html（e.call（this，t，n.html（））））） empty（）。append（e）; else {e = e.replace（ye，“<$ 1></ $ 2>”）; try {for（var n = 0，r = this.length; r> n; n ++ ）1 ===此[n]的.nodeType &&（H.cleanData（此[n]的.getElementsByTagName（ “*”）），这[N] .innerHTML = E）}赶上（I）{this.empty（）。 append（e）}} return this}，replaceWith：function（e）{return this [0] && this [0] .parentNode？HisFunction（e）？this.each（function（t）{var n =这个），r = n.html（）; n.replaceWith（e.call（this，t，r））}）:(“string”！= typeof e &&（e = H（e）.detach（））， this.each（function（）{var t = this.nextSibling，n = this.parentNode; H（this）.remove（），t？H（t）.before（e）：H（n）.append ）}））：this.length this.pushStack（H（H.isFunction（E）E（）：？e）中， “replaceWith”，E）：本}，DET ach：function（e）{return this.remove（e，！0）}，domManip：function（e，n，r）{var i，o，a，s，l = e [0]，u = [] ; if（！H.support.checkClone && 3 === arguments.length &&“string”== typeof l && we.test（l））return this.each（function（）{H（this）.domManip（e，n，r，函数（i）{var o = H（this）; e [0] = l.call（this，i，n？o） HTML（）：T），o.domManip（E，N，R）}）;如果（在此[0]）{如果（S = 1 && l.parentNode，I = H.support.parentNode &&小号&& 11 === s.nodeType &&秒。 childNodes.length === this.length {片段：S}：？H.buildFragment（E，由此，U）中，a = i.fragment，O = 1 === a.childNodes.length一个= a.firstChild ：a.firstChild）{n = n && H.nodeName（o，“tr”）; for（var c = 0，f = this.length，p = f-1; f> c; c ++）r.call D（该[C]，O）：这并[c]，i.cacheable ||˚F> 1个&& p>çH.clone（A，0，0！）：A）} u.length && H.each（U， v）}返回this}}），H.buildFragment = function（e，t，n）{var r，i，o，a; return t && t [0] &&（a = t [0] .ownerDocument || t [ 0]），a.createDocumentFragment ||（a = L），1 === e.length &&“string”== typeof e [0] && e [0] .length <512 && a === L &&“<”=== E [0] .charAt（0）&&！Te.test（E [0]）&&（H.support.checkClone ||！we.test（E [0]））&&（I =！0，
O = H.fragments [E [0]]，邻&& 1！==Ö&&（R = 0））中，r ||（R = a.createDocumentFragment（），H.clean（E，A，R，N）），我&&（H.fragments [E [0]] = O R：？1），{片段：R，可高速缓存的：ⅰ}}，H.fragments = {}，H.each（{appendTo： “追加”，prependTo： “prepend”，insertBefore：“before”，insertAfter：“after”，replaceAll：“replaceWith”}，function（e，t）{H.fn [e] = function（n）{var r = [] H（n），o = 1 === this.length && this [0] .parentNode; if（o && 11 === o.nodeType && 1 === o.childNodes.length && 1 === i.length）return i [t]这个[0]），这个;对于（var a = 0，s = i.length; s> a; a ++）{var l =（a> 0？this.clone（！0）：this）.get ; H（i [a]）[t]（l），r = r.concat（l）} return this.pushStack（r，e，i.selector）}}），H.extend（{clone：function e，t，n）{var r，i，o，a = e.cloneNode（！0）; if（！（H.support.noCloneEvent && H.support.noCloneChecked || 1！== e.nodeType && 11！ .nodeType || H.isXMLDoc（E））），用于（H（E，A）中，r = M（e）中，I = M（a）中，o是0; R [O]; ++ O）H（ [R [0]，I [O]）;如果（T &&（p（E，A）中，n）），用于（R = M（e）中，I = M（a）中，o是0; R [O]; ++ o）p（r [o]，i [o]）; return r = i = null，a}，clean：function（e，t，n，r）{var i; t = t || L， “undefined”== typeof t.createElement &&（t = t.ownerDocument || t [0] && t [0] .ownerDocument | 对于（var o，a，s = []，l = 0; null！=（a = e [l]）; l ++）if（“number”== typeof a &&（a + =“”） a）{if（“string”== typeof a）if（xe.test（a））{a = a.replace（ye，“<$ 1></ $ 2>”）; var u =（ve.exec一）|| [ “”， “”]）[1] .toLowerCase（）中，c =的Ee [U] || Ee._default中，f = C [0]，D = t.createElement（ “DIV”）;对于（d.innerHTML = c [1] + a + c [2]; f  - ;）d = d.lastChild; if（！H.support.tbody）{var p = be.test（a），h ！？= “表” ==ù|| p “的<table>” == C [1] || p []：d.childNodes：！d.firstChild && d.firstChild.childNodes;对于（O = h.length -1;○> = 0;！ - O）H.nodeName（H [0]， “TBODY”）&& H [O] .childNodes.length && H [O] .parentNode.removeChild（H [O]）}！ H.support.leadingWhitespace && ge.test（a）&& d.insertBefore（t.createTextNode（ge.exec（a）[0]），d.firstChild），a = d.childNodes} else a = t.createTextNode（a）;对于（o = 0; m> o; o ++）y（a [o]），if（!H.support.appendChecked）if（a [0] &&“number”== typeof（m = a.length） ]）; else y（a）; a.nodeType？s.push（a）：s = H.merge（s，a）} if（n）for（i = function（e）{return！e.type | | Ne.test（e.type）}，L = 0; S [1];升++）如果（！ - [R || H.nodeName（S [1]， “脚本”）|| S [1] .TYPE && “文本/ JavaScript的”！== S [1] .type.toLowerCase（））{如果（1个=== S [1] .nodeType）{风险 G = H.grep（S [1] .getElementsByTagName（ “脚本”）中，i）; s.splice.apply（S，[L + 1,0] .concat（克））} n.appendChild（S [升]）} else r.push（s [l] .parentNode？s [l] .parentNode.removeChild（s [l]）：s [l]）; return s}，cleanData：function（e）{for（var T，N，R，I = H.cache，O = H.expando，A = H.event.special，S = H.support.deleteExpando，L = 0;！NULL =（R = E [1]）;升++）如果（（！r.nodeName ||！H.noData [r.nodeName.toLowerCase（）]）&&（N = R [H.expando]））{如果（T = 1 [N] && I [n]的[o]，t && t.events）{for（var u in t.events）a [u]？H.event.remove（r，u）：H.removeEvent（r，u，t.handle）; t.handle && （t.handle.elem = null）} s？delete r [H.expando]：r.removeAttribute && r.removeAttribute（H.expando），delete i [n]}}}）; var Se，Ae，ke，De = /α-\（[^）] * \）/ I，铁= /不透明度=（[^）] *）/，JE = /（[AZ] |？^毫秒）/克，乐= / ^ - \ D + （？：PX）？$ / I中，Me = / ^ - \ D /，OE = / ^ [+ \ - ] = /，他= / [^ + \ - \ \代] + /克，成为= {位置： “绝对”，可见性： “隐藏”，显示： “块”}，PE = [ “左”， “右”]，即，= [ “顶部”， “底部”]; H.fn.css = function（e，n）{return 2 === arguments.length && n === t？this：H.access（this，e，n，！0，function（e，n，r）{return r！ ？吨H.style（E，N，R）：H.css（E，N）}）}，H.extend（{cssHook s：{opacity：{get：function（e，t）{if（t）{var n = Se（e，“opacity”，“opacity”）; return“”=== n？“1”：n}返回e.style.opacity}}}，cssNumber：{fillOpacity：！0，fontWeight：！0，lineHeight：！0，opacity：！0，孤儿：！0，widows：！0，zIndex：！0，zoom： ！0}，cssProps：{ “浮动”：H.support.cssFloat “cssFloat”： “styleFloat”}，样式：！功能（E，N，R，I）{如果（E && 3 == e.nodeType && 8 = = e.nodeType && e.style）{var o，a，s = H.camelCase（n），l = e.style，u = H.cssHooks [s]; if（n = H.cssProps [s] || s ，r === t）return u &&“get”in u &&（o = u.get（e，！1，i））！== t？o：l [n]; if（a = typeof r，！ “数量” ===一个&& isNaN（R）||空== - [R ||（ “串” ===一个&& Oe.test（R）&&（R = + r.replace（他“”）+ parseFloat（H。 c（e，n）），a =“number”），“number”！== a || H.cssNumber [s] ||（r + =“px”），u &&“u” .set（e，r））=== t）））try {l [n] = r} catch（c）{}}}，css：function（e，n，r）{var i，o; return N = H.camelCase（n）时，O = H.cssHooks [N]中，n = H.cssProps [n]的|| N “cssFloat” === N &&（N = “浮动”），邻&& “获得”在（e，t，n）{var r = {}; for（var i in t）r [i] = e.style [i]，e.style [i] = t [i]; n.call（e）; for（i in t）e.style [I] = R [I]}}），H.css = H.css，H.each（[“height”，“width”]，function（e，t）{H.cssHooks [t] = {get：function（e，n，r）{var i ;返回n？0！== e.offsetWidth？b（e，t，r）:( H.swap（e，Be，function（）{i = b（e，t，r）}），i） void 0}，set：function（e，t）{return Le.test（t）？（t = parseFloat（t），t> = 0？t +“px”：void 0）：t}}}），H .support.opacity ||（H.cssHooks.opacity = {get：function（e，t）{return Fe.test（（t && e.currentStyle？e.currentStyle.filter：e.style.filter）||“”） ？parseFloat（RegExp。$ 1）/ 100 +“”：t？“1”：“”}，set：function（e，t）{var n = e.style，r = e.currentStyle; n.zoom = 1 ; var i = H.isNaN（t）？“”：“alpha（opacity =”+ 100 * t +“）”，o = r && r.filter || n.filter ||“”; n.filter = De.test （o）？o.replace（De，i）：o +“”+ i}}），H（function（）{H.support.reliableMarginRight ||（H.cssHooks.marginRight = {get：function（e，t ）{var n; return Hswap（e，{display：“inline-block”}，function（）{n = t？Se（e，“margin-right”，“marginRight”）：e.style.marginRight }}），L.defaultView && L.defaultView.getComputedStyle &&（Ae = function（e，n）{var r，i，o; return n = n.replace（je，“ -  $ 1”）toLowerCase （）中，（i = e.ownerDocument.defaultView）？（（O = i.getComputedStyle（例如 ，NULL））&&（R = o.getPropertyValue（N） “”！== - [R || H.contains（e.ownerDocument.documentElement，E）||（R = H.style（E，N））） ，r）：t}），L.documentElement.currentStyle &&（ke = function（e，t）{var n，r = e.currentStyle && e.currentStyle [t]，i = e.runtimeStyle && e.runtimeStyle [t]，o = e.style;返回Le.test（R）&& Me.test（R）&&（N = o.left，我&&（e.runtimeStyle.left = e.currentStyle.left），o.left = “fontSize的” ==！ = T “1em的”：R || 0，R = o.pixelLeft + “PX”，o.left = N，I &&（e.runtimeStyle.left = i））的“” === R' “自动”： r}），Se = Ae || ke，H.expr && H.expr.filters &&（H.expr.filters.hidden = function（e）{var t = e.offsetWidth，n = e.offsetHeight; return 0 ===吨&& 0 ===ñ||！H.support.reliableHiddenOffsets && “无” ===（e.style.display || H.css（例如， “显示”））}，H.expr.filters.visible =函数（ e）{return！H.expr.filters.hidden（e）}）; var qe，_e，Re = /％20 / g，We = / \ [\] $ /，$ e = / \ r？\ n / g，ze = /＃。* $ /，Xe = / ^（。*？）：[\ t] *（[^ \ r \ n] *）\ r？$ / gm，Ve = / ^ ：色|日期|日期时间|电子邮件|隐藏|本月|号码|密码|范围|搜索|电话|文|时间|网址|周）$ / I，则UE = / ^（?:约|应用|应用\吸藏。| + \ -扩展|文件|插件）：$ /，JE = / ^（?: GET | HEAD）$ /叶= / ^ ？\ / \ //，戈= / \ /，柯= / <脚本\ B [^ <] *（：？！（<\ / SCRIPT>）<[^ <] *）* <\ / SCRIPT> / GI，Qe的= / ^（?:选择| textarea的）/ I，泽= / \ S + /。，等= /（[？＆]）_ = [^＆] * / TT = / ^（[\瓦特\ + \ \ - ] +：？）（？：？\ / \ /（[^ \ /＃：] *）（？::（\ D +）））/，NT = H.fn.load， RT = {}，它= {}; {尝试QE = O.href}赶上（OT）{QE = L.createElement（ “A”），qe.href = “”，QE = qe.href} _E = TT .exec（qe.toLowerCase（））|| []，H.fn.extend（{load：function（e，n，r）{if（“string”！= typeof e && nt）return nt.apply（this，arguments ）; if（！this.length）return this; var i = e.indexOf（“”）; if（i> = 0）{var o = e.slice（i，e.length）; e = e.slice （0，i）} var a =“GET”; n &&（H.isFunction（n）？（r = n，n = t）：“object”== typeof n &&（n = H.param（n， ajaxSettings.traditional），a =“POST”））; var s = this; return H.ajax（{url：e，type：a，dataType：“html”，data：n，complete：function（e，t， N）{N = e.responseText，e.isResolved（）&&（e.done（函数（E）{N = E}），s.html（O 2 H（ “<DIV>”）。附加（N。替换（Ke，“”））find（o）：n）），r && s.each（r，[n，t，e]）}}），this}，serialize：function（）{return H.param this.serializeArray（））}，serializeArray：function（）{return this.map（function（）{return this.elements？H.makeArray（this.eleme nts）：this}）。filter（function（）{return this.name &&！this.disabled &&（this.checked || Qe.test（this.nodeName）|| Ve.test（this.type））}）。map （函数（e，t）{var n = H（this）.val（）;返回null == n？null：H.isArray（n）名：t.name，值：e.replace（$ E，为“\ r \ n”个）}}）：{名称：t.name，值：n.replace（$ E，为“\ r \ n”个）} }}），H.each（“ajaxStart ajaxStop ajaxComplete ajaxError ajaxSuccess ajaxSend”.split（“”），function（e，t）{H.fn [t] = function（e）{return this函数（e，n）{H [n] =函数（e，r，i，o）{return H .isFunction（R）&&（O = O || I，I = R，R = T），H.ajax（{类型：N，网址：E，数据：R，成功：ⅰ，的dataType：○}）} }），H.extend（{getScript：function（e，n）{return hget（e，t，n，“script”）}，getJSON：function（e，t，n）{return E，T，N “JSON”）}，ajaxSetup：？！功能（E，T）{吨H.extend（0，即，H.ajaxSettings，吨）:( T = E，E = H.extend（在H.ajaxSettings &&（e [n]）中，t∈e[n] = t [n]：n中的（var。 = hajaxSettings [n]）; return e}，ajaxSettings：{url：qe，isLocal：Ue.test（_e [1]），global：！0，type：“GET”，conte ntType：“application / x-www-form-urlencoded”，processData：！0，async：！0，accept：{xml：“application / xml，text / xml”，html：“text / html” text / plain“，json：”application / json，text / javascript“，”*“：”* / *“}，内容：{xml：/ xml /，html：/ html /，json：/ json / responseFields：{xml：“responseXML”，text：“responseText”}，转换器：{“* text”：e.String，“text html”：！0，“text json”：H.parseJSON，“text xml”函数r（e，n，r，a）{if（2！== x）{（x，y） x = 2，l && clearTimeout（l），s = t，o = a ||“”，w.readyState = e 4：0; var u，f，v，b，T，E = r？N（d， W，R）：吨;若（E> = 200 && 300>电子|| 304 === e）如（d.ifModified &&（（b = w.getResponseHeader（ “上次修改”））&&（H.lastModified [I ] = b），（T = w.getResponseHeader（“Etag”））&&（H.etag [i] = T）），304 === e）n =“notmodified”，u =！0; else try { f = C（d，E），n =“成功”，u =！0} catch（S）{n =“parsererror”，v = S} else v = n，（！n || e）&& = “错误”，0>电子&&（E = 0））; w.status = E，w.statusText = N，U m.resolveWith（ρ，F，N，W]）：m.rejectWith（p， [W，N，v]），w.statusCode（Y），Y = T，C && h.trigger（ “AJAX” +（U “成功”： “错误”），[W，D，U F：·v ] ），g.resolveWith（ρ，W，N]），C &&（h.trigger（ “ajaxComplete”，[W，D]）， - H.active || H.event.trigger（ “ajaxStop”）） }}“object”== typeof e &&（n = e，e = t），n = n || {}; var i，o，a，s，l，u，c，f，d = H.ajaxSetup {}，n），p = d.context || d，h = p！== d &&（p.nodeType || p instanceof H）？H（p）：H.event，m = H.Deferred（） G = H._Deferred（），Y = d.statusCode || {}，v = {}，b = {}，X = 0，W = {readyState的：0，setRequestHeader：功能（E，T）{如果（ ！x）{var n = e.toLowerCase（）; e = b [n] = b [n] || e，v [e] = t} return this}，getAllResponseHeaders：function（）{return 2 ===对于（a = {}; n = Xe.exec（o）;）if（！a）for（a = {}; n [1] .toLowerCase（）] = n [2]; n = a [e.toLowerCase（）]} return n === t？null：n}，overrideMimeType：function（e）{return x || d.mimeType = e），this}，abort：function（e）{return e = e ||“abort”，s && s.abort（e），r（0，e），this}}; if（m.promise （w），w.success = w.done，w.error = w.fail，w.complete = g.done，w.statusCode = function（e）{if（e）{var t; if（2> x ）对于（t in e）y [t] = [y [t]，e [t]]; else t = e [w.status]，w.then（t，t）} return this}，d.url =（（E || d.url）+ “”）。代替（ZE， “”）。代替（叶，_E [1] + “//”），d.dataTypes = H.trim（d.dataType || “*”）。toLowerCase（）。分裂（泽），空== d.crossDomain &&（U = tt.exec（d.url.toLowerCase（）），d.crossDomain =！ ！（U || U [1] == _ E [1] && U [2] == _ E [2] &&（U [3] ||（ “HTTP：” === U [1] 80：443） ）==（_ e [3] ||（“http：”=== _ e [1]？80：443）））），d.data && d.processData &&“string”！= typeof d.data &&（d.data = H.param（d.data，d.traditional）），T（RT，D，N，W），2 === x）的返回1;！如果（C = d.global，d.type = d.type .toUpperCase（），d.hasContent =！Je.test（d.type）中，c 0 && === H.active ++ && H.event.trigger（ “ajaxStart”）,! d.hasContent &&（d.data &&（D。 url + =（Ge.test（d.url）？“＆”：“？”）+ d.data），i = d.url，d.cache ===！1））{var E = ），S = d.url.replace（等， “$ 1 _ =” + E）; d.url = S +（S === d.url（Ge.test（d.url） “＆”：”？ ？ “）+” _ = “+ E：”！ “）}（d.data && d.hasContent && d.contentType == 1 || n.contentType）&& w.setRequestHeader（”内容类型”，d.contentType），D .ifModified &&（I = I || d.url，H.lastModified [I] && w.setRequestHeader（ “如果-Modified-Since的”，H.lastModified [I]），H.etag [I] && w.setRequestHeader（“如果-none -匹配”，H.etag [I]）），w.setRequestHeader（ “接受”，d.dataTypes [0] && d.accepts [d.dataTypes [0]]？d.accepts [d.dataTypes [0 ]] +（“*”！== d.dataTypes [0]？“，* / *; q = 0.01“：”“）：d.accepts [”*“]）; for（f in d.headers）w.setRequestHeader（f，d.headers [f]）; if（d.beforeSend &&（d.beforeSend .call（p，w，d）===！1 || 2 === x））return w.abort（），！1; for（f in {success：1，error：1，complete：1} ）W [F]（D [F]）;如果（S = T（它，D，N，W））{w.readyState = 1，C && h.trigger（ “ajaxSend”，[W，D]）中，d .async && d.timeout> 0 &&（L = setTimeout的（函数（）{w.abort（ “超时”）}，d.timeout））;尝试{X = 1，s.send（v，R）}赶上（A） {status <2？r（-1，A）：H.error（A）}} else r（-1，“No Transport”）; return w}，param：function（e，n）{var r = ]，I =函数（E，T）{T = H.isFunction（T）T（）：T，R [r.length] = encodeURIComponent方法（E）+ “=” + encodeURIComponent方法（T）};如果（ ñ===吨&&（N = H.ajaxSettings.traditional），H.isArray（E）|| e.jquery &&！H.isPlainObject（e））的H.each（即，函数（）{I（this.name， return（Re，“+”）}}）; else（），（e，o，e， ，H.extend（{active：0，lastModified：{}，etag：{}}）; var at = H.now（），st = /（\ =）\？（＆| $）| \？\ /i;H.ajaxSetup({jsonp:"callback ",jsonpCallback:function(){return H.expando +“_”+ at ++}}），H.ajaxPrefilter（“json jsonp”，function（t，n，r） {var i =“app lication / x-www-form-urlencoded“=== t.contentType &&”string“== typeof t.data; if（”jsonp“=== t.dataTypes [0] || t.jsonp！==！1 && （st.test（t.url）|| i && st.test（t.data）））{var o，a = t.jsonpCallback = H.isFunction（t.jsonpCallback）？t.jsonpCallback（）：t.jsonpCallback， s = e [a]，l = t.url，u = t.data，c =“$ 1”+ a +“$ 2”; return t.jsonp！==！1 &&（l = l.replace（st，c） ，t.url ===升&&（ⅰ&&（U = u.replace（ST，C）），t.data ===ù&&（L + =（/ \ /测试（L） “和”：？？“？ “）+ t.jsonp +”=“+一））），t.url = 1，t.data = U，E [A] =函数（E）{O = [E]}，r.always（函数（ ）{e [a] = s，o && H.isFunction（s）&& e [a]（o [0]）}），t.converters [“script json”] = function（）{return o || H.error a +“未被调用”），o [0]}，t.dataTypes [0] =“json”，“script”}}），H.ajaxSetup（{accept：{script：“text / javascript，application / javascript ，application / ecmascript，application / x-ecmascript“}，contents：{script：/ javascript | ecmascript /}，转换器：{”text script“：function（e）{return H.globalEval（e），e}}} ），H.ajaxPrefilter（ “脚本”，函数（E）{e.cache ===吨&&（e.cache =！1），e.crossDomain &&（e.type = “GET”，e.global =！1） }），H.ajaxTransport（ “脚本”，函数的 n（e）{if（e.crossDomain）{var n，r = L.head || L.getElementsByTagName（“head”）[0] || L.documentElement; return {send：function（i，o）{ N = L.createElement（ “脚本”），n.async = “异步”，e.scriptCharset &&（n.charset = e.scriptCharset），n.src = e.url，n.onload = n.onreadystatechange =函数（ E，I）{（I || || n.readyState /加载|！完整/。测试（n.readyState））&&（n.onload = n.onreadystatechange = NULL，R && n.parentNode && r.removeChild（N）中，n = T，I || O（200， “成功”））}，r.insertBefore（N，r.firstChild）}，中止：函数（）{N && n.onload（0,1）}}}}）;无功lt; ut = e.ActiveXObject？function（）{for（var e in lt）lt [e]（0,1）}：！1，ct = 0; H.ajaxSettings.xhr = e.ActiveXObject？function {return！this.isLocal && E（）|| S（）}：E，function（e）{H.extend（H.support，{ajax：!! e，cors：!! e &&“withCredentials”in e}）} （H.ajaxSettings.xhr（）），H.support.ajax && H.ajaxTransport（function（n）{if（！n.crossDomain || H.support.cors）{var r; return {send：function（i，o ）{var a，s，l = n.xhr（）; if（n.username？l.open（n.type，n.url，n.async，n.username，n.password）：l.open （n.type，n.url，n.async），n.xhrFields）for（s in n.xhrFields）l [s] = n .xhrFields [S]; n.mimeType && l.overrideMimeType && l.overrideMimeType（n.mimeType），n.crossDomain || I [ “X-请求-随着”] ||（I [ “X-请求-随着”] =“XMLHttpRequest的“）; try {for（s in i）l.setRequestHeader（s，i [s]）} catch（u）{} l.send（n.hasContent && n.data || null），r = function（e，i ）{var s，u，c，f，d; try {if（r &&（i || 4 === l.readyState））if（r = t，a &&（l.onreadystatechange = H.noop，ut && delete lt [ ！A]）中，i）4 == l.readyState && l.abort（）;否则{S = l.status，C = l.getAllResponseHeaders（）中，f = {}，D = l.responseXML，D && d.documentElement &&（F .XML = D），f.text = l.responseText;！？尝试{U = l.statusText}赶上（p）{U = “”}Š|| n.isLocal || n.crossDomain 1223 ===小号&& （S = 204）：S = 200 f.text：？！404}}赶上（H）{I || O（-1，H）} F到&& O（S，U，F，C）}，n.async && 4 = ？= l.readyState（A = ++ CT，UT &&（LT ||（LT = {}，H（e）中.unload（UT）），LT [α] = R），l.onreadystatechange = R）：R （）}，abort：function（）{r && r（0,1）}}}}）; var ft，dt，pt，ht，mt = {}，gt = / ^（？：toggle | show | hide）$ /,yt=/^([+\-]=)?([\d+.\-]+)([az%]*)$/i,vt=[["height ","marginTop ","marginBottom“”paddingTop“，”paddingBottom来“]， [”宽度“，”marginLeft“，”marginRight“，”paddingLeft“，”paddingRig ht“]， [”opacity“]]，bt = e.webkitRequestAnimationFrame || e.mozRequestAnimationFrame || e.oRequestAnimationFrame; H.fn.extend（ {
        show：
        function（e，t，n） {
            var r，i;如果（e || 0 === e）返回this.animate（D（“show”，3），e，t，n）;
            for（
            var o = 0，a = this.length;
            a > o;
            o++）R = 此 [O]，r.style && （I = r.style.display，H._data（R，“olddisplay”） || “无”！ == 我 || （I = r.style.display = “”）“”我 === &&“无” === H.css（R，“显示器”） && H._data（R，“olddisplay”，F（r.nodeName）））;对于（O = 0;一 > 0;○++）R = 此 [O]，r.style && （I = r.style.display，（“”我 === ||“无” === ⅰ） && （r.style.display = h_data（r，“olddisplay”） || “”））;
            return this
        }，hide：
        function（e，t，n） {
            if（e || 0 === e）
            return this.animate（“hide”，3），e，t，n）;
            for（
            var r = 0，i = this.length;
            i > r;
            r++）
            if（this[r].style） {
                var o = H.css（此 [R]，“显示器”）;“无” === Ó || H._data（此 [R]，“olddisplay”） || H._data（此 [R]，“olddisplay”，O）
            }
            for（r = 0;
            i > r;
            r++）this[r].style && （this[r].style.display = “none”）;
            return this
        }，_ toggle：H.fn.toggle，toggle：
        function e，t，n） {
            var r = “boolean” == typeof e;
            return H.isFunction（e） && H.isFunction（t）？this._toggle.apply（this，arguments）：null == e || （？）（）（）（）（）（）（）（）（）this.animate（D（“toggle”，3），e，t，n），this
        }，fadeTo：
        function（e，t，n，r） {
            return this.filter（“：hidden”opacity“，0）.show（）。end（）。animate（ {
                opacity：t
            }，e，n，r）
        }，animate：
        function（e，t，n，r） {
            var i = t，n，r）;
            return H.isEmptyObject（e）？this.each（i.complete， [！1]）: (e = H.extend（ {}，e），this[i.queue == ！1？“each”：“queue”]（
            function（） {
                i.queue === ！1 && H._mark（this）;
                var t，n，r，o，a，s，l，u，c，f = H.extend（ {}，i），d = 1 === this.nodeType，p = d && H（this）.is（“：hidden”）;
                f.animatedProperties = {};
                for（r in e） {如果（t = H.camelCase（r），r！ == t && （e[t] = e[r]，删除e[r]），n = e[t]，H.isArray（n）.animatedProperties[T] = N[1]中，n = E[T] = N[0]）：f.animatedProperties[T] = f.specialEasing && f.specialEasing[吨] || ||f.easing“摇摆”，“hide” === n && p || “show” === n && ！p）
                    return f.complete.call（this）;！d || “height”！ == t && “width”！ == t || f.overflow = [this.style.overflow，this.style.overflowX，this.style.overflowY]，“内联” === H.css（这一点，“显示器”） && “无” === H.css（这一点，“浮动”） && （H.support.inlineBlockNeeds布局？（O = F（this.nodeName），“内联” === O 3 this.style.display = “直列块”: (this.style.display = “内联”，this.style.zoom = 1））：this.style.display = “inline - block”））
                }
                null！ = f.overflow && （this.style.overflow = “hidden”）;
                for（r in e）a = new H.fx（this，F，R）中，n = E[R]，gt.test（n）的一个 [“肘节” === N p个“显示”：？“隐藏”：N]（）: (S = yt.exec？（N），L = a.cur（）中，s（U = parseFloat（S[2]），C = S[3] || （H.cssNumber[R]？“”：“PX”），”PX“！ == ç && （H.style（此，R，（U || 1） + c）中，L = （U || 1） / a.cur（） * L，H.style（此，R，L + C））中，s[1] && （U = （“ - =” === S[1] - 1：1） * U + 1），a.custom（L，U，C））：（e，t） {
                    return e && this.queue（ []），this.each（
                    function（） {
                        var e = H.timers中，n = e.length; [对于（t || H._unmark（0，这一点）; N - ;！）！E[N].elem === 本 && （吨 && E[N]（0），e.splice（N，1））
                    }），叔 || this.dequeue（），这
                }
            }），H.each（ {了slideDown：D（“显示”，1），效果基本show：D（“隐藏”，1），的slideToggle：D（“切换”，1），淡入： {不透明度：“节目”
                }，淡出： {不透明度：“隐藏”
                }，fadeToggle： {不透明度：“切换”
                }
            }，函数（例如，叔） {
                H.fn[e] = 函数（e，n，r） {
                    return this.animate（t，e，n，r）
                }
            }），H.extend（ {
                speed：
                function（e，t，n） {
                    var r = e && “对象“ == typeof e？H.extend（ {}，e）： {
                        complete：n || ！n && t || H.isFunction（e） && e，duration：e，easing：n && t || t && ！） && t
                    };
                    return r.duration = H.fx.off？0：“number” == typeof r.duration？r.duration：r.duration in H.fx.speeds？H.fx.speeds[r.duration]：H.fx.speeds._default，r.old = r.complete，r.complete = 函数（E） {
                        H.isFunction（r.old） && r.old.call（本），r.queue == ！1？H.dequeue（this）：e！ == ！1 && H._unmark（this）
                    }，r
                }，缓和： {
                    linear：
                    function（e，t，n，r） {
                        return n + r * e
                    }摆动：功能（E，T，N，R） {返回（ - Math.cos（E * Math.PI） / 2 + .5） * R + N
                    }
                }，定时器： []，FX：功能（例如，T，N） {
                    this.options = t时，this.elem = E，this.prop = N，t.orig = t.orig || {}
                }
            }），H.fx.prototype = {更新：（）的函数 {
                    this.options.step && this.options.step.call（this.elem，this.now，此），（H.fx.step[this.prop] || H.fx.step._default）（这个）
                }，cur：
                function（） {
                    if（null！ = this.elem[this.prop] && （！this.elem.style || null == this.elem.style[this.prop]））
                    return this.elem[this.prop];
                    var e，t = H.css（this.elem，this.prop）;
                    return isNaN（e = parseFloat（t））？t && “auto”！ == t？t：0：e
                }，custom：
                function（e，t，n） {
                    function r（e） {
                        return o.st ep（e）
                    }
                    var i，o = this，a = H.fx;
                    this.startTime = ht || A（），this.start = e，this.end = t，this.unit = n || this。单元 || （H.cssNumber[this.prop]？“”：“PX”），this.now = this.start，this.pos = this.state = 0，r.elem = this.elem，R（） && H.timers.push（R） && PT && （BT（PT = 0，I = 函数（） {
                        PT && （BT（i）中，a.tick（））
                    }，BT（i））的：！？！PT = setInterval的（a.tick，a.interval））
                }，显示：！功能（） {
                    this.options.orig[this.prop] = H.style（this.elem，this.prop），this.options.show = 0，this.custom（“宽度” === this.prop || “高度” === this.prop？1：0，this.cur（）），H（this.elem）.show（）
                }，隐藏：函数（） {
                    this.options.orig[this.prop] = H.style（this.elem，this.prop），this.options.hide = 0，this.custom（this.cur（），0）
                }，step：
                function（e） {
                    var t，n，r = ht || A（），i = ！0，o = this.elem，a = this.options;
                    if（e || r > =a。持续时间 + this.startTime） {
                        this.now = this.end，this.pos = this.state = 1，this.update（），a.animatedProperties[this.prop] = ！0;
                        for（t in a.animatedProperties）a.animatedProperties[吨] == 0 && （I = 1）;！！如果（i） {如果（空 == a.overflow || ||H.support.shrinkWrapBlocks H.each（ [“”，”X”，“Y”]，功能（E，T） {
                                o.style[“溢出” + T] = a.overflow[E]
                            }），a.hide && H（o）.hide（），a.hide || a.show）
                            for（
                            var. in a.animatedProperties）H.style（o，s，a.orig[s]）;
                            a.complete.call（o）
                        }
                        return！1
                    }
                    return a.duration == 1 / 0？this.now = r：（n = r - this.startTime，this.state = n / a.duration，this.pos = H.easing[a.animatedProperties[this.prop]]（this.state中，n，0,
                    1，a.duration），this.now = this.start + （this.end - this.start） * this.pos），这一点。update（），！0
                }
            }，H.extend（H.fx， {
                tick：
                function（） {
                    for（
                    var e = H.timers，t = 0;
                    t < e.length; ++t）e[]（） || e.splice（吨 - ，1）;
                    e.length || H.fx.stop（）
                }，间隔：13，停止：函数（） {
                    clearInterval（PT），PT = NULL
                }，速度： {慢：600，快：200，_default：400
                }，在步骤 {不透明度：功能（E） {
                        H.style（e.elem，“不透明”，e.now）
                    }，_默认：函数（e）中 {
                        e.elem.style && 空！ = e.elem.style[e.prop] e.elem.style[e.prop] = （“宽度” === e.prop || “高度” === 即丙Math.max（0，e.now）：e.now） + e.unit：e.elem[e.prop] = e.now
                    }
                }
            }），H.expr && H.expr.filters && （H.expr.filters.animated = function（e） {
                return H.grep（H.timers，
                function（t） {
                    return e === t.elem
                }）。length
            }）;
            var xt = / ^ t（？ d | h）$ /i，Tt = / ^（？：body | html）$ /i;“getBoundingClientRect” in L.doc umentElement？H.fn.offset = function（e） {
                var t，n = this[0];
                if（e）
                return this.each（
                function（t） {
                    H.offset.setOffset（this，e，t）
                }）;
                if（！n || ！n.ownerDocument）返回null;
                if（n === n.ownerDocument.body）返回H.offset.bodyOffset（n）;
                try {
                    t = n.getBoundingClientRect（）
                } catch r） {}
                var i = n.ownerDocument，o = i.documentElement;
                if（！t || ！H.contains（o，n））
                return t？ {
                    top：t.top，left：t.left
                }： {
                    top：0，left：0
                };
                var a = i.body，s = j（i），l = o.clientTop || a.clientTop || 0，u = o.clientLeft || a.clientLeft || O，C = s.pageYOffset || H.support.boxModel && o.scrollTop || a.scrollTop，F = s.pageXOffset || H.support.boxModel && o.scrollLeft || a.scrollLeft峰，d = t.top + CL，p = t.left + fu;
                return {
                    top：d，left：p
                }
            }：H.fn.offset = function（e） {
                var t = this[0];
                if（e）
                return this.each（
                function t） {
                    H.offset.setOffset（this，e，t）
                }）;
                if（！t || ！t.ownerDocument）返回null;
                if（t === t.ownerDocument.body）返回H.offset.bodyOffset（t）;
                H.offset.initialize（）;
                for（
                var n，r = t.offsetParent，i = t，o = t.ownerDocument，a = o.documentElement，s = o.body，l = o.defaultView中，u = 1 l.getComputedStyle（吨，空）：t.currentStyle，C = t.offsetTop，F = t.of fsetLeft;！（T = t.parentNode） && 吨 == 小号 && 吨 == 一个 && （H.offset.supportsFixedPosition || “固定” == u.position！）;！？）N = L l.getComputedStyle（吨，空）：t.currentStyle，C - =t.scrollTop，F - =t.scrollLeft，叔 === ř && （C + =t.offsetTop中，f + =t.offsetLeft，H.offset.doesNotAddBorder || 水平偏移量！。doesAddBorderForTableAndCells && xt.test（t.nodeName） || （C + =parseFloat（n.borderTopWidth） || 0，F + =parseFloat（n.borderLeftWidth） || 0）中，i = R，R = t.offsetParent），水平偏移量！.subtractsBorderForOverflowNotVisible && “可见” == n.overflow && （C + =parseFloat（n.borderTopWidth） || 0，F + =parseFloat（n.borderLeftWidth） || 0）中，u = N;返回（“相对” === Ù.POSITION || “静态” === u.position） && （C + =s.offsetTop中，f + =s.offsetLeft），H.offset.supportsFixedPosition && “固定” === u.position && （C + =Math.max（a.scrollTop，s.scrollTop），f + =Math.max（a.scrollLeft，s.scrollLeft））， {
                    top：c，left：f
                }
            }，H.offset = {
                initialize：
                function（） {
                    var e，t，n，r = L.body，i = L.createElement（“div”），o = parseFloat（H.css（r，“marginTop”）） || 0，a = “ < div style = 'position： absolute; top：0; left：0; margin：0; border：5px solid＃000; padding：0; width：1px; height ：1px;' > <div > </ div> </div > <table style = 'position：absolute; top：0; left：0; margin：0; border：5px solid＃000; padding：0; width： 1px的;高度：1px的;” cellpadding ='0 'cellspacing ='0 '> <tr> <td> </ td> </ tr></ table>“; H.extend（i.style，{position：”absolute“，top：左：0，余量：0，边界：0，宽度： “1像素”，高度： “1像素”，可见性： “隐藏”}），i.innerHTML = A，r.insertBefore（I，r.firstChild）中，e = i.firstChild，T = e.firstChild，N = e.nextSibling.firstChild.firstChild，this.doesNotAddBorder = 5！== t.offsetTop，this.doesAddBorderForTableAndCells = 5 === n.offsetTop，t.style.position = “固定的”，t.style.top = “20像素”，this.supportsFixedPosition = 20 === t.offsetTop || 15 === t.offsetTop，t.style.position = t.style.top = “” ，e.style.overflow = “隐藏”，e.style.position = “相对”，this.subtractsBorderForOverflowNotVisible = -5 === t.offsetTop，this.doesNotIncludeMarginInBodyOffset = r.offsetTop！== O，r.removeChild（ i），H.offset.initialize = H.noop}，bodyOffset：function（e）{var t = e.offsetTop，n = e.offsetLeft; return H.offset.initialize（），H.offset.doesNotIncludeMarginInBodyOffset &&（t + = parseFloat（H.css（即， “marginTop”））|| 0，N + = parseFloat（H.css（即， “marginLeft”））|| 0），{顶部：吨，左：N}}，setOffset ：function（e，t，n）{var r = H.css（e，“positi on“）;”static“=== r &&（e.style.position =”relative“）; var i，o，a = H（e），s = a.offset（），l = H.css ， “顶部”）中，u = H.css（例如， “左”），C =（ “绝对” === - [R || “固定” === R）&& H.inArray（ “自动”，[1,1' - ？ü]） > -1，F = {}，D = {};
                    C（D = a.position（）中，i = d.top，O = d.left）: (I = parseFloat（升） || 0，O = parseFloat（u）的 || 0），H.isFunction（吨） && （T = t.call（E，N，S）），空！ = t.top && （f.top = t.top - s.top + i），null！ = t.left && （f.left = t.left - s.left + o），在t？t.using.call（e，f）中使用“a”f）
                }
            }，H.fn.extend（ {
                position：
                function（） {
                    if（！this[0]）
                    return null;
                    var e = this[0]，t = this.offsetParent（），n = this.offset（），r = Tt.test（t[0].nodeName）？ {
                        top：0，left：0
                    }：t.offset（）;
                    return n.top - =parseFloat（H.css（e，“marginTop”）） || 0，n.left - =parseFloat（H.css（即，“marginLeft”）） || 0，r.top + =parseFloat（H.css（T[0]，“borderTopWidth”）） || 0，r.left + =parseFloat（H.css（T[0]，“borderLeftWidth”）） || 0， {顶部：n.top - r.top，左：n.left - r.left
                    }
                }，offsetParent：
                function（） {
                    return this.map（
                    function（） {
                        for（
                        var e = this.offsetParent || L.body;
                        e && ！Tt.test（e.nodeName） && “static” === H.css（e，“position”）;）e = e.offsetParent;
                        return e
                    }）
                }
            }），H.each（ [“Left”，“Top”]，
            function（e，n） {
                var r = “scroll” + n;
                H.fn[r] = function（n） {
                    var i，o;
                    return n === t？（i = this[0]）？（o = j（i），o？“oXOffset” in o？o[e？“pageYOffset”：“pageXOffset”]：H.support.boxModel && o.document.documentElement[r] || o.document.body[R]：I[R]）：空：this.each（函数（） {Ô = j的（这个），邻o.scrollTo（E H（O）.scrollLeft（）：？N，E N：4 H（o）.scrollTop（））：this[r] = n
                    }）
                }
            }），H.each（ [“Height”，“Width”]，
            function（e，n） {
                var r = n.toLowerCase;
                hfn[“inner” + n] = function（） {
                    var e = this[0];
                    return e && e.style？parseFloat（H.css（e，r，“padding”））：null
                }，H。fn[“outer” + n] = function（e） {
                    var t = this[0];
                    return t && t.style？parseFloat（H.css（t，r，e？“margin”：“border”））：null
                }，H.fn[r] = function（e） {
                    var i = this[0];
                    if（！i）
                    return null == e？null：this;
                    if（H.isFunction（e））返回这个。define（“ / select - plugin”，
                    function（e，t，n） {
                        var r = e（“ / lib / jquery - 1.6.2”）;
                        r.fn.sel = function（e） {
                            var t = r.extend（ {}，r.fn.sel.defaults，e），n = r（this），i = r（'<ul id =“' + t.containerId + '”></ ul>'）appendTo（n）.addClass（“sel”）;
                            if（“number” == typeof t.number）
                            for（
                            var o = t.number <= t.hintList.length？t.number：t.hintList.length，a = 0;
                            o > a;
                            a++）i.append（'<li class =“' + t.hintList[a].liClass + '”> <a val =“' + t.hintList[a].val + '” =“＃”>' + t.hintList[a].liText + “ < /a></li > ”）;
                            else if（“number”！ = typeof t.number）
                            throw“number阃夐”蹇呴“暟瀛“;
                            return n.click（
                            function（） {
                                return i.toggle（）。show（），r（”＃customSelectBtn“）。addClass（”selectbtn“），！1
                            }），r“）。单击（函数（） {
                                i.hide（）中，r（”＃customSelectBtn“）。removeClass（”焦点“）中，r（”＃customSelectBtn“）。removeClass（”selectbtn“）
                            }）中，r（”＃（val）;
                            return t.callback（e），n.toggleClass（“焦点”）中，r（“＃customSelectVal”）。VAL（e）中，n.find（”。btn_text“）。文本（R（本）的.text（））中，r（”＃outputLang“）。html的（”“），i.hide（），n.removeClass（“焦点”），i.find（“关于”）。removeClass（“接通”）中，r（本）.parent（）。addClass（“上”）,
                            !1
                        }）中，n
                    }，r.fn.sel.defaults = {号：16，hintList： [{
                            VAL：“AUTO”，liText：“镊姩妫€娴嬭瑷€”，liClass：“正常”
                        }， {
                            VAL：“SPACE”，liText：“”，liClass：“空间”
                        }， {
                            VAL：“ZH - CHS2en”，liText：“涓枃＆NBSP;禄鑻辫“，liClass：”isfl topBorder1“
                        }， {
                            val：”en2zh - CHS“，liText：”鑻辫＆nbsp;禄涓枃“，liClass：”isfl rightBorder topBorder“
                        }， {
                            val：”zh - CHS2ja“，liText：”涓枃禄镞ヨ“，liClass：”isfl“
                        }， {
                            val：”ja2zh - CHS“，liText：”镞ヨ＆nbsp;禄涓枃“，liClass：”isfl rightBorder“
                        }， {
                            val：”zh - CHS2ko“，liText：”涓枃禄广阔╄“，liClass：”isfl“
                        }， {
                            val：”ko2zh - CHS“，liText：”阔╄＆nbsp;禄涓枃“，liClass：”isfl rightBorder“
                        }， {
                            val：”zh - CHS2fr“，liText：”涓枃禄娉曡“，liClass：”isfl“
                        }， {
                            val：”fr2zh - CHS“，liText：”娉曡“禄涓枃“，liClass：”isfl rightBorder“
                        }， {
                            val：”zh - CHS2ru“，liText：”涓枃“禄禄勮“，liClass：”isfl“
                        }， {
                            val：”ru2zh - CHS“，liText：”淇勮禄涓枃“，liClass：”isfl rightBorder“
                        }， {
                            val：”zh - CHS2es“，liText：”涓枃“禄瑗彮鐗栾“，liClass：”isfl“
                        }， {
                            val：”es2zh - CHS“，liText：”瑗跨彮鐗栾禄涓枃“，liClass：”isfl rightBorder“
                        }， {
                            val：”zh - CHS2pt“，liText：”涓枃禄钁¤鐗栾“，liClass：”isfl“
                        }， {
                            val：”pt2zh - CHS“，liText：”钁¤悇鐗栾禄禄涓枃“，liClass：”isfl rightBorder“
                        }]，containerId：”customSelectOption“，init：
                        function（） {}，callback：
                        function（） {}
                    }
                }）define（“ / atEntrance”，
                function（e，t） {
                    var n = e（“ / lib / jquery - 1.6.2”）;
                    t.showAtButton = function（e，t） {
                        function i（e） {““ === e？（o.removeClass（o.className），o.addClass（”onEnhanceBtn“））：”disable“ === e？（o.removeClass（o.className），o.addClass（”按钮atDisableBtn“），n（”＃atBtn“）。hover（
                            function（） {
                                n（”＃atBtnhover“）。css（”display“，”none“）
                            }））: (o.removeClass（o.className），o.addClass（“button atNormalBtn”））
                        }
                        var o = n（“＃atBtn”）;
                        if（“AUTO” === t || “zh - CHS2en” === t || “en2zh - CHS” === t）
                        if（“”！ == e）
                        if（“AUTO” === t） {
                            var a = r（e）;
                            i（“en - zh” === a || “zh - en“（”禁用“）
                        } else i（”增强“）;
                        else i（”normal“）;
                        else i（”disable“）
                    }，t.timero = function（e，t） {
                        var r = function（e，t） {
                            this.func = e，this.time = t
                        };
                        return r.prototype = {
                            run：
                            function（） {
                                var e = this;
                                this.clear（），this.timeout = setTimeout（
                                function（） {
                                    n.isFunction（e.func） && e.func（）
                                }，e.time）
                            }，clear：
                            function（） {
                                clearTimeout（this.timeout）
                            }
                        }，new r（e，t）
                    };
                    var r = function（e） {
                        function t（e） {
                            var t = e.charCodeAt（0）;
                            return“銆€” === e？！0：32 > =t || 255 === t？！0：！1
                        }函数r（e） {
                            return v[e.charCodeAt（0）] === ！0
                        }函数i（e） {
                            var t = e.charCodeAt（0）;
                            return t > =x[0] && t <= x[1] || t > =T[0] && t <= T[1]：！1
                        }
                        function o（e） {
                            var t = e.charCodeAt（0）;
                            return t > =w[0] && t <= w[1] || t > =N[0] && t <= N[1] || t > =C[0] && t <= C[1] || t > =S[0] && t <= S[1]？！0：！1
                        }函数a（e） {
                            var t = e.charCodeAt（0）;
                            return t > =E[0] && t <= E[1] || t > =A[0] && t <= A[1] || t > =k[0] && t <= k[1]？！0：！1
                        }
                        function s（e） {
                            if（“” === n.trim（e））
                            return [c，0];
                            for（
                            var s = []，l = [] u = 0，p = 0，h = 0，m = 0，g = 0，v = ！1，y = ！1，b = 0，x = e.length;
                            x > b;
                            b++） {
                                var T = e.charAt（b）中，W = 1，N = 1;如果（T（T） || R（T）（W = N = 0，U++）：！？！？O（T）（ⅴ || （v！ = 0），N = 0）：I（λT）（Y || （Y！ = 0），W = 0）：一（T）（W = N = 0，p++）！：（w = N = ！0，h++），v && （w || b == x - 1） || y && （N || b == x - 1）） {
                                    var C = b;
                                    C == x - 1 && （C = b + 1）;
                                    var S = e.substring（g，C）;
                                    if（S.length > 24）返回 [c，0];
                                    S.length > 10 && m++，v s s[s.length] = S：！Ý && （升 [l.length] = S），（v || Y） && （G = b）中，v = 1，Y = 1
                                }瓦特 && N && （G = b + 1，v = 1！，y = ！1）
                            }
                            var E = l.length，A = s.length，k = A + p，D = k + E;
                            0 == k && （A = E，k = E，D = E）
                            var F = D + h，j = h / F;
                            if（j > =.4）
                            return [c，0];
                            var L = A / k;
                            if（L > =.8）
                            return m / A > =。4 && m > =2？ [c，0]： [f，F];
                            var O = p / k;返回O > =8[d，F]： [c，0] U = 不存在，C = 0，F = 1，D = 2，p = “EN”，H = “ZH”中，m = [[“'”，“鈥 “ ”鈥“]，[ '”'， “鈥”， “鈥”]，[“， ”“ 锛 ”]，[ “銆 ”]，[“”。“; “ ”锛“]，[ ”：“， ”锛“]，[ ”銆“]，[ ”路“]，[ ”/“， ”锛“]，[ ”“，” 锛“]，[” \\ “ ”锛“]，[ ”|！“， ”锝“]，[ ”`“]，[ ”〜“， ”锝“]，[ ”“，”锛 “]，[” @”， “锛”]，[ “＃”， “锛”]，[ “$”， “锛”]，[ “楼”， “锟”]，[ “％”， “锛”]，[ “^”， “锛”， “鈥”]，[ “＆”， “锛”]，[ “_”]，[ “（”，“） “]，[” 锛 “ ”锛“]，[ ”[“， ”]“]，[ ”锛“， ”锛“]，[ ”{“， ”}“]，[”< ”， “>”]，[ “+”， “锛”]，[ “ - ”， “锛”]，[ “*”， “锛”， “脳”]，[ “梅”]， [ “=”， “锛”]]，G = [[10078,12301,12303,12318,65379]，[12305,12309,12311,12313,12315]，[8250,12297,12299]，v = {}，y = 0; y <m.length; y ++）for（var b = 0; b <m [y] .length; b ++）v [m [y] [b] .charCodeAt（0）] =！对于（var b = 0; b <g [y] .length; b ++）v [g [y] [b] -1] =！0的（var y = 0; y <g.length; y ++） ，v [g [y] [b]] =！0; var x = [48,57]，T = [65296,65305]，w = [65,90]，N = [97,122]，C = [65313 ，65338]，S = [65345,65370]，E = [19968,40959]，A = [13312,19903]，K = [63744,64255]，D = S（e）中，F = D [0]; if（F === c）return null; if（F == f）l = p，u = h; else {if（F！= d）return null; l = h，u = p} return l + “+ U}}）;
define（“/ sel”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”）; e（“/ select-plugin”）; var r = e（“/ atEntrance” ）中，i =函数（）{N（窗口）.height（）<610？的setTimeout（函数（）{N（ “赞助内容 ”）。addClass（“ 隐藏模式换广告”）}，100 ）：的setTimeout（函数（）{。N（ “赞助内容 ”）removeClass（“ 隐藏模式换广告”）}，100）}; I（）中，n（窗口）.resize（i）中， t.initSel = function（）{n（“＃customSelectBtn”）。sel（{callback：function（e）{var t = n（“＃inputText”）。val（）; r.showAtButton（t，e）} }）}}）;
define（“/ ZeroClipboard”，function（e，t）{！function（e，t）{“use strict”; Array.prototype.map ||（Array.prototype.map = function（e，t） ，r，i; if（null == this）throw newTypeError（“this is null or not defined”）; var a = Object（this），o = a.length >>> 0; if（“function”！ = typeof e）throw newTypeError（e +“不是函数”）; for（arguments.length> 1 &&（n = t），r = new Array（o），i = 0; o> i;）{var s ，l; i in a &&（s = a [i]，l = e.call（n，s，i，a），r [i] = 1），i ++} return r}）; var n，r，i中，a = E，O = a.document，S = a.navigator，L = a.setTimeout，U = a.clearTimeout，C = a.setInterval，F = a.clearInterval峰，d = a.getComputedStyle，p =一.encodeURIComponent，H = a.ActiveXObject，M = a.Error，G = a.Number.parseInt || a.parseInt，v = a.Number.parseFloat || a.parseFloat，Y = a.Number.isNaN || a.isNaN，b = a.Date.now，X = a.Object.keys，W =（a.Object.defineProperty，a.Object.prototype.hasOwnProperty），T = a.Array.prototype.slice，C = function（）{var e = function（e）{return e}; if（“function”== typeof a.wrap &&“function”== typeof a.unwrap）try {var t = o.createElement（“div”）中，n = a.unwrap（T）; 1 === t.nodeType && N && 1 === n.nodeType &&（E = a.unwr ap）} catch（r）{} return e}（），N = function（e）{return T.call（e，0）}，E = function（）{var e，n，r，i， O，S = N（参数），L = S [0] || {};对于（E = 1，N = s.length; N>电子; e ++）！如果（空=（R = S [E] ））for（i in r）w.call（r，i）&&（a = 1 [i]，o = r [i]，l！== o && o！== t &&（l [i] = o） ; return l}，S = function（e）{var t，n，r，i; if（“object”！= typeof e || null == e ||“number”== typeof e.nodeType）t = （t = []，n = 0，r = e.length; r> n; n ++）w.call（e，n）&&（t [对于（i in e）w.call（e，i）&&（t [i] = S（e [i]）}}返​​回的值为{（e [n]））; else {t = {} t}，e =（e，t）{for（var n = {}，r = 0，i = t.length; i> r; r ++）t [r] = e [t [r]]; return n}，k = function（e，t）{var n = {}; for（var r in e）-1 === t.indexOf（r）&&对于（e）中的（var t）w.call（e，t）&& delete e [t]; return e}，返回n}，j =函数（e）{if（e） D =函数（E，T）{如果（E && 1 === e.nodeType && e.ownerDocument &&吨&&（1 === t.nodeType && t.ownerDocument && t.ownerDocument === e.ownerDocument || 9 === t.nodeType &&！吨。所有者文档&& t === e.ownerDocument））do {if（e === t）return！0; e = e.parentNode} while（e）; return！1}，F = function（e）{var t; return “string”== typeof e && e &&（T = e.split（ “＃”）[0] .split（ “？”）[0]，T = e.slice（0，e.lastIndexOf（ “/”）+ 1）），T}， L = function（e）{var t，n; return“string”== typeof e && e &&（n = e.match（/ ^（?: | [^：@] * @ |。+ \）@ （？：）？？？？））））））））））））））））））））））））））））））） ：\ / \ / [\ /] + \ / [^：\）]。？？？？？？*）（:: \ D +）（:: \ D +）/）中，n && N [1] T = N [1] :( N = e.match（/ \）@（（?: HTTP [S] |文件）：\ / \ / [\ /] + \ / [^：\？？）] *？ ）（？:: \ d +）（？:: \ d +）？/），n && n [1] &&（t = n [1]））），t}，O = function（）{var e，t; try {throw new m} catch（n）{t = n} return t &&（e = t.sourceURL || t.fileName || L（t.stack）），e}，I = function（）{var e，n ，r; if（o.currentScript &&（e = o.currentScript.src））return e; if（n = o.getElementsByTagName（“script”），1 === n.length）return n [0] .src |对于（r = n.length; r  - ;）if（“interactive”=== n [r] .readyState &&（e = n [r] .src）中的if（“readyState”在n [0] ）返回e;返回“loading”=== o.readyState &&（e = n [n.length-1] .src）？e：（e = O（））？e：t}，B = function {v e，n，r，i = o.getElementsByTagName（“script”）; for（e = i.length; e  - ;）{if（！（r = i [e] .src））{n = null; break} if（r = F（r），null == n）n = r; else if（n！== r）{n = null; break}} return n || t}，M = function ）{var e = F（I（））|| B（）||“”; return e +“ZeroClipboard.swf”}，H = function（）{return null == e.opener &&（!! e.top && e！= e.top || !! e .parent && E = e.parent）}（），P = {桥：空，版本： “0.0.0”，pluginType： “未知”，禁用：空的，过时的：空，沙盒：空，不可用：空，降级：空，失活：空，过期日期null，准备：空}，_ = “11.0.0”，Z = {}，$ = {}，q =零，R = 0，W = 0，X = {准备：“Flash通信建立”，错误：{“flash-disabled”：“Flash已禁用或未安装。“，”flash-outdated“：”Flash太过于支持ZeroClipboard“，”flash-sandboxed“：”尝试在沙盒iframe中运行Flash，这是不可能的“，”闪存不可用“：”Flash无法与JavaScript进行双向通信“，”闪存降级“：”与JavaScript通信时，Flash无法保持数据保真度“，”闪存禁用“：”闪存对于您的浏览器和/或配置为点击激活，它太过时了。\ n这也可能意味着无法加载ZeroClipboard SWF对象，因此请检查您的“swfPath”配置和/或网络连接。尝试在沙盒iframe中运行Flash，这是不可能的。“，”flash-overdue“：”Flash通信已建立，但不在可接受的时限内“，”版本不匹配“：”ZeroClipboard JS版本号不匹配ZeroClipboard SWF版本号“，”剪贴板错误“：”至少有一个错误被抛出 “ZeroClipboard尝试将数据注入到剪贴板”，“配置不匹配”：“ZeroClipboard配置与Flash的现实不匹配”，“swf-not-found”：“ZeroClipboard SWF对象无法加载，所以请检查“swfPath”配置和/或网络连接“}}，V = [”闪存不可用“，”闪存降级“，”闪存过期“，”版本不匹配“，”配置不匹配“，”剪贴板错误“]，Z = [”闪禁用”，‘闪过时的’，‘闪沙盒’，‘闪不可用’，‘闪降解’，‘闪减活的’，‘快速过期’]，U = new RegExp（“^ flash  - （”+ Z.map（function（e）{return e.replace（/ ^ flash  -  /，“”）}）。join（“|”）+“）$”）， Y = new RegExp（“^ flash  - （”+ Z.slice（1）.map（function（e）{return e.replace（/ ^ flash  -  /，“”）}）join（“|”）+ “）$”），J = {swfPath：M（），trustedDomains：e.location.host [e.location.host]：[]，cacheBust：0，forceEnhancedClipboard：1，flashLoadTimeout：3E4，autoActivate： ！0，bubbleEvents：0，数据筒： “全球zeroclipboard-HTML桥”，containerClass： “全球zeroclipboard容器”，swfObjectId：“全球寿 oclipboard闪光桥”，hoverClass： “zeroclipboard-是悬停”，activeClass： “zeroclipboard-是活性”，forceHandCursor：1，标题：空，zIndex的：999999999}，G =函数（E）{如果（ “object”== typeof e && null！== e）for（var t in e）if（w.call（e，t））if（/ ^（?: forceHandCursor | title | zIndex | bubbleEvents）$ /。test t））J [t] = e [t]; else if（null == P.bridge）if（“containerId”=== t ||“swfObjectId”=== t）{if（！de（e [ t]））throw new Error（“指定的”“+ t +”“值作为HTML4元素ID无效”）; J [t] = e [t]} else J [t] = e [t] {if（“string”！= typeof e ||！e）return S（J）; if（w.call（J，e））return J [e]}}，K = function（）{return We {浏览器：A（S，[ “的userAgent”， “平台”， “应用程序名称”]），闪速：K（P，[ “桥”]），zeroclipboard：{版本：Ve.version，配置：Ve.config （）}}}，Q =函数（）{返回!!（P.disabled || || P.outdated || P.sandboxed || P.unavailable || P.degraded P.deactivated）}，ee =对功能（（），（），（），（），（），（） == typeof e && e &&“undefined”== typeof r）for（i in e）w.call（e，i）&&“string”== typeof i && i &&“function”= =（i = 0，a = o.length; a> i; i ++）e = o [i]。 ！替换（/ ^上/ “”），S [E] = 0，Z [E] ||（Z [E] = []）中，z [E] .push（R）;如果（s.ready && P页。就绪&& Ve.emit（{类型： “就绪”}），s.error）{对于（I = 0，A = Z.length;一> I;我++）如果（P [Z [I] .replace（/ ^闪光灯- /， “”）] === 0）{Ve.emit（{类型： “错误”，名称：Z [I]}）;破}！n ==可吨&& Ve.version == N && Ve.emit （{type：“error”，name：“version-mismatch”，jsVersion：Ve.version，swfVersion：n}）}} return Ve}，te = function（e，t）{var n，r，i，a ，o; if（0 === arguments.length）a = x（z）; else if（“string”== typeof e && e）a = e.split（/ \ s + /）; else if（“object”= = typeof e && e &&“undefined”== typeof t）for（n in e）w.call（e，n）&&“string”== typeof n && n &&“function”== typeof e [n] && Ve.off（n，e [N]）;如果（一个&&则为a.length）为（n = 0时，R =则为a.length; R> N;在n ++）如果（E = A [n]的.toLowerCase（）。代替（/ ^上/，” “），O = Z [E]，邻&& o.length）如果（T），用于（ⅰ= o.indexOf（T）; - 1 == I;！）o.splice（I，1），I = 0。 indexOf（t，i）; else o.length = 0; return Ve}，ne = function（e）{var t; return t =“string”== typeof e && e？S（z [e]）|| null： S（z）}，re = function（e）{var t，n，r; return e = pe（e），e &&！xe（e）？“ready”=== e.type && P.overdu Ë=== 0 Ve.emit（{类型： “错误”，名称： “闪逾期”}）！？:( T = E（{}，E），ye.call（这一点，T），“复制“=== e.type &&（r = ke（$），n = r.data，q = r.formatMap），n）：void 0}，ie = function（）{var e = P.sandboxed; if We（），“boolean”！= typeof P.ready &&（P.ready =！1），P.sandboxed！== e && P.sandboxed ===！0）P.ready =！1，Ve.emit（{type ：“error”，name：“flash-sandboxed”}）; else if（！Ve.isFlashUnusable（）&& null === P.bridge）{var t = J.flashLoadTimeout;“number”== typeof t && t> = 0 && （{type：“error”，name：“flash-停用“}）}，t））的P.overdue =！1，硒（）}}，AE =函数（）{Ve.clearData（），Ve.blur（），Ve.emit（”消灭“）， Ae（），Ve.off（）}，oe = function（e，t）{var n; if（“object”== typeof e && e &&“undefined”== typeof t）n = e，Ve.clearData（）; else {if（“string”！= typeof e ||！e）return; n = {}，n [e] = t} for（var r in n）“string”== typeof r && r && w.call（n，r ）&&“string”== typeof n [r] && n [r] &&（$ [r] = n [r]）}，se = function（e）{“undefined”== typeof e？（j（$） ，q = null）：“string”== typeof e && w.call（$，e）&& delete $ [e]}，le = function（e）{return“un 定义“== typeof e？S（$）：”string“== typeof e && w.call（$，e）？$ [e]：void 0}，ue = function（e）{if（e && 1 === e .nodeType）{r &&（Me（r，J.activeClass），r！== e && Me（r，J.hoverClass）），r = e，Be（e，J.hoverClass）; var t = e.getAttribute标题“）|| J.title; if（”string“== typeof t && t）{var n = Ee（P.bridge）; n && n.setAttribute（”title“，t）} var i = J.forceHandCursor === ！0 ||“pointer”=== He（e，“cursor”）; qe（i），$ e（）}}，ce = function（）{var e = Ee（P.bridge）; e && .removeAttribute（ “标题”），e.style.left = “0像素”，e.style.top = “ - 9999px”，e.style.width = “1像素”，e.style.height = “1像素”）， r &&（Me（r，J.hoverClass），Me（r，J.activeClass），r = null）}，fe = function（）{return r || null}，de = function（e）{return“string” == typeof e && e && / ^ [A-Za-z] [A-Za-z0-9 _：\  -  \。] * $ /。test（e）}，pe = function（e）{var t; if（“ string“== typeof e && e？（t = e，e = {}）：”object“== typeof e && e &&”string“== typeof e.type && e.type &&（t = e.type），t）{t = t .toLowerCase（）,! e.target &&（/ ^（复印件| aftercopy |。_Click）$ /测试（T）|| “错误” ===牛逼&& “剪贴板错误” === e.name）&&（E .TARGET = I）中，E（即，{式：T，目标：e.target || ||ř空，relatedTarget：e.relatedTarget ||空，铜 rrentTarget：P && P.bridge || null，timeStamp：e.timeStamp || b（）|| null}）; var n = X [e.type];返回“error”=== e.type && e.name && n &&（n = N [e.name]）中，n &&（e.message = N）， “准备” === e.type && E（即，{目标：空，版本：P.version}）， “错误” ===即键入&&（U.test（e.name）&& E（即，{目标：空，minimumVersion：_}），Y.test（e.name）&& E（即，{版本：P.version}））， “复制” === e.type &&（e.clipboardData = {使用setData：Ve.setData，clearData：Ve.clearData}）， “aftercopy” === e.type &&（E = JE（E，q）），e.target &&！ e.relatedTarget &&（e.relatedTarget = he（e.target）），me（e）}}，he = function（e）{var t = e && e.getAttribute && e.getAttribute（“data-clipboard-target”）; return t ？o.getElementById（T）：空}，我=功能（E）{如果（E && / ^ _（？：点击|鼠标（？：超过|走出|下载|向上|移动））$ /测试（E .type））{var n = e.target，r =“_ mouseover”=== e.type && e.relatedTarget？e.relatedTarget：t，i =“_ mouseout”=== e.type && e.relatedTarget？e.relatedTarget： T，S = PE（N），L = a.screenLeft || || a.screenX 0，U = a.screenTop || || a.screenY 0，C = o.body.scrollLeft + o.documentElement.scrollLeft中，f = o.body.scrollTop + o.documentElement.scrollTop峰，d = s.left +（“numbe r“== typeof e._stageX？e._stageX：0），p = s.top +（”number“== typeof e._stageY？e._stageY：0），h = dc，m = pf，g = l + h，v = u + m，y =“number”== typeof e.movementX？e.movementX：0，b =“number”== typeof e.movementY？e.movementY：0; delete e._stageX，删除e._stageY，E（e，{srcElement：n，fromElement：r，toElement：i，screenX：g，screenY：v，pageX：d，pageY：p，clientX：h，clientY：m，x： y：m，motionX：y，movementY：b，offsetX：0，offsetY：0，layerX：0，layerY：0}）} return e}，ge = function（e）{var t = e &&“string”==类型e.type && e.type ||“”; return！/ ^（？:( ?:之前）？copy | destroy）$ /​​。test（t）}，ve = function（e，t，n，r）{ r（l）（）函数（）{e.apply（t，n）}，0）：e.apply（t，n）}，ye = function（e）{if（“object”== typeof e && e && e.type） {var t = ge（e），n = z [“*”] || []，r = z [e.type] || []，i = n.concat（r）; if（i && i.length） {var o，s，l，u，c，f = this; for（o = 0，s = i.length; s> o; o ++）l = i [o]，u = f，“string”== typeof l &&“function”== typeof a [l] &&（l = a [l]），“object”== typeof l && l &&“function”== typeof l.handleEvent &&（u = l，l = l.handleEvent） “function”== typeof l &&（c = E（{}，e），ve（l，u，[c]，t））} return this}}，be = function（e）{var t = null; return （H === 1！| | e &&“error”=== e.type && e.name &&  -  1！== V.indexOf（e.name））&&（t =！1），t}，xe = function（e）{var t = target || r || null，a =“swf”=== e._source; switch（delete e._source，e.type）{case“error”：var o =“flash-sandboxed”=== e。名称|| be（e）;“boolean”== typeof o &&（P.sandboxed = o）， -  1！== Z.indexOf（e.name）？E（P，{disabled：“flash-disabled”= == e.name，过时： “闪过时” === e.name，不可用： “闪不可用” === e.name，退化： “闪退化” === e.name，停用： “闪停用” === e.name，逾期： “闪逾期” === e.name，准备：1}）： “版本不匹配” === e.name &&（N = e.swfVersion ，E（P，{！！！禁用：1，过时的：1，不可用：1，降低：1，禁用：1，逾期：1，准备：！！！！1}）），泽（）;打破; case“ready”：n = e.swfVersion; var s = P.deactivated ===！0; E（P，{disabled：！1，过期：！1，沙盒：！1，不可用：！1， ！1，停用：！1，逾期：s，ready：！s}），ze（）; break; case“beforecopy”：i = t; break; case“copy”：var l，u，c = e。 relatedTarget;！$ [ “text / html的”] && $ [ “文本/纯”] &&ç&&（U = c.value || || c.outerHTML c.innerHTML）&&（L = c.value ||！C。的textContent || c.innerTex T）（e.clipboardData.clearData（），e.​​clipboardData.setData（ “text / plain的”，L），U ==升&& e.clipboardData.setData（ “text / html的”，U））：？！$ [ “文本/纯”] && e.target &&（L = e.target.getAttribute（ “数据剪贴板文本”））&&（e.clipboardData.clearData（），e.​​clipboardData.setData（ “text / plain的”，升））;打破;案件“aftercopy”：我们（E），Ve.clearData（），T &&牛逼==即（）&& t.focus && t.focus（）;打破;案件“_mouseover”：Ve.focus（T） !!! J.bubbleEvents === 0 &&一个&&（吨&&吨== e.relatedTarget && D（e.relatedTarget，吨）&&碲（E（{}，E {类型： “的mouseenter”，气泡：1，取消选择：1 }）），碲（E（{}，E {类型： “鼠标悬停”}）））;打破;案件“_mouseout”：Ve.blur（），J.bubbleEvents === 0 &&一个&&（吨&&吨==！ e.relatedTarget && D（e.relatedTarget，吨）&&碲！（E（{}，E {类型： “鼠标离开”，气泡：1，取消选择：1}）），碲（E（{}，E， {类型： “鼠标移出”}）））;打破;案件“_mousedown”：！成为（T，J.activeClass），J.bubbleEvents === 0 &&一个&&碲（E（{}，E {类型：e.type。片（1）}））;打破;案件“_mouseup”：ME（T，J.activeClass），J.bubbleEvents === 0 &&一个&&碲（E（{}，E {类型：e.type.slice（1！ ）}））;打破;案件“_Click”中：i =空，J.bubbleEvents === 0 &&一个&&碲（E（{}，E {类型：电子！。type.slice（1）}））;打破;案件“_mousemove”：J.bubbleEvents === 0 &&一个&&碲（E（{}，E {类型：e.type.slice（1）}））}返回/！ ^ _（？：click | mouse（？：over | out | down | up | move））$ /。test（e.type）?! 0：void 0}，we = function（e）{if（e。错误&& e.errors.length> 0）{var t = S（e）; E（t，{type：“error”，name：“clipboard-error”}），delete t.success，l（function（）{Ve .tit（t）}，0）}}，Te = function（e）{if（e &&“string”== typeof e.type && e）{var t，n = e.target || null，r = n && n.ownerDocument || O，I = {视图：r.defaultView ||一个，canBubble：0，或取消：0，细节： “点击” === e.type？1：0，按钮： “数字” == typeof运算e.which？e.which-1：“number”== typeof e.button？e.button：r.createEvent？0：1}，s = E（i，e）; n && r.createEvent && n.dispatchEvent &&（s = [s.type，s.canBubble，s.cancelable，s.view，s.detail，s.screenX，s.screenY，s.clientX，s.clientY，s.ctrlKey，s.altKey，s.shiftKey，S .metaKey，s.button，s.relatedTarget]，T = r.createEvent（ “MouseEvents”），t.initMouseEvent &&（t.initMouseEvent.apply（T，S），t._source = “JS”，n.dispatchEvent（ t）））}}，Ce = function（）{var e = J.flashLoadTimeout; if（“number”== typeof e && e> = 0）{var t = Math.min（1e3，e = e，e = e（e）&&（ze（），P.deactivated = null，Ve。发送（{type：“error”，name：“swf-not-found”}））}，t）}}，Ne = function（）{var e = o.createElement（“div”）; return e.id = J.containerId，e.className = J.containerClass，e.style.position = “绝对”，e.style.left = “0像素”，e.style.top = “ - 9999px”，e.style.width = “1px”，e.style.height =“1px”，e.style.zIndex =“”+ Re（J.zIndex），e}，Ee = function（e）{for（var t = e && e.parentNode; t && “OBJECT”=== t.nodeName && t.parentNode;）t = t.parentNode; return t || null}，Se = function（）{var e，t = P.bridge，n = Ee（t）; if ！t）{var r = Oe（a.location.host，J），i =“never”=== r？“none”：“all”，s = Fe（E（{jsVersion：Ve.version} J）），l = J.swfPath + De（J.swfPath，J）; n = Ne（）; var u = o.createElement（“div”）; n.appendChild（u），o.body.appendChild n）; var c = o.createElement（“div”），f =“activex”=== P.pluginType; c.innerHTM L =' < object id = “'+ J.swfObjectId +'”name = “'+ J.swfObjectId +'“width = ”100％“height = ”100％“'+（f？'classid = ”clsid：d27cdb6e - ae6d - 11cf - 96b8 - 444553540000“'：'type = ”application / x - shockwav e - flash“data = ”'+ l +'“'）+”>“+（f？' < param name = ”movie“value = ”'+ l +'“ / >'：”“）+' < =“allowScriptAccess”value = “'+ r +'” / ><param name = “allowNetworking”value = “'+ i +'” / ><param name = “menu”value = “false” / ><param name = wmode“value = ”transparent“ / ><param name = ”flashvars“value = ”'+ s +'“ / ><div id = ”'+ J.swfObjectId +'_ fallbackContent“ > ＆nbsp; < / div></object > '，t = c.firstChild，c = null，C（t）.ZeroClipboard = Ve，n.replaceChild（t，u），Ce（）} return t ||（t = o [J.swfObjectId]，t && e = t.length）&&（t = t [e-1]），！t && n &&（t = n.firstChild）），P.bridge = t || null，t}，Ae = function（）{var e = （e）（e）（e）（e.style.display =“none”，函数i（）{（e）{var r = Ee（e）; r &&（“activex”===PluginType &&“readyState” if（4 === e.readyState）{for（var t in e）“function”== typeof e [t] &&（e [t] = null）; e.parentNode && e.parentNode.removeChild（e），r .parentNode && r.parentNode.removeChild（r）} else l（i，10）}（））:( e.parentNode && e.parentNode.removeChild（e），r.parentNode && r.parentNode.removeChild（r））），ze（） ，pready = null，P.bridge = null，P.deactivated = null，n = t}}，ke = function（e）{var t = {}，n = {} “object”== typeof e && e）{for（var r in e）if（r && w.call（e，r）&&“string”== typeof e [r] && e [r]）switch（r.toLowerCase（）） {壳体“文本/纯”：案“文本”：案“空气：文”：案“闪光：文”：t.text = E [R]，n.text = R;打破;案件“text / html的” ：壳体“HTML”：案“空气：HTML”：案“闪光：HTML”：t.html = E [R]，n.html = R;打破;案件“应用/ RTF”：案“文本/ RTF” ：案“RTF”：案“富文本”：案“空气：RTF”：案“闪光：RTF”：t.rtf = E [R]，n.rtf = R}返回{数据：吨，formatMap：N} }}，je = function（e，t）{if（“object”！= typeof e ||！e ||“object”！= typeof t ||！t）return e; var n = {}如果（w.call（e，r））if（“errors”=== r）{n [r] = e [r]？e [r] .slice（）：[]; for （var i = 0，a = n [r] .length; a> i; i ++）n [r] [i] .format = t [n [r] [i] .format] ！== r &&“data”！== r）n [r] = e [r]; else {n [r] = {}; var o = e [r]; for（var s in o）s && w.call （o，s）&& w.call（t，s）&&（n [r] [t [s]] = o [s]）} return n}，De = function（e，t）{var n = null = = t || t && t.cacheBust ===！0; return n？（ -  1 === e.indexOf（“？”）？“？”：“＆”）+“noCache =”+ b（） “}，Fe = function（e）{var t，n，r，i，o =”“，s = []; if（e.trustedDomains &&（”string“== typeof e.trustedDomains？i = [e。相信 （t = 0，n = i.length; n> t; t ++）的e.trustedDomains &&（i = e.trustedDomains）中的“object”== typeof e.trustedDomains &&“length”），i && i.length） if（w.call（i，t）&& i [t] &&“string”== typeof i [t]）{if（r = Le（i [t]），！r）continue; if（“*”= == R）{s.length = 0，s.push（R）;破} s.push.apply（S，[R， “//” + R，a.location.protocol + “//” + R] ）} return s.length &&（o + =“trustedOrigins =”+ p（s.join（“，”））），e.forceEnhancedClipboard ===！0 &&（o + =（o？“＆”：“”）+ forceEnhancedClipboard = true“），”string“== typeof e.swfObjectId && e.swfObjectId &&（o + =（o？”＆“：”“）+”swfObjectId =“+ p（e.swfObjectId）），”string“== typeof e.jsVersion && e.jsVersion &&（O + =（O “＆”： “”）+ “jsVersion =” + p（e.jsVersion）），邻}，乐=函数（E）{如果（空==Ë|| “”=== e）return null; if（e = e.replace（/ ^ \ s + | \ s + $ / g，“”），“”=== e）return null; var t = e.indexOf “//");e=-1===t?e:e.slice(t+2);var n = e.indexOf（”/“）; return e = -1 === n？e： -1 ===吨|| 0 ===ñ空：e.slice（0，N）中，e && “SWF”。=== e.slice（-4）.toLowerCase（）空量：我|| null}，Oe = function（）{var e = function（e）{var t，n，r，i = []; if（“string”== typeof e &&（e = [e]），“object”！ = typeof e ||！e ||“number”！= typeo （t = 0，n = e.length; n> t; t ++）if（w.call（e，t）&&（r = Le（e [t]）））{ if（“*”=== r）{i.length = 0，i.push（“*”）; break} -1 === i.indexOf（r）&& i.push（r）} return i};返回函数（t，n）{var r = Le（n.swfPath）; null === r &&（r = t）; var i = e（n.trustedDomains），a = i.length; if（a> 0 ）{if（1 === a &&“*”=== i [0]）return“always”; if（-1！== i.indexOf（t））return 1 === a && t === r？ “isDomain”：“always”} return“never”}}（），Ie = function（）{try {return o.activeElement} catch（e）{return null}}，Be = function（e，t） n，r，i，a = []; if（“string”== typeof t && t &&（a = t.split（/ \ s + /）），e && 1 === e.nodeType && a.length> 0）if（e。 （n = 0，r = a.length; r> n; n ++）e.classList.add（a [n]）; else if（e.hasOwnProperty（“className”））{for（i = “+ e.className +”“，n = 0，r = a.length; r> n; n ++） -  1 === i.indexOf（”“+ a [n] +”“）&&（i + = a [ n] +“”）; e.className = i.replace（/ ^ \ s + | \ s + $ / g，“”）} return e}，Me = function（e，t）{var n，r，i， a = []; if（“string”== typeof t && t &&（a = t.split（/ \ s + /）），e && 1 === e.nodeType && a.length> 0）if（e.classList && e.classList.length> 0）for（n = 0，r = a.length; r> n; n ++）e.classList.remove（a [n]）; else if（e.cl assName）{for（i =（“”+ e.className +“”）.replace（/ [\ r \ n \ t] / g，“”），n = 0，r = a.length; r> n; n ++）i = i.replace（“”+ a [n] +“”，“”）; e.className = i.replace（/ ^ \ s + | \ s + $ / g，“”）} return e}， He = function（e，t）{var n = d（e，null）.getPropertyValue（t）; return“cursor”！== t || n &&“auto”！== n ||“A”！== e.nodeName？n：“pointer”}，Pe = function（e）{var t = {left：0，top：0，width：0，height：0}; if（e.getBoundingClientRect）{var n = e .getBoundingClientRect（）中，r = a.pageXOffset，I = a.pageYOffset，S = o.documentElement.clientLeft || 0，L = o.documentElement.clientTop || 0，U = 0，C = 0;如果（”相对“=== He（o.body，”position“））{var f = o.body.getBoundingClientRect（），d = o.documentElement.getBoundingClientRect（）; u = f.left-d.left || 0 ，c = f.top-d.top || 0} t.left = n.left + rsu，t.top = n.top + ilc，t.width =“width”in n？n.width：n。 right-n.left，t.height =“height”in n？n.height：n.bottom-n.top} return t}，_ e = function（e）{if（！e）return！1; var t = D（E，空）中，n = v（t.height）> 0，R = v（t.width）> 0，I = v（t.top）> = 0，A = v（t.left） > = 0，O = N &&ř&&我&&一个，S = O空：？！PE（e）中，L = “无” == t.display && “崩溃” == t.visibility &&（O || !!小号&&（N || s.height> 0）&& （r || s.width> 0）&&（i || s.top> = 0）&&（a || s.left> = 0））; return l}，ze = function（）{u（R） ，R = 0，f（W），W = 0}，$ e = function（）{var e; if（r &&（e = Ee（P.bridge）））{var t = Pe（r） e.style，{宽度：t.width + “PX”，高度：t.height + “PX”，顶端：t.top + “PX”，左：t.left + “PX”，zIndex的： “” +重（j。 zIndex）}）}}，qe = function（e）{P.ready ===！0 &&（P.bridge &&“function”== typeof P.bridge.setHandCursor？P.bridge.setHandCursor（e）：P.ready =！1）}，Re = function（e）{if（/ ^（?: auto | inherit）$ /。test（e））return e; var t; return“number”！= typeof e || y e）？“string”== typeof e &&（t = Re（g（e，10）））：t = e，“number”== typeof t？t：“auto”}，We = function（t）{ var n，r，i，a = P.sandboxed，o = null; if（t = t ===！0，H ===！1）o =！1; else {try {r = e.frameElement | |空}赶上（S）{I = {名称：s.name，消息：s.message}}如果（R && 1 === r.nodeType && “IFRAME” === r.nodeName）尝试{O = r.hasAttribute （ “沙箱”）}赶上（S）{O = NULL}否则{尝试{N = document.domain的||空}赶上（S）{N = NULL}（空===ñ||我&& “的SecurityError”= == i.name && /（^ | [\ S \（\ [@]）沙箱（ES |编辑|荷兰国际集团| [\ S \，\）\] @！] | $）/测试（i.message .toLowerCase（）））&&（o =！0）}} return P.sandboxed = o，a === o || t || Xe（h），o}，Xe = fu （e）{function t（e）{var t = e.match（/ [d] + / g）; return t.length = 3，t.join（“。”）} function n（e）{返回!!Ë&&（E = e.toLowerCase（））&&（/ ^（pepflashplayer \ .dll文件| libpepflashplayer \。所以|。pepperflashplayer \ .plugin）$ /测试（E）|| “Chrome.plugin的” === e.slice（-13））}函数r（e）{e &&（l =！0，e.version &&（f = t（e.version）），！f && e.description &&（f = t（e.description） ，e.filename &&（c = n（e.filename）））} var i，a，o，l =！1，u =！1，c =！1，f =“”; if（s.plugins && s.plugins .length）i = s.plugins [“Shockwave Flash”]，r（i），s.plugins [“Shockwave Flash 2.0”] &&（l =！0，f =“2.0.0.11”）; else if .mimeTypes && s.mimeTypes.length）o = s.mimeTypes [“application / x-shockwave-flash”]，i = o && o.enabledPlugin，r（i）; else if（“undefined”！= typeof e）{u =！ 0;尝试{a = new e（“ShockwaveFlash.ShockwaveFlash.7”），l =！0，f = t（a.GetVariable（“$ version”））} catch（d）{try {a = new e “ShockwaveFlash.ShockwaveFlash.6”），l =！0，f =“6.0.21”} catch（p）{try {a = new e（“ShockwaveFlash.ShockwaveFlash”），l =！0，f = a.GetVariable（ “$版本”））}赶上（H）{U =！1}}}} P.disabled = 1！==！0，P.outdated = F && v（F）<v（_），P .version = F || “0.0.0”，P.pluginType = c？“pepper”：u？“activex”：l？“netscape”：“unknown”}; Xe（h），We（！0）; var Ve = function（）{return this instanceof Ve？void “== typeof Ve._createClient && Ve._createClient.apply（this，N（arguments）））：new Ve}; Ve.version =”2.2.0“，Ve.config = function（）{return G.apply（this， N（arguments））}，Ve.state = function（）{return K.apply（this，N（arguments））}，Ve.isFlashUnusable = function（）{return Q.apply（this，N（arguments））} ，Ve.on = function（）{return ee.apply（this，N（arguments））}，Ve.off = function（）{return te.apply（this，N（arguments））}，Ve.handlers = function （）{return ne.apply（this，N（arguments））}，Ve.emit = function（）{return re.apply（this，N（arguments））}，Ve.create = function（）{return ie。 apply（this，N（arguments））}，Ve.destroy = function（）{return ae.apply（this，N（arguments））}，Ve.setData = function（）{return oe.apply（this，N参数））}，Ve.clearData = function（）{return se.apply（this，N（arguments））}，Ve.getData = function（）{return le.apply（this，N（arguments））}，Ve .focus = Ve.activate = function（）{return ue.apply（this，N（arguments））}，Ve.blur = Ve.deactivate = functi on（）{return ce.apply（this，N（arguments））}，Ve.activeElement = function（）{return fe.apply（this，N（arguments））}; var Ze = 0，Ue = {} Ye = 0，Je = {}，Ge = {}; E（J，{autoActivate：！0}）; var Ke = function（e）{var t = this; t.id =“”+ Ze ++， t.id] = {instance：t，elements：[]，处理程序：{}}，e && t.clip（e），Ve.on（“*”，function（e）{return t.emit（e）}） ，Ve.on（“destroy”，function（）{t.destroy（）}），Ve.create（）}，Qe = function（e，r）{var i，a，o，s = {} = Ue [this.id]，u = l && l.handlers; if（！l）throw new Error（“尝试向已销毁的ZeroClipboard客户端实例添加新的监听器”）; if（“string”== typeof e && e ）o = e.toLowerCase（）。split（/ \ s + /）; else if（“object”== typeof e && e &&“undefined”== typeof r）for（i in e）w.call（e，i）&& “string”== typeof i && i &&“function”== typeof e [i] && this.on（i，e [i]）; if（o && o.length）{for（i = 0，a = o.length; a> I;！我++）E =问题o [I] .replace（/ ^上/ “”），S [E] = 0，U [E] ||（U [E] = []）中，u [E] .push（R）;如果（s.ready && P.ready && this.emit（{类型： “就绪”，客户端：此}），s.error）{对于（I = 0，A = Z.length;一> I;我++）如果（P [Z [I] .replace（/ ^闪光灯- /， “”）]）{this.emit（{类型： “错误”，名称：Z [I]，客户端：此}）;破} N！== t && Ve.version！== n && this.emit（{type：“error”，name：“version-mismatch”，jsVersion：Ve.version，swfVersion：n}）}} return this}，et = function（e， t）{var n，r，i，a，o，s = Ue [this.id]，l = s && s.handlers; if（！l）return this; if（0 === arguments.length）a = x （l）; else if（“string”== typeof e && e）a = e.split（/ \ s + /）; else if（“object”== typeof e && e &&“undefined”== typeof t）for（n in e ）w.call（e，n）&&“string”== typeof n && n &&“function”== typeof e [n] && this.off（n，e [n]）; if（a && a.length）for（n =中，r =则为a.length; R> N;在n ++）如果（E = A [n]的.toLowerCase（）代替（/ ^上/ “”），O = 1 [E]，邻&& o.length）如果（ t）for（i = o.indexOf（t）;  -  1！== i;）o.splice（i，1），i = o.indexOf（t，i）; else o.length = 0;返回此}，tt = function（e）{var t = null，n = Ue [this.id] && Ue [this.id] .handlers; return n &&（t =“string”== typeof e && e？n [e]？n [e] .slice（0）：[]：S（n）），t}，nt = function（e）{if（st.call（this，e））{“object”== typeof e && e &&“string” == typeof e.type && e.type &&（e = E（{}，e））; var t = E（{}，pe（e），{client：this}）; lt.call（this，t）} return这个}，rt = function（e）{if（！Ue [this.id]）throw new Error（“尝试将元素剪切到一个被破坏的Zer 对于（var t = 0; t <e.length; t ++）if（w.call（e，t）&& e [t] && 1 === e [t] .nodeType）{E [T] .zcClippingId？-1 ===济[E [T] .zcClippingId] .indexOf（this.id）&&济[E [T] .zcClippingId] .push（this.id）:( e [t] .zcClippingId =“zcClippingId _”+ Ye ++，Je [e [t] .zcClippingId] = [this.id]，J.autoActivate ===！0 && ct（e [t]））; var n = Ue [ this.id] && Ue [this.id] .elements; -1 === n.indexOf（e [t]）&& n.push（e [t]）} return this}，it = function（e）{var t = Ue [this.id]; if（！t）return this; var n，r = t.elements; e =“undefined”== typeof e？r.slice（0）：ut（e）; for I = e.length; I  - ）如果（w.call（E，I）&& E [I] && 1个=== E [I] .nodeType）{对于（N = 0; -1 ==（N！ = r.indexOf（e [i]，n））;）r.splice（n，1）; var a = Je [e [i] .zcClippingId]; if（a）{for（n = 0; -1 ！==（N = a.indexOf（this.id，N））;）a.splice（N，1）;！0 ===则为a.length &&（J.autoActivate === 0 &&英尺（E [I]） ，删除e [i] .zcClippingId）}} return this}，at = function（）{var e = Ue [this.id]; return e && e.elements？e.elements.slice（0）：[]}，ot = function（）{Ue [this.id] &&（this.unclip（），this.off（），delete Ue [this.id]）}，st = function（e）{if（！e ||！e .TYPE）返回1;！如果（e.client && e.cl 唔！== this）return！1; var t = Ue [this.id]，n = t && t.elements，r = !! n && n.length> 0，i =！e.target || r &&  -  1！ n.indexOf（e.target），a = e.relatedTarget && r &&  -  1！== n.indexOf（e.relatedTarget），o = e.client && e.client === this; return t &&（i || a || o ）？！0：！1}，lt = function（e）{var t = Ue [this.id]; if（“object”== typeof e && e && e.type && t）{var n = ge（e），r = t && t .handler [“*”] || []，i = t && t.handlers [e.type] || []，o = r.concat（i）; if（o && o.length）{var s，l，u， c，f，d = this; for（s = 0，l = o.length; l> s; s ++）u = o [s]，c = d，“string”== typeof u &&“function”== typeof a [u] &&（u = a [u]），“object”== typeof u && u &&“function”== typeof u.handleEvent &&（c = u，u = u.handleEvent），“function”== typeof u && f = E（{}，e），ve（u，c，[f]，n））}}}，ut = function（e）{return“string”== typeof e &&（e = []数字“！= typeof e.length？[e]：e}，ct = function（e）{if（e && 1 === e.nodeType）{var t = function（e）{（e ||（e = a .event））&&（“js”！== e._source &&（e.stopImmediatePropagation（），e.​​preventDefault（）），delete e._source）}，n = function（n）{（n ||（n = a.event））&&（T（N），Ve.focus（E））};！e.addEventListener（ “鼠标悬停”，N，1），e.addEventListener（ “鼠标移出”，T，1）中，e 。（！ “鼠标移动”，T，1）的addEventListener（！ “的mouseenter”，T，1），e.addEventListener（@ “鼠标离开”，T，1），e.addEventListener，戈[e.zcClippingId] = {鼠标悬停： n，mouseout：t，mouseenter：t，mouseleave：t，mousemove：t}}}，ft = function（e）{if（e && 1 === e.nodeType）{var t = Ge [e.zcClippingId]; if （“object”== typeof t && t）{for（var n，r，i = [“move”，“leave”，“enter”，“out”，“over”]，a = 0，o = i.length ; o> a; a ++）n =“mouse”+ i [a]，r = t [n]，“function”== typeof r && e.removeEventListener（n，r，！1）; delete Ge [e.zcClippingId] }}}; Ve._createClient = function（）{Ke.apply（this，N（arguments））}，Ve.prototype.on = function（）{return Qe.apply（this，N（arguments））}，Ve .prototype.off = function（）{return et.apply（this，N（arguments））}，Ve.prototype.handlers = function（）{return tt.apply（this，N（arguments））}，Ve.prototype .emit = function（）{return nt.apply（this，N（arguments））}，Ve.prototype.clip = function（）{return rt.apply（this，N（arguments））}，Ve.prototype.unclip = function（）{return it.apply（this，N（arguments））}，Ve.prototype.elements = function（）{return at.apply（this，N（arguments））}，Ve.prototype.destroy = function（）{return ot.apply（this，N（arguments））}，Ve.prototype.setText = function（e）{if（！Ue [this.id]）throw new Error（“Attempt to set pending clipboard数据来自销毁的ZeroClipboard客户端实例“）;返回Ve.setData（”text / plain“，e），this}，Ve.prototype.setHtml = function（e）{if（！Ue [this.id]）throw new错误（“尝试从销毁的ZeroClipboard客户端实例设置挂起的剪贴板数据”）;返回Ve.setData（“text / html”，e），this}，Ve.prototype.setRichText = function（e）{if（！ [this.id]）throw new Error（“尝试从销毁的ZeroClipboard客户端实例设置挂起的剪贴板数据”）;返回Ve.setData（“application / rtf”，e），this}，Ve.prototype.setData = function （）{if（！Ue [this.id]）throw new Error（“尝试从销毁的ZeroClipboard客户端实例设置挂起的剪贴板数据”）; return Ve.setData.apply（this，N（arguments）），this} ，Ve.prototype.clearData = function（）{if（！Ue [this.id]）throw new Error（“尝试从销毁的ZeroClipboard客户端实例清除待处理的剪贴板数据” ）; return Ve.clearData.apply（this，N（arguments）），this}，Ve.prototype.getData = function（）{if（！Ue [this.id]）throw new Error（“Tryempt to get pending clipboard数据来自销毁的ZeroClipboard客户端实例“）;返回Ve.getData.apply（this，N（arguments））}，”function“== typeof define && define.amd？define（”/ ZeroClipboard“，function（）{return Ve} ）：“object”== typeof module && module &&“object”== typeof module.exports && module.exports？module.exports = Ve：e.ZeroClipboard = Ve}（function（）{return this || window}（））}）;
define（“/ css3-mediaqueries”，function（e，t）{“function”！= typeof Object.create &&（Object.create = function（e）{function t（）{} return t.prototype = e，new t }}; var n = {toString：function（）{return navigator.userAgent}，test：function（e）{return this.toString（）。toLowerCase（）。indexOf（e.toLowerCase（））>  -  1}} ; n.version =（n.toString（）。toLowerCase（）。match（/ [\ s \ S] +（?: rv | it | ra | ie）[\ /：]（[\ d。] + /）|| []）[1]，n.webkit = n.test（ “WebKit的”），n.gecko = n.test（ “壁虎”）&&！n.webkit，n.opera = n.test（ “opera”），n.ie = n.test（“msie”）&&！n.opera，n.ie6 = n.ie && document.compatMode &&“undefined”== typeof document.documentElement.style.maxHeight，n.ie7 = n.ie && document.documentElement &&“undefined”！= typeof document.documentElement.style.maxHeight &&“undefined”== typeof XDomainRequest，n.ie8 = n.ie &&“undefined”！= typeof XDomainRequest; var r = function（）{var e = []，t = function（）{if（！arguments.callee.done）{arguments.callee.done =！0; for（var t = 0; t <e.length; t ++）e [t]（） }}; return document.addEventListener && document.addEventListener（“DOMContentLoaded”，t，！1），n.ie &&（！function（）{t ry {document.documentElement.doScroll（“left”），document.body.length} catch（e）{return void setTimeout（arguments.callee，50）} t（）}（），document.onreadystatechange = function（） “完整的” === document.readyState &&（document.onreadystatechange = NULL，T（））}），n.webkit && document.readyState &&功能（）{ “加载” == document.readyState T（）：！？的setTimeout（参数（）;（）; e（e，l，n），n}} （），i = function（）{var e，t = {BLOCKS：/ [^ \ s {] [^ {] * \ {（？：[^ {}] * \ {[^ {}] * \ [^ {}] * | [^ {}] *）* \} /克，BLOCKS_INSIDE：/ [^ \ S {] [^ {] * \ {[^ {}] * \} /克，DECLARATIONS：/ [A-ZA-Z \  - ] + [^] *：[^] +; /克，RELATIVE_URLS：/ URL \（[ '“]（ [ ^ \ / \）'”] [^：\ ）“ '] + ）'”] \）/克，REDUNDANT_COMPONENTS：/（？：？！\ / \ *（[^ * \\\\] | \ *（\ /））+ \ * \ / | @import [^] +; | @ -moz文档\ S * URL前缀\（\）\ S * {（（[^ {}]）+ {（[^ {}]）+}（[ ^ {}]）+）+}）/克，REDUNDANT_WHITESPACE：/ \ S *（，|：|; | \ {| \}）\ S * /克，MORE_WHITESPACE：/ \ S {2，} /克， FINAL_SEMICOLONS：/; \} / g，NOT_WHITESPACE：/ \ S + / g}，o =！1，a = []，s = function（e）{“function”== typeof e &&（a [a.length] = e）}，l = function（）{for（var t = 0 ; t <a.length; t ++）a [t]（e）}，u = {}，c =函数（e，t）{if（u [e]）{var n = u [e] if（n）for（var r = 0; r <n.length; r ++）n [r]（t）}}，f = function（e，t，r）{if（n.ie &&！window.XMLHttpRequest && window.XMLHttpRequest = function（）{return new ActiveXObject（“Microsoft.XMLHTTP”）}），！XMLHttpRequest）return“”; var i = new XMLHttpRequest; try {i.open（“get”，e，！0） i.setRequestHeader（“X_REQUESTED_WITH”，“XMLHttpRequest”）} catch（o）{return void r（）} var a =！1; setTimeout（function（）{a =！0}，5e3），document.documentElement.style .cursor = “进步”，i.onreadystatechange =函数（）{4 == i.readyState || ||一个（i.status && “文件：”！=== location.protocol || i.status> = 200 &&我.status <300 || 304 === i.status || navigator.userAgent.indexOf（“Safari”）>  -  1 &&“undefined”== typeof i.status？t（i.responseText）：r（），document .documentElement.style.cursor =“”，i = null）}，i.send（“”）}，d = function（e）{return e = e.replace（t.REDUNDANT_COMPONENTS，“”），e = e .replace（t.REDUNDANT_WHITESPACE，“$ 1”），e = e.replace（t.MORE_WHITESPACE，“”），e = e.replace（t.FINAL_SEMICOLONS，“}”）}，p = {mediaQueryList：function ）{var n = { }，r = e.indexOf（“{”），i = e.substring（0，r）; e = e.substring（r + 1，e.length-1）; for（var o = []，a = []，S = i.toLowerCase（）子（7）.split（ “”）中，l = 0;升<s.length;升++）O [o.length] = p.mediaQuery（S [升]，n）; var u = e.match（t.BLOCKS_INSIDE）; if（null！== u）for（l = 0; l <u.length; l ++）a [a.length] = p.rule u [l]，n）; return n.getMediaQueries = function（）{return o}，n.getRules = function（）{return a}，n.getListText = function（）{return i}，n.getCssText = function （）{return e}，n}，mediaQuery：function（e，n）{e = e ||“”; for（var r，i =！1，o = []，a =！0，s = e .match（t.NOT_WHITESPACE），l = 0; l <s.length; l ++）{var u = s [l]; if（r ||“not”！== u &&“only”！== u）if （r）{if（“（”=== u.charAt（0））{var c = u.substring（1，u.length-1）.split（“：”）; o [o.length] = {mediaFeature：c [0]，value：c [1] || null}}} else r = u; else“not”=== u &&（i =！0）} return {getList：function（）{return n || null}，getValid：function（）{return a}，getNot：function（）{return i}，getMediaType：function（）{return r}，getExpressions：function（）{return o}}}，rule：function （0，r），o = i.split（“，”），a = [（n， ]，S = e.substring（R + 1，E。length = 1）.split（“;”），l = 0; l <s.length; l ++）a [a.length] = p.declaration（s [l]，n）; return n.getMediaQueryList = function ）{return t || null}，n.getSelectors = function（）{return o}，n.getSelectorText = function（）{return i}，n.getDeclarations = function（）{return a}，n.getPropertyValue = function （e）{for（var t = 0; t <a.length; t ++）if（a [t] .getProperty（）=== e）返回一个[t] .getValue（）;返回null}，n} ，声明：function（e，t）{var n = e.indexOf（“：”），r = e.substring（0，n），i = e.substring（n + 1）; return {getRule：function ）{return t || null}，getProperty：function（）{return r}，getValue：function（）{return i}}}}，h = function（n）{if（“string”== typeof n.cssHelperText ）{var r = {mediaQueryLists：[]，rules：[]，selectors：{}，declarations：[]，properties：{}}，i = r.mediaQueryLists，o = r.rules，a = n.cssHelperText。 match（t.BLOCKS）; if（null！== a）for（var s = 0; s <a.length; s ++）“@ media”=== a [s] .substring（0,7）？ I [i.length] = p.mediaQueryList（一个[S]），O = r.rules = o.concat（I [i.length-1] .getRules（）））：○[o.length] = p .rule（a [s]）; var l = r.selectors，u = function（e）{for（var t = e.getSelectors（），n = 0; n <t.len g（n））（）（）（）（）（）（） （s = 0; s <o.length; s ++）c = r.declarations = c.concat（o [s] .getDeclarations（））; var f = r.properties; for（s = 0; s <c.length; s ++）{var d = c [s] .getProperty（）; f [d] || f [d] = []），f [d] [f [d] .length] = c [s]} return n.cssHelperParsed = r，e [e.length] = n，r}}，m = （e，t）{return e.cssHelperText = d（t || e.innerHTML），h（e）}，g = function（）{o =！0，e = []; for（var n = [] ，r = function（）{for（var e = 0; e <n.length; e ++）h（n [e]）; var t = document.getElementsByTagName（“style”）; for（e = 0; e < t.length; e ++）m（t [e]）; o =！1，l（）}，i = document.getElementsByTagName（“link”），a = 0; a <i.length; a ++）{var s = I [A]; s.getAttribute（ “相对”）的indexOf（ “风格”）>  -  1 && s.href && 0 == s.href.length && s.disabled &&（N [n.length] = S）}如果！！ （n.length> 0）{var u = 0，c = function（）{u ++，u === n.length && r（）}，p = function（e）{var n = e.href; f（n，功能（R）{R = D（r）的.replace（t.RELATIVE_URLS， “URL（” + n.substring（0，n.lastIndexOf（ “/”））+ “/ $ 1）”），e.cssHelperText = r，c（）}，c）}; for（a = 0; a <n.length; a ++）p（n [a]）} else r（）}，y = {mediaQuer yLists： “阵列”，规则： “阵列”，选择器： “对象”，声明： “阵列”，属性： “对象”}，V = {mediaQueryLists：空，规则：空，选择器：无效，声明：空，属性：null}，b = function（e，t）{if（null！== v [e]）{if（“array”=== y [e]）return v [e] = v [e]。 concat（t）; var n = v [e]; for（var r in t）t.hasOwnProperty（r）&&（n [r]？n [r] = n [r] .concat（t [r] ：n [r] = t [r]）; return n}}，x = function（t）{v [t] =“array”=== y [t]？[]：{}; for（var n = 0; n <e.length; n ++）b（t，e [n] .cssHelperParsed [t]）; return v [t]}; r（function（）{for（var e = document.body.getElementsByTagName “*”），T = 0;吨<e.length;吨++）E [T] .checkedByCssHelper = 0;！？document.implementation.hasFeature（ “MutationEvents”， “2.0”）|| window.MutationEvent document.body的.addEventListener（“DOMNodeInserted”，function（e）{var t = e.target; 1 === t.nodeType &&（c（“DOMElementInserted”，t），t.checkedByCssHelper =！0）}，！1）：setInterval （function（）{for（var e = document.body.getElementsByTagName（“*”），t = 0; t <e.length; t ++）e [t] .checkedByCssHelper ||（c（“DOMElementInserted”，e [ t]），e [t] .checkedByCssHelper =！0）}，1e3）}）; var w = function（e）{r eturn“undefined”！= typeof window.innerWidth？window [“inner”+ e]：“undefined”！= typeof document.documentElement &&“undefined”！= typeof document.documentElement.clientWidth && 0！= document.documentElement.clientWidth？document。 document.ElementById（“css-mediaqueries-js”）？n = document.getElementById （ “CSS-mediaqueries-JS”）:( N =使用document.createElement（ “风格”），n.setAttribute（ “类型”， “文本/ CSS”），n.setAttribute（ “ID”，“CSS-mediaqueries- JS “），document.getElementsByTagName（” 头“）[0] .appendChild（N）），n.styleSheet n.styleSheet.cssText + = E：n.appendChild（document.createTextNode（E）），n.addedWithCssHelper = ！0，“undefined”== typeof t || t ===！0？i.parsed（function（t）{var r = m（n，e）; for（var i in r））r.hasOwnProperty（i ）&& b（i，r [i]）; c（“newStyleParsed”，n）}）：n.parsingDisallowed =！0，n}，removeStyle：function（e）{return e.parentNode？e.parentNode.removeChild e）：void 0}，解析：function（t）{o？s（t）：“undefined”！= typeof e？“function”== typeof t && t（e）:( s（t），g（）） }，媒体 QueryLists：功能（E）{i.parsed（函数（t）的{E（v.mediaQueryLists || X（ “mediaQueryLists”））}）}，规则：函数（E）{i.parsed（函数（t）的{ E（v.rules || X（ “规则”））}）}，选择器：功能（E）{i.parsed（函数（t）的{E（v.selectors || X（ “选择”））}） }，声明：功能（E）{i.parsed（函数（t）的{E（v.declarations || X（ “声明”））}）}，属性：功能（E）{i.parsed（函数（吨）{e（v.properties || x（“properties”））}）}，broadcast：c，addListener：function（e，t）{“function”== typeof t &&（u [e] ||（u [ e] = {listeners：[]}），u [e] .listeners [u [e] .listeners.length] = t）}，removeListener：function（e，t）{if（“function”== typeof t && u对于（var n = u [e] .listeners，r = 0; r <n.length; r ++）n [r] === t &&（n.splice（r，1），r- = 1 ）}，getViewportWidth：function（）{return w（“Width”）} getViewportHeight：function（）{return w（“Height”）}}}（）; r（function（）{var e，t = {LENGTH_UNIT ：/ [0-9] +（EM | EX | PX |在|厘米|毫米| PT | PC）$ /，RESOLUTION_UNIT：/ [0-9] +（DPI | DPCM）$ /，ASPECT_RATIO：/ ^ [ 0-9] + \ / [0-9] + $ /，ABSOLUTE_VALUE：/ ^ [0-9] *（\ [0-9] +）* $ /}，R = []，O =函数（ ）{var e =“css3-mediaqueries-test”，t = document.c reateElement（“div”）; t.id = e; var n = i.addStyle（“@ media all and（width）{＃”+ e +“{width：1px！}}“，！1）; document.body.appendChild（t）; var r = 1 === t.offsetWidth; return n.parentNode.removeChild（n），t.parentNode.removeChild（t），o = function （）{return r}，r}，a = function（）{e = document.createElement（“div”），e.style.cssText =“position：absolute; top：-9999em; left：-9999em; margin： 0;边界：无;填充：0;宽度：1EM;字体大小：1em的;”，document.body.appendChild（e）中，16 == e.offsetWidth &&（e.style.fontSize = 16 / e.offsetWidth + “em”），e.style.width =“”}，s = function（t）{e.style.width = t; var n = e.offsetWidth; return e.style.width =“”，n} l = function（e，n）{var r = e.length，i =“min  - ”=== e.substring（0,4），o =！i &&“max  - ”=== e.substring（0 ，4）; if（null！== n）{var a，l; if（t.LENGTH_UNIT.exec（n））a =“length”，l = s（n）; else if（t.RESOLUTION_UNIT.exec （n））{a =“resolution”，l = parseInt（n，10）; var u = n.substring（（l +“”）。length）} else t.ASPECT_RATIO.exec（n）？（a =宽高比“，l = n.split（”/“））：t.ABSOLUTE_VALUE？（a =”absolute“，l = n）：a =”unknown“} var c，f; if（”device-width “=== e.substring（r-12，r））return c = screen.width，null！== n？”length“=== a？i && c> = l || o && l> c ||！i &&！ O！&&ç===升：1：C> 0;如果（“dev的 ice-height“=== e.substring（r-13，r））return f = screen.height，null！== n？”length“=== a？i && f> = l || o && l> f || ！i &&！o && f === l：！1：f> 0; if（“width”=== e.substring（r-5，r））return c = document.documentElement.clientWidth || document.body.clientWidth ，空== N “长度” === A I && C> = 1 ||ö&& L> c ^ ||我&&ö&&ç===升：1：！？！！C> 0;如果（ “高度” === e.substring（r-6，r））return f = document.documentElement.clientHeight || document.body.clientHeight，null！== n？“length”=== a？i && f> = l || o && l> f ||！i &&！o && f === l：！1：f> 0; if（“orientation”=== e.substring（r-11，r））return c = document.documentElement.clientWidth || document.body ？.clientWidth，F = document.documentElement.clientHeight || document.body.clientHeight， “绝对” ===一个 “纵向” ===升˚F> = C：C> F：？！1;如果（“纵横-ratio“=== e.substring（r-12，r））{c = document.documentElement.clientWidth || document.body.clientWidth，f = document.documentElement.clientHeight || document.body.clientHeight; var d = C / F，p = 1 [1] / L [0];返回 “纵横比” === A I && D> = p ||ö&& p>ð||我&&ö&&ð===号码：1？！！ }如果（ “设备纵横比” === e.substring（R-19，R））返回 “纵横比” ===一个＆＆screen.width * l [1] === screen.height * l [0]; if（“color-index”=== e.substring（r-11，r））{var h = Math.pow ，screen.colorDepth）; return null！== n？“absolute”=== a？i && h> = l || o && l> h ||！i &&！o && h === l：！1：h> 0} if “color”=== e.substring（r-5，r））{var m = screen.colorDepth; return null！== n？“absolute”=== a？i && m> = l || o && l> m | |！i &&！o && m === l：！1：m> 0} if（“resolution”=== e.substring（r-10，r））{var g; return g = s（“dpcm”== = U “1厘米”？： “1英寸”），空== N “分辨率” === A I &&克> = 1 ||ö&&升>克||我&&ö&&克===升：！？!!! 1：克> 0} return！1}，u = function（e）{var t = e.getValid（），n = e.getExpressions（），r = n.length; if（r> 0）{for（var i = 0; r> i && t; i ++）t = l（n [i] .mediaFeature，n [i] .value）; var o = e.getNot（）; return t &&！o || o &&！t}}，c =函数（e）{for（var t = e.getMediaQueries（），n = {}，o = 0; o <t.length; o ++）u（t [o]）&&（n [t [o] .getMediaType （）] =！0）; var a = []，s = 0; for（var l in n）n.hasOwnProperty（l）&&（s> 0 &&（a [s ++] =“，”），a [ ] = l）; a.length> 0 &&（r [r.length] = i.addStyle（“@ media”+ a.join（“”）+“{”+ e.getCssText（）+“}” 1））}，f = function（e）{for（var t = 0; t <e.length; t ++）c（e [t]）; n.ie?(document.documentElement.style.display="bl 玉珠 “的setTimeout（函数（）{document.documentElement.style.display = ”“}，0），的setTimeout（函数（）{i.broadcast（ ”cssMediaQueriesTested“）}，100））：i.broadcast（” cssMediaQueriesTested “）}，d = function（）{for（var e = 0; e <r.length; e ++）i.removeStyle（r [e]）; r = []，i.mediaQueryLists（f）}，p = 0，h = function（）{var e = i.getViewportWidth（），t = i.getViewportHeight（）; if（n.ie）{var r = document.createElement（“div”）; r.style.width = “100像素”，r.style.height = “100像素”，r.style.position = “绝对”，r.style.top = “ -  9999em”，r.style.overflow = “滚动”，document.body.appendChild （r），p = r.offsetWidth-r.clientWidth，document.body.removeChild（r）} var a，s = function（）{var n = i.getViewportWidth（），r = i.getViewportHeight（）; Math.abs（NE）>点|| Math.abs（RT）> p）&&（E = N，T = R，clearTimeout（a）中，= setTimeout的（函数（）{O（）？i.broadcast（ “cssMediaQueriesTested”）：d（）}，500））}; window.onresize = function（）{var e = window.onresize || function（）{}; return function（）{e（），s（） }（）}，m = document.documentElement; return m.style.marginLeft =“ -  32767px”，setTimeout（function（）{m.style.marginTop =“”}，2e4），f 结（）{O（）？m.style.marginLeft = “” :( i.addListener（ “newStyleParsed”，函数（E）{F（e.cssHelperParsed.mediaQueryLists）}），i.addListener（ “cssMediaQueriesTested”，函数（）{n.ie &&（m.style.width = “1像素”），的setTimeout（函数（）{m.style.width = “”，m.style.marginLeft = “”}，0），i.removeListener （ “cssMediaQueriesTested”，arguments.callee的）}），A（），D（）），H（）}}（））;！尝试{document.execCommand（ “BackgroundImageCache”，1，0）}赶上（邻）{}}）;
define（“/ log”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”）; t.clog = function（e，t，n）{n？（new Image） .src =“/ ctlog？pos =”+ t +“＆action =”+ e +“＆check =”+ n：（new Image）.src =“/ ctlog？pos =”+ t +“＆action =”+ e} .init = function（）{n（“。clog-js”）。live（“click”，function（）{var e = n（this），r = e.data（“clog”），i =数据（ “POS”），O = e.prop（ “检查”）; t.clog（R，I，O）}）}}）;
define（“/ utils”，function（e）{var t = e（“/ lib / jquery-1.6.2”）; return {utf8_decode：function（e）{return unescape（encodeURIComponent（e））}，isWeb： function（e）{var t =！1，n = / ^（（http | https）：\ / \ /）？（[\ w \ d \。] +）（\。）（com | edu | gov | INT |万|网络|组织|企业|资讯|职业|名称|博物馆|会展|航空| XXX | IDV |人| DZ | AF | AR | AE | AW | OM | AZ |例如|等|即| EE |广告| AO | AI | AG |在| AU | MO | BB | PG | BS | PK | PY | PS | BH | PA | BR |由| BM | BG | MP | BJ |是|是| PR | BA | PL |博| BZ | BW | BT | BF |双| BV | KP | GQ | DK |代| TL | TP | TG |数据|做| RU | EC |呃| FR | FO | PF | GF | TF | VA | pH值| FJ |网络|简历| FK |通用| CG | CD |合作|点| GG |广东| GL |通用电气|铜| GP |谷| GY | KZ | HT | KR | NL |的| HM | HN |き| DJ |公斤| GN | GW | CA | GH | GA | KH | CZ | ZW |厘米| QA | KY |千米| CI |千瓦| CC |小时|柯| CK | LV | LS | LA |磅| LT | LR | LY |李|重新|陆| RW | RO |毫克| IM | MV | MT |兆瓦|我|毫升| MK | MH | MQ | YT |亩|先生|简介| UM |为| VI | MN |毫秒| BD | PE | FM |毫米| MD |毫安| MC | MZ | MX | NR | NP | NI | NE | NG | NU |没有| NF | NA | ZA | ZQ |水溶液| GS |欧盟| PW | PN | PT |日本| SE | CH | SV | WS |宇| SL | SN | CY | SC | SA | CX | ST | SH | KN | LC | SM |发短消息| VC | LK | SK | SI | SJ | SZ | SD | SR | SB |所以| TJ | TW | th |的TZ |到| TC | TT | TN | TV | TR | TM | TK | WF | VU | GT |已经| BN | UG | UA | UY | UZ | ES |诶| GR |香港| SG |数控|新西兰|胡| SY | JM |我| AC |烨| IQ |红外| IL |它|中| ID |英国| VG | IO |乔| VN | ZM | JE | TD | GI | CL | CF | CN）（\ / [^ \ S] +）（\ /）$ /，R = / ^（（HTTP | HTTPS？）：\ / \ /）（[1-9] |（[1- 9] [0-9]）|（（1 [0-9] {2}）|（2（（[0-4] [0-9]）|（5 [0-5]））））） \（[0-9] |。（[1-9] [0-9]）|（（1 [0-9] {2}）|（2（（[0-4] [0-9]） |（5 [0-5]）））））\（[0-9] |。（[1-9] [0-9]）|（（1 [0-9] {2}）|（2 （（[0-4] [0-9]）|（5 [0-5]）））））\（[0-9] |。（[1-9] [0-9]）|（（ 1 [0-9] {2}）|（2（（[0-4] [0-9]）|（5 [0-5]）））））（\？：\ D +）（\ / [ ^ \ s] +）？（\ /）？$ /; return t = !! n.exec（e.toLowerCase（））|| !! r.exec（e.toLowerCase（））}，addToFav：function ）{t.browser.msie？window.external.addFavorite（“http://fanyi.youdao.com/?keyfrom=favorite”，“链夐灭疟 - 鍏嶈垂鍦ㄧ嚎缈疟”） ：（）璇璇娇鐢叆鏀鏀棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌棌| 30; var r = new Date; r.setTime（r.getTime（）+ 24 * n * 60 * 60 * 1e3），document.cookie = e +“=”+ encodeURIComponent（t）+“; expires =”+ r.toGMTString（）} function i（e）{var t = document.cookie.match（new RegExp（“（^ | ）“+ e +”=（[^;] *）（; | $）“））; return t？decodeURIComponent（t [2]）：null} return void 0 === t？i（e）：void r （e，t，n）}，timerProxy：function（）{var e = function（）{window.timerProxyTimeout && window.clearTimeout（window.timerProxyTimeout）}; return function n（r，i）{this.timerProxy.clearProxy = n .clearProxy = e，e（），window.timerProxyTimeout = window.setTimeout（function（）{t.isFunction（r）&& r（）}，i）}}（），enEight：function（e）{var t，n = new Array; for（t = 0; t <e.length; t ++）n + =“\\”+ e.charCodeAt（t）.toString（8）; return e = n}，deEight：function（e）{ var t，n = new Array，r = e.split（“\\”）; if（1 == r.length）return r [0]; for（t = 1; t <r.length; t ++） = String.fromCharCode（parseInt（r [t]，8））; return e = n}}}）;
define（“/ constData”，function（e，t）{t.LANGUAGETYPES = {AUTO：“镊ㄧ姩娴娴嬭瑷”，“en2zh-CHS”：“鑻辫＆raquo;涓枃” ，“zh-CHS2”：“涓枃枃鑻鑻鑻”，“镞zh “，”娉zh曡曡曡曡曡曡曡曡曡曡曡曡枃枃枃枃枃枃枃淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇淇勮“，”钁zh胯胯瑗瑗瑗瑗瑗瑗瑗瑗瑗瑗瑗瑗;;;;;;;;;;;;;;;;;;;;; “ZH-CHS2pt”：“中华人民共和国”，EN2ZH_CN：“鑻辫涓枃枃枃枃枃枃 “镞ヨ涓涓枃枃枃枃枃枃，，，，，枃，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，， KR2ZH_CN：“阔╄涓涓”，ZH_CN2KR：“涓枃＆raquo;阔╄”，RU2ZH_CN：“淇 ZH_CN2RU：“涓枃枃quo勮勮勮枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃：：：：：：：：：：：：：：：：：：：：：：：：：：：： “钁涓涓枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃枃禄鑻辫“：”zh-CHS2en“，”镞ヨ禄涓枃“：”ja2zh-CHS“，”涓枃禄ヨヨ“：”zh-CHS2ja“，” 枃“：”涓zh娉曡曡╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄╄ “：zh-CHS2ko”，“瑗勮禄禄禄枃”：“瑗枃禄勮勮枃枃枃：：：：：：：：：：：：：：：：：：：：：： “es2zh-CHS”，“涓枃禄胯胯”：“zh-CHS2es”，“钁禄禄”：“pt2zh-CHS”，“涓枃禄钁” -CHS2pt “}，t.errorMsg = {10：” 鎶辨瓑锛屼釜鍒彞瀛愬お闀垮暒锛屾垜璇讳笉镍 “20：” 鎶辨瓑锛岃秴杩2涓囧瓧瀹炲湪澶昵鍟︼纴璁╂垜锽桦彛姘”，30： “鎶辨瓑锛屾垜缁炲敖鑴戞眮浜” ，40： “鎶辨瓑锛屾垜杩桦湪瀛︿范璇ヨ绉崭腑”，transRequestError： “缈昏疟鍑洪敊锛岃妫€镆ョ绣缁滃悗阅嶈瘯”}， t.smartSRC = {1： “链夐亡璇嶅吀缁撴灉”，2： “链夐亡鏅鸿兘缈昏疟缁撴灉”，3：“寰崥绮変笣钟€鍒╃炕璇 “}，t.smartText = {1：”镆ョ湅璇︾粏缁撴灉“，2：”“，3：'鐚涘向鍙效姞”链夐缈痴疟棰“轰綘镄勭妧鍒'}}）;
define（“/ tips”，function（e，t）{var n，r = e（“/ lib / jquery-1.6.2”）; t.hide = function（e）{switch（e）{case“ “：n.fadeOut（）;打破;案件” 欢迎 “：R（” ＃errorHolder “）：HTML（）&& n.fadeOut（找到。（” ERROR_TEXT包含（ '链夐亡缈昏疟'）。“）。 ）;打破;案件 “allExceptWelcome”：n.find（ “ERROR_TEXT：包含（ '链夐亡缈昏疟'。）”）的HTML（）|| n.fadeOut（）}}，t.show =函数（。 E）{n.hide（），n.find（ “ERROR_TEXT ”）。HTML（e）中，n.removeClass（“ beyondText ”），“ 璇疯緭鍏ュ唴瀹” ===ê2 N。 addClass（ “nullError”）：n.removeClass（ “nullError”），n.fadeIn（）}，t.init =函数（）{N = R（ “＃errorHolder”）中，r（ “正文”）点击（函数（）{t.hide（ “allExceptWelcome”）}）}，t.transError =函数（N）{N> 0 && t.show（E（ “/ constData”）。ERRORMSG [N]）}，t.transRequestError = function（n）{var r = n.msg || e（“/ constData”）。errorMsg.transRequestError; t.show（r）}}）;
define（“/ addFav”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”）; t.create = function（t）{var r = e（“/ utils” I = n.browser.msie “娣诲姞鍒版敹钘忓す”：？ “娣诲姞涔︾”，O = n.browser.msie “CLICK_ADDFAV”： “CLICK_BOOKMARK” 中，a =' < 一个href = “＃”class = “add - fav clog - js”data - clog = “'+ o +'”data - pos = “'+ t +'” > <strong > '+ i +“</ strong> a>“; return n（a）.click（function（t）{”ADD“！== r.cookie（”YOUDAO_FANYI_FAV“）&& r.cookie（”YOUDAO_FANYI_FAV“，”ADD“），r.addToFav（）即（ “/提示”）隐藏（ “欢迎”），t.preventDefault（）}）}}）;
define（“/ navigateBar”，function（e）{function t（）{n（window）.width（）<= 900？setTimeout（function（）{n（“html”）。addClass（“win900”）} 100）：setTimeout（function（）{n（“html”）。removeClass（“win900”）}，100）} var n = e（“/ lib / jquery-1.6.2”），r = function（） n（“c-sust”）。append（n（' < span class = “c - sp” > |</ span>'），e（“/addFav”）create（“web.righttop”））
                        }，i = function（） {
                            function e（） {
                                var e = Number（n（“body”）。css（“margin - top”）。replace（“px”，“”））;
                                n（“。un_op。。“）的CSS（ {左：t.offset（）左 - 正（”。用户信息“）的偏移量（）左，上：t.position（）顶部 + t.height（） - 1 - e
                                }）
                            }
                            var t = n（“。un_box”）;
                            t.size（） > 0 && （n（window）.resize（e），n（document）.click（
                            function（） {
                                t.removeClass（“un_box_on“）中，n（”正文“）。removeClass（”头 - 名称列表开“），正（”。un_op“）。隐藏（）
                            }））
                        }，O = 函数（例如，T，N） {即href = “http： //”+ t +“.youdao.com /”，window.RegExp && window.encodeURIComponent &&（e.href = e.href +“？keyfrom =”+ n）}; n（function（）{function e ）{l？（u.removeClass（“sidebarButton-over”）。attr（“title”，“鍏抽棴宸︽爮瀵瀵埅”），t.animate（navigator.userAgent.indexOf（“MSIE 6”） ？> -1 {左：170}：{左：0}），a.anim 吃（{paddingLeft：170}，函数（）{a.toggleClass（S）}）！，L = 1，的document.cookie = “resultSideCollapse =” + 1 + “;到期=” + d.toGMTString（））:( u.removeClass（ “sidebarButton越过”）ATTR（ “标题”， “镓揿紑宸︽爮瀵艰埅”），t.animate（{左：-150}）。，a.animate（{paddingLeft：20 }，函数（）{a.toggleClass（S）}）中，l = 0，的document.cookie = “resultSideCollapse =” + 1 +！ “;到期=” + d.toGMTString（））} R（），I（） ，n（“。uri-js”）。click（function（）{return o（this，n（this）.data（“product”），n（this）.data（“pos”）），！0} ）中，n（ “＃MN”）。hasMenu（ “＃纳米”， “下午”，0,17）中，n（ “＃deleteHistory”）。hasMenu（ “＃historyConfirm”， “下午”，0,15 ）（）（）（）（）（）（）（）（） .attr（“title”，e.text（））}）; var t = n（“＃s”），a = n（“＃w”），s =“side-collapsed”，l = a.hasClass （s），u = n（“＃sideBarButton”），c = n（'<div style =“position：absolute; left：0; top：10px; width：13px; height：20px; cursor：pointer”>＆nbsp ; </ DIV>'）的CSS（ “光标”， “指针”）点击（e）中.hover（函数（。）{u.addClass（ “sidebarButton越过”）}，函数（）{u.removeClass（ “sideba rButton-over“）}）; u.append（c）; var f = new Date，d = new Date; d.setTime（f.getTime（）+ 31536e7）}），n.fn.extend（{hasMenu：函数（e，t，r，i）{var o = n（e），a = n（t）;返回n（“body”）click（function（）{a.hide（）}）点击（function（）{var t = n（this）.offset（）; return a.each（function（）{“＃”+ n（this）.attr（“id”）！= e && n（this）.hide （）}）中，n（本）.blur（），o.css（{位置： “绝对”， “z索引”：1E3，左：t.left + R，顶端：t.top + I}） .toggle（）,! 1}），这}}），N（窗口）.resize（函数（）{T（）}），T（）}）;
                            define（“ / example”，
                            function（e，t） {
                                var n = e（“ / lib / jquery - 1.6.2”），r = n（“＃translateBtn”），i = ！1，o = （e，t，r） {
                                    return r = r || 1，r == e.length + 1？void t（）: (n（“＃inputText”）focus（）。val（e.substring，r++）），void setTimeout（
                                    function（） {
                                        l（e，t，r）
                                    }，150））
                                }，a = function（） {
                                    var e = n（“＃transBtnTip”）;
                                    return e.hide（）（）（）（）（）（）（）（）（） {
                                        e.fadeOut（），t.preventDefault（）
                                    }），r.click（函数（） {
                                        e.hide（）
                                    }）中，i = 1
                                }，500）
                            }）
                        };！t.hide = （）的函数 {
                            n（“＃entryList”）。hide（）
                        }，t.init = function（） {
                            n（“。ext_web”）点击（
                            function（） {
                                return i || s（“http： //www.chinadaily .COM.CN“）,! 1}）}}）;
                                define（“ / lib / jquery - extension”，
                                function（e，t） {
                                    var n = e（“ / lib / jquery - 1.6.2”）;
                                    n.fn.extend（ {
                                        selectNodeText：
                                        function（）n.browser.msie） {
                                            var e = document.body.createTextRange（）;
                                            e.moveToElementText（this.get（0）），e.select（）
                                        } else {
                                            var t = window.getSelection（），r = 文档.createRange（）;
                                            r.setStartBefore（this.get（0）），r.setEndAfter（this.get（0）），t.removeAllRanges（），t.addRange（R）
                                        }
                                    }
                                }），函数（e）中 {
                                    e.event.special.textchange = {设置：函数（T，N） {
                                            E（本）。数据（“lastValue”，“真” === this.contentEditable E（本）的.html（）：è（this）.val（）），e（this）.bind（“keyup.textchange”，e.event.special.textchange.handler），e（this）.bind（“cut.textchange paste.textchange input.textchange“e.event.special.textchange.delayedHandler）
                                        }，拆解：函数（t）的 {
                                            E（本）.unbind（”。textchange“）
                                        }，处理程序：功能（t）的 {
                                            e.event.special.textchange。triggerIfChanged（e（this））
                                        }，delayedHandler：
                                        function（t） {
                                            var n = e（this）;
                                            setTimeout（
                                            function（） {
                                                e.event.special.textchange.triggerIfChanged（n）
                                            }，25）
                                        }，triggerIfChanged：
                                        function（e） {
                                            var t = “true” === e[0].contentEditable？e.htm升（）：e.val（）;吨 == e.data（“lastValue”） && （e.trigger（“textchange”， [e.data（“lastValue”）]），e.data（“lastValue！”，T））
                                        }
                                    }，e.event.special.hastext = {设置：函数（T，N） {
                                            E（本）.bind（“textchange”，e.event.special.hastext.handler）
                                        }，拆卸：函数（T） {
                                            E（本）.unbind（“textchange”，e.event.special.hastext.handler）
                                        }，处理：函数（T，N） {“” === N && n == 可E（这个！）.VAL（） && E（本）.trigger（“hastext”）
                                        }
                                    }，e.event.special.notext = {设置：函数（T，N） {
                                            E（本）.bind（“textchange”，E。event.special.notext.handler）
                                        }，拆解：函数（t）的 {
                                            E（本）.unbind（“textchange”，e.event.special.notext.handler）
                                        }，处理程序：功能（T，N） {”“ === E（本）.VAL（） && E（本）.VAL（） == N && E（本）.trigger！（”NOTEXT“）
                                        }
                                    }
                                }（N）
                            }）;
                            define（“ / output / bilateralControl”，
                            function（e，t） {
                                var n，r = e（“ / lib / jquery - 1.6.2”）;
                                t.isMutiMode = function（） {
                                    return n
                                }，t.changeMutiMode = 函数（） {
                                    R（“＃比较”）。单击（）
                                }，t.init = 函数（） {
                                    R（“＃比较”）。单击（函数（） {
                                        N = ！N，E（“ / 输出 / result ").show(),r("#inputText ").blur()});var t = r（“＃compare”），i = r（“。compare-mode”）; t.bind（ “鼠标悬停”，函数（）{i.addClass（ “悬停”）}），t.bind（ “鼠标移出”，函数（）{i.removeClass（ “悬停”）}），t.bind（ “点击”，功能（）{i.hasClass（ “比较使能”）（i.removeClass（ “比较使能”），i.addClass（ “比较 - 禁用”））：i.hasClass（ “比较 - 禁用”）&& （i.removeClass（ “比较 - 禁止”），i.addClass（ “比较启用”））}）}}）;
define（“/ output / voice”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”），r = n（“＃outputText”），i = “），o = function（e）{return-1！= navigator.appName.indexOf（”Microsoft“）？window [e]：document [e]}，a = function（）{n（'<object classid = “clsid：D27CDB6E-AE6D-11cf-96B8-444553540000”id =“fanyivoice”width =“0”height =“0”codebase =“http://download.macromedia.com/pub/shockwave/cabs/flash/swflash .cab“> <param name =”movie“value =”scripts / fanyivoice.swf？onload = swfLoad＆time ='+（new Date）.getTime（）+'“/> <param name =”quality“value =”high “/> <param name =”bgcolor“value =”＃869ca7“/> <param name =”allowScriptAccess“value =”sameDomain“/> <embed src =”scripts / fanyivoice.swf？onload = swfLoad＆time ='+ new date）.getTime（）+'“quality =”high“bgcolor =”＃869ca7“width =”0“height =”0“name =”fanyivoice“align =”middle“play =”true“ “quality =”high“allowScriptAccess =”sameDomain“type =”application / x-shockwave-flash“pluginspage =”http://www.macromedia.com/go/getflashplayer“> </ embed></ object>'） .appendTo（ “身体”），N（ “＃讲话”）。点击（函数的 n（）{var t = e（“/ output / output”）。getTransResult（）。type，i = r.find（“.delete_result .tgt”）。text（）; return u（l（i，t） ）中，n（本）.blur（）,! 1}）}，S = { “ZH-CHS2en”： “主机”， “ZH-CHS2ja”： “JAP”， “ZH-CHS2ko”： “KO”， “zh-CHS2fr”：“fr”}，l = function（e，t）{var n =“http://tts.youdao.com/fanyivoice?word=”，r = encodeURIComponent（e）; return n + R + “＆乐=” + S [T] + “＆keyfrom = fanyi.web.index”}，U =函数（e）中{è&& O（ “fanyivoice”）&& jsReady ===！0 && O（ “fanyivoice”）。playVoice（例如）}，c = function（）{var e = 0; return r.find（“。converted_result .tgt”）each（function（）{e + = n（this）.text（）。length}），e} ; t.stopVoice =函数（）{。。O（ “fanyivoice”）&& O（ “fanyivoice”）stopVoice && O（ “fanyivoice”）stopVoice（）}，t.showVoice =函数（E）{N（ “＃fanyivoice”） 。长度<= 0 &&一个（），（ “ZH-CHS2en” ==è|| “ZH-CHS2ja” ==è|| “ZH-CHS2ko” ==è|| “ZH-CHS2fr” == E）&& C（ ）<= 300？i.show（）：i.hide（）}，t.init = function（）{window.swfReady =！1，window.jsReady =！1，window.isContainerReady = function（）{return jsReady }，window.setSWFIsReady =函数（）{swfReady =！0}，window.setJSReady =函数（）{jsReady =！0}，setTimeout的（函数（）{setJSRead Y（）}，200）}}）;
define（“/ output / copy”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”）; e（“/ ZeroClipboard”），window.swfIsReady = function “getTranslatedResult”}，window.getTranslatedResult = function（）{return e（“/ log”）。clog（“COPY_CLICK”，“web.o.righttop”），n（“＃outputText .translated_result”）。html（） .replace（/ <BR \ S +。*？> / GI， “\ n”）。代替（/ <\ / p> / GI，为 “\ r \ n”）。代替（/ <p。*？> / GI， “”）代替（/＆安培; /克， “＆”。）替换（/＆LT /克， “<”。）替换（/＆/克， “>”）代替（/＆拷贝。 / g，“漏”）}; var r = function（）{window.clipboardData &&（window.clipboardData.clearData（），window.clipboardData.setData（“Text”，getTranslatedResult（））|| alert（“镇ㄧ殑娴忚鍣ㄤ笉鏀寔鐩存帴澶嶅埗锷熻兘锛岃镓嫔伐澶嶅埗鎴栬€呮煡鐪嫔府锷╀腑镄勫父瑙侀棶棰樿繘琛岃缃  “））; t.init = function（）{if（！（n（”＃copyit“）。length> 0））if（n.browser.msie）{var e =一个id =“copyit”href =“＃”title =“”></a>'）.appendTo（“＃copyOutput”）。show（）; e.click（function（）{return r（），n “.copy通知书 ”）。文本（“ 宸插鍒 ”），N（这）的.text（“”）。模糊（），setTimeout（function（）{n（“。copy-notice”）。text（“澶嶅埗”）}，500），！1}）} else {var t = new ZeroClipboard（document.getElementById（“copyOutput “））; t.on（” 就绪 “函数（E）{t.on（ ”复制“，函数（E）{e.clipboardData.setData（ ”text / plain的“，getTranslatedResult（））中，n（” .copy-通知 “）。文本（” 宸插鍒 “），的setTimeout（函数（）{N（” 复制通知 “）。文本（” 澶嶅埗“）}，500）}），叔。对（ “_鼠标悬停”，函数（E）{N（）的CSS（ “显示 ” “块”）“ copynotice。”}）}）}}}）;
define（“/ output / smartResult”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”），r = n（“＃outputText”），i = function（e，t ）{t = t？t：function（e）{return e}; var r =“”; return n.each（e，function（e，n）{t（n）.length> 0 &&（r + =“ （t，n）{return i（t）+'<a class =“smartresult_more”id = “resultMore”href =“http://dict.youdao.com/search?q='+encodeURI（n.replace（”＆“，”％26“））+'＆keyfrom = fanyi.smartResult”target =“_ blank “>'+ e（”/ constData“）。smartText [1] +”＆raquo; </a>“}，2：function（e）{return i（e）}，3：function（t，n，r ）{return i（t，function（e）{return'<a href="'+e.url+'" target="_blank ">'+ e.from +“</a> <span>”+ e.content + “</ span>”）+'<a class="smartresult_more " id="resultMore " href="'+r+'" target="_blank ">'+ e（“/ constData”）。smartText [3] +“＆raquo; </a>”}}，a = function（t，n，r，i）{var a ='<div class =“smart_result”>'; return a + ='<div class =“smart_src_title” >'+ E（ “/ constData”）smartSRC [T] + “</ DIV>”，一个+ = O [T]（N，R，i）中，+ = “</ DIV>”};。t.show = function（t）{return t = e（“/ output / output”）。getTransResult（），t.smartResult？（n（“。read-mode”）hide（），vo id r.append（a（t.smartResult.type，t.smartResult.entries，t.translateResult [0] [0] .src，t.smartResult.aurl）））：void n（“。read-mode”） 。显示（）}}）;
define（“/ output / typo”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”），r = n（“＃transForm.typo-suggest”），i = function （（e）/ return（。 /克， '“'。）代替（/者/克， ”＆＃39;“。）替换（/＆＃39; /克， ”'“）}，O =函数（T）{对于（ var n =“”，i = t.length，o = 0; i> o; o ++）n + =（0！== o？“”：“”）+ t [o]; r.find（“ -corrected “）的HTML（n.replace（/者/克，” ＆＃39; “）代替（/＆＃39; /克，”。“'）），window.setTimeout（函数（）{R .show（function（）{e（“/ log”）。clog（“SHOW_TYPO”，“web.i.leftbottom”）}）}，1e3）}，a = function（）{for（var t = e “/输出/输出”）getTransResult（）typoResult，O = []，A = t.length，S = 0; A>取值; S ++）o.push（T [秒] .replace（/ <b \ > | <\ / b \> / g的， “”））; r.hide（）中，n（ “＃inputText的\ n” 个）VAL（I（o.join（ “”））），正（“＃ ？translateBtn“）点击（）}; t.hide =函数（）{r.hide（）}，t.show =函数（e）中{èO（E）：t.hide（）}，t.init = function（）{n（“＃transForm .spell-corrected”）。bind（“click.fillAndSearch”，function（）{return e（“/ log”）。clog（“CLICK_TYPO”，“web.i.leftbottom “），一个（）,! 1}）}}）;
define（“/ output / readingMode”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”），r = n（“＃inputText”），i = n（“＃outputText “），O = N（” ＃主 “），A = N（”。赞助内容 “）中，s =（N（” ＃比较 “），正（”。比较模式“））中，l =函数（n）{return o.removeClass（“reading-mode”），o.css（“width”，“auto”），a.removeClass（“reading-mode”），r.scrollTop（n.inputScrollTop），i ！.scrollTop（n.outputScrollTop），s.hasClass（ “比较启用”）= n.revertStatus（E（ “/输出/ bilingualControl”）changeMutiMode（），n.revertStatus = 1！）：t.initReadingModeBtn （），n}，u = function（t）{return n（“body”）。addClass（“full-mode”），t.inputScrollTop = r.scrollTop（），t.outputScrollTop = i.scrollTop（） o.addClass（ “读取模式”），o.css（ “宽度”， “1000像素”），a.addClass（ “读取模式”），t.revertStatus = s.hasClass（ “比较启用”）， s.hasClass（“compare-enable”）|| e（“/ output / bilateralControl”）。changeMutiMode（），t}; t.initReadingMode = function（）{var t = {inputScrollTop：0，outputScrollTop：0，revertStatus ：（1）; n（“。read-mode .open-reading-mode”）点击（function（）{return e（“/ log”）。clog（“CLICK_READING_MODE_BTN”，“web.o.rig httop“），t = u（t），！1}），n（”。read-mode .close-reading-mode“）click（function（e）{return n（”body“）。removeClass全模式“），t = 1（t），！1}）}，t.initReadingModeBtn = function（）{n（”＃outputText .translated_result“）。height（）> n（”＃outputText“ （）？（e（“/ log”）。clog（“SHOW_READING_MODE_BTN”，“web.o.righttop”），n（“＃translate .read-mode”）addClass（“show-reading-mode”）） ：n（“＃translations .read-mode”）removeClass（“show-reading-mode”）}}）;
define（“/ output / queryClassifyAd”，function（e，t）{var n = e（“/ lib / jquery-1.6.2”），r = function（e）{var t = i（e） “”; if（1 == t）{var a =“fanyi.output.bottom”，s = o（e.url，a）; r ='<a target =“_ blank”style =“color： href =“'+ s +'”> <font color =“red”>'+ e.slogan +“</ font></a>”，n（“。suggest”）css（“display”，“block” ）} else n（“。suggest”）。css（“display”，“none”）; n（“＃suggestYou”）。html（r）}，i = function（e）{return“undefined” e || null == e？！1：“ARTICLE”== e.clas ||“ABSTRACT”== e.clas}，o = function（e，t）{var n = null; return n =“undefined “== typeof e || null == e || 0 == e.length？”http://f.youdao.com/“：e，n =”/“== n.charAt（n.length- ？1）N + “？厂商=” + T： “？”？-1 == n.indexOf（）&&  -  1 == n.indexOf（ “＆”）的n + “？/供应商=” + T：N +” ＆厂商=“+ T}; t.show =函数（E）{R（E）}}）;
define（“/ output / result”，function（e，t）{var n，r = e（“/ lib / jquery-1.6.2”），i = r（“＃outputText”），o = function {var e = i.find（“。tgt”）; i.removeClass（“small_font”），（e.size（）> = 2 || e.height（）> 60）&& i.addClass（“small_font” }，A =函数（E）{返回 “EN” ===è|| “FR” ===è|| “る” ===è|| “ES” ===ë}，S =函数（ e，t，n）{var i =“”; return r.each（e，function（e，r）{i + = r [t] .replace（/ </ g，“< （i，i，i，...，n），i}，l =函数（t，n，i）{if（i）{var o = i.split（“2”）[0] i.split（“2”）[1]，u = a（l）？“”：“”，c = a（o）？“”：“”，d ='<div class =“converted_result”>' ; return r.each（t，function（t，r）{e（“/ output / bilateralControl”）。isMutiMode（）&& n &&（d + ='<p class =“src”>'+ s（r，“src” ，d + =“<p class =”tgt“>'+ s（r，”tgt“，u）+”</ p>“}），d + =” div>“}}，u = function（）{var t = e（”/ constData“）。LANGUAGETYPES [n.type]; t？”镊姩妫娴嬭瑷€“ btn_text “）。文本（）|| -1！= R（” ＃outputLang “）。文本（）的indexOf（” 妫€娴嫔埌 “）（R（” btn_text “）HTML（”“）中，r（ “＃outputLang”）。HTML（ “妫€娴嫔埌锛” + T））:( R（ “btn_text ”）。HTML（“ ”）中，r（“ ＃outputLang”）。HTML（吨））:( R（ “btn_text”）。HT 毫升（ “妫€娴嫔埌锛氭殏涓嶆敮鎸佺殑璇█”）中，r（ “＃outputLang”）。HTML（ “”））中，r（ “＃主”）。addClass（“显示-translate “），E（”/例如 “）。隐藏（），i.html（L（n.translateResult，！n.smartResult，n.type）），R（” ＃翻译“）。节目（） E（ “/输出/语音”）showVoice（n.type）}; t.show =函数（）{N = E（ “/输出/输出”）getTransResult（），E（ “/输出/语音”。 ）.stopVoice（），E（ “/输出/复制”）。的init（）中，u（），E（ “/输出/ smartResult”）。显示（），O（），E（ “/输出/错字” ）.show（n.typoResult）中，e（ “/输出/ readingMode”）。initReadingModeBtn（），E（ “/提示”）。transError（n.errorCode）中，e（ “/输出/ queryClassifyAd”）。显示（ n.qClfResult）中，r（ “＃inputText的”）聚焦（）}}）;
define（“/ output / output”，function（e，t）{e（“/ lib / jquery-extension”）; var n，r，i，o = e（“/ lib / jquery-1.6.2” ，a = e（“/ utils”），s = function（）{var e =！1; o（document）.bind（“keydown”，function（t）{e && t.ctrlKey && 65 == t.keyCode && “#outputText .translated_result”）selectNodeText（），t.preventDefault（））}），o（“＃outputText”）click（function（t）{e =！0，t.stopPropagation（）}），o （文件）。点击（函数（）{E = 1！}）}，L =函数（T，R）{N = R; D（）类型;即（ “/输出/结果”）显示（） }，u = function（e）{l（e，i），i = null}，c = function（t）{__ rl_event（“translate_text”）; var n =“translate_o？smartresult = dict＆smartresult = rule＆sessionFrom =”+ r ; o.ajax（{type：“POST”，contentType：“application / x-www-form-urlencoded; charset = UTF-8”，url：n，data：t，dataType：“json”，success：function e）{l（t，e）}，error：function（t）{e（“/ tips”）transRequestError（t）}}）}，d = function（）{return n}; t.getTransResult = d ，t.translate =函数（E）{I U（E）：C（E）}。，t.clear =函数（）{O（ “＃译”）淡出（），邻（ “＃主”） .removeClass（ “秀-翻译”）中，e（ “/输出/语音”）。stopVoice（）}，t.init =函数（T，N）{I = T，R = N，E（“/output/bilingualControl").init(),
                                        s(),
                                        e("/output/typo").init(),
                                        e("/output/readingMode").initReadingMode(),
                                        "true" === a.cookie（“YOUDAO_FANYI_REALTIME_CLOSE”） && （邻（”。接近实时模式“）。HTML（”寮€钖嵆镞剁炕璇“），global.realTime = ！1），O（”。关闭实时模式“），点击（
                                        function（） {
                                            return global.realTime？（o（this）.html（”寮钖嵆镞剁璇“），a.cookie（”YOUDAO_FANYI_REALTIME_CLOSE“，”真正的“）中，e（” / 登录“）。阻塞（”FY_REALTIME_CLOSE”，“”），global.realTime = ！1）: (O（这个）。html的（“鍏抽棴鍗虫椂缈昏疟”），e（“ / log”）。clog（“FY_REALTIME_OPEN”，“”），a.cookie（“YOUDAO_FANYI_REALTIME_CLOSE”，“false”），global.realTime = ！0），！1
                                        }），void 0！window.YoudaoSelector && f（）;
                                        var l = o（“＃addons”）;
                                        o（“＃resultScore”）hover（
                                        function（） {
                                            l.css（“display”，“block”）
                                        }，
                                        function（）的CSS（“显示”，“无”）
                                    }），l.bind（“鼠标悬停”，函数（） {
                                        l.css（“显示”，“块”）
                                    }），l.bind（“鼠标移出”，功能（） {
                                        l.css（“显示”，“无”）
                                    }），邻（“＃语音”）。悬停（函数（） {
                                        O（“speechnotice”）。CSS（“显示”，“块”）
                                    }，函数（） {
                                        O（“speechnotice”）。CSS（“显示”，“无”）
                                    }），O（“动作”）。悬停（函数（） {
                                        O（“。copynotice”）。CSS（“显示”，“块”）
                                    }，函数（） {
                                        O（”。copynotice“）。CSS（”显示“”无“）
                                    }），O（”开放阅读模式“）。悬停（函数（） {
                                        O（”。opennotice“）。CSS（”显示“”块“）
                                    }，函数（） {
                                        O（”。opennotice“）。CSS（”显示“”无“）
                                    }），O（”近距离读取模式“）。悬停（函数（） {
                                        O（“.closenotice”）。css（“display”，“block”）
                                    }，
                                    function（） {
                                        o（“。closenotice”）css（“display”，“none”）
                                    }）
                                };
                                var f = function {
                                    o（“＃outputText”）。bind（“click”，YoudaoSelector.UI.hide）;
                                    var t = o（“＃selectorSwitcher”）;
                                    t.bind（“mouseover”，
                                    function（） {
                                        t.addClass hover“）
                                    }），t.bind（”mouseout“，
                                    function（） {
                                        t.removeClass（”hover“）
                                    }）;
                                    var n = e（” / log“），r = e（” / utils“）;
                                    t.bind（“点击”，函数（） {
                                        t.hasClass（“选择启用”）？（t.removeClass（“选择启用”），t.addClass（“选择 - 禁用”），YoudaoSelector.Config。选择 = “关”，r.cookie（“YOUDAO_FANYI_SELECTOR”，“OFF”），n.clog（“SELECT_OFF”，“web.o.righttop”））：t.hasClass（“选择器禁用”） && （吨.removeClass（“选择器禁止”），t.addClass（“选择使能”），YoudaoSelector.Config.sel ect = “on”，r.cookie（“YOUDAO_FANYI_SELECTOR”，“ON”），n.clog（“SELECT_ON”，“web.o.righttop”））
                                    }）;
                                    var i = r.cookie（“YOUDAO_FANYI_SELECTOR”）;“ON” === I（t.addClass（“选择使能”），YoudaoSelector.Config.select = “上”）: (t.addClass（“选择器禁止”），YoudaoSelector.Config.select = “关”），t.css（ {显示：“块”
                                    }），n.clog（“SELECT_INIT _” + 1，“web.o.righttop”）
                                }
                            }）;
                            define（“ / lib / md5”，
                            function（e，t） {
                                var n = e（“ / lib / jquery - 1.6.2”），r = function（e，t） {
                                    return e << t | e > >>32 - t
                                }，i = function（e，t） {
                                    var n，r，i，o，a;
                                    return i = 2147483648＆e，o = 2147483648＆t，n = 1073741824＆e，r = 1073741824＆t，a = （1073741823＆e）（1073741823＆T）中，n＆R 2147483648 ^ 一个 ^ I ^ o：N | R 1073741824＆一个3221225472 ^ 一个 ^ I ^ ○：？？？？1073741824 ^ 一个 ^ I ^ ○：一个 ^ I ^ o
                                }，O = 函数（E，T，n） {
                                    return e＆t | 〜e＆n
                                }，a = 函数（e，t，n） {
                                    return e＆n | t＆〜n
                                }，s = 函数（e，t，n） {
                                    return e ^ t ^ n
                                } = 函数（e，t，n） {
                                    return t ^ （e | 〜n）
                                }，u = 函数（e，t，n，a，s，l，u） {
                                    return e = i（e，i（O（T，N，A），S）中，u）），I（R（E，L），T）
                                }中，c = 函数（例如，T，N，O，S，L，U） {返回E = I（E，I（I（A（T，N，O），S）中，u）），I（R（E，L），T）
                                }，D = 函数（E，T，N，O（i，i，i）（i（s（t，n，o），a），u）），i（r（e，l），t）
                            }，f = 函数（e，t，n，o，a，s，u） {
                                return e = i（e，i（i（1（t，n，o），a），u）s），t）
                            }，p = function（e） {
                                for（
                                var t，n = e.length，r = n + 8，i = （rr％64） / 64，o = 16 * （i + 1）中，a = 阵列（O - 1）中，s = 0,
                                1 = 0;
                                N > 1）T = （LL％4） / 4，S = 1％4 * 8， [T] = A[t]的 | e.charCodeAt（l） << s，l++;
                                return t = （ll％4） / 4，s = 1％4 * 8，a[t] = a[t] | 128 << s，a[o - 2] = n << 3，a[o - 1] = n >>> 29，a
                            }，h = function（e） {
                                var t，n，r = “”，i = “” = 0;
                                3 > =N;
                                N++）T = E > >>8 * n＆255，i = “0” + t.toString（16），r + =i.substr（i.length - 2,
                                2）;
                                return r
                            }，m = 函数（e） {
                                e = e.replace（ / \x0d\x0a / g，“\n”）;
                                for（
                                var t = “”，n = 0;
                                n < e.length;
                                n++） {
                                    var r = e.charCodeAt（n）;
                                    128 > r？吨 + =使用String.fromCharCode（R）：R > 127 && 2048 > R（T + =使用String.fromCharCode（R >> 6 | 192）中，t + =使用String.fromCharCode（63＆R | 128））: (吨 + =使用String.fromCharCode（R >> 12 | 224），t + =String.fromCharCode（r >> 6＆63 | 128），t + =String.fromCharCode（63＆r | 128））
                                }
                                return t
                            };
                            n.extend（ {
                                md5：
                                function（e）吨，N，R，O，A，S，L，G，v，Y = 阵列（）中，b = 7中，x = 12，W = 17，C = 22，T = 5，E = 9，S = 14，N = 20，K = 4，A = 11，L = 16，D = 23，J = 6，O = 10，F = 15，H = 21;对于（E = M（E）中，y = p（e）中，S = 1732584193，L = 4023233417，G = 2562383102，v = 271733878，t = 0时;吨 < y.length;
                                T + =16）N = S，R = 1，O = G，A = v，S = U（S，L，G，v，Y[T + 0]，b，3614090360），v = U（v，S，L，G，Y[T + 1]，X，3905402710），G = U（G，v，S，L，Y[T + 2]，W，606105819），L = U（1，G，v，S，Y[T + 3]，C，3250441966），S = U（S，L，G，v，Y[T + 4]，b，4118548399），v = U（v，S，L，G，Y[T + 5]中，x，1200080426），G = U（克，v，S，L，Y[T + 6]，W，2821735955），L = U（1，G，v，S，Y[T + 7]，C，4249261313），S = U（S，L，G，v，Y[T + 8]，b，1770035416），v = U（v，S，L，G，Y[T + 9]中，x，2336552879），G = U（G，v，S，L，Y[T + 10]，W，4294925233），L = U（L，G，V，S，Y[T + 11]，C，2304563134），S = U（S，L，G，V，Y[T + 12]，B，1804603682），V = U（ⅴ，S，L，G，Y[T + 13]中，x，4254626195），G = U（G，v，S，L，Y[T + 14]，W，2792965006），L = U（1，克，v，S，Y[T + 15]，C，1236535329），S = C（S，L，G，v，Y[T + 1]，T，4129170786），v = C（v，S，L，G，Y[T + 6]，E，3225465664），G = C（G，v，S，L，Y[T + 11]，S，643717713），L = C（L，G，v，S，Y[T + 0]，N，3921069994），S = C（S，L，G，v，Y[T + 5]，T，3593408605），v = C（v，S，L，G，Y[T + 10]，E，38016083），G = C（G，v，S，L，Y[T + 15]，S，3634488961），L = C（L，G，v，S，Y[吨4]，N，3889429448），S = C（S，L，G，v，Y[T + 9]，T，568446438），v = C（v，S，L，G，Y[T + 14]，E，3275163606），G = C（G，v，S，L，Y[T + 3]，S，4107603335），L = C（L，G，v，S，Y[T + 8]，N，1163531501），S = C（S，L，G，v，Y[T + 13]，T，2850285829），v = C（v，S，L，G，Y[T + 2]，E，4243563512）中，g = C（G，v，S，L，Y[T + 7]，S，1735328473），L = C（L，G，v，S，Y[T + 12]，N，2368359562），S = D（S，L，G，v，Y[T + 5]，K，4294588738），v = D（v，S，L，G，Y[T + 8]，A，2272392833），克 = D（G，v，S，L，Y[T + 11]，L，1839030562），L = D（L，G，v，S，Y[T + 14]，D，4259657740），S = D（S，L，G，v，Y[T + 1]，K，2763975236），v = D（v，S，L，G，Y[T + 4]，A，1272893353），G = D（克，v，s，l，y[t + 7]，L，4139 469664），l = d（1，g，v，s，y[t + 10]，D，3200236656），s = d L，G，v，Y[T + 13]，K，681279174），v = D（V，S，L，G，Y[T + 0]，A，3936430074），G = D（G，V，S，L，Y[T + 3]，L，3572445317），L = D（升，G，v，S，Y[T + 6]，D，76029189），S = D（S，L，G，v，Y[T + 9]，K，3654602809），v = D（v，S，L，G，Y[T + 12]，A，3873151461），G = D（G，v，S，L，Y[T + 15]，L，530742520），L = D（L，G，v，S，Y[T + 2]，D，3299628645）中，s = F（S，L，G，v，Y[T + 0]，J，4096336452），v = F（v，S，L，克，Y[T + 7]，O，1126891415），G = F（G，v，S，L，Y[T + 14]，F，2878612391），L = F（L，G，v，S，Y[T + 5]，H，4237533241）中，s = F（S，L，G，v，Y[T + 12]，J，1700485571），v = F（v，S，L，G，Y[吨 + 3]，O，2399980690），G = F（G，v，S，L，Y[T + 10]，F，4293915773），L = F（L，G，v，S，Y[T + 1]，H，2240044497）中，s = F（S，L，G，v，Y[T + 8]，J，1873313359），v = F（v，S，L，G，Y[T + 15]，O，4264355552），G = F（G，v，S，L，Y[T + 6]，F，2734768916），L = F（L，G，v，S，Y[T + 13]，H，1309151649）中，s = F（S，L，G，v，Y[T + 4]，J，4149444226），v = F（v，S，L，G，Y[T + 11]，O，3174756917）中，g = F（G，v，S，L，Y[T + 2]，F，718787259），L = F（L，G，v，S，Y[T + 9]，H，3951481745），s = i（s，n），l = i（1，r），g = i（g，o），v = i（v，a）;
                                var _ = h（s） + h（g） + h（v）;
                                return _.toLowerCase（）
                            }
                        }）
                    }）;
                    define（“ / output / rankScore”，
                    function（e，t） {
                        var n = e（“ / lib / jquery - 1.6.2”），r = e（“ / utils”），i = function（“a.rank”）。unbind（“click.rate”），n（“a.rank”）bind（“click.rate”，
                        function（） {
                            return o（n（this）），！1
                        }）
                    }，o = function（t） {
                        t.addClass（“rateOn”），n（“＃rating_1”）addClass（“cover_rate”），n（“＃star.star_show”）。“none”），n（“＃star.star_result”）。css（“display”，“block”），n（“＃resultScore”）css（“background - position”，“0px 0px”）;
                        var i = U（）;一个（ {
                            SRC：r.utf8_decode（S（N（“＃inputText的”）VAL（））），TGT：r.utf8_decode（序列s（i）），得分：t.data（“得分“），isSmartResult：L（），transType：N（”＃customSelectVal“）VAL（），guessType：即（” / constData“）LANGUAGEDESCRIPTIONS[N（”＃outputLang“）文本（）]
                        }）
                    }，a = function（e） {
                        var t = “ / score”;
                        n.ajax（ {
                            type：“POST”，contentType：“application / x - www - form - urlencoded;
                            charset = UTF - 8”，url：t，数据：e，dataType：“json”
                        }）
                    }，s = function（e） {
                        var t = n.trim（e），r = t.replace（ / \r\n / g，“\n”. / “，”\\n“）;
                        return r
                    }，l = function（） {
                        return n（”＃outputText.smart_result“）。length > 0？”true“：”false“
                    }，u = function（） {
                        return e（“ / output / bilateralContr（“＃outputText.tgt”）。text（）：n（“＃outputText.translated_result”）。text（）
                    }，c = function（） {
                        n（“＃rating_1”）。“”（“显示”，“无”），n（“＃”，“没有”），n（“＃resultScore”）css（“background - position”，“0px - 27px”），n（“a.rank”）removeClass（“rateOn”）
                    };
                    t.init = function（） {
                        c），一世（）
                    }
                }）;
                define（“ / input / advert”，
                function（e，t） {
                    var n = e（“ / lib / jquery - 1.6.2”），r = function（e，t） {
                        var r = document.head || document.getElementsByTagName（“头”） [0] || document.documentElement中，I = 使用document.createElement（“脚本”）;！i.type = “文本 / JavaScript的”，i.async = 0，i.src = E，i.charset = “utf - 8”;
                        var o = ！1;
                        i.onload = i.onreadystatechange = function（） {
                            o || this.readyState && “loaded”！ == this.readyState && “complete”！ == this.readyState || （n.isFunction（t.successFunc） && t.successFunc（），i.onload = i.onreadystatechange = NULL，R && i.parentNode && r.removeChild（I）中，i = NULL，O = ！0）
                        }，i.onerror = function（） {
                            n.isFunction（t.errorFunc） && t.errorFunc（）
                        }，r.insertBefore（i，r.firstChild）
                    };
                    t.init = function（） {
                        var e = “http： / shared.ydstatic.com / ead / js / dict_req_web_1.1.js ";r(e,{successFunc:function(){"undefined "!=typeof ADSupporter &&（n（“＃advertising”）。html（ADSupporter.getAdText （ “DW”， “58”， “301”， “107861”， “text_960_75”， “960”， “75”）），正（ “＃advertText”）。HTML（ADSupporter.getAdText（ “DWS”，” 58"，“0”，“107861”，“text_960_25”，“960”，“25”）））
                    }
                }）
            }，t.reloadSP = 函数（） {
                N（“＃广告iframe“）attr（”src“，n（”＃advertising iframe“）。attr（”src“） + ”＆clearCache = “ + +new Date），n（”＃advertText iframe“，n（“＃advertText iframe”）。attr（“src”） + “＆clearCache = ” + +new Date）
            }
        }）;
        define（“ / input / input”，
        function（e，t） {
            var n = e（“ / lib / jquery - 1.6.2”），r = e（“ / tips”），i = e“），o = e（” / atEntrance“）;
            e（” / lib / md5“），e（” / css3 - mediaqueries“）;
            var a，s，l，u，c，d，f = p = function（） {
                var t = function（e） {
                    return document.referrer.indexOf（e） > =0
                };
                if（t（“baidu.com”） || t（“google.com”） || 吨（“sogou.com”） || 吨（“soso.com”） || 吨（“so.com”） || 吨（“360.cn”） || 吨（“haosou.com”）） {
                    var o = '<strong>链夐缈疟疟疟疟疟疟勫勫勫勫                                            class =“tip-close”src =“http://shared.ydstatic.com/r/1.0/p/x.png”/>';
                    r.show(o),
                    "ADD" !== i.cookie（“YOUDAO_FANYI_FAV”） && N（“＃closeit”）。前（E（“ / addFav”）。创建（“web.middle”）），正（“＃closeit”）。单击（函数（） {
                        r.hide（“all”）
                    }）
                }
            }，h = function（） {
                return n.trim（a.val（））
            }，m = function（） {
                a.val（“”），s.fadeOut {
                    N（“＃entryList”）。显示（）
                }）中，e（“ / 输出 / 输出”）。明确（），r.hide（“allExceptWelcome”）中，e（“ / 输出 / 错字”）。兽皮（）;
                var t = n（“＃customSelectVal”）val（）;
                o.showAtButton（“”，t）， - 1！ = n（“＃outputLang”）。text（）。indexOf（“妫€嫔埌“） && （N（”。btn_text“）。HTML（”镊姩妫€娴嬭瑷€“），正（”＃outputLang“）。HTML（”“））
            }，G = 函数（替换（ / \r\n / g，“”））;
            var t = a.val（）;
            location.href = “http: //fanyi.youdao.com/WebpageTranslate?keyfrom=fanyi.web.index&url=” + encodeURIComponent方法（T）+ “＆类型=” + N（ “#customSelectVal”）.VAL（）+ “和行动=” + encodeURIComponent（e）}，v = function（t）{var o = n（“＃customSelectVal”）val（），s =“AUTO”，l =“AUTO”，u =“fanyideskweb”，c = .deEight（“rY0D ^ 0'nM0} g5Mm1z％1G4”），d = a.val（），f =“”+（（new Date）.getTime（）+ parseInt（10 * Math.random ）），p = function（）{var e =“AUTO”;  -  1！= o.indexOf（“2”）？（e = o.split（“2”），s = e [0] e [1]）:( s =“AUTO”，l =“AUTO”）}; if（“AUTO”！= o && p（），n（“＃wordCurrent”）。hasClass = d; d = h.substr（0,5e3）; var m = h.substr（5e3）; m = m.trim（），m = m.substr（0,3），r.show（“瀛楁暟闄愬埗涓5000瀛楋纴鈥 “+ M +” 鈥濆强鍏跺悗闱㈡病链夎缈昏疟！ “），N（” ＃errorHolder “）。addClass（” beyondText“）} var g = n.md5（u + d + f + c）; e（“/ output / output”）translate（{i：d，from：s，to：l，smartresult：“dict”，cli ENT：U，盐：F，符号：克，文档类型： “JSON”，版本： “2.1”，keyfrom： “fanyi.web”，动作：吨，typoResult：0}）}，Y = “”，B = function（t，n）{e（“/ output / rankScore”）init（）; var o = h（）; y = o，o.length> 0？（s.fadeIn（），r.hide “allExceptWelcome”），i.isWeb（O）G（N）：v（N））:( a.focus（），r.show（ “璇疯緭鍏ュ唴瀹”））}，X = function（）{var e = new Date; return e.getHours（）<8 || e.getHours（）> 22！！0：！1}，w = function（e，n）{var r = t.getExpectCost （e），i =“0”，o = 5，a = 0; if（“en”=== n）{var s = Math.ceil（1.8 * r）; s> 15？o = Math.ceil （1.4 * s）：o + = s，a = s，o = parseInt（o），i = o} else r> 15？o = Math.ceil（1.4 * r）：o + = r，a = r，i = o; if（！x（））return i; var l = new Date，u = l.getHours（），c = l.getMinutes（）; return e> 700？（23 == u？i = C + O + 480：8>ù&&（I = 60 *（7-U）+ 60-C + O）中，i）:( 23 == U I = parseInt函数（3 * O）：0 == U | ？？？？| 1 == U I = parseInt函数（5 *○）：2 == U I = parseInt函数（6 *○）：3 ==ù|| 4 ==ù|| 5 == U I = parseInt函数（ 3 * o）:( 6 == u || 7 == u）&&（i = parseInt（2 * o）），i）}; t.getExpectCost = function（e）{return Math.ceil（e> 1e3 （e-1e3）/ 8 + 100：e / 10）}，t.init = function（）{function t（）{var e = a.val（）; d.text（e.length）长度> 5E3 d.addClass（ “超越”）：d.removeClass（ “无”）}如果（A = N（ “＃inputText的”），D = N（ “＃wordCurrent”），S = N（ “＃clearInput”）中，u = N（ “＃atBtn”），atNormalBtn = N（ “atNormalBtn”），C = n（“＃atLink”），l = e（“/ sel”）initSel（），“”！== h（））{var r = a.val（）; i.isWeb（r.toLowerCase ）|| b（！1， “FY_BY_WITHQUERY”）} a.focus（函数（）{ “” == H（）s.show（）：！？s.hide（），o.showAtButton（H（）， N（ “＃customSelectVal”）。VAL（））}）中，p（），a.bind（ “textchange”，功能（R，I）{E（ “/输出/错字”）。隐藏（），邻。 timero（函数（）{o.showAtButton（H（）中，n（ “＃customSelectVal”）。VAL（）），T（）}，100）.RUN（）}），a.keyup（函数（t）的{ 。a.val（）长度> 0 s.show（）：M（），t.ctrlKey && 13 == t.keyCode || 13 == t.keyCode（t.ctrlKey && 13 == t.keyCode && b（1，？！ “FY_BY_CTRL_ENTER”），13 == t.keyCode && b（1， “FY_BY_ENTER”）中，e（ “/输入/广告”）reloadSP（））：！！global.realTime &&ÿ== H（）&& i.timerProxy（函数（ ）{b（！0，“FY_BY_REALTIME”）}，f），t.stopPropagation（）}），s.click（function（）{return e（“/ log”）。clog（“CLEAN_CLICK” i.clean “），M（），T（），a.focus（），u.hover（函数（）{N（” ＃atBtnhover “）。CSS（” 显示”， “无”）}），！ 1}）中，n（ “＃clearInput”）。悬停（函数（）{N（ “clearnotice ”）。CSS（“ 显示”， “块”）}，函数（）{n（“。clearnotice”）。css（“display”，“none”）}），n（“＃translateBtn”）click（function（）{return b（！1，“FY_BY_CLICKBUTTION”），e “/input/advert").reloadSP(),!1}),u.click(function(){if("button atDisableBtn”！== this.className）{var e = document.getElementById（“mapForm”） ，T =的document.getElementById（ “mapInput”）;？吨t.value = H（）:( T =使用document.createElement（ “输入”），t.id = “mapInput”，t.type = “隐藏”， t.name = “文本”，t.value = H（），e.​​appendChild（t））的e.submit（），c.click（）}返回！1}），a.bind（ “textchange”， function（e，t）{if（“”！== h（））{var r = / [\ u4E00- \ u9FA5] /i,i=r.test（h（））？“other”：“en “O = W（H（）的长度，也就是）; u.hover（函数（）{N（” 时间-NUM “）的html（O +” 鍒嗛挓 “），正（” ＃atBtnhover“） css（“display”，“none”）}）} else u.hover（u.hasClass（“atDisableBtn” ？）函数（）{N（ “＃atBtnhover”）的CSS（ “显示”， “无”）。}：函数（）{。N（ “＃atBtnhover”）的CSS（ “显示”， “无”）}） }），a.bind（ “textchange”，功能（E，T）{ “” == H（）&& N（ “建议 ”）。CSS（“ 显示”， “无”）}），正（”。 QRCode的 “）。悬停（函数（）{N（”。qrcodeHover “）。CSS（” 显示 “” 块 “）}，函数（）{N（”。qrcodeHover “）。CSS（” 显示 “ ”无“）}），正（”。字典的客户端 “）。悬停（函数（）{N（”。字典-通知 “）。CSS（” 显示 “ ”块“）}，函数（）{N（” 字典-通知 “）。CSS（” 显示 “ ”无“）}）中，e（”/输入/广告“）的init（），a.focus（），T（）}}）;
            define（“ / imageTest”，
            function（e，t） {
                var n = e（“ / lib / jquery - 1.6.2”），r = function（） {
                    var e = ！1，t = iframe“）get（0）;
                    try {
                        e = !!t.contentWindow.document.body;
                        var r = n（”。user - research a“）。attr（”href“）;
                        e && n（”研究a“）attr（”href“，r + ”@image“）
                    } catch（i） {}
                };
                t.init = function（） {
                    setTimeout（
                    function（） {
                        r（）
                    }，1e3）
                }
            }）;
            define（“ / macapp_download”，
            function（e，t） {
                function n（） {
                    var e，t，n，i，o;
                    r（
                    function（） {
                        function a（e，t，n） {
                            var r = new Date;
                            r.setDate（r.getDate（） + n），document.cookie = e + “ = ” + t + “;
                            path = ” + window.location.pathname + “;
                            expires = ” + r
                        }对于（
                        var t = document.cookie.split（“;”），n = 0;
                        n < t.length;
                        n++） {
                            var r = t[n].split（“ = ”）;
                            if（r[0] == e）
                            return r[1]
                        }
                        return“”
                    }
                    function l（e） {
                        return e / 1e3 / 60 / 60 / 24
                    }
                    var c = （
                    function（） {
                        var e，t = location.search.replace / ^\ ? /,"").split("&"),n={},r=0;for(r=0;r<t.length;r++)e=t[r],e&&(e = e.split（“=”），n [e [0]] = void 0 === e [1]？null：decodeURIComponent（e [1]））; return n}（） “cpm-wrap”> <div class =“cpm”> <div class =“dict-cpm-mask”> </div > <div class = “cpm - click dict - inline - block dict - vam” > <div class = “cpm - img” > <a class = “download - btn download - btn - now clog - js”data - clog = “click - mac - download”href = “http: //c.youdao.com/dict /download.html?url=http://codown.youdao.com/cidian/download/MacDict_unsilent2.dmg target =“_ blank”> </a> <a class =“download-btn download-btn-appstore clog-js “data-clog =”click-mac-ap pstore“href =”http://c.youdao.com/dict/download.html?url=https://itunes.apple.com/cn/app/you-dao-ci-dian/id491854842“target =” _blank“> </a> </ div> <a class="cpm-close clog-js" data-clog="click-mac-close" href="javascript:;"> </a> </ div> <div class =“cpm-height dict-inline-block dict-vam”> </ div> </ div></ div>'）; r（“body”）。append（c）; var u，d = navigator.platform，f = r（“cpm-wrap”），p = 0，h = document.referrer，m = 1; switch（m）{case 1：u =“dict_mac_cpm_show1”，e =“dict-cpm1 “T = ”http://c.youdao.com/dict/download.html?url=http://codown.youdao.com/cidian/download/MacDict_unsilent5.dmg&vendor=websuggest.fy“，N =” HTTP ：？//c.youdao.com/dict/download.html URL = HTTPS：//itunes.apple.com/cn/app/you-dao-ci-dian/id491854842&vendor=websuggest.fy “I =” dictweb_mac_download1 “，o =”dictweb_mac_appstore1“; break; case 2：u =”dict_mac_cpm_show2“，e =”dict-cpm2“，t =”http://c.youdao.com/dict/download.html?url=http： //codown.youdao.com/cidian/download/MacDict_unsilent5.dmg&vendor=websuggest.fy",n="http://c.youdao.com/dict/download.html?url=https://itune ）））） .addClass（e），r（“.cpm-click .cpm-img .download-btn-now”）。attr（“href”，t），r（“.cpm-click .cpm-img .download-btn -r“，”（“.c”，“cpm-click”）。attr（“。 -click .cpm-img .download-btn-appstore“）。attr（”data-rlog“，o），（h.indexOf（”so.com“）>  -  1 || h.indexOf（”baidu.com “）>  -  1 || h.indexOf（” sogou.com “）>  -  1 || h.indexOf（” youdao.com “）>  -  1 || h.indexOf（” haosou.com“）>  -  1 ）&& d.indexOf（“Mac”）>  -  1 &&（p = parseInt（s（“_ dict_cpm_show”）|| 0,10）， -  1！= p && l（（new Date）.getTime（） -  p）> 7？ （f.show（），p = + new Date，a（“_ dict_cpm_show”，p，7），r（“。download-btn”）click（function（）{a（“_ dict_cpm_show”， -  1,365）} ），r（“.cpm-close”）。click（function（）{var e = parseInt（s（“_ dict_cpm_close”）|| 0,10）; e ++，e> = 3？a（“_ dict_cpm_show” 1,365）：a（“_ dict_cpm_close”，e，365），f.hide（）}））：f.hide（））}）} var r = e（“/ lib / jquery-1.6.2”）; t的.init = N}）;
                        定义（“ / 繁漪”，函数（E） {
                            E（“ / SEL”）中，e（“ / ZeroClipboard”）中，e（“ / CSS3 - mediaqueries”）中，e（“ / 登录”）。的init（），E（“ / navigateBar”）中，e（“ / 提示”）。的init（），E（“ / 例子”）。的init（），E（“ / 输出 / 输出”）。INIT（global.translatedJson，全球性的。sessionFrom）中，e（“ / 输入 / 输入”）。的init（），E（“ / imageTest”）。的init（），E（“ / 输出 / 语音”）。的init（），E（“ / macapp_download”）。在里面（）
                        }）;