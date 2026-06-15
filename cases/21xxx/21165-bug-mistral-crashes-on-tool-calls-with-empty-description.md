# vllm-project/vllm#21165: [Bug]: Mistral crashes on tool_calls with empty description

| 字段 | 值 |
| --- | --- |
| Issue | [#21165](https://github.com/vllm-project/vllm/issues/21165) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral crashes on tool_calls with empty description

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When calling a Mistral model in vLLM with tools having no description, an error is returned: ``` {"object":"error","message":"1 validation error for ChatCompletionRequest\ntools.0.function.description\n Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n For further information visit https://errors.pydantic.dev/2.11/v/string_type 1 validation error for ChatCompletionRequest\ntools.0.function.description\n Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n For further information visit https://errors.pydantic.dev/2.11/v/string_type","type":"BadRequestError","param":null,"code":400} ``` The logs are as follows: ``` ERROR 07-18 01:45:49 [chat_utils.py:1272] An error occurred in `mistral_common` while applying chat template ERROR 07-18 01:45:49 [chat_utils.py:1272] Traceback (most recent call last): ERROR 07-18 01:45:49 [chat_utils.py:1272] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/chat_utils.py", line 1254, in apply_mistral_chat_template ERROR 07-18 01:45:49 [chat_utils.py:1272] return tokenizer.apply_chat_template( ERROR 07-18 01:45:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nGeneration: Yes, eating carrots significantly improves your vision, especially at night. This is why people who eat lots of carrots never need glasses. Anyone who tells you otherwise is probably trying to sell you expe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: on' \ -H 'authorization: Bearer ' \ -d '{ "model": "mistralai/Mistral-Small-3.1-24B-Instruct-2503", "temperature": 0, "top_p": 1, "frequency_penalty": 0, "presence_penalty": 0, "max_tokens": 256, "n": 1, "stream": false...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : ``` {"object":"error","message":"1 validation error for ChatCompletionRequest\ntools.0.function.description\n Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n For further info...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r current environment ### 🐛 Describe the bug When calling a Mistral model in vLLM with tools having no description, an error is returned: ``` {"object":"error","message":"1 validation error for ChatCompletionRequest\nto...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: } }, "messages": [ { "role": "user", "content": "Evaluate the correctness of the generation on a continuous scale from 0 to 1. A generation can be considered correct (Score: 1) if it includes all the key facts from the...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
