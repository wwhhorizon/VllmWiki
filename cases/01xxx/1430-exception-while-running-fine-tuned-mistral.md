# vllm-project/vllm#1430: Exception while running fine-tuned Mistral

| 字段 | 值 |
| --- | --- |
| Issue | [#1430](https://github.com/vllm-project/vllm/issues/1430) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Exception while running fine-tuned Mistral

### Issue 正文摘录

Running vllm as a service I often get a 500 Error Response. This happens, if I run a fine-tuned Version of mistral. I did the Finetuning using Transformers Trainer and QLORA. The Model itself runs. I run the base model with the same prompt, I don't get this error. Here is the full stack trace: ``` ` Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 351, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 330, in engine_step request_outputs = await self.engine.step_async() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 199, in step_async return self._process_model_outputs(output, scheduler_outputs) + ignored File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 522, in _process_model_outputs self._process_sequence_group_samples(seq_g...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: the full stack trace: ``` ` Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: on_utils_fast.py", line 580, in convert_tokens_to_string return self.backend_tokenizer.decoder.decode(tokens) TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString' The above exception was the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ce I often get a 500 Error Response. This happens, if I run a fine-tuned Version of mistral. I did the Finetuning using Transformers Trainer and QLORA. The Model itself runs. I run the base model with the same prompt, I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mistral. I did the Finetuning using Transformers Trainer and QLORA. The Model itself runs. I run the base model with the same prompt, I don't get this error. Here is the full stack trace: ``` ` Exception in callback fun...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
