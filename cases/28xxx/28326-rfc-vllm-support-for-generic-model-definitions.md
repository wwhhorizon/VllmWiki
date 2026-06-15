# vllm-project/vllm#28326: [RFC]: vLLM Support for Generic Model Definitions

| 字段 | 值 |
| --- | --- |
| Issue | [#28326](https://github.com/vllm-project/vllm/issues/28326) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM Support for Generic Model Definitions

### Issue 正文摘录

### Motivation. As users experiment with model architectures they often need a fast inference path to explore post-training (with reinforcement learning). Since training in this domain is inference dominated, vLLM should increase support for research by providing utilities to construct fast-inference models directly from training code with low cognitive overhead. Recent exploration in [bitwise-exact reinforcement learning](https://github.com/pytorch/torchtitan/tree/main/torchtitan/experiments/deterministic_vllm_rl) with vLLM has shown that leveraging the features of vLLM are crucial to ensure stability in training runs. Further, vLLM is already used in many RL frameworks (such as VERL and TorchForge), and by simplifying integration, we can continue to help grow the vLLM impact and community. ### Proposed Change. The goal is to support generic training/etc. ⇔ inference compatibility. We propose a formal **specification** and **helper utilities** for use of `ModelRegistry.register_model` with training and other workloads. - A specification of the minimum set of features needed to use vLLM with a user-defined model - A wrapper that will enable simplistic “training-only” model specifi...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: from training code with low cognitive overhead. Recent exploration in [bitwise-exact reinforcement learning](https://github.com/pytorch/torchtitan/tree/main/torchtitan/experiments/deterministic_vllm_rl) with vLLM has sh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el Definitions RFC;stale ### Motivation. As users experiment with model architectures they often need a fast inference path to explore post-training (with reinforcement learning). Since training in this domain is infere...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: vLLM Support for Generic Model Definitions RFC;stale ### Motivation. As users experiment with model architectures they often need a fast inference path to explore post-training (with reinforcement learning). Sinc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ](https://github.com/pytorch/torchtitan/tree/main/torchtitan/experiments/deterministic_vllm_rl) with vLLM has shown that leveraging the features of vLLM are crucial to ensure stability in training runs. Further, vLLM is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm_rl) with vLLM has shown that leveraging the features of vLLM are crucial to ensure stability in training runs. Further, vLLM is already used in many RL frameworks (such as VERL and TorchForge), and by simplifying i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
