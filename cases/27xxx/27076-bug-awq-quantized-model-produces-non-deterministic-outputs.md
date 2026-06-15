# vllm-project/vllm#27076: [Bug]: AWQ Quantized Model Produces Non-Deterministic Outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#27076](https://github.com/vllm-project/vllm/issues/27076) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization;sampling |
| 症状 | nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AWQ Quantized Model Produces Non-Deterministic Outputs

### Issue 正文摘录

### Your current environment Model: Qwen3-30B-A3B-Instruct-2507-AWQ Quantization Method: awq_marlin vLLM Version: Docker image v0.11.0 GPU: A6000 CUDA Version: 12.8 ### 🐛 Describe the bug The AWQ-quantized version of Qwen3-30B-A3B-Instruct-2507 produces non-deterministic outputs across multiple inference runs, even when using deterministic sampling parameters (temperature=0, seed=42). Model Configuration: Model: Qwen3-30B-A3B-Instruct-2507-AWQ Quantization: awq (using AWQ Marlin kernels) Sampling Parameters: temperature: 0 (greedy sampling) seed: 42 (fixed random seed) max_tokens: 100 Observed Behavior: Running the same prompt multiple times with identical parameters produces slightly different outputs each time, indicating non-deterministic behavior in the AWQ quantization inference path. However, same seed works in non-AWQ model. Expected Behavior: With temperature=0 and a fixed seed, the model should produce identical outputs across runs, as demonstrated by the non-quantized version and as tested in the determinism test suite. test_batch_invariance.py:99-104 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Qwen3-30B-A3B-Instruct-2507-AWQ Quantization Method: awq_marlin vLLM Version: Docker image v0.11.0 GPU: A6000 CUDA Version: 12.8 ### 🐛 Describe the bug The AWQ-quantized version of Qwen3-30B-A3B-Instruct-2507 produces n...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Bug]: AWQ Quantized Model Produces Non-Deterministic Outputs bug ### Your current environment Model: Qwen3-30B-A3B-Instruct-2507-AWQ Quantization Method: awq_marlin vLLM Version: Docker image v0.11.0 GPU: A6000 CUDA Ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ation Method: awq_marlin vLLM Version: Docker image v0.11.0 GPU: A6000 CUDA Version: 12.8 ### 🐛 Describe the bug The AWQ-quantized version of Qwen3-30B-A3B-Instruct-2507 produces non-deterministic outputs across multipl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: AWQ Quantized Model Produces Non-Deterministic Outputs bug ### Your current environment Model: Qwen3-30B-A3B-Instruct-2507-AWQ Quantization Method: awq_marlin vLLM Version: Docker image v0.11.0 GPU: A6000 CUDA Ve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: AWQ Quantized Model Produces Non-Deterministic Outputs bug ### Your current environment Model: Qwen3-30B-A3B-Instruct-2507-AWQ Quantization Method: awq_marlin vLLM Version: Docker image v0.11.0 GPU: A6000 CUDA Ve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
