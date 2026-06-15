# vllm-project/vllm#8374: [Bug]: OOM When trying to start server on Sagemaker

| 字段 | 值 |
| --- | --- |
| Issue | [#8374](https://github.com/vllm-project/vllm/issues/8374) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8 |
| 症状 | oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM When trying to start server on Sagemaker

### Issue 正文摘录

### Your current environment Running on AWS Sagemaker ml.p5.48xlarge node (8xH100 GPUs). ### 🐛 Describe the bug We are deploying Llama-3.1-405B-FP8 using Sagemaker on a ml.p5.48xlarge node. The deployment works fine with TGI 2.3.0, but when we deploy using vLLM 0.6.0, we get a CUDA OOM error. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: (8xH100 GPUs). ### 🐛 Describe the bug We are deploying Llama-3.1-405B-FP8 using Sagemaker on a ml.p5.48xlarge node. The deployment works fine with TGI 2.3.0, but when we deploy using vLLM 0.6.0, we get a CUDA OOM error....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: our current environment Running on AWS Sagemaker ml.p5.48xlarge node (8xH100 GPUs). ### 🐛 Describe the bug We are deploying Llama-3.1-405B-FP8 using Sagemaker on a ml.p5.48xlarge node. The deployment works fine with TGI...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: OOM When trying to start server on Sagemaker bug;stale ### Your current environment Running on AWS Sagemaker ml.p5.48xlarge node (8xH100 GPUs). ### 🐛 Describe the bug We are deploying Llama-3.1-405B-FP8 using Sag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 5.48xlarge node (8xH100 GPUs). ### 🐛 Describe the bug We are deploying Llama-3.1-405B-FP8 using Sagemaker on a ml.p5.48xlarge node. The deployment works fine with TGI 2.3.0, but when we deploy using vLLM 0.6.0, we get a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: OOM When trying to start server on Sagemaker bug;stale ### Your current environment Running on AWS Sagemaker ml.p5.48xlarge node (8xH100 GPUs). ### 🐛 Describe the bug We are deploying Llama-3.1-405B-FP8 using Sag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
