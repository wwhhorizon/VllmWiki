# vllm-project/vllm#32534: [Bug]: Olmo-3 does not call tools even with auto tool choice enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#32534](https://github.com/vllm-project/vllm/issues/32534) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Olmo-3 does not call tools even with auto tool choice enabled

### Issue 正文摘录

### Your current environment ## Environment / Docker image The issue occurs when running vLLM inside the following Docker image: Image: lmcache/vllm-openai:build-latest ### Relevant characteristics - Base OS: Ubuntu 24.04 - Python: 3.12 - CUDA: 12.8.1 - Driver compatibility: 570.124.06 - NCCL: 2.25.1 - cuDNN: 9.8.0 - TensorRT: 10.9.0 - vLLM: nightly (built from source via build.txt) - Architecture: amd64 - NVIDIA_VISIBLE_DEVICES=all - TORCH_CUDA_ARCH_LIST=10.0+PTX 12.0+PTX ### 🐛 Describe the bug ## 🐛 Describe the bug When serving Olmo-3.1-32B via vLLM, the model never emits structured tool calls, even when tool calling is explicitly enabled. Instead of returning a tool invocation compatible with the `olmo3` tool call parser, the model produces only natural-language reasoning describing how it would call a tool. As a result, vLLM never triggers any tool execution, even though the model otherwise generates correct text responses and does not crash or error. The model is served using the following command: vllm serve cyankiwi/Olmo-3.1-32B-Think-AWQ-4bit \ --port 8000 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --max-model-len 80000 \ --tool-call-parser olmo3 \ --enabl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: choice enabled bug;stale ### Your current environment ## Environment / Docker image The issue occurs when running vLLM inside the following Docker image: Image: lmcache/vllm-openai:build-latest ### Relevant characterist...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Relevant characteristics - Base OS: Ubuntu 24.04 - Python: 3.12 - CUDA: 12.8.1 - Driver compatibility: 570.124.06 - NCCL: 2.25.1 - cuDNN: 9.8.0 - TensorRT: 10.9.0 - vLLM: nightly (built from source via build.txt) -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: asked to do so via VLLM website to tool calling) A minimal example that reproduces the issue is the prompt: write file A.txt in root. The observed output consists only of free-form reasoning text such as “Okay, the user...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the bug ## 🐛 Describe the bug When serving Olmo-3.1-32B via vLLM, the model never emits structured tool calls, even when tool calling is explicitly enabled. Instead of returning a tool invocation compatible with the `ol...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;model_support;quantization cuda;quantization build_error;crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
