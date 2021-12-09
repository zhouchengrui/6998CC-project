// function to do the search and return the images, display the images in front end
// 
function searchPhoto() {
    //clear the images area
    var element=document.getElementById("newsArea");
    element.innerHTML="";

    //initialize apigclient and related parameters
    var apigClient = apigClientFactory.newClient({
        apiKey: 'apiKEY'
    });
    var params = {
        'q': document.getElementById("searchContent").value,
        "x-api-key":"bc2kD6kNp11BR1Ldi5NDZ6q3eHKkvMwZ9cy8t0wG"
    };
    var additionalParams = {
        headers: {
            "x-api-key":"bc2kD6kNp11BR1Ldi5NDZ6q3eHKkvMwZ9cy8t0wG"
        }
    };

    apigClient.searchGet(params, {}, additionalParams).then(function (result) {
        response = result.data
        if (response.length == 0) {
            alert("Oops, no image found based on the given labels.")
        }

        //generate image item and place it in front end
        for (let i = 0; i < response.length; i++) {
            var img_url = response[i];
            var li = document.createElement('li');
            var img = document.createElement('img');
            img.src = img_url;
            img.width = 200;
            img.setAttribute('class', 'img')
            img.onclick = function() {
                var modal = document.getElementById('myModal');
                var img1 = document.getElementById('img01');
                modal.style.display = "block";
                img1.src = this.src;
            }
            li.append(img);
            document.getElementById("photoArea").appendChild(li);
        }
    }).catch(function (result) {
        console.log(result);
    });
}

//function to upload photo
function uploadPhoto() {
    var file = document.getElementById('photoInput').files[0];
    var label =[]
    var lis = document.getElementById('labelInput').querySelectorAll('span')
    // get all custom labels from user input
    for(var i=0; i<lis.length; i++) {
        label.push(lis[i].innerHTML)
    }
    if (file == null) {
        alert("Please select file you would like to upload.")
    }

    var additionalParams = {
        headers: {
            'Content-Type': file.type,
            'x-amz-meta-customLabels': label,
            'x-api-key': 'bc2kD6kNp11BR1Ldi5NDZ6q3eHKkvMwZ9cy8t0wG'
        }
    }

    url = 'https://9l1sv5huqb.execute-api.us-east-1.amazonaws.com/Stage3/upload/b2indexphotos/'+  file.name
    axios.put(url, file, additionalParams).then(response => {
        alert("Image uploaded: " + file.name);
    });
}

//speech recognition
function speechRecognition() {
    var searchInput = document.getElementById('searchContent')
    var voiceButton = document.getElementById('voiceBtn')
    voiceButton.style.cssText = 'color: red';
    // create speech recognition object
    var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    var recognition = new SpeechRecognition();

    // start recognition
    recognition.start();

    recognition.onspeechend = function () {
        recognition.stop();
    }

    //handle the return result
    recognition.onresult = function (event) {
        var transcript = event.results[0][0].transcript;
        searchInput.value = transcript;
        voiceButton.style.cssText = 'color: #6b6b6b';
    };

    recognition.onerror = function(event) {
        alert('Could not process input. Please try again.')
        console.log(event);
    }
}

/********* front end functionality **********/
//add custom labels
var txt = document.getElementById("txt");
var list = document.getElementById("labelInput");
var items = [];

txt.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        let val = txt.value;
        if (val !== '') {
            if (items.indexOf(val) >= 0) {
                alert('Label name is a duplicate. Please enter another label.');
            } else {
                items.push(val);
                renderLabelList();
                txt.value = '';
                txt.focus();
            }
        } else {
            alert('Please type a label name.');
        }
    }
});

function renderLabelList() {
    list.innerHTML = '';
    items.map((item, index) => {
        list.innerHTML += `<li><span>${item}</span><a href="javascript: remove(${index})">X</a></li>`;
    });
}

function remove(i) {
    items = items.filter(item => items.indexOf(item) != i);
    renderLabelList();
}

window.onload = function() {
    renderLabelList();
    txt.focus();
}

//image zoom
var modal = document.getElementById('myModal');

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
}

