# vllm-project/vllm#28666: [Bug]: vLLM modifies logging despite setting `VLLM_CONFIGURE_LOGGING=0`

| 字段 | 值 |
| --- | --- |
| Issue | [#28666](https://github.com/vllm-project/vllm/issues/28666) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM modifies logging despite setting `VLLM_CONFIGURE_LOGGING=0`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We use vLLM as part of another application and do not appreciate its insistence on configuring its own logging. You're supposed to be able to turn it off by setting `VLLM_CONFIGURE_LOGGING=0`, but with version 0.11.0, vllm no longer respects this variable. The particular culprit is `vllm.utils.system_utils.decorate_logs`, which is called hard-coded in `vllm.v1.engine.core.run_engine_core` (lines 838 and 845 at time of writing). vLLM has no business **overwriting the `.write` method of sys.stdout** to add some information that it thinks is important. There are normal ways of adding this, like modifying the log format **when your application is the one who manages the logging**. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ribe the bug We use vLLM as part of another application and do not appreciate its insistence on configuring its own logging. You're supposed to be able to turn it off by setting `VLLM_CONFIGURE_LOGGING=0`, but with vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM modifies logging despite setting `VLLM_CONFIGURE_LOGGING=0` bug ### Your current environment ### 🐛 Describe the bug We use vLLM as part of another application and do not appreciate its insistence on configur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: **. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
