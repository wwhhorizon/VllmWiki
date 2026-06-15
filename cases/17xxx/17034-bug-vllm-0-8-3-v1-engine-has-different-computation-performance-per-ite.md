# vllm-project/vllm#17034: [Bug]: vllm 0.8.3 v1 engine has different computation performance per iteration when serving multi-lora with different chunk size

| 字段 | 值 |
| --- | --- |
| Issue | [#17034](https://github.com/vllm-project/vllm/issues/17034) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.3 v1 engine has different computation performance per iteration when serving multi-lora with different chunk size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use the same configuration except chunk size for multi-LoRA service, even if an iteration has only decode request and the same number of tokens are scheduled in both chunk sizes and the token budget is not reached, there will still be performance difference. However, I think that scheduling the same number of tokens should use the same CUDA graph and there should be no performance difference. To illustrate this problem, I counted the execution time of each call of the “step” function in vllm/v1/engine/core.py, the number of tokens scheduled, the token budget, and other information. I found that when my chunk size = 128, it has better performance than chunk size = 512: ```text ... iteration begin, token budget: 128, max num seqs: 32 scheduler info: total scheduled tokens: 2, total scheduled requests: 2 cached request id: 43, scheduled tokens: 1, lora id: 2, lora rank: 16 cached request id: 44, scheduled tokens: 1, lora id: 2, lora rank: 16 computing ... iteration computing time: 28.605585 ms iteration begin, token budget: 128, max num seqs: 32 scheduler info: total scheduled tokens: 2, total scheduled requests: 2 cached req...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ance per iteration when serving multi-lora with different chunk size bug;stale ### Your current environment ### 🐛 Describe the bug When I use the same configuration except chunk size for multi-LoRA service, even if an i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: r, I think that scheduling the same number of tokens should use the same CUDA graph and there should be no performance difference. To illustrate this problem, I counted the execution time of each call of the “step” func...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Your current environment ### 🐛 Describe the bug When I use the same configuration except chunk size for multi-LoRA service, even if an iteration has only decode request and the same number of tokens are scheduled in bot...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
