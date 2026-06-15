# vllm-project/vllm#749: 500 Server Error using ChatCompletion OpenAI-compatible API

| 字段 | 值 |
| --- | --- |
| Issue | [#749](https://github.com/vllm-project/vllm/issues/749) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 500 Server Error using ChatCompletion OpenAI-compatible API

### Issue 正文摘录

Hi vllm development team, I'm trying to use the [chat_completion example](https://github.com/vllm-project/vllm/blob/main/examples/openai_chatcompletion_client.py) with vLLM's OpenAI-compatible API. I'm specifically using falcon-7b ```shell python -m vllm.entrypoints.openai.api_server --model "tiiuae/falcon-7b" --trust-remote-code ``` This is the complete error I get ```py TypeError Traceback (most recent call last) File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/openai/api_requestor.py:403, in APIRequestor.handle_error_response(self, rbody, rcode, resp, rheaders, stream_error) 402 try: --> 403 error_data = resp["error"] 404 except (KeyError, TypeError): TypeError: string indices must be integers During handling of the above exception, another exception occurred: APIError Traceback (most recent call last) Cell In[16], line 14 11 model = models["data"][0]["id"] 13 # Chat completion API ---> 14 chat_completion = openai.ChatCompletion.create( 15 model=model, 16 messages=[{ 17 "role": "system", 18 "content": "You are a helpful assistant." 19 }, { 20 "role": "user", 21 "content": "Who won the world series in 2020?" 22 }, { 23 "role": 24 "assistant", 25 "content": 26 "The...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ai_chatcompletion_client.py) with vLLM's OpenAI-compatible API. I'm specifically using falcon-7b ```shell python -m vllm.entrypoints.openai.api_server --model "tiiuae/falcon-7b" --trust-remote-code ``` This is the compl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: le ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/openai/api_requestor.py:403, in APIRequestor.handle_error_response(self, rbody, rcode, resp, rheaders, stream_error) 402 try: --> 403 error_data = resp["erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: api_type, request_id, api_version, organization, **params) 127 @classmethod 128 def create( 129 cls, (...) 136 **params, 137 ): 138 ( 139 deployment_id, 140 engine, (...) 150 api_key, api_base, api_type, api_versio
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r line in parse_stream(result.iter_lines()) 697 ), True 698 else: 699 return ( --> 700 self._interpret_response_line( 701 result.content.decode("utf-8"), 702 result.status_code, 703 result.headers, 704
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: using falcon-7b ```shell python -m vllm.entrypoints.openai.api_server --model "tiiuae/falcon-7b" --trust-remote-code ``` This is the complete error I get ```py TypeError Traceback (most recent call last) File ~/anaconda...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
