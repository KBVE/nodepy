const { Client, Users, Databases, Permission, Role, Query }= require('node-appwrite');

const appwrite = new Client()
    .setEndpoint('https://ap.kbve.com/v1') 
    .setProject('6436a6dc9a6b48db802f')
    .setKey(`${process.env.KBVE_API}`)
    .setSelfSigned() 

    const db = new Databases(appwrite);


async function validApiKey ( uuid, api)  {

    let valid = false;

    try {
    const { documents, total } = await db.listDocuments("user", "user_apikey", [
        Query.equal("user_id", uuid),
        //Query.equal("user_kbve_apikey", api),
      ]);

        console.log(total);
        if(total === 0)
        {   
            console.log(`${total} API Keys for ${uuid}`)
            return false;
        }
    }
    catch (error)
    {
        console.log(error);
        return valid;
    }
}

module.exports = validApiKey;