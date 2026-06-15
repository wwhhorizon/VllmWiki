# 并发下的 KV Cache Identity

状态：reviewed seed page。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)

## 契约

KV cache block 必须只代表它真实对应的 prompt、adapter、model、dtype、layout 和请求状态。并发、offload、prefix sharing、block reuse 或 metadata cleanup 都不能让请求读取到别人的 KV。

## 机制

KV identity 失败通常不是单纯数值误差，而是状态身份错误：

- cache key 缺少 adapter/LoRA/external KV 维度。
- block allocator 重用 block 时没有清理 stale data。
- block table、slot mapping 或 metadata tail 保留旧值。
- CPU offload/restore 或并发 prefill 让 block ownership 混乱。
- prefix cache 的 hybrid group layout 与 first-block key 不一致。

## Curated Case

| Case | 观察 | 优化/修复 |
| --- | --- | --- |
| [#39589](https://github.com/vllm-project/vllm/issues/39589) | variable-length concurrent prefill 下 `temperature=0` 非确定输出 | 直接指向 KV read/write index corruption |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | linked fix | 需要继续抽取 changed metadata 字段 |
| [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069) | LoRA/adapters 影响 K/V 语义 | cache key 必须纳入 adapter identity |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | LoRA/external KV cache identity gap | candidate：需要 source review |
| [#39146](https://github.com/vllm-project/vllm/issues/39146), [#43741](https://github.com/vllm-project/vllm/pull/43741) | recycled block / metadata cleanup 问题 | 清理 stale block 或 tail metadata |
| [#37076](https://github.com/vllm-project/vllm/issues/37076) | 并发或 cache pressure 下错误输出 | candidate：需要链接修复与评论 |

## Fix Pattern

1. 把 cache identity 明确建模：prompt、model、adapter、dtype、layout、backend、cache group。
2. block reuse 前清理 stale data 与 stale metadata。
3. 并发 prefill/decode 中明确 block ownership 与 slot mapping。
4. 对 offload/restore 路径做 exact identity test。
5. 对 LoRA/external KV 场景加入 cross-adapter negative test。

## Open Review Queue

使用 [bitwise_review_queue.csv](../bitwise_review_queue.csv) 中 cluster 为 `kv_identity_concurrency` 的行。
