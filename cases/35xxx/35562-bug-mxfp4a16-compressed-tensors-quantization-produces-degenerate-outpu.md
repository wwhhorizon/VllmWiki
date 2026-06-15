# vllm-project/vllm#35562: [Bug]: MXFP4A16 compressed-tensors quantization produces degenerate output (PPL 22,953 vs 8.74 BF16)

| 字段 | 值 |
| --- | --- |
| Issue | [#35562](https://github.com/vllm-project/vllm/issues/35562) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;gemm_linear;model_support;moe;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MXFP4A16 compressed-tensors quantization produces degenerate output (PPL 22,953 vs 8.74 BF16)

### Issue 正文摘录

### Your current environment - vLLM: v0.16.0 (also reproduced on v0.15.1) - llm-compressor: 0.9.0.2 - compressed-tensors: 0.13.0 (bundled with vLLM v0.16.0) - Model: Qwen/Qwen3-30B-A3B (MoE, 128 experts, 30B total / 3B active) - GPUs tested: 2x NVIDIA RTX 5880 Ada (SM89), NVIDIA B200 (SM100) - Docker image: vllm/vllm-openai:v0.16.0 ### 🐛 Describe the bug single-word loops and WikiText-2 perplexity of **22,953** (vs 8.74 BF16 baseline, a 262,000% regression). The `NVFP4A16` preset (same RTN weight-only approach, same model, same serving path through Marlin) works correctly with PPL 9.02 (+3.2%). This is not a quantization quality issue — a 262,000% PPL regression from weight-only RTN is impossible from quantization error alone. This points to a bug in the Marlin MXFP4 dequantization kernel or the compressed-tensors MXFP4 weight packing/preparation code. ## Reproduction ### Minimal reproducer ```python """Run inside vllm/vllm-openai:v0.16.0 container. pip install --no-deps llmcompressor==0.9.0.2 """ from llmcompressor import oneshot from llmcompressor.modifiers.quantization import QuantizationModifier from vllm import LLM, SamplingParams MODEL_ID = "Qwen/Qwen3-30B-A3B" OUTPUT_DIR =...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: [Bug]: MXFP4A16 compressed-tensors quantization produces degenerate output (PPL 22,953 vs 8.74 BF16) bug;stale ### Your current environment - vLLM: v0.16.0 (also reproduced on v0.15.1) - llm-compressor: 0.9.0.2 - compres
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: - GPUs tested: 2x NVIDIA RTX 5880 Ada (SM89), NVIDIA B200 (SM100) - Docker image: vllm/vllm-openai:v0.16.0 ### 🐛 Describe the bug single-word loops and WikiText-2 perplexity of **22,953** (vs 8.74 BF16 baseline, a 262,0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: A3B (MoE, 128 experts, 30B total / 3B active) - GPUs tested: 2x NVIDIA RTX 5880 Ada (SM89), NVIDIA B200 (SM100) - Docker image: vllm/vllm-openai:v0.16.0 ### 🐛 Describe the bug single-word loops and WikiText-2 perplexity...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nsors: 0.13.0 (bundled with vLLM v0.16.0) - Model: Qwen/Qwen3-30B-A3B (MoE, 128 experts, 30B total / 3B active) - GPUs tested: 2x NVIDIA RTX 5880 Ada (SM89), NVIDIA B200 (SM100) - Docker image: vllm/vllm-openai:v0.16.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : 0.9.0.2 - compressed-tensors: 0.13.0 (bundled with vLLM v0.16.0) - Model: Qwen/Qwen3-30B-A3B (MoE, 128 experts, 30B total / 3B active) - GPUs tested: 2x NVIDIA RTX 5880 Ada (SM89), NVIDIA B200 (SM100) - Docker image:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
