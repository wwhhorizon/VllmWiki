# Bitwise 下一轮复核队列

状态：active queue。  
作用：记录下一轮要补证的 bitwise/deterministic 工作项。本文只放队列和缺口，不承载最终机制结论；稳定结论应下沉到 [curated/bitwise/](curated/bitwise/)。

## 已完成本轮推进

| Source | 状态 | 本轮结论 |
| --- | --- | --- |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) / [#38938](https://github.com/vllm-project/vllm/pull/38938) | include | 已确认 batch invariance regression 至少包含两个具体机制：`ParallelLMHead` 的 `UnquantizedEmbeddingMethod.apply` 未走 deterministic Triton persistent kernel，以及 SM<90 下 `torch.compile` + CUDA graphs 组合需要边界处理。 |

## Must Review

| Source | 机制 | 当前状态 | 缺口 | 下一步 |
| --- | --- | --- | --- | --- |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | quant/dtype loading identity | defer | 缺 linked fix PR、changed files、maintainer resolution；当前只有 issue body。 | 寻找 `runai_safetensors_weights_iterator`、model loader copy synchronization、shared buffer lifetime 相关 PR。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | external KV / LoRA identity | defer | 已有复现评论，但缺 LMCacheMPConnector key schema fix、adapter identity/version keying patch 和 regression test。 | 继续抓取或等待 linked fix PR；重点看 external KV key 是否纳入 LoRA identity。 |

## Strong Include Needs More Detail

| Source | 机制 | 下一步 |
| --- | --- | --- |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | prefix cache 等价 | 抽取 scheduler split、cache config、e2e test 的 patch 摘要，补充 cache miss/hit verification matrix。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | KV cache identity | 继续细化 `BlockTable` row tail invariant、`move_row`、`clear_row` 的测试边界。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | deterministic reduction | 补充 `splitK=0` scoped fix 的性能/硬件边界，以及上游 CK reduction 未修复前的适用范围。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | verification contract | 抽成 verification matrix：`rtol=0, atol=0`、slot mapping、dtype cache、MHA/GQA、token count。 |

## 不应 Promotion 的情况

- 只有关键词命中，没有 issue/PR 正文或评论证据。
- 只有问题描述，没有 linked fix、patch、maintainer resolution 或复现闭环。
- umbrella issue 没有拆到具体 PR 或具体机制。
- 只能证明 semantic answer 相似，不能证明 token/logprob/tensor/KV identity。
