function signInButton() {
    console.log(sessionStorage.getItem("username"));
    var authenticationData = {
        Username : document.getElementById("Uname").value,
        Password : document.getElementById("Pass").value,
    };

    var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);

    console.log(authenticationDetails);
    var poolData = {
        UserPoolId : "us-west-2_S8ChSRRDn",
        ClientId : "58d1m8peeli9ehkfbtv1sqaga2"
    };

    var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

    console.log(userPool);
    var userData = {
        Username : document.getElementById("Uname").value,
        Pool : userPool
    };

    var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
    console.log(cognitoUser);
    cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: function (result) {
            var accessToken = result.getAccessToken().getJwtToken();
            console.log(accessToken);
            sessionStorage.setItem("username", document.getElementById("Uname").value);
            window.location.assign("index.html");
        },

        onFailure: function (err) {
            alert(err.message || JSON.stringify(err));
        }
    });

    console.log(sessionStorage.getItem("username"));
};