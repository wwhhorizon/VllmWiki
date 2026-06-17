# 并发下的 KV Cache Identity

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。

## 契约

KV cache block 必须只代表它真实对应的 prompt、token range、model、adapter、dtype、layout、backend、cache group 和请求状态。并发、offload、prefix sharing、block reuse 或 metadata cleanup 都不能让请求读取到其他请求、其他 adapter 或旧生命周期的 KV。

## 机制

KV identity 失败不是“浮点误差”，而是状态身份错误。常见路径包括：cache key 缺少 LoRA/external KV 维度；block table 或 slot mapping 尾部保留旧 block id；recycled block 未清零；CPU offload/restore 混淆 ownership；并发 prefill 复用 row slot 时没有清理 metadata。

## Source Evidence

| Source | 证据 | 炼化结论 |
| --- | --- | --- |
| [#39589](https://github.com/vllm-project/vllm/issues/39589) | variable-length concurrent prefill 在 `temperature=0` 下产生非确定输出；`VLLM_BATCH_INVARIANT=1`、禁用 prefix cache、已有 recycled-block fix 都不能解释。 | 这是 KV read/write identity 问题。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | PR 明确修复 `BlockTable` row tail 未清零，stale block id 会让 FlashInfer page-indices kernel 读取其他请求 KV；新增 concurrent prefill determinism 和 block table unit tests。 | row reuse / `move_row` 必须清理 `num_blocks_per_row` 之外的 tail。 |
| [#39146](https://github.com/vllm-project/vllm/issues/39146), [#43741](https://github.com/vllm-project/vllm/pull/43741) | FullAttentionSpec 的 recycled KV cache blocks 未清零，导致标准 attention 在 `temperature=0` 下非确定。PR 修正 zeroing gate 和 manager 类型判断。 | block reuse 前必须清理 stale data，不只 Mamba 路径需要 zeroing。 |
| [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069) | LoRA prefix cache hash 使用 `lora_name` 而非全局唯一 `lora_int_id`，同名不同 ID adapter 会错误共享 cache block。 | adapter identity 是 KV cache key 的必填维度。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | LMCache external KV key 缺少 LoRA identity，可能让 adapter B 命中 adapter A 生成的 K/V。 | 强 candidate，仍缺 linked fix PR，保持 defer。 |

## Fix Pattern

1. 显式建模 cache identity：prompt/token range、base model、adapter/LoRA id、dtype、layout、backend、cache group、rank/world、salt。
2. block reuse、row move、offload restore 前后清理 stale block id、stale data 和 metadata tail。
3. 对 concurrent prefill、不同 prompt length、prefix sharing、LoRA 切换、external KV 命中写 negative tests。
4. KV identity 测试优先使用 exact equality 或 token equality；不能只用宽松 `allclose`。
5. 对候选问题区分“KV 读错对象”和“backend math drift”，两者修复手段不同。

## Open Review Queue

下一轮优先复核 `#44250` 的 linked fix、LMCache key schema、以及 external KV cache 与 LoRA/adapter version 的边界。
