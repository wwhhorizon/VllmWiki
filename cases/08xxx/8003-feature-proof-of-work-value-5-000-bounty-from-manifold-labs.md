# vllm-project/vllm#8003: [Feature]: Proof of Work value ($5,000 Bounty) from Manifold Labs

| 字段 | 值 |
| --- | --- |
| Issue | [#8003](https://github.com/vllm-project/vllm/issues/8003) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | quantization;sampling |
| 症状 | nondeterministic |
| 根因提示 | memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Proof of Work value ($5,000 Bounty) from Manifold Labs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Background We design incentive algorithms for people to run LLM's. We have absolutely no control of who runs or how these llms are run (to the extent that they pass a verification system, the goal of this bounty). All we know is an ip address for a person running a model. These are called miners. On the other side are validators, each run by some team. Our company purely controls what code these validators run and how miners are scored, although we don't have access to these validators themselves. Validators will query 28 miners (total ~230ish) at a time and score their responses continuously in order to ensure miners are running the right model. Miners receive two types of requests, organic and challenge requests. These semi-indistinguishable from one another (the goal is for them to be completely indistinguishable), and for these organics to possibly be scored later on. All queries, organic and non, are saved to a database with virtually all their data. Miners are highly incentivized to cheat and keep their costs down while maximizing their profits. Since LLMs are non-deterministic in nature (even at zero temp) due to rounding errors in fl...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: and keep their costs down while maximizing their profits. Since LLMs are non-deterministic in nature (even at zero temp) due to rounding errors in floating point math from shared memory access during parallel processing...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: uery wont be scored. If we only use queries with 0 temp, miners can just block any organic request. What we want: A proof of work value (PoWv) per token (int, hexadec, string, hash, float, etc) that can only be generate...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oal of this bounty). All we know is an ip address for a person running a model. These are called miners. On the other side are validators, each run by some team. Our company purely controls what code these validators ru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: keep their costs down while maximizing their profits. Since LLMs are non-deterministic in nature (even at zero temp) due to rounding errors in floating point math from shared memory access during parallel processing, it...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oal **IS NOT** to have miners run models that give better answers. We specifically want to verify miners are running the exact model they claim they are running. Validators want to be able to sell their bandwidth to min...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
