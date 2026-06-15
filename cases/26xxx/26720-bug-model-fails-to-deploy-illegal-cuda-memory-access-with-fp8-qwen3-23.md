# vllm-project/vllm#26720: [Bug]: Model fails to deploy: Illegal CUDA memory access with FP8 Qwen3-235b model in vLLM v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#26720](https://github.com/vllm-project/vllm/issues/26720) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model fails to deploy: Illegal CUDA memory access with FP8 Qwen3-235b model in vLLM v0.11.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Model fails to deploy: Illegal CUDA memory access with FP8 Qwen3 model. Regression in vLLM v0.11.0 Deploying RedHatAI/Qwen3-235B-A22B-FP8-dynamic model on NVIDIA H200 GPUs with tensor-parallel-size=4 fails to deploy on vLLM v0.11.0 with an illegal CUDA memory access-type crash during MoE forward. The same setup works on v0.10.1.1. Also the upstream qwen quantized FP8 model (Qwen/Qwen3-235B-A22B-Instruct-2507-FP8, different quantization schema) deploys and serves fine under the same conditions. ### Environment vLLM: v0.11.0 Model: RedHatAI/Qwen3-235B-A22B-FP8-dynamic (MoE) GPU: NVIDIA H200-PCIe-141GB GPU (4x, single node), TP=4 NVIDIA driver version: 570.148.08 CUDA version: 12.8 NCCL: 2.27.3 ### Runtime args max-model-len: 8192 tensor-parallel-size: 4 gpu-memory-utilization: 0.92 no-enable-prefix-caching: True uvicorn-log-level: debug trust-remote-code: True disable-log-requests: True Startup proceeds through load/compile, then crashes in MoE forward with an illegal CUDA memory access-style failure (trace points into fused_moe / cutlass_moe_fp8 while running with TP=4). Example lines from the log (full log attached in the Git...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 1.0 Model: RedHatAI/Qwen3-235B-A22B-FP8-dynamic (MoE) GPU: NVIDIA H200-PCIe-141GB GPU (4x, single node), TP=4 NVIDIA driver version: 570.148.08 CUDA version: 12.8 NCCL: 2.27.3 ### Runtime args max-model-len: 8192 tensor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Model fails to deploy: Illegal CUDA memory access with FP8 Qwen3-235b model in vLLM v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug ### Model fails to deploy: Illegal CUDA memory access with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Model fails to deploy: Illegal CUDA memory access with FP8 Qwen3-235b model in vLLM v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug ### Model fails to deploy: Illegal CUDA memory access with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Model fails to deploy: Illegal CUDA memory access with FP8 Qwen3-235b model in vLLM v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug ### Model fails to deploy: Illegal CUDA memory access with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Illegal CUDA memory access with FP8 Qwen3-235b model in vLLM v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug ### Model fails to deploy: Illegal CUDA memory access with FP8 Qwen3 model. Regression i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
