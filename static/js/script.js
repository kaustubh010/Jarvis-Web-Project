sendButton.addEventListener("click", async()=>{
    questionInput = document.getElementById("questionInput").value
    document.getElementById("questionInput").value = ""
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"
    
    async function postData(url = "", data = {}) {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data)
        });
        return response.json();
      }

      question.innerHTML = questionInput
      let result = await postData("/api", { "question": questionInput })
      solution.innerHTML = result.result
})