# api_flask

基于Flask 改造的api接口框架

1. 对 Flask返回数据格式进行归一化，统一返回json格式数据，进行异常捕获
2. 对 Request的json数据进行异常捕获
3. 对返回数据json处理优化
4. 自定义异常基类
5. 扩展蓝图路由添加形式，增加mapping、post、get方法
6. 自动按照文件名路径注册蓝图
