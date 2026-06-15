# vllm-project/vllm#20186: [Bug]: [V1] DeepSeek MTP is broken after #20022

| 字段 | 值 |
| --- | --- |
| Issue | [#20186](https://github.com/vllm-project/vllm/issues/20186) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1] DeepSeek MTP is broken after #20022

### Issue 正文摘录

> Something has changed since the working commit (0.9.2.dev223+gee5ad8d2c plus my PR). I can reproduce the same gibberish on 0.9.2.dev283+ge9fd658af even without the full cudagraph compile option. > > After bisecting [the commits from what I have worked on for the fix to what the PR has been merged](https://github.com/vllm-project/vllm/compare/ee5ad8d..8359f4c), it seems #19717 breaks MTP. > > -------- > > As a reproducer, what I have checked is as follows: > > For the commits which [merges #19717](https://github.com/vllm-project/vllm/commit/015fab8c2fa4db8776f7e91abd50371911673d88) and [just before it](https://github.com/vllm-project/vllm/commit/f59fc60fb317e7e04456de50b7abce99a9017225), apply the diffs at #20022 and run the test script. > > Then for f59fc60 MTP works normal and the draft acceptance rate in the log is about ~80%. For 015fab8 however, model output is a total gibberish and the draft acceptance rate is almost 0. > > -------- > > It seems like #19717 changes the forward pass of MTP module from FlashMLA to FusedMoE where it shouldn't. cc @bnellnm , it would be helpful if you can shed some light on what is going wrong. _Originally posted by @cjackal in [#20021](https:/...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ged since the working commit (0.9.2.dev223+gee5ad8d2c plus my PR). I can reproduce the same gibberish on 0.9.2.dev283+ge9fd658af even without the full cudagraph compile option. > > After bisecting [the commits from what...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ame gibberish on 0.9.2.dev283+ge9fd658af even without the full cudagraph compile option. > > After bisecting [the commits from what I have worked on for the fix to what the PR has been merged](https://github.com/vllm-pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: duce the same gibberish on 0.9.2.dev283+ge9fd658af even without the full cudagraph compile option. > > After bisecting [the commits from what I have worked on for the fix to what the PR has been merged](https://github.c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: the draft acceptance rate in the log is about ~80%. For 015fab8 however, model output is a total gibberish and the draft acceptance rate is almost 0. > > -------- > > It seems like #19717 changes the forward pass of MTP...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: like #19717 changes the forward pass of MTP module from FlashMLA to FusedMoE where it shouldn't. cc @bnellnm , it would be helpful if you can shed some light on what is going wrong. _Originally posted by @cjackal in [#2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
