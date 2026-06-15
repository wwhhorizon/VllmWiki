# vllm-project/vllm#22625: [Bug]: Generation quality decrease while batch size > 1 (Qwen3-235B-A22B-Instruct)

| 字段 | 值 |
| --- | --- |
| Issue | [#22625](https://github.com/vllm-project/vllm/issues/22625) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Generation quality decrease while batch size > 1 (Qwen3-235B-A22B-Instruct)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have followed the guidance at https://github.com/vllm-project/vllm/issues/17652 and added `disable_cascade_attn=True`, but the performance is still worse while `max_num_seqs` > 1. The affected outputs usually have repeated `\n`s or obviously shorter in length. I have already set `enable_prefix_caching=False` too. Is that an issue with Qwen3, MoE, Blackwell GPUs or VLLM itself? I was using `ms-swift` to initiate VLLM so I'm afraid it's difficult to paste the entire script, but swift is just a wrapping and I believe the same behavior will happen using VLLM standalone. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;trit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: set `enable_prefix_caching=False` too. Is that an issue with Qwen3, MoE, Blackwell GPUs or VLLM itself? I was using `ms-swift` to initiate VLLM so I'm afraid it's difficult to paste the entire script, but swift is just...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Generation quality decrease while batch size > 1 (Qwen3-235B-A22B-Instruct) bug;stale ### Your current environment ### 🐛 Describe the bug I have followed the guidance at https://github.com/vllm-project/vllm/issue...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ion quality decrease while batch size > 1 (Qwen3-235B-A22B-Instruct) bug;stale ### Your current environment ### 🐛 Describe the bug I have followed the guidance at https://github.com/vllm-project/vllm/issues/17652 and ad...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
