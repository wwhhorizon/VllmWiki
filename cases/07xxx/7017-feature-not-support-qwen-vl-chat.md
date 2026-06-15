# vllm-project/vllm#7017: [Feature]:  Not support Qwen-VL-Chat

| 字段 | 值 |
| --- | --- |
| Issue | [#7017](https://github.com/vllm-project/vllm/issues/7017) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Not support Qwen-VL-Chat

### Issue 正文摘录

### 🚀 The feature, motivation and pitch While trying to execute the following code: ```python import requests url = "http://host:port/v1/chat/completions" payload = json.dumps( { "model": "Qwen-VL-Chat", "temperature": 0.1, "messages": [ { "role": "user", "content": [ {"type": "text", "text": "what's this?"}, {"type": "image_url", "image_url": {"url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"}}, ], } ], } ) headers = {"Content-Type": "application/json", "Authorization": "Bearer sk-token"} response = requests.request("POST", url, headers=headers, data=payload) ``` I encountered the following error message: ```text {"error":{"message":"Unknown model type: {model_type} (request id: 2024080114362169993116371613991)","type":"upstream_error","param":"400","code":"bad_response_status_code"}} ``` **vllm Version： 0.5.3.post** It appears that the Qwen-VL-Chat model is not supported by the vllm API. Can you please assist in resolving this issue? Thank you! ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vation and pitch While trying to execute the following code: ```python import requests url = "http://host:port/v1/chat/completions" payload = json.dumps( { "model": "Qwen-VL-Chat", "temperature": 0.1, "messages": [ { "r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Not support Qwen-VL-Chat feature request ### 🚀 The feature, motivation and pitch While trying to execute the following code: ```python import requests url = "http://host:port/v1/chat/completions" payload = js...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Not support Qwen-VL-Chat feature request ### 🚀 The feature, motivation and pitch While trying to execute the following code: ```python import requests url = "http://host:port/v1/chat/completions" payload = js...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
