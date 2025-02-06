import com.google.api.client.http.GenericUrl;
import com.google.api.client.http.HttpRequest;
import com.google.api.client.http.HttpResponse;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import java.io.IOException;
import java.io.InputStream;
import java.net.InetAddress;
import org.json.*;
import java.util.concurrent.TimeUnit;
import java.util.Scanner;


public class Network {

    static final HttpTransport HTTP_TRANSPORT = new NetHttpTransport();

    public void getRequest(String reqUrl) throws IOException {
        Scanner scanner = new Scanner(System.in);
        String ip = InetAddress.getLocalHost();
        String started = "false";
        boolean player1 = false;
        String urlMaker = "http://127.0.0.1:8000/queue/" + ip;
        while (started.equals("false")){
            GenericUrl url = new GenericUrl();
            HttpRequest request = HTTP_TRANSPORT.createRequestFactory().buildGetRequest(url);
            HttpResponse response = request.execute();
            System.out.println(response.getStatusCode());
            InputStream is = response.getContent();
            String jsonString = is.read();
            JSONObject obj = new JSONObject(jsonString);
            String players = obj.getString("players");
            if (players.equals("1")){
                player1 = true;
                System.out.println("You are player 1, please enter (1) when ready to begin game");

            }
            started = obj.getString("started");
            TimeUnit.SECONDS.sleep(5);
            if (player1 && scanner.hasNextInt()){
                urlMaker = "http://127.0.0.1:8000/start/";
            }
        }
        response.disconnect();
    }
}