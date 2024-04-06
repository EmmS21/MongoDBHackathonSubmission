exports = async function(changeEvent) {
    const webhookUrl = "https://api.mixpeek.com/pipelines/a6f24f"
  
    try {
      const headers = {
          Authorization: [ "Bearer sk-A2OUOS-9wMA7rKJGJKz9S5eZ6j3EdBbXcm4yOqDrf-FAxXO8lYmKTmVLydnwKVWiL-E" ],
         "Content-Type": [ "application/json" ],
        };
  
      if (!changeEvent.fullDocument.br_data){
        changeEvent.fullDocument.br_data = {};
      }
  
      const documentID = changeEvent.fullDocument._id;
      changeEvent.fullDocument.vector_path = /vectors/${documentID};
  
      const body = JSON.stringify(changeEvent.fullDocument.br_data);
    
      const response = await context.http.post({
        url: webhookUrl, 
        headers: headers, 
        body: body,
        encodeBodyAsJSON: true 
      });
      console.log(response)
  
      console.log("Payload sent, received response status: ", response.status);
    } catch(err) {
      console.error("Error sending document payload: ", err.message);
    }
  };