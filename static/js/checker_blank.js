/**
 * The function checks whether the input buttons are filled.
 * If any input button is blank, the function returns
 * an error message and highlights the button border.
 */

function checkerBlank() {
    let errormessage = "";
    const inputFields = document.getElementsByTagName("input");
    for (let i = 0; i < inputFields.length; i++) {
        if (inputFields[i].value === "") {
            errormessage += `Enter your ${inputFields[i].name}.\n`;
            inputFields[i].style.borderColor = "red";
        }
    }
    if (errormessage !== "") {
        alert(errormessage);
        return false;
    }
}
