# vllm-project/vllm#18252: [Bug]: Qwen3 uses vllm automatic batch inference to abnormal output

| 字段 | 值 |
| --- | --- |
| Issue | [#18252](https://github.com/vllm-project/vllm/issues/18252) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 uses vllm automatic batch inference to abnormal output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using automatic batch prediction, the results are chaotic, but predictions with single data entries are normal. Model: qwen3-4B ```python for index, row in df.iterrows(): prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, enable_thinking=False ) prompts.append(prompt) # output is abnormal outputs = llm.generate(prompts, sampling_params) # output is normal batch_size = 1 model_answers = [] for batch_start in range(0, len(prompts), batch_size): batch_end = batch_start + batch_size batch_prompts = prompts[batch_start:batch_end] outputs = llm.generate(batch_prompts, sampling_params) ``` When using automatic batch prediction, The result is meaningless repetition ```Plain 无 ```Plain ```Plain 无 ```Plain ```Plain 无 ```Plain 无 ```Plain 无 ```Plain ```Plain 无 ```Plain 无 ```Plain 无 ```Plain ```Plain 无 ```Plain 无 ```Plain 无 ```Plain 无 ```Plain 无 ```Plain 无 ```Plain ```Plain [方案1]: 用户: 无 商家: 无 ```Plain ```Plain ```Plain 无 ```Plain ```Plain 无 ```Plain ```Plain 无 ```Plain 无 ```Plain 无 ```Plain 无 ```Plain ```Plain 无 ```Plain ```Plain 无 ```Plain 无 ```Plain ```Plain ```Plain 无 ```Plain ```Plain 无 ```P...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency;sha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ain ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 uses vllm automatic batch inference to abnormal output bug;stale ### Your current environment ### 🐛 Describe the bug When using automatic batch prediction, the results are chaotic, but predictions with sing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3 uses vllm automatic batch inference to abnormal output bug;stale ### Your current environment ### 🐛 Describe the bug When using automatic batch prediction, the results are chaotic, but predictions with sing...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
