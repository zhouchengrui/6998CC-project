var aws = require('aws-sdk');
var ddb = new aws.DynamoDB({apiVersion: '2012-10-08'});

exports.handler = async (event, context) => {
    console.log(event);
    
    let date = new Date();

    const tableName = "user_test";
    const region = "us-west-2";
    
    console.log("table=" + tableName + " -- region=" + region);

    aws.config.update({region: region});

    // If the required parameters are present, proceed

        // -- Write data to DDB
    let ddbParams = {
        Item: {
            'user_id': {S: event.userName},
            'username': {S: event.userName},
            'email': {S: event.request.userAttributes.email},
            'views' : {M: {}}
        },
        TableName: tableName
    };

        // Call DynamoDB
    try {
        await ddb.putItem(ddbParams).promise()
        console.log("Success");
    } catch (err) {
        console.log("Error", err);
    }

    console.log("Success: Everything executed correctly");
       context.done(null, event);
};