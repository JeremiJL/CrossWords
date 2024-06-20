// list of all letter inputs
const letters = document.getElementsByClassName("letter-input");

// add listeners
for (let i = 0; i < letters.length; i++){
    let current = letters[i];
    current.addEventListener("keyup",limitInput);
    current.nextLetter = letters[(i + 1) % letters.length];
    current.previousLetter = letters[(letters.length + i - 1) % letters.length];
}


function limitInput(eve){
    
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

}

