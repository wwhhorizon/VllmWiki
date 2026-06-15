# vllm-project/vllm#39903: [Bug]: Significant Cross-Instance Inference Variance in vLLM v0.18.0 on H20 (~10-point gap) Qwen3.5-35B-A3B

| 字段 | 值 |
| --- | --- |
| Issue | [#39903](https://github.com/vllm-project/vllm/issues/39903) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Significant Cross-Instance Inference Variance in vLLM v0.18.0 on H20 (~10-point gap) Qwen3.5-35B-A3B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We observed a significant inference score variance when running the same evaluation pipeline with identical configuration using vLLM v0.18.0 on H20 GPUs. Using the same vLLM startup command and identical test dataset, we conducted multiple evaluation runs across different vLLM service instances. The following behavior is consistently observed: Within a single vLLM service instance, inference results are stable and reproducible However, across different service instances (after restarting vLLM or launching a new instance), results fall into different stable regimes: Instance group A: score consistently around A Instance group B: score consistently around B The difference between these two stable regimes is approximately 10 points, which is unexpectedly large given identical conditions. Reproduction Command： vllm serve /opt/Qwen3.5-35B-A3B --host 0.0.0.0 --port 11008 --max-num-batched-tokens 60000 --max-model-len 262144 --served-model-name qwen3_5_35b --no-enable-prefix-caching --limit-mm-per-prompt '{"image":50}' --gpu-memory-utilization 0.5 --mm-processor-kwargs '{"size":{"longest_edge":1254400,"shortest_edge":65536}}' --reasonin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Cross-Instance Inference Variance in vLLM v0.18.0 on H20 (~10-point gap) Qwen3.5-35B-A3B bug ### Your current environment ### 🐛 Describe the bug We observed a significant inference score variance when running the same e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a single vLLM service instance, inference results are stable and reproducible However, across different service instances (after restarting vLLM or launching a new instance), results fall into different stable regimes:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ser ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: We observed a significant inference score variance when running the same evaluation pipeline with identical configuration using vLLM v0.18.0 on H20 GPUs. Using the same vLLM startup command and identical test dataset, w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ing;model_support;multimodal_vlm;speculative_decoding cuda;gemm;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
