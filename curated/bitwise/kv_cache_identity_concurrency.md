# 并发下的 KV Cache Identity

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。  
范围：并发、offload、prefix sharing、LoRA/external KV、block reuse 和 metadata cleanup 下的 KV 身份一致性。

## 问题定义

KV cache block 必须只代表它真实对应的 prompt、token range、model、adapter、dtype、layout、backend、cache group 和请求状态。任何请求读取到其他请求、其他 adapter 或旧生命周期的 KV，都不是数值误差，而是 correctness bug。

## 典型触发条件

- concurrent prefill 中不同 prompt length 复用同一个 persistent row slot。
- block table、slot mapping 或 page indices 的尾部未清理。
- recycled KV block 或 offload/restore 路径保留旧数据。
- LoRA、adapter、external KV cache 的 key 缺少 adapter identity/version。
- prefix sharing 或 LMCache 命中跨越了语义不同的请求状态。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#39589](https://github.com/vllm-project/vllm/issues/39589) | variable-length concurrent prefill 在 `temperature=0` 下产生非确定输出；`VLLM_BATCH_INVARIANT=1`、禁用 prefix cache、已有 recycled-block fix 都不能解释。 | 这是 KV read/write identity 问题。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | PR 修复 `BlockTable` row tail 未清零：row 被较短请求复用或成为 `move_row` target 时，旧 block id 留在 tail；changed files 增加 concurrent prefill determinism test 和 block table unit tests。 | row reuse / `move_row` 必须清理 `num_blocks_per_row` 之外的 tail。 |
| [#39146](https://github.com/vllm-project/vllm/issues/39146), [#43741](https://github.com/vllm-project/vllm/pull/43741) | FullAttentionSpec 的 recycled KV cache blocks 未清零，导致标准 attention 在 `temperature=0` 下非确定。 | block reuse 前必须清理 stale data，不只 Mamba 路径需要 zeroing。 |
| [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069) | LoRA prefix cache hash 使用 `lora_name` 而非全局唯一 `lora_int_id`，同名不同 ID adapter 会错误共享 cache block。 | adapter identity 是 KV cache key 的必填维度。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | LMCache external KV key 包含 base model、token IDs/chunk hashes、token range、rank/world、`cache_salt`，但缺少 LoRA adapter identity/version；adapter B 可能命中 adapter A 的 KV。 | 强 candidate，但缺 linked fix PR，保持 defer。 |

## 根因机制

KV identity 失败通常来自状态身份建模不完整。cache key 少一个维度、metadata tail 没清理、block reuse 没 zero、offload ownership 混淆，都会让下游 attention 读取错误语义的 K/V。由于 KV 会参与后续所有 decode step，这类错误常表现为 nondeterministic token，而不是局部 tensor mismatch。

## 修复方式

1. 显式建模 cache identity：prompt/token range、base model、adapter/LoRA id、dtype、layout、backend、cache group、rank/world、salt。
2. block reuse、row move、offload restore 前后清理 stale block id、stale data 和 metadata tail。
3. 对 concurrent prefill、不同 prompt length、prefix sharing、LoRA 切换、external KV 命中写 negative tests。
4. LMCache/external KV key 若不复用 vLLM 已含 adapter identity 的 block hash，就必须显式纳入 adapter identity/version。

## 验证契约

- metadata 层：block table tail、row move、clear row、append row 必须有 unit tests。
- 系统层：concurrent variable-length prefill 在 `temperature=0` 下输出 token 稳定。
- adapter 层：同 base model、同 token、不同 LoRA/adapters 不能共享 KV 命中。
- KV identity 测试优先使用 exact equality 或 token equality，不能只用宽松 `allclose`。

## 适用边界

- [#39591](https://github.com/vllm-project/vllm/pull/39591) 直接覆盖 V1 + FlashInfer + variable-length concurrent prefill 的 row tail 问题；其他 backend 仍需复核相同 metadata invariant。
- [#44250](https://github.com/vllm-project/vllm/issues/44250) 目前只有问题描述和少量讨论，不能作为已修复结论。
- LoRA identity 与 external KV identity 应同时检查本地 cache key 和远端/cache connector key。

## 仍需补证

- 继续等待或寻找 `#44250` 的 linked fix PR、LMCache key schema patch 和 regression test。
- 复核 external KV cache 与 LoRA/adapter version 的边界：adapter reload、同名不同 ID、cache_salt 复用、multi-rank chunk hash。
