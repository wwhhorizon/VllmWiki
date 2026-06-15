# vllm-project/vllm#23983: [Installation]: Dependency conflict installing vLLM 0.6.3 due to outlines → pyairports dependency

| 字段 | 值 |
| --- | --- |
| Issue | [#23983](https://github.com/vllm-project/vllm/issues/23983) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Dependency conflict installing vLLM 0.6.3 due to outlines → pyairports dependency

### Issue 正文摘录

### Your current environment Hi, When I try to install vllm==0.6.3, pip fails with a dependency resolution error. The problem seems to be that outlines (versions 0.0.43–0.0.46) depends on pyairports, but pyairports is not available on PyPI, so the installation cannot proceed. Here is the relevant part of the log: ------------------------------------------------------------ ERROR: Cannot install vllm because these package versions have conflicting dependencies. The conflict is caused by: outlines 0.0.46 depends on pyairports outlines 0.0.45 depends on pyairports outlines 0.0.44 depends on pyairports outlines 0.0.43 depends on pyairports To fix this you could try to: 1. loosen the range of package versions you've specified 2. remove package versions to allow pip to attempt to solve the dependency conflict ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts ----------------------------------------------------------------- When I try to install pyairports directly (pip install pyairports), I get the following error: ERROR: Could not find a version that satisfies the requirement pyairports (from versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Dependency conflict installing vLLM 0.6.3 due to outlines → pyairports dependency installation ### Your current environment Hi, When I try to install vllm==0.6.3, pip fails with a dependency resolution e
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 6.3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ct ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts ----------------------------------------------------------------- When I try t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
