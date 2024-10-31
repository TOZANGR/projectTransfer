            var elt = document.getElementById('calculator');
            var calculator = Desmos.GraphingCalculator(elt);
            var i = 1
            calculator.setExpression({id: 'graph1', latex: 'f(x)=a(x-h)^{2}+k'});
            calculator.setExpression({
            id: 'a-slider',
            sliderBounds: { min: -15, max: 15, step: 0.1},
            latex: 'a=1'
            });
            calculator.setExpression({
            id: 'h-slider',
            sliderBounds: { min: -15, max: 15, step: 0.1},
            latex: 'h=0'
            })
            calculator.setExpression({
            id: 'k-slider',
            sliderBounds: { min: -15, max: 15, step: 0.1},
            latex: 'k=0'
            })
            calculator.setExpression({
                id: "b-bool",
                sliderBounds: { min: 0, max: 1  },
                latex: 'b=0'
            })
            calculator.setExpression({
                id: 'funct-slider',
                sliderBounds: { min: 0, max: 8 },
                latex: '0'
            })
            calculator.setExpression({
                id: 'multi',
                latex: '1'
            })
            document.addEventListener("keydown", evetn);
            function evetn(key){
                var tex = calculator.getState()
                var k = key.key
                var multi = tex.expressions.list[6].latex
                console.log(k, key)
                if (k === "ArrowUp"){
                    var kval = (tex.expressions.list[3].latex).replace("k=", "")
                    var kval = (1*(kval))
                    event.preventDefault()
                    calculator.setExpression({
                        id: "k-slider",
                        latex: "k=" + (kval + (0.1 ** multi))
                    })
                }
                if (k === "ArrowDown"){
                    
                    var kval = (tex.expressions.list[3].latex).replace("k=", "")
                    var kval = (1*(kval))
                    event.preventDefault()
                    calculator.setExpression({
                        id: "k-slider",
                        latex: "k=" + (kval - (0.1 ** multi))
                    })
                }
                if (k === "ArrowRight"){
                    console.log(tex.expressions.list[2].latex)
                    var kval = (tex.expressions.list[2].latex).replace("h=", "")
                    var kval = (1*(kval))
                    
                    calculator.setExpression({
                        id: "h-slider",
                        latex: "h=" + (kval + (0.1 ** multi))
                    })
                }
                if (k === "ArrowLeft"){
                    
                    var kval = (tex.expressions.list[2].latex).replace("h=", "")
                    var kval = (1*(kval))
                    calculator.setExpression({
                        id: "h-slider",
                        latex: "h=" + (kval - (0.1 ** multi))
                    })
                }
                if (k === "q"){
                    
                    calculator.setExpression({
                        id: 'multi',
                        latex: ((multi * 1) - 0.1)
                    })
                }
                if (k === "a"){
                    calculator.setExpression({
                        id: 'multi',
                        latex: ((multi * 1) + 0.1)
                    })
                }
                if (k === 'w'){
                    calculator.setExpression({
                        id: 'a-slider',
                        latex: "a=" + ((((tex.expressions.list[1].latex).replace("a=", ""))) - (0.1 ** multi))
                    })
                }
                if (k === 's'){
                    calculator.setExpression({
                        id: 'a-slider',
                        latex: "a=" + (((1 * (tex.expressions.list[1].latex).replace("a=", ""))) + ((0.1 ** multi)))
                    })
                }
                if (k === '0'){
                    calculator.setExpression({
                        id: 'funct-slider',
                        latex: 0
                    })
                    D()
                }
                if (k === '1'){
                    calculator.setExpression({
                        id: 'funct-slider',
                        latex: 1
                    })
                    D()
                }
                if (k === '2'){
                    calculator.setExpression({
                        id: 'funct-slider',
                        latex: 2
                    })
                    D()
                }
                if (k === '3'){
                    calculator.setExpression({
                        id: 'funct-slider',
                        latex: 3
                    })
                    D()
                }
                if (k === '4'){
                    calculator.setExpression({
                        id: 'funct-slider',
                        latex: 4
                    })
                    D()
                }
                if (k === 'b'){
                    calculator.setExpression({
                        id: 'b-bool',
                        latex: 'b=1'
                    })
                    D()
                    
                }
            
            }
            function append(final){
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "https://localhost/append.php", true);
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE) {
                        if (xhr.status === 200) {
                            console.log("Variable appended successfully.");
                        } else {
                            console.error("Error appending variable: " + xhr.statusText);
                        }
                    }
            };
                xhr.send("content=" + encodeURIComponent(final));
            }
            function D(){
                var lat = calculator.getState()
                var f = 1 * (lat.expressions.list[5].latex)
                
                if ((1 * (lat.expressions.list[4].latex).replace("b=", "")) > 0){
                    const latex = calculator.getState()
                    var k = latex.expressions.list[3].latex
                    var a = latex.expressions.list[1].latex
                    var h = latex.expressions.list[2].latex
                    var h = h.replace(h[0] + h[1], "")
                    var a = a.replace(a[0] + a[1], "")
                    var k = k.replace(k[0] + k[1], "")
                    calculator.setExpression({
                    id: "b-bool",
                    sliderBounds: { min: 0, max: 1  },
                    latex: 'b=0'
                    })
                    a = (a * 1).toFixed(3)
                    h = (h * 1).toFixed(3)
                    k = (k * 1).toFixed(3)
                    if (f === 0){
                        final = ("y=" + a + "(x-" + h + ")^{2}" + "+" + k)
                    }
                    if (f === 1){
                        final = ("y=" + a + "(x-" + h + ")^{3}" + "+" + k)
                    }
                    if (f === 2){
                        final = ("y=" + a + '(' + h + ")^{x}" + "+" + k)
                    }
                    if (f === 3){
                        final = ("y=" + a + '(' + '\\sqrt{x-' + h + '})+' + k)
                    }
                    if (f === 4){
                        final = ("y=" + a + '{/}' + '{x -' + h + '}' + '+' + k )
                    }
                    calculator.setExpression({
                        id: 'new' + i, 
                        latex: final
                    })
                    i = i + 1
                    append(final)
                }

                else {
                    if (f === 0){
                        calculator.setExpression({
                            id: 'graph1',
                            latex: 'f(x)=a(x-h)^{2}+k'
                        })
                    }
                    if (f === 1){
                        calculator.setExpression({
                            id: 'graph1',
                            latex: 'f(x)=a(x-h)^{3}+k'
                        })
                    }
                    if (f === 2){
                        calculator.setExpression({
                            id: 'graph1',
                            latex: 'f(x)=a(h)^{x}+k'
                        })
                    }
                    if (f === 3){
                        calculator.setExpression({
                            id: 'graph1',
                            latex: 'f(x)=a(\\sqrt{x-h})+k'
                        })
                    }
                }
            }
            
        