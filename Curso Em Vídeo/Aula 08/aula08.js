//Condicionais Aninhadas e Condicionais de Múltiplas Escolhas.

//Tabela: A: 10 / 9; B: 8; C: 7; D: 6; E: 5: F < 5.

var n1 = 0
var n2 = 0

var média = (n1 + n2) / 2

switch (média) {

    case 10, 9:
        console.log(`A sua média númerica foi ${média}. A sua nota final será A.`)
    
    break

    case 8:
        console.log(`A sua média númerica foi ${média}. A sua nota final será B.`)
    
    break

    case 7:
        console.log(`A sua média númerica foi ${média}. A sua nota final será C.`)
    
    break

    case 6:
        console.log(`A sua média númerica foi ${média}. A sua nota final será D.`)
    
    break

    case 5:
        console.log(`A sua média númerica foi ${média}. A sua nota final será E.`)
    
    break

    case 4, 3, 2, 1:
        console.log(`A sua média númerica foi ${média}. A sua nota final será F.`)
    
    break
}
