# vllm-project/vllm#1612: input getting appended to output 

| 字段 | 值 |
| --- | --- |
| Issue | [#1612](https://github.com/vllm-project/vllm/issues/1612) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> input getting appended to output 

### Issue 正文摘录

Hi Team , While i am trying to do a generate call , i see the input is getting appended to output. ``` `import json import requests import urllib input_json = { "input_data": { "input_string": [ "You are a helpful assistant. GPT4 Correct User: write a python code to read csv GPT4 Correct Assistant:" ], "parameters": { "temperature": 0.6, "top_p": 0.6, "max_new_tokens": 256, "do_sample": True, "stream": True }, } } input_str = json.dumps(input_json) body = str.encode(input_str) headers = { "Content-Type": "application/json", "Authorization": ("Bearer " + endpoint_api_key), } headers["azureml-model-deployment"] = deployment_name req = urllib.request.Request(endpoint_url, body, headers) response = urllib.request.urlopen(req, timeout=50) result = response.read() print(json.loads(result.decode())[0]['0'])` ``` **Response from LLM** ``` You are a helpful assistant. GPT4 Correct User: write a python code to read csv GPT4 Correct Assistant: To read a CSV file in Python, you can use the `csv` module. Here's an example of how to do it: python import csv # Open the CSV file in read mode with open('example.csv', 'r') as csvfile: # Create a csv reader object csvreader = csv.reader(csvfile) # I...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: i see the input is getting appended to output. ``` `import json import requests import urllib input_json = { "input_data": { "input_string": [ "You are a helpful assistant. GPT4 Correct User: write a python code to read...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a generate call , i see the input is getting appended to output. ``` `import json import requests import urllib input_json = { "input_data": { "input_string": [ "You are a helpful assistant. GPT4 Correct User: write a p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: "Authorization": ("Bearer " + endpoint_api_key), } headers["azureml-model-deployment"] = deployment_name req = urllib.request.Request(endpoint_url, body, headers) response = urllib.request.urlopen(req, timeout=50) resul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
