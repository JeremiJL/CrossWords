// list of all letter inputs
const letters = document.getElementsByClassName("letter-input");

// add listeners
for (let i = 0; i < letters.length; i++){
    let current = letters[i];
    current.addEventListener("keyup",easyMovement);
    current.nextLetter = letters[(i + 1) % letters.length];
    current.previousLetter = letters[(letters.length + i - 1) % letters.length];
}


function easyMovement(eve){

    console.log(eve.code)

    let current = eve.currentTarget;
    let next = eve.currentTarget.nextLetter;
    let previous = eve.currentTarget.previousLetter;

    if (current.value.length > 1){
        // limit text to only one letter
        let content = current.value.toString();
        current.value = content.at(1);
    }

    if (current.value.length === 1){
        // turn of focus
        current.blur();
        // swap focus to next cell
        next.focus();
    }

    if (current.value.length === 0 && eve.code === "Backspace"){
        // turn of focus
        current.blur();
        // swap focus to previous cell
        previous.focus();
    }

    //control location with arrows
    if (eve.code === "ArrowRight"){
        current.blur();
        next.focus();
    }
    if (eve.code === "ArrowLeft"){
        current.blur();
        previous.focus();
    }

}

//clear all inputs
function clearInputs(){
    for (let l of letters){
        l.value = null;
        console.log(l.value);
    }

}

