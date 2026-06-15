# vllm-project/vllm#43996: [Bug]: [PD + SpecDec] Prefix-cache trimming drops wrong block when P has extra lookahead block

| 字段 | 值 |
| --- | --- |
| Issue | [#43996](https://github.com/vllm-project/vllm/issues/43996) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [PD + SpecDec] Prefix-cache trimming drops wrong block when P has extra lookahead block

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Chatting with @benchislett re: #43733, we realized the original workaround introduced for PD (#22317) can cause similar silent KV Cache corruption issues. When P/D disaggregation is used with speculative decoding (EAGLE), the effective_lookahead_tokens workaround ([scheduler.py:L700-707](https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/sched/scheduler.py#L700-L707)) only zeroes lookahead on D (gated by load_kv_async). P keeps its full num_lookahead_tokens, so at block boundaries P allocates one more block than D. The connector's prefix-cache trimming then drops the first data block instead of the extra lookahead block at the end. Example block_size=16, num_prompt_tokens=16, P has num_lookahead_tokens=1: P allocates ceil(17/16) = 2 blocks: [b0, b1] b0: KV for tokens 0-15 (prompt data) b1: KV for token 16 (lookahead / draft) D allocates ceil(16/16) = 1 block: [a0] _apply_prefix_caching ([worker.py:L2312-2316](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/nixl/worker.py#L2312-L2316)) sees 1 local D's a0 (should hold KV for tokens 0-15) D ends up with the wrong data: KV for a s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: silent KV Cache corruption issues. When P/D disaggregation is used with speculative decoding (EAGLE), the effective_lookahead_tokens workaround ([scheduler.py:L700-707](https://github.com/vllm-project/vllm/blob/main/vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: addressed by something like #39266). ## Proposed fix I believe the specialized logic above introduces unnecessary complexity that we should address from a design prospective. Therefore I propose the following - Introduc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: er we're prefilling or decoding with current instance in a PD setup from config - skip sampling from draft model entirely on P and set `num_lookahead_tokens=0` on P; no extra lookahead_tokens are ever allocated on P. -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ock boundary**, causing the lookahead to spill into an extra block. Most test prompts don't hit this alignment. Additionally, P wastes compute on drafter prefill + sampling + drafting that D discards entirely (to be add...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ps) . Current fixed version https://github.com/vllm-project/vllm/blob/11dfa3169d16b85adf74f7a9fc386b50b67bc732/vllm/v1/core/sched/scheduler.py#L710 already accounts for this (and currently handles loading in chunks). Ot...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
