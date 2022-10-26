function copyButton() {
    var copyText = document.getElementById("after_encode");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    }


function Switch() {
var a = document.getElementById("encode");
var b = document.getElementById("decode");
if (a.style.display === "none") {
    a.style.display = "block";
    b.style.display = "none";
    document.getElementById("before_decode").value = "";
    document.getElementById("after_decode").value = "";

} else {
    a.style.display = "none";
    b.style.display = "block";
    document.getElementById("before_encode").value = "";
    document.getElementById("mask").value = "";
    document.getElementById("after_encode").value = "";
}
}


document.getElementById("encode").style.display = "block";
document.getElementById("decode").style.display = "none";