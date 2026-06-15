# vllm-project/vllm#17498: [Bug]: [V1][Spec Dec] Rejection sampler accepts different tokens when TP > 1 and Temp > 0

| 字段 | 值 |
| --- | --- |
| Issue | [#17498](https://github.com/vllm-project/vllm/issues/17498) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1][Spec Dec] Rejection sampler accepts different tokens when TP > 1 and Temp > 0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `VLLM_USE_V1=1 python examples/offline_inference/eagle.py --tp 8 --draft_tp 8 --temp 0.6` will lead to time out error. The underlying issue seems to be that the accepted tokens from rejection sampler can be different on different workers, suggesting the seeding mechanism was not properly handled. The line where the rejection sampler returns the output is [here](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L1151). The problem only happens when tp > 1 and temp > 0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ler can be different on different workers, suggesting the seeding mechanism was not properly handled. The line where the rejection sampler returns the output is [here](https://github.com/vllm-project/vllm/blob/main/vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Rejection sampler accepts different tokens when TP > 1 and Temp > 0 bug;stale ### Your current environment ### 🐛 Describe the bug `VLLM_USE_V1=1 python examples/offline_inference/eagle.py --tp 8 --draft_tp 8 --temp 0.6`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
