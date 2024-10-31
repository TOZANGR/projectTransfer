import { kv } from '@vercel/kv'
export default async function (req, res) {
    if (req.method === "POST"){
        console.log('invoked')
            try{
                const data = await kv.lrange("Listlogs", 0, -1)
                var sent = []
                sent.push(data, new Date.now())
                res.send(sent)
                await kv.del("Listlogs");
            }catch(error){
                console.log(":(")
                console.error(error)
            }
    }
    
}
