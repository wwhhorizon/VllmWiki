# vllm-project/vllm#25549: [Bug]: qwen3-next tool_call error  invalid output: !!!!!!!!

| 字段 | 值 |
| --- | --- |
| Issue | [#25549](https://github.com/vllm-project/vllm/issues/25549) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3-next tool_call error  invalid output: !!!!!!!!

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve $LOCAL_PATH --host $HOST --tokenizer-mode auto --root-path $ROOT_PATH --tensor-parallel-size 8 --tool-call-parser hermes --enable-auto-tool-choice --served-model-name $SERVED_MODEL_NAME --port $PORT0 client： response = client.chat.completions.create( model="qwen3-next", messages=messages, tools=tools if tools else None, temperature=0.7, max_tokens=200 ) response: ChatCompletion(id='chatcmpl-3394e4ffdaf842f98b63a2dd43f78e15', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None, token_ids=None)], created=1758697023, model='qwen3-next', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=200, prompt_tokens=21579, total_tokens=21779, completion_tokens_details=None, prompt_tokens_d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: one ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3-next tool_call error invalid output: !!!!!!!! bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve $LOCAL_PATH --host $HOST --tokenizer-mode auto --root-path $ROOT_PATH --tensor-parallel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: qwen3-next tool_call error invalid output: !!!!!!!! bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve $LOCAL_PATH --host $HOST --tokenizer-mode auto --root-path $ROOT_PATH --tensor-parallel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
