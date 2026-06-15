# vllm-project/vllm#22983: [Usage]:  vLLM `/score` with Mixedbread reranker (Qwen2 seq-cls override): **scores differ vs local Mixedbread**; small payload = same order/different scores; large payload (\~1K chars/doc) = **order diverges**

| 字段 | 值 |
| --- | --- |
| Issue | [#22983](https://github.com/vllm-project/vllm/issues/22983) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  vLLM `/score` with Mixedbread reranker (Qwen2 seq-cls override): **scores differ vs local Mixedbread**; small payload = same order/different scores; large payload (\~1K chars/doc) = **order diverges**

### Issue 正文摘录

**Title:** vLLM `/score` with Mixedbread reranker (Qwen2 seq-cls override): **scores differ vs local Mixedbread**; small payload = same order/different scores; large payload (\~1K chars/doc) = **order diverges** ### Summary Using vLLM with `hf_overrides` to serve `mixedbread-ai/mxbai-rerank-base-v2` as `Qwen2ForSequenceClassification` and querying `/score`, I observe: * **Scores differ between vLLM and local Mixedbread usage.** * On a **small test**, ranking **matches** Mixedbread, but vLLM probabilities are **much higher on negatives** (calibration mismatch). * On a **larger test** (10 docs, \~1000 chars each), the **ranking order diverges** vs Mixedbread. Looking for guidance on **label tokens**, **pair template**, and any **calibration** needed for parity. ### Environment * Server: **AWS g6e.xlarge** (NVIDIA **L40S 48 GB**) * vLLM command: ```bash vllm serve mixedbread-ai/mxbai-rerank-base-v2 \ --hf_overrides '{"architectures":["Qwen2ForSequenceClassification"],"classifier_from_token":["0","1"],"method":"from_2_way_softmax"}' \ --host 0.0.0.0 --port 8000 ``` * Endpoint: **`/score`** * Reference baseline: `from mxbai_rerank import MxbaiRerankV2` run **locally on Mac M3 Pro (CPU)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: vLLM `/score` with Mixedbread reranker (Qwen2 seq-cls override): **scores differ vs local Mixedbread**; small payload = same order/different scores; large payload (\~1K chars/doc) = **order diverges** usage **T...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ``` * Endpoint: **`/score`** * Reference baseline: `from mxbai_rerank import MxbaiRerankV2` run **locally on Mac M3 Pro (CPU)** ### Repro 1 — Small payload (same order, **different scores**) **Query:** `Who wrote To Kil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eranker (Qwen2 seq-cls override): **scores differ vs local Mixedbread**; small payload = same order/different scores; large payload (\~1K chars/doc) = **order diverges** usage **Title:** vLLM `/score` with Mixedbread re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: *Scores differ between vLLM and local Mixedbread usage.** * On a **small test**, ranking **matches** Mixedbread, but vLLM probabilities are **much higher on negatives** (calibration mismatch). * On a **larger test** (10...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ad, but vLLM probabilities are **much higher on negatives** (calibration mismatch). * On a **larger test** (10 docs, \~1000 chars each), the **ranking order diverges** vs Mixedbread. Looking for guidance on **label toke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
