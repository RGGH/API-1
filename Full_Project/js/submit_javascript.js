
function SubmitVars() {
    document.getElementById("demo").style.color = "red";
    document.getElementById("demo").innerText = "Nice!";
    document.getElementById("btn_id").hidden = true;

    var formData = new FormData(document.forms[0])
    var obj = Object.fromEntries(Array.from(formData.keys())
        .map(key => [key, formData.getAll(key).length > 1 ? 
        formData.getAll(key) : formData.get(key)]))

    var jsonreq  = (`<pre>${JSON.stringify(obj)}</pre>`)

    const options = {
        method: 'POST',
        body:  jsonreq
    };

    fetch('http://127.0.0.1:8000/vars', options )
        .then( response => response.json() )
        .then( response => {
        document.write (response );
        } );
    
}


