# vllm-project/vllm#26203: [Bug]: Missing Sink Tensor in Flash Attention Cascade Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#26203](https://github.com/vllm-project/vllm/issues/26203) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing Sink Tensor in Flash Attention Cascade Attention

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We noticed a 10% decline in the [MMLU‑Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) score for the [GPT‑OSS 20B](https://huggingface.co/openai/gpt-oss-20b) model, dropping from 0.68 to 0.58 when prefix caching was enabled. After a thorough investigation, we discovered that the [cascade‑attention implementation omitted the sink tensor](https://github.com/vllm-project/vllm/blob/v0.10.2/vllm/v1/attention/backends/flash_attn.py#L795), leading to numerical instability. This sink tensor is crucial for models like GPT‑OSS that use hybrid attention with a sliding‑window component. In contrast, [non‑cascade attention correctly includes the sink tensor ](https://github.com/vllm-project/vllm/blob/v0.10.2/vllm/v1/attention/backends/flash_attn.py#L552)and does not suffer from the score drop. By incorporating the sink tensor into the cascade‑attention code and re‑running the MMLU‑Pro evaluation, the issue was resolved To replicate the problem, enable cascade attention and execute the following query from the MMLU‑Pro dataset. You can force cascade attention by modifying the [use_cascade_attention function](https://github.com/vllm-pro...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Missing Sink Tensor in Flash Attention Cascade Attention bug ### Your current environment ### 🐛 Describe the bug We noticed a 10% decline in the [MMLU‑Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) scor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _attn.py#L795), leading to numerical instability. This sink tensor is crucial for models like GPT‑OSS that use hybrid attention with a sliding‑window component. In contrast, [non‑cascade attention correctly includes the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hat the law is based on what is \"correct.\"\nOptions:\nA. Legal Pragmatism\nB. Legal Formalism\nC. Comparative\nD. Analytical\nE. Sociological\nF. Historical\nG. Critical Legal Studies\nH. Realist\nI. Positivist\nJ. Na...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # 🐛 Describe the bug We noticed a 10% decline in the [MMLU‑Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) score for the [GPT‑OSS 20B](https://huggingface.co/openai/gpt-oss-20b) model, dropping from 0.68 to 0.5...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: /blob/v0.10.2/vllm/v1/attention/backends/flash_attn.py#L795), leading to numerical instability. This sink tensor is crucial for models like GPT‑OSS that use hybrid attention with a sliding‑window component. In contrast,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
