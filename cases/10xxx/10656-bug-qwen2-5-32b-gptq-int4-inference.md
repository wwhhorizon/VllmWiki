# vllm-project/vllm#10656: [Bug]: Qwen2.5-32B-GPTQ-Int4 inference `!!!!!`

| 字段 | 值 |
| --- | --- |
| Issue | [#10656](https://github.com/vllm-project/vllm/issues/10656) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | kernel;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-32B-GPTQ-Int4 inference `!!!!!`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We have been receiving reports that the 4-bit GPTQ version of Qwen2.5-32B-Instruct cannot be used with `vllm`. The generation only contains `!!!!!`. However, it was also reported that the same model worked using `transformers` and `auto_gptq`. Here are some related issues: - https://github.com/QwenLM/Qwen2.5/issues/945 (v0.6.1.post2, v0.6.2, v0.6.3) - https://github.com/QwenLM/Qwen2.5/issues/1103 (v0.6.1) - https://github.com/QwenLM/Qwen2.5/issues/1038 (v0.4.2, v0.5.1) We attempted to reproduce the issue, which appears related to quantization kernels, and the following is a summary: - `gptq_marlin` works - `gptq` fails for requests with `len(prompt_token_ids)<=50` but works for longer input sequences The results are consistent for - `tensor-parallel-size`: 2, 4, 8 - `vllm` versions: v0.6.1.post2, v0.6.2, v0.6.3.post1, v0.6.4.post1 - nvidia driver versions: 535.183.06, 560.35.05 As `gptq_marlin` is not available for turing and volta cards, we are not able to find a workaround for those users. It would help a lot if one could help investigate the issue. ### Before submitting a new issue... - [X]...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen2.5-32B-GPTQ-Int4 inference `!!!!!` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We have been receiving reports that the 4-bit GPTQ version of Qwen2.5-32B-Instru...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: # 🐛 Describe the bug We have been receiving reports that the 4-bit GPTQ version of Qwen2.5-32B-Instruct cannot be used with `vllm`. The generation only contains `!!!!!`. However, it was also reported that the same model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5-32B-GPTQ-Int4 inference `!!!!!` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We have been receiving reports that the 4-bit GPTQ version of Qwen2.5-32B-Instruc
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /github.com/QwenLM/Qwen2.5/issues/1038 (v0.4.2, v0.5.1) We attempted to reproduce the issue, which appears related to quantization kernels, and the following is a summary: - `gptq_marlin` works - `gptq` fails for reques...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
