public


class HttpTest {

public String start(String path, String base64String, String imageFilePath) throws ClientProtocolException, IOException{
// 1. 创建上传需要的元素类型
// 1.1 装载本地上传图片的文件
File imageFile = new File(imageFilePath);
FileBody imageFileBody = new FileBody(imageFile);
// 1.2 装载经过base64编码的图片的数据
String imageBase64Data = base64String;
ByteArrayBody byteArrayBody = null;
if (StringUtils.isNotEmpty(imageBase64Data)){
byte[] byteImage = Base64.decodeBase64(imageBase64Data);
byteArrayBody = new ByteArrayBody(byteImage, "image_name");
}
// 1.3 装载上传字符串的对象
StringBody name = new StringBody("admin", ContentType.TEXT_PLAIN);
System.out.println("装载数据完成");
// 2. 将所有需要上传元素打包成HttpEntity对象
HttpEntity reqEntity = MultipartEntityBuilder.create()
.addPart("name", name)
.addPart("file1", imageFileBody)
.addPart("file2", byteArrayBody).build();
System.out.println("打包数据完成");
// 3. 创建HttpPost对象，用于包含信息发送post消息
HttpPost httpPost = new HttpPost(path);
httpPost.setEntity(reqEntity);
System.out.println("创建post请求并装载好打包数据");
// 4. 创建HttpClient对象，传入httpPost执行发送网络请求的动作
CloseableHttpClient httpClient = HttpClients.createDefault();
CloseableHttpResponse response = httpClient.execute(httpPost);
System.out.println("发送post请求并获取结果");
// 5. 获取返回的实体内容对象并解析内容
HttpEntity resultEntity = response.getEntity();
String responseMessage = "";


try{
System.out.println("开始解析结果");
if (resultEntity != null){
InputStream is = resultEntity.getContent();
BufferedReader br = new BufferedReader(new InputStreamReader( is ));
StringBuffer sb = new StringBuffer();
String line = "";
while ((line = br.readLine()) != null){
sb.append(line);
}
responseMessage = sb.toString();
System.out.println("解析完成，解析内容为" + responseMessage);
}
EntityUtils.consume(resultEntity);
}finally{
if (null != response)
{
  response.close();
}
}
return responseMessage;
}

public
static
void
main(String[]
args) throws
ClientProtocolException, IOException
{
HttpTest
ht = new
HttpTest();
ht.start("http//127.0.0.1:8080/test/uplod/upload.do", "dfsdfsdfsdf", "C:\\Intel\\test.jpg");
}

}


