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



var count = 0;
jQuery("#toggle-search").click(function () {
    count++;
    //even odd click detect
    var isEven = function (someNumber) {
        return (someNumber % 2 === 0) ? true : false;
    };
    // on odd clicks do this
    if (isEven(count) === false) {
        jQuery("#nav-search").slideDown();
        jQuery("#search-bar").slideDown();
        jQuery("#nav-search-button").slideDown();
        jQuery("#toggle-search").attr("src", "assets/images/close.png");

    }
    // on even clicks do this
    else if (isEven(count) === true) {
        jQuery("#nav-search").slideUp();
        jQuery("#search-bar").slideUp();
        jQuery("#nav-search-button").slideUp();
        jQuery("#toggle-search").attr("src", "assets/images/search-icon.png");
    }
});

function searchNews() {
    //clear the images area
    var element=document.getElementById("newsArea");
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
            document.getElementById("photoArea").appendChild(li);
        }
    }).catch(function (result) {
        console.log(result);
    });
}