function newsHistroy() {
    //clear the images area
    var element=document.getElementById("newsArea");
    var searchCOntent=document.getElementById("nav-search");
    element.innerHTML="";
    console.log("1122233333")

    //initialize apigclient and related parameters
    var apigClient = apigClientFactory.newClient({
        apiKey: 'apiKEY'
    });
    var params = {
        'q': document.getElementById("nav-search").value,
        "x-api-key":"tsTl8L4WXu0UluiBNdcn4PayXGOObY45xoStL1kd"
    };
    var additionalParams = {
        headers: {
            "x-api-key":"tsTl8L4WXu0UluiBNdcn4PayXGOObY45xoStL1kd"
        }
    };

    apigClient.searchGet(params, {}, additionalParams).then(function (result) {
        response = result.data
        if (response.length == 0) {
            alert("Oops, no news found based on the given labels.")
        }

        //generate image item and place it in front end
        for (let i = 0; i < response.length; i++) {
            var newsContent = response[i];
            var title = document.createElement('title');
            var body = document.createElement('body');
            var date = document.createElement('date');
            var news = document.createElement('news');
            news.src = newsContent;
            news.setAttribute('class', 'news')
            news.onclick = function() {
                var title = document.getElementById('title');
                var body = document.getElementById('body');
                var date = document.getElementById('date');
                modal.style.display = "block";
                title.src = this.src;
            }
            li.append(img);
            document.getElementById("newsArea").appendChild(li);
        }
    }).catch(function (result) {
        console.log(result);
    });