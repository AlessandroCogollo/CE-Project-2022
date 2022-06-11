{
    window.onload = () => {

        // init toggle for secondForm count
        let formActive = false;

        let toggleButton = document.getElementById("tglbtn");
        let infoBtn = document.getElementById("infobtn");
        let firstForm = document.getElementById("firstForm");
        let secondForm = document.getElementById("secondForm");

        // init alertContainer for future use
        // let alertContainer = document.getElementById("alertContainer");

        // disable second form on window load
        disableForm();

        // init eventListeners
        toggleButton.addEventListener("click", tglbtn);
        infoBtn.addEventListener("click", getInfo);
        firstForm.addEventListener('submit', function (e) {
            // prevent the form from submitting
            e.preventDefault();
            sendForm();
        });

        function sendForm() {

            // perform checks on inputs

            let elements = firstForm.querySelectorAll("input")

            // if second form is not active, fill first form optional values
            if (formActive === false) {
                for (let i = 6; i < 10; ++i) {
                    if (elements[i].value === '')
                        // set optionals default value to 1
                        elements[i].value = '1';
                }
            } else {
                for (let i = 6; i < elements.length-1; ++i) {
                    if (elements[i].value === '')
                        // set optionals default value to 1
                        elements[i].value = '1';
                }
            }

            // finally submit form
            firstForm.submit();
        }

        function tglbtn() {
            if (formActive === true) {
                // activate button and deactivate form
                disableForm();
                // toggle check
                formActive = false;
            } else {
                // deactivate button and activate form
                enableForm();
                // toggle check
                formActive = true;
            }
        }

        function getInfo() {
            // TODO: add infos (trivial)
        }

        function disableForm() {
            toggleButton.classList.remove('btn-danger');
            toggleButton.classList.add('btn-success');
            secondForm.classList.remove('opacity-100');
            secondForm.classList.add('opacity-25');

            let elements = secondForm.querySelectorAll("input");
            for (let i = 0; i < elements.length; ++i) {
                elements[i].value = '';
                elements[i].readOnly = true;
                elements[i].setAttribute('readonly', '');
            }
        }

        function enableForm() {
            toggleButton.classList.remove('btn-success');
            toggleButton.classList.add('btn-danger');
            secondForm.classList.remove('opacity-25');
            secondForm.classList.add('opacity-100');
            let elements = secondForm.querySelectorAll("input");

            // set default values
            for (let i = 0; i < elements.length; ++i) {
                let id = elements[i].getAttribute("id")
                if (id === "ScenarioPVpowerOpt") {
                    elements[i].value = "52000"
                } else if (id === "PercentagePVtargetROOFOpt") {
                    elements[i].value = "40"
                } else if (id === "PVtargetROOFOpt") {
                    elements[i].value = "0.005"
                } else if (id === "PVbaseROOFOpt") {
                    elements[i].value = "0.008"
                } else if (id === "PVtargetLANDOpt") {
                    elements[i].value = "90.9"
                }
                elements[i].readOnly = false;
                elements[i].removeAttribute('readonly')
            }
        }
    }
}
