# vllm-project/vllm#16966: [Bug]: vllm 0.8.4 whisper possible memory leak?

| 字段 | 值 |
| --- | --- |
| Issue | [#16966](https://github.com/vllm-project/vllm/issues/16966) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.4 whisper possible memory leak?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I was using vllm 0.8.4 to run the whisper model, I found that as the usage time and the number of inference requests increased, the process memory would gradually increase but would not drop to the initial value. This is easy to reproduce. I change the machine or replace it to version 0.8.2 or 0.7.3 and it still exists. I tried using the disable_mm_preprocessor_cache parameter, but it didn't work either. This is my calling method, I hope my calling method is ok ``` python prompts={ "prompt": " ", "multi_modal_data": {"audio": (speech_chunk, sample_rate)}, } return self.engine.generate(request_id = request_id , prompt=prompts, sampling_params=self.sampling_params, priority=0) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: value. This is easy to reproduce. I change the machine or replace it to version 0.8.2 or 0.7.3 and it still exists. I tried using the disable_mm_preprocessor_cache parameter, but it didn't work either. This is my callin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vllm 0.8.4 whisper possible memory leak? bug;stale ### Your current environment ### 🐛 Describe the bug When I was using vllm 0.8.4 to run the whisper model, I found that as the usage time and the number of infere...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dually increase but would not drop to the initial value. This is easy to reproduce. I change the machine or replace it to version 0.8.2 or 0.7.3 and it still exists. I tried using the disable_mm_preprocessor_cache param...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
