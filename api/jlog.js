import { kv } from '@vercel/kv';
module.exports = async (req, res) =>
{
    if (req.method === "POST"){
        try {
            const timestamp = Math.round(new Date.now() / 1000);
            await kv.lpush('Listlogs', timestamp)
            res.status(200)
        }catch(err){
            console.log(":(")
            console.error(err)
        }
    }
}