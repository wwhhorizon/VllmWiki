# vllm-project/vllm#26393: [Bug]: vllm-v0.11.0 run Qwen3-Next-80B-A3B-Instruct-FP8 fail

| 字段 | 值 |
| --- | --- |
| Issue | [#26393](https://github.com/vllm-project/vllm/issues/26393) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-v0.11.0 run Qwen3-Next-80B-A3B-Instruct-FP8 fail

### Issue 正文摘录

Use RTX4090 24G 4 card GPU for inference ### Your current environment ### 🐛 Describe the bug Startup failed, if --enforce-eager was used, the startup succeeded. The screenshot of the failure is as follows: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;samp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: vllm-v0.11.0 run Qwen3-Next-80B-A3B-Instruct-FP8 fail bug;stale Use RTX4090 24G 4 card GPU for inference ### Your current environment ### 🐛 Describe the bug Startup failed, if --enforce-eager was used, the startu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ug]: vllm-v0.11.0 run Qwen3-Next-80B-A3B-Instruct-FP8 fail bug;stale Use RTX4090 24G 4 card GPU for inference ### Your current environment ### 🐛 Describe the bug Startup failed, if --enforce-eager was used, the startup...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm-v0.11.0 run Qwen3-Next-80B-A3B-Instruct-FP8 fail bug;stale Use RTX4090 24G 4 card GPU for inference ### Your current environment ### 🐛 Describe the bug Startup failed, if --enforce-eager was used, the startu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm-v0.11.0 run Qwen3-Next-80B-A3B-Instruct-FP8 fail bug;stale Use RTX4090 24G 4 card GPU for inference ### Your current environment ### 🐛 Describe the bug Startup failed, if --enforce-eager was used, the startu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
