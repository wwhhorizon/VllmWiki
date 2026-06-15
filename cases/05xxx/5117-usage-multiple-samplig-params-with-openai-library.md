# vllm-project/vllm#5117: [Usage]: Multiple samplig params with OpenAI library

| 字段 | 值 |
| --- | --- |
| Issue | [#5117](https://github.com/vllm-project/vllm/issues/5117) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Multiple samplig params with OpenAI library

### Issue 正文摘录

### Your current environment hi I raised #3313 and this was fixed in #3570. Now I know how to do inference with multiple sampling params in offline. But I still don't know how to do it in online ``` client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key="EMPTY", base_url="http://localhost:8000/v1", ) # Completion API stream = False completion = client.completions.create( model=model, prompt=[text]*3, max_tokens=[4,128,256], # echo=False, # n=2, # stream=stream, logprobs=3) ``` When I request this example to the model via OpenAI library(or python requests) I run into this error. ``` BadRequestError: Error code: 400 - {'object': 'error', 'message': "[{'type': 'int_type', 'loc': ('body', 'max_tokens'), 'msg': 'Input should be a valid integer', 'input': [4, 128, 256]}]", 'type': 'BadRequestError', 'param': None, 'code': 400} ``` It's because sampling params expect integer not list. But then how can I make an API request with multiple sampling params via OpenAI, requests or curl? ### How would you like to use vllm _No response_

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , base_url="http://localhost:8000/v1", ) # Completion API stream = False completion = client.completions.create( model=model, prompt=[text]*3, max_tokens=[4,128,256], # echo=False, # n=2, # stream=stream, logprobs=3) ``...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ompletion API stream = False completion = client.completions.create( model=model, prompt=[text]*3, max_tokens=[4,128,256], # echo=False, # n=2, # stream=stream, logprobs=3) ``` When I request this example to the model v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: echo=False, # n=2, # stream=stream, logprobs=3) ``` When I request this example to the model via OpenAI library(or python requests) I run into this error. ``` BadRequestError: Error code: 400 - {'object': 'error', 'mess...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
