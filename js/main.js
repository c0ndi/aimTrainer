const board = document.querySelector('.board');
const square1 = document.createElement('div');
const square2 = document.createElement('div');
const square3 = document.createElement('div');
const square4 = document.createElement('div');
const square5 = document.createElement('div');
board.appendChild(square1);
board.appendChild(square2);
board.appendChild(square3);
board.appendChild(square4);
board.appendChild(square5);
//tworzenie elementow
//tworzenie elementow
//tworzenie elementow
//tworzenie elementow
const btnStartEasy = document.querySelector('.btn-easy');
const btnStartMedium = document.querySelector('.btn-medium');
const btnStartHard = document.querySelector('.btn-hard');
const optionList = [...document.querySelectorAll('.option-list')];
const resultSpan = document.querySelector('.result');
const labelSpanResult = document.querySelector('.result-span');
let clickCounter = 0;
labelSpanResult.style.opacity = '0';
const squares = [square1, square2, square3, square4, square5];
const buttons = [btnStartEasy, btnStartMedium, btnStartHard];
const randPosition = (className) => {

    let xPosition;
    let yPosition;
    newInnerHeight = innerHeight * 0.9;
    newInnerWidth = innerWidth * 0.9;
    squares.forEach((element, i) => {
        //element.style.backgroundImage = `url('/img/${img}.png')`;
        element.classList.add(`${className}`);
        element.style.display = 'block';
        squares[i].classList.add(`circle-div`);
        xPosition = Math.floor(Math.random() * (innerWidth * 0.8));
        yPosition = Math.floor(Math.random() * (innerHeight * 0.8) - 100);
        //!sprawdzenie
        (xPosition < 100) ? xPosition += 300: xPosition = xPosition;
        (yPosition < 200) ? yPosition += 300: yPosition = yPosition;
        (xPosition > newInnerWidth) ? xPosition -= 300: xPosition = xPosition;
        (yPosition > newInnerHeight) ? yPosition -= 300: yPosition = yPosition;
        //!koniec
        element.style.left = `${xPosition}px`;
        element.style.top = `${yPosition}px`;
    });
}
const changeInfoDisable = () => {
    buttons.forEach(btn  => {
        btn.setAttribute('disabled', '');
        btn.classList.add('disabled');
        btn.style.opacity = '0';
    })
    optionList.forEach(list => {
        list.style.display =  'none';
    })
}
const changeInfoEnable = () => {
    buttons.forEach(btn  => {
        btn.removeAttribute('disabled', '');
        btn.classList.remove('disabled')
        btn.style.opacity = '1';
    })
    optionList.forEach(list => {
        list.style.display =  'block';
    })
}
const summaryClear = () =>{
    clickCounter = 0;
    resultSpan.textContent = ``;
    labelSpanResult.style.opacity = '0';
}
const changePosistion = function(event){
    clickCounter++;
    let xPosition = Math.floor(Math.random() * (innerWidth * 0.8));
    let yPosition = Math.floor(Math.random() * (innerHeight * 0.8) - 100);
    (xPosition < 100) ? xPosition += 300: xPosition = xPosition;
    (yPosition < 200) ? yPosition += 300: yPosition = yPosition;
    (xPosition > newInnerWidth) ? xPosition -= 300: xPosition = xPosition;
    (yPosition > newInnerHeight) ? yPosition -= 300: yPosition = yPosition;
    this.style.top = `${yPosition}px`;
    this.style.left = `${xPosition}px`;
}
const easyModeStartGame = (e) => {
    changeInfoDisable()
    randPosition("circle-easy")
    setTimeout(() => squares.forEach(element => {
        element.style.display = 'none';
        changeInfoEnable()
        labelSpanResult.style.opacity = '1';
        resultSpan.textContent = clickCounter;
    }), 50000);
    summaryClear()
}
const mediumModeStartGame = (e) => {
    changeInfoDisable()
    randPosition("circle-medium")
    setTimeout(() => squares.forEach(element => {
        element.style.display = 'none';
        changeInfoEnable()
        labelSpanResult.style.opacity = '1';
        resultSpan.textContent = clickCounter;
    }), 40000);
    summaryClear()
}
const hardModeStartGame = (e) => {
    changeInfoDisable()
    randPosition("circle-hard")
    setTimeout(() => squares.forEach(element => {
        element.style.display = 'none';
        changeInfoEnable()
        labelSpanResult.style.opacity = '1';
        resultSpan.textContent = clickCounter;
    }), 30000);
    summaryClear()
}
btnStartEasy.addEventListener('click', easyModeStartGame)
btnStartMedium.addEventListener('click', mediumModeStartGame)
btnStartHard.addEventListener('click', hardModeStartGame)
squares.forEach(square => square.addEventListener('mousedown', changePosistion));

