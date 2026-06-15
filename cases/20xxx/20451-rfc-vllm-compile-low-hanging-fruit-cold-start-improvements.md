# vllm-project/vllm#20451: [RFC]: vLLM-compile low-hanging fruit cold start improvements

| 字段 | 值 |
| --- | --- |
| Issue | [#20451](https://github.com/vllm-project/vllm/issues/20451) |
| 状态 | closed |
| 标签 | RFC;torch.compile;stale;startup-ux |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM-compile low-hanging fruit cold start improvements

### Issue 正文摘录

### Motivation. This issue tracks potential low-hanging fruit for improving vLLM-compile cold start time. @anijain2305, @BoyuanFeng, and I sat down to look at some traces and noticed some things we can improve. There are more longer-term projects for improving torch.compile cold start time, but those will probably take a bit to hit. ### Proposed Change. - [ ] vLLM's [custom bytecode hook](https://github.com/vllm-project/vllm/blob/536fd330036b0406786c847f68e4f67cba06f421/vllm/compilation/wrapper.py#L77-L121) seems to take a long time (~7 seconds on llama-3.1-70b model). I'm not sure how much of this is actually needed for runtime execution. We should guard the decompilation step behind an envvar. If VLLM_COMPILE_DEPYF=0 (default), we write out a `transformed_code.py` that has a comment that says "Please set VLLM_COMPILE_DEPYF=1 to populate this file". - [ ] In llama-3.1-70b, with piecewise cudagraphs, we split a module into 80 different subgraphs. A lot of these subgraphs are literally the same. However, subgraphs 2-79 (approx) are cache-hitting in fx_graph_cache, but they are cache missing in AOTAutogradCache. This needs some more investigation as to why they are cache missing the...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: e subgraphs are literally the same. However, subgraphs 2-79 (approx) are cache-hitting in fx_graph_cache, but they are cache missing in AOTAutogradCache. This needs some more investigation as to why they are cache missi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: E_DEPYF=1 to populate this file". - [ ] In llama-3.1-70b, with piecewise cudagraphs, we split a module into 80 different subgraphs. A lot of these subgraphs are literally the same. However, subgraphs 2-79 (approx) are c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ompilation/wrapper.py#L77-L121) seems to take a long time (~7 seconds on llama-3.1-70b model). I'm not sure how much of this is actually needed for runtime execution. We should guard the decompilation step behind an env...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: vLLM-compile low-hanging fruit cold start improvements RFC;torch.compile;stale;startup-ux ### Motivation. This issue tracks potential low-hanging fruit for improving vLLM-compile cold start time. @anijain2305, @B...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: but really, anytime until these things are fixed. ### CC List. cc @ProExpertProg @youkaichao @WoosukKwon @jamesjwu @zhxchen17 ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
