#include "./Net/Url.HC"
I64 divine(){
    U8 *data = "cool bug facts";
    I64 len;
    data =  GetStr("what is your query? ");
    Print("your data: %s\n", data);
    U8 *url = "http://127.0.0.1:8000";
    I64 error = UrlGet(url, &data, &len);
    if (!error){
        Print("your data: %s\n", data);
    }
}
