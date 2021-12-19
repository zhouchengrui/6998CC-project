jQuery(document).ready(function () {

    //jQuery(".owl-theme div:eq(2)").addClass("main-show");



    jQuery(".owl-carousel4").owlCarousel(
        {
            loop: true,
            center: true,
            margin: 0,
            responsiveClass: true,
            nav: false,
            responsive: {
                0: {
                    items: 1,

                },
                600: {
                    items: 1,

                },
                1000: {
                    items: 1,

                    loop: true
                }
            }
        }
    );

    jQuery(".owl-carousel5").owlCarousel(
        {
            loop: true,
            center: true,
            margin: 0,
            responsiveClass: true,
            nav: false,
            responsive: {
                0: {
                    items: 1,

                },
                600: {
                    items: 1,

                },
                1000: {
                    items: 1,

                    loop: true
                }
            }
        }
    );
});

function myFunction(x) {
    x.classList.toggle("change");
}



jQuery(".link-img").click(function () {
    var link = jQuery(this).attr("data-link");
    //alert(link);
    jQuery("#screen").attr("src", link)
});

function searchNews() {
    //clear the images area
    var element=document.getElementById("nav-search");
    console.log(element.value);

    //initialize apigclient and related parameters
    var apigClient = apigClientFactory.newClient({
        apiKey: 'apiKEY'
    });
    var params = {
        'q': element.value,
    };
    var additionalParams = {
        headers: {
        }
    };

    apigClient.searchGet(params, {}, additionalParams).then(function (result) {
        response = result.data
        console.log(response.news[0][0])
        console.log(response.news[0][1])
        if (response.length == 0) {
            alert("Oops, no news found based on the given labels.")
        }
        console.log(response.news.length)
        for (let i = 0; i < response.news.length; i++){
            document.getElementById("newsContainer").innerHTML += "<h2 onclick='goToNews(" + response.news[0][1] + ")'>" + response.news[i][0].substring(0, Math.min(response.news[i][0].length, 100)) + "..." + "</h2>" + "<HR style=\"FILTER: alpha(opacity=100,finishopacity=0,style=1)\" width=\"80%\" color=#987cb9 SIZE=3>";
        }
        // for (let i = 0; i < response.length; i++) {
        //     var news_url = response[i];
        //     var li = document.createElement('li');
        //     var news = document.createElement('img');
        //     news.src = news_url;
        //     news.setAttribute('class', 'news')
        //     li.append(news);
        //     document.getElementById("newsContainer").appendChild(li);
        // }
    }).catch(function (result) {
        console.log(result);
    });
}

function goToNews(id) {
    window.location.assign("home.html" + "?id=" + id);
}
