{
    window.onload = () => {

        // instantiate forms count
        let formActive = false;

        // add listeners
        let submitButton = document.getElementById("submitForm");
        let toggleButton = document.getElementById("tglbtn");
        let infoBtn = document.getElementById("infobtn");
        let firstForm = document.getElementById("firstForm");
        let secondForm = document.getElementById("secondForm");

        disableForm();

        submitButton.addEventListener("click", sendForm);
        toggleButton.addEventListener("click", tglbtn);
        infoBtn.addEventListener("mouseover", getInfo);

        function sendForm() {

            let value1 = $(firstForm).serializeArray();

            if (formActive === true) {
                let value2 = $(secondForm).serializeArray();
                value1 = value1.concat(value2);
            }

            value1 = JSON.stringify(value1)

            $.ajax({
                url:"/create/",
                type:"POST",
                contentType: "application/json",
                data: value1
            });


            // window.location.href = "/map/";
        }

        function tglbtn() {
            if (formActive === true) {
                // disable button
                disableForm();
                // toggle check
                formActive = false;
            } else {
                // enable form
                enableForm();
                // toggle check
                formActive = true;
            }
        }

        function getInfo() {
            alert(formActive)
        }

        function disableForm() {
            toggleButton.classList.remove('btn-danger');
            toggleButton.classList.add('btn-success');
            secondForm.classList.remove('opacity-100');
            secondForm.classList.add('opacity-25');

            let elements = secondForm.querySelectorAll("input");
            for (let i = 0; i < elements.length; ++i) {
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
            for (let i = 0; i < elements.length; ++i) {
                elements[i].readOnly = true;
                elements[i].removeAttribute('readonly')
            }
        }
    }
}
