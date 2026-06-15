# vllm-project/vllm#26201: [Tracking Issue]: Prefix Caching for Hybrid Models

| 字段 | 值 |
| --- | --- |
| Issue | [#26201](https://github.com/vllm-project/vllm/issues/26201) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking Issue]: Prefix Caching for Hybrid Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This issue is meant to track follow-up work items for the [Mamba2 Automatic Prefix Caching](https://github.com/vllm-project/vllm/pull/25752). Below is a non-exhaustive list of already identified work items: - [x] Address some comments leftover from review (#26222) - [ ] Implement policy for freeing mamba blocks to fix performance in throughput benchmarks - [ ] Relax constraint that mamba block size must be multiple of chunk size - [x] Give user flexibility to set mamba caching granularity (https://github.com/vllm-project/vllm/pull/27289) - [ ] Support mamba prefix caching and spec decode - [ ] Fuse logic for SSM state writing into kernels (https://github.com/vllm-project/vllm/pull/26235) - [ ] Test TP>1 behaviour - [ ] Cache meta-data builds across KV cache groups (https://github.com/vllm-project/vllm/pull/22788) - [ ] Additional cleanup in causal_conv1d kernels (e.g., strip out unused logic) - [x] Enable prefix caching for Mamba1 (https://github.com/vllm-project/vllm/pull/26377) - [ ] Enable prefix caching for ShortConv - [ ] Enable prefix caching for LinearAttention - [ ] Enable prefix caching for GDN (https://github.com/vllm-project/vllm/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Tracking Issue]: Prefix Caching for Hybrid Models feature request ### 🚀 The feature, motivation and pitch This issue is meant to track follow-up work items for the [Mamba2 Automatic Prefix Caching](https://github.com/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 2) - [ ] Implement policy for freeing mamba blocks to fix performance in throughput benchmarks - [ ] Relax constraint that mamba block size must be multiple of chunk size - [x] Give user flexibility to set mamba caching...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - [ ] Support mamba prefix caching and spec decode - [ ] Fuse logic for SSM state writing into kernels (https://github.com/vllm-project/vllm/pull/26235) - [ ] Test TP>1 behaviour - [ ] Cache meta-data builds across KV c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s leftover from review (#26222) - [ ] Implement policy for freeing mamba blocks to fix performance in throughput benchmarks - [ ] Relax constraint that mamba block size must be multiple of chunk size - [x] Give user fle...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: project/vllm/pull/26235) - [ ] Test TP>1 behaviour - [ ] Cache meta-data builds across KV cache groups (https://github.com/vllm-project/vllm/pull/22788) - [ ] Additional cleanup in causal_conv1d kernels (e.g., strip out...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
