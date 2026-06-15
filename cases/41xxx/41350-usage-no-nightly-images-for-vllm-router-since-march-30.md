# vllm-project/vllm#41350: [Usage]: no nightly images for vllm-router since March 30

| 字段 | 值 |
| --- | --- |
| Issue | [#41350](https://github.com/vllm-project/vllm/issues/41350) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: no nightly images for vllm-router since March 30

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to run the latest vllm-router using docker, for productivity and reproducibility. On https://hub.docker.com/r/vllm/vllm-router/tags the last published nightly was [nightly-20260330-4f56d66](https://hub.docker.com/layers/vllm/vllm-router/nightly-20260330-4f56d66/images/sha256-36ad05a77e37a4bb24b82fa1bfbd7791e028d4c7f6d32c2112a597d95fbb1087) (one month old) and the unpinned nightly-x86_64 image. I would like to use the cutting-edge version of the router. Is this expected? If it is, what is the recommended way to get official nightly release of the router? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d you like to use vllm I would like to run the latest vllm-router using docker, for productivity and reproducibility. On https://hub.docker.com/r/vllm/vllm-router/tags the last published nightly was [nightly-20260330-4f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: no nightly images for vllm-router since March 30 usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to run the latest vllm-route...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: no nightly images for vllm-router since March 30 usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to run the latest vllm-route...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: v.py` ``` ### How would you like to use vllm I would like to run the latest vllm-router using docker, for productivity and reproducibility. On https://hub.docker.com/r/vllm/vllm-router/tags the last published nightly wa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
