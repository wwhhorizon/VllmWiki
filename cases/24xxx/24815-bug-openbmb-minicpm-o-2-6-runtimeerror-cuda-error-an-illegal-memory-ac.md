# vllm-project/vllm#24815: [Bug]: openbmb/MiniCPM-o-2_6  RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#24815](https://github.com/vllm-project/vllm/issues/24815) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openbmb/MiniCPM-o-2_6  RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA error: an illegal memory access was encountered when using vLLM to deploy openbmb/MiniCPM-o-2_6. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n answer lots of frequently asked questions. correctness activation_norm;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization activation;cuda;kernel;quantization build_error;crash;mismatc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: openbmb/MiniCPM-o-2_6 RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug CUDA error: an illegal memory access was encountered when usi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: . correctness activation_norm;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization activation;cuda;kernel;quantization build_error;crash;mismatch dtype;env_dependency Your current environ...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization activation;cuda;kernel;quantization build_error;crash;mismatch dtype;env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: l_vlm;quantization activation;cuda;kernel;quantization build_error;crash;mismatch dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
