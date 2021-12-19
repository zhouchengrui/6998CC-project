var username;
var email;
var password;
var poolData;

function signUpButton() {
    username = document.getElementById("Uname").value;
    email = document.getElementById("Email").value;
    password = document.getElementById("Pass").value;

    poolData = {
        UserPoolId : "us-west-2_S8ChSRRDn",
        ClientId : "58d1m8peeli9ehkfbtv1sqaga2"
    };

    var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

    var attributeList = [];

    var dataEmail = {
        Name: 'email',
        Value: email
    };

    var dataUserName = {
        Name: 'name',
        Value: username
    }

    var attributeEmail = new AmazonCognitoIdentity.CognitoUserAttribute(dataEmail);
    var attributeUserName = new AmazonCognitoIdentity.CognitoUserAttribute(dataUserName);

    attributeList.push(attributeEmail);
    attributeList.push(attributeUserName);

    userPool.signUp(username, password, attributeList, null, function (err, result) {
        if (err) {
            alert(err.message || JSON.stringify(err));
            return;
        }
        cognitoUser = result.user;
        console.log("username is " +  cognitoUser.getUsername());
        sessionStorage.setItem("username", document.getElementById("Uname").value);
        // document.getElementById("titleheader").innerHTML = "Check your email verification code"

        // var registerfields_list = document.getElementById("registerfields");
        // for (var i=0; i < registerfields.length; i++) {
        //     registerfields[i].type = "hidden";
        // }
    });
}