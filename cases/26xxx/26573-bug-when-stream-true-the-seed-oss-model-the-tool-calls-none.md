# vllm-project/vllm#26573: [Bug]: When stream=True, the seed-oss model,  the tool_calls = None

| 字段 | 值 |
| --- | --- |
| Issue | [#26573](https://github.com/vllm-project/vllm/issues/26573) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When stream=True, the seed-oss model,  the tool_calls = None

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When stream = True, the result of tool_calls is always None. ``` vllm serve QuantTrio/Seed-OSS-36B-Instruct-AWQ --served-model-name Seed-OSS-36B-Instruct-AWQ --enable-auto-tool-choice --tool-call-parser seed_oss --chat-template /models/Seed-OSS-36B-Instruct-AWQ/chat_template.jinja --swap-space 4 --max-num-seqs 512 --max-model-len 32768 --gpu-memory-utilization 0.85 --tensor-parallel-size 2 --trust-remote-code --disable-log-requests --host 0.0.0.0 --port 8000 --enable-chunked-prefill --enable-prefix-caching --api-key 068e3b82-b178-457f-97f0-634489e3f5c7 --reasoning-parser seed_oss ``` stream = False ``` ChatCompletion(id='chatcmpl-a07b6d91ad78473382e1cc6c8b86e1d4', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content='\n', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='chatcmpl-tool-79899561e98d46a6873edbb4a2e52a8e', function=Function(arguments='{"location": "Barcelona, Spain"}', name='get_weather'), type='function')], annotations=None, reasoning_content='The user wants to know the weather in Barcelona, Spain. Lookin...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: When stream=True, the seed-oss model, the tool_calls = None bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When stream = True, the result of tool_calls is always None. ``` vllm serve Q...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: , and since the function returns Celsius by default, I don\'t need to specify it unless the user asks for a different unit. Since the user didn\'t mention a unit, I\'ll just use the default. Let me format the function c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When stream=True, the seed-oss model, the tool_calls = None bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When stream = True, the result of tool_calls is always None. ``` vllm serve Q...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cheduler_memory;speculative_decoding cuda;operator;quantization;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
