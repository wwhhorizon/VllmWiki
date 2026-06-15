# vllm-project/vllm#43545: [RFC]: Add Gumiho speculative decoding to vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#43545](https://github.com/vllm-project/vllm/issues/43545) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;operator;sampling |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add Gumiho speculative decoding to vLLM

### Issue 正文摘录

### Motivation. ## Motivation. [Gumiho](https://arxiv.org/abs/2503.10135) (ICML 2025) is a hybrid speculative decoding drafter: 1. The first two speculative tokens are produced autoregressively by an EAGLE-style transformer head. 2. Every additional speculative token is produced **in parallel** by per-step MLP heads conditioned on the embeddings and hidden states of the first two draft tokens. The motivation is that **early speculative tokens matter more than late ones**. Each accepted prefix token unlocks all later tokens in the same draft, so allocating more compute to the first two positions (a small but high-quality transformer head) and amortising the rest with cheap parallel MLP heads yields a better acceptance-rate / drafter-latency trade-off than either a pure EAGLE drafter (all transformer, sequential) or a pure MLPSpeculator drafter (all MLP, parallel but lower quality). Concretely, this means a lower per-step drafter latency than EAGLE/EAGLE3 when `num_speculative_tokens > 2`, with similar end-to-end accepted-token gains. We have a working ROCm prototype on top of vLLM v0.16.0 and have already ported it to current `main` with all CI hygiene applied; the changes are smal...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: github.com/vllm-project/vllm/pull/43544 ### Surface ```python LLM( model="meta-llama/Meta-Llama-3-8B-Instruct", speculative_config={ "method": "gumiho", "model": "amd/Gumiho-llama3-8b", "num_speculative_tokens": 3, "dra...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: with cheap parallel MLP heads yields a better acceptance-rate / drafter-latency trade-off than either a pure EAGLE drafter (all transformer, sequential) or a pure MLPSpeculator drafter (all MLP, parallel but lower quali...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: op of vLLM v0.16.0 and have already ported it to current `main` with all CI hygiene applied; the changes are small and contained. ## Proposed Change. Add `"method": "gumiho"` as a new V1 speculative decoding method. htt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the same draft, so allocating more compute to the first two positions (a small but high-quality transformer head) and amortising the rest with cheap parallel MLP heads yields a better acceptance-rate / drafter-latency t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Add Gumiho speculative decoding to vLLM RFC ### Motivation. ## Motivation. [Gumiho](https://arxiv.org/abs/2503.10135) (ICML 2025) is a hybrid speculative decoding drafter: 1. The first two speculative tokens are...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
