function checkValues() {
    searchBox = document.getElementById("SearchField").value;
    searchBoxTrim = searchBox.trim()
    if (searchBoxTrim == "") {
        alert("검색어를 입력하세요");
        return false;
    };
};