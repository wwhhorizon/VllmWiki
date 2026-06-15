# vllm-project/vllm#16501: [RFC]: vLLM x torch.compile caching should be opt-out by default

| 字段 | 值 |
| --- | --- |
| Issue | [#16501](https://github.com/vllm-project/vllm/issues/16501) |
| 状态 | closed |
| 标签 | good first issue;RFC;torch.compile |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM x torch.compile caching should be opt-out by default

### Issue 正文摘录

### Motivation. How vLLM decides to cache torch.compile compilations is brittle. There's [a list of configs](https://github.com/vllm-project/vllm/blob/70de35a8816e224663aede45b7f54eef250a5cfe/vllm/compilation/backends.py#L360-L394) that it takes into account and hashes, if any of these configs change then vLLM decides that it needs to do a fresh torch.compile run. As we saw in https://github.com/vllm-project/vllm/pull/16491, it's very easy to add a new feature to one of the configs and forget to update the hash function. In that PR, the problem was that ModelConfig's hash function did not take into account [everything that could change the compilation](https://github.com/vllm-project/vllm/blob/70de35a8816e224663aede45b7f54eef250a5cfe/vllm/config.py#L279-L303). ### Proposed Change. The hash functions are currently opt-in: when someone adds a new feature or does a refactor they may need to add something to the hash functions. After discussion with the PyTorch Compiler team (cc @oulgen), we instead propose changing the hash functions to be opt-out. What that means is that ModelConfig's compute_hash function instead contains a list of fields that it should not include in the hash: ```...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: vLLM x torch.compile caching should be opt-out by default good first issue;RFC;torch.compile ### Motivation. How vLLM decides to cache torch.compile compilations is brittle. There's [a list of configs](https://gi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eriod. EOD Friday, April 18th, 2025. ### CC List. @youkaichao @tlrmchlsmth @mgoin @ProExpertProg @houseroad ### Any Other Things. thank you ### Before submitting a new issue... - [x] Make sure you already searched for r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cides to cache torch.compile compilations is brittle. There's [a list of configs](https://github.com/vllm-project/vllm/blob/70de35a8816e224663aede45b7f54eef250a5cfe/vllm/compilation/backends.py#L360-L394) that it takes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ject/vllm/blob/70de35a8816e224663aede45b7f54eef250a5cfe/vllm/compilation/backends.py#L360-L394) that it takes into account and hashes, if any of these configs change then vLLM decides that it needs to do a fresh torch.c...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ay, April 18th, 2025. ### CC List. @youkaichao @tlrmchlsmth @mgoin @ProExpertProg @houseroad ### Any Other Things. thank you ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
