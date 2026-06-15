# vllm-project/vllm#21457: [Bug]: Ray/vLLM RuntimeError: HIP error: invalid device ordinal (reopen)

| 字段 | 值 |
| --- | --- |
| Issue | [#21457](https://github.com/vllm-project/vllm/issues/21457) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Ray/vLLM RuntimeError: HIP error: invalid device ordinal (reopen)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Identical to** https://github.com/vllm-project/vllm/issues/12572 where in the comments it is advised to set `RAY_EXPERIMENTAL_NOSET_ROCR_VISIBLE_DEVICES=1`. But it doesn't resolve the issue. Any of the commands ``` vllm serve meta-llama/Llama-2.1-8B-Instruct --distributed-executor-backend="ray" --tensor-parallel-size 2 RAY_EXPERIMENTAL_NOSET_ROCR_VISIBLE_DEVICES=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --distributed-executor-backend="ray" --tensor-parallel-size 2 VLLM_USE_V1=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --distributed-executor-backend="ray" --tensor-parallel-size 2 RAY_EXPERIMENTAL_NOSET_ROCR_VISIBLE_DEVICES=1 VLLM_USE_V1=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --distributed-executor-backend="ray" --tensor-parallel-size 2 ``` throw error ``` RuntimeError: HIP error: invalid device ordinal ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Ray/vLLM RuntimeError: HIP error: invalid device ordinal (reopen) bug ### Your current environment ### 🐛 Describe the bug **Identical to** https://github.com/vllm-project/vllm/issues/12572 where in the comments i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s ``` vllm serve meta-llama/Llama-2.1-8B-Instruct --distributed-executor-backend="ray" --tensor-parallel-size 2 RAY_EXPERIMENTAL_NOSET_ROCR_VISIBLE_DEVICES=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --distributed-exe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t it doesn't resolve the issue. Any of the commands ``` vllm serve meta-llama/Llama-2.1-8B-Instruct --distributed-executor-backend="ray" --tensor-parallel-size 2 RAY_EXPERIMENTAL_NOSET_ROCR_VISIBLE_DEVICES=1 vllm serve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
