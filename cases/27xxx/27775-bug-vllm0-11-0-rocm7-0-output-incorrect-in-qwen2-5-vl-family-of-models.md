# vllm-project/vllm#27775: [Bug]: VLLM0.11.0+Rocm7.0 output incorrect in Qwen2.5-VL family of models when `--enforce-eager` True

| 字段 | 值 |
| --- | --- |
| Issue | [#27775](https://github.com/vllm-project/vllm/issues/27775) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM0.11.0+Rocm7.0 output incorrect in Qwen2.5-VL family of models when `--enforce-eager` True

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With Qwen2.5-VL family of models on vllm0.11.0 release, when --enforce-eager is true (disable cuda graph capture) the LLM output is inaccurate (language mixing, only 1-2 tokens generated). This issue is not seen in vllm0.9.2, vllm0.10.1 and vllm0.10.2. The same error is apparent across multiple quantization schemes/model sizes, but running a non-VL model (such as Qwen2.5-3B-Instruct) yields good accuracy. Suspect the issue has to do with torch.compile specific to qwen2.5_vl architecture. Models observed with error in question - Qwen/Qwen2.5-VL-3B-Instruct-AWQ - Qwen/Qwen2.5-VL-7B-Instruct-AWQ - RedHatAI/Qwen2.5-VL-7B-Instruct-quantized.w4a16 - etc.. When --enforce-eager is enabled, the output often is incorrectly in Chinese and only includes 1-2 tokens, even though we set `--override-generation-config.max_new_tokens 30`. With --enforce-eager disabled (e.g. cuda graph is captured), the output from LLM is correct. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: B-Instruct) yields good accuracy. Suspect the issue has to do with torch.compile specific to qwen2.5_vl architecture. Models observed with error in question - Qwen/Qwen2.5-VL-3B-Instruct-AWQ - Qwen/Qwen2.5-VL-7B-Instruc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: VLLM0.11.0+Rocm7.0 output incorrect in Qwen2.5-VL family of models when `--enforce-eager` True bug;rocm ### Your current environment ### 🐛 Describe the bug With Qwen2.5-VL family of models on vllm0.11.0 release,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: VLLM0.11.0+Rocm7.0 output incorrect in Qwen2.5-VL family of models when `--enforce-eager` True bug;rocm ### Your current environment ### 🐛 Describe the bug With Qwen2.5-VL family of models on vllm0.11.0 release,...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: es, but running a non-VL model (such as Qwen2.5-3B-Instruct) yields good accuracy. Suspect the issue has to do with torch.compile specific to qwen2.5_vl architecture. Models observed with error in question - Qwen/Qwen2....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: es, but running a non-VL model (such as Qwen2.5-3B-Instruct) yields good accuracy. Suspect the issue has to do with torch.compile specific to qwen2.5_vl architecture. Models observed with error in question - Qwen/Qwen2....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
