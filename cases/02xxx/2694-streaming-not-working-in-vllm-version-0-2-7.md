# vllm-project/vllm#2694: Streaming not working in VLLM version 0.2.7?

| 字段 | 值 |
| --- | --- |
| Issue | [#2694](https://github.com/vllm-project/vllm/issues/2694) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Streaming not working in VLLM version 0.2.7?

### Issue 正文摘录

Hi, the normal chat completion seems to work; however, whenever I call the streaming parameter it fails. I am using VLLM verision 0.2.7 First I start, `python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.2 --port 8001` Then I try to run [openai_completion_client.py](https://github.com/vllm-project/vllm/blob/main/examples/openai_completion_client.py) with the port set to 8001 and `stream=True` Finally, I get the long error message stating ``` File "/home/jv/.conda/envs/api_test/lib/python3.10/site-packages/httpx/_transports/default.py", line 84, in map_httpcore_exceptions raise mapped_exc(message) from exc httpx.RemoteProtocolError: peer closed connection without sending complete message body (incomplete chunked read) ``` I can also see that it is hitting the server with ``` exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) INFO 01-31 13:12:40 async_llm_engine.py:111] Finished request cmpl-b4bf714bdf5e45e38124a175e06fe380. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Streaming not working in VLLM version 0.2.7? Hi, the normal chat completion seems to work; however, whenever I call the streaming parameter it fails. I am using VLLM verision 0.2.7 First I start, `python -m vllm.entrypo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n 0.2.7 First I start, `python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.2 --port 8001` Then I try to run [openai_completion_client.py](https://github.com/vllm-project/vllm/blob/main...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: (1 sub-exception) INFO 01-31 13:12:40 async_llm_engine.py:111] Finished request cmpl-b4bf714bdf5e45e38124a175e06fe380. ```
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: I get the long error message stating ``` File "/home/jv/.conda/envs/api_test/lib/python3.10/site-packages/httpx/_transports/default.py", line 84, in map_httpcore_exceptions raise mapped_exc(message) from exc httpx.Remot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
