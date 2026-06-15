# vllm-project/vllm#712: Potential degredation in sampling/too repetitive

| 字段 | 值 |
| --- | --- |
| Issue | [#712](https://github.com/vllm-project/vllm/issues/712) |
| 状态 | closed |
| 标签 |  |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cuda;kernel;sampling |
| 症状 | nondeterministic |
| 根因提示 | memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Potential degredation in sampling/too repetitive

### Issue 正文摘录

### Moving from Discussions https://github.com/vllm-project/vllm/discussions/471 Hi guys, great work! I have been experimenting with the library for several weeks, and immediately noticed that sampled tokens (with the same temperature and such) are significantly more deterministic with Vllm vs. HF Transformers using the same models - with temperature lower than 0.7, often the first 5-10 sampled tokens are exactly same across few different generations, even recreating the original text in the datasets verbatim, like there is some greedy decoding going on (when it is not). This unfortunately leads to a significant repetition issue I've never seen with HF. The issue is not related to special tokens such as ` `. I modified vllm so that it never generates those special tokens like HF's bad_words_ids, but the issue persists (those special tokens will also make the inference quality significantly worse especially with non-chat prompts, but it is a different issue). In the mean time, I have also been checking and modifying codebase to see if there is any discrepancy between the sampling process, but I am not sure about the difference. I'm suspecting either cuda kernels or partitioning/blo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: temperature and such) are significantly more deterministic with Vllm vs. HF Transformers using the same models - with temperature lower than 0.7, often the first 5-10 sampled tokens are exactly same across few different...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: mpled tokens (with the same temperature and such) are significantly more deterministic with Vllm vs. HF Transformers using the same models - with temperature lower than 0.7, often the first 5-10 sampled tokens are exact...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g process, but I am not sure about the difference. I'm suspecting either cuda kernels or partitioning/block in PagedAttention. https://github.com/vllm-project/vllm/issues/590: Related topic with actual examples. The top...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: about the difference. I'm suspecting either cuda kernels or partitioning/block in PagedAttention. https://github.com/vllm-project/vllm/issues/590: Related topic with actual examples. The topic is about GPTJ, but the iss...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: epetition issue I've never seen with HF. The issue is not related to special tokens such as ` `. I modified vllm so that it never generates those special tokens like HF's bad_words_ids, but the issue persists (those spe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
