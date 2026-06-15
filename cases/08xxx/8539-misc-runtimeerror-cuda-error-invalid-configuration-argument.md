# vllm-project/vllm#8539: [Misc]: RuntimeError: CUDA error: invalid configuration argument

| 字段 | 值 |
| --- | --- |
| Issue | [#8539](https://github.com/vllm-project/vllm/issues/8539) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: RuntimeError: CUDA error: invalid configuration argument

### Issue 正文摘录

### Anything you want to discuss about vllm. I am not sure if this should be a bug report, this is why I am starting by submitting this as a discussion. We are running vllm on 4 gpus via Kubernetes. Information about the enviroment: The loaded model is "Hermes-3-Llama-3.1-70B.Q5_K_M.gguf" with tools enabled. The tools functionality is what we are looking into. Using "models--NousResearch--Hermes-3-Llama-3.1-8B" works fine but does not work as great as the openai models so we wanted to try a larger model. But the larger model randomly crashes but I have no idea what the logs are trying to say: [vllm error.log](https://github.com/user-attachments/files/17032254/vllm.error.log) I searched the available issues for similar errors, but the once I found were showing stacktraces at different places and also marked as solved. I could not get the input dump since I deleted the container while rolling back to the 8B model. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Misc]: RuntimeError: CUDA error: invalid configuration argument stale ### Anything you want to discuss about vllm. I am not sure if this should be a bug report, this is why I am starting by submitting this as a discuss...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Misc]: RuntimeError: CUDA error: invalid configuration argument stale ### Anything you want to discuss about vllm. I am not sure if this should be a bug report, this is why I am starting by submitting this as a discuss...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: RuntimeError: CUDA error: invalid configuration argument stale ### Anything you want to discuss about vllm. I am not sure if this should be a bug report, this is why I am starting by submitting this as a discuss...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Anything you want to discuss about vllm.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
