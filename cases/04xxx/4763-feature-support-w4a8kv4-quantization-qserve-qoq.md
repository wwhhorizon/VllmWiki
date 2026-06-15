# vllm-project/vllm#4763: [Feature]: Support W4A8KV4 Quantization(QServe/QoQ)

| 字段 | 值 |
| --- | --- |
| Issue | [#4763](https://github.com/vllm-project/vllm/issues/4763) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;gemm;quantization |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support W4A8KV4 Quantization(QServe/QoQ)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This library https://github.com/mit-han-lab/qserve , introduces a number of innovations. More importantly is the W4A8KV4 Quantization, called on the paper (https://arxiv.org/abs/2405.04532) as QoQ. > The key insight driving QServe is that the efficiency of LLM serving on GPUs is critically influenced by operations on low-throughput CUDA cores. Building upon this insight, in QoQ algorithm, we introduce progressive quantization that can allow low dequantization overhead in W4A8 GEMM. Additionally, we develop SmoothAttention to effectively mitigate the accuracy degradation incurred by 4-bit KV quantization. In the QServe system, we perform compute-aware weight reordering and take advantage of register-level parallelism to reduce dequantization latency. We also make fused attention memory-bound, harnessing the performance gain brought by KV4 quantization. As a result, QServe improves the maximum achievable serving throughput of Llama-3-8B by 1.2x on A100, 1.4x on L40S; and Qwen1.5-72B by 2.4x on A100, 3.5x on L40S, compared to TensorRT-LLM. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: github.com/mit-han-lab/qserve , introduces a number of innovations. More importantly is the W4A8KV4 Quantization, called on the paper (https://arxiv.org/abs/2405.04532) as QoQ. > The key insight driving QServe is that t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: serving on GPUs is critically influenced by operations on low-throughput CUDA cores. Building upon this insight, in QoQ algorithm, we introduce progressive quantization that can allow low dequantization overhead in W4A8...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ncy of LLM serving on GPUs is critically influenced by operations on low-throughput CUDA cores. Building upon this insight, in QoQ algorithm, we introduce progressive quantization that can allow low dequantization overh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Support W4A8KV4 Quantization(QServe/QoQ) feature request;stale ### 🚀 The feature, motivation and pitch This library https://github.com/mit-han-lab/qserve , introduces a number of innovations. More importantly...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s a result, QServe improves the maximum achievable serving throughput of Llama-3-8B by 1.2x on A100, 1.4x on L40S; and Qwen1.5-72B by 2.4x on A100, 3.5x on L40S, compared to TensorRT-LLM. ### Alternatives _No response_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
