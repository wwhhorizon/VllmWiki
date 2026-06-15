# vllm-project/vllm#41551: [Feature]: Implement EDEN over TurboQuant (better performance and more accurate attribution)

| 字段 | 值 |
| --- | --- |
| Issue | [#41551](https://github.com/vllm-project/vllm/issues/41551) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implement EDEN over TurboQuant (better performance and more accurate attribution)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch You're already working towards a TurboQuant implementation. I think you'll find EDEN (NeurIPS 2021, ICML 2022) to be **_a bit too similar_**, easier to implement, and more performant (saving an entire bit per coordinate in the unbiased case). Please see the following article for an overview: https://towardsdatascience.com/how-a-2021-quantization-algorithm-quietly-outperforms-its-2026-successor/ . Disclaimer: I am the author of the linked article and a co-author of the original EDEN papers (NeurIPS 2021, ICML 2022). I am happy to answer any questions regarding this situation or the underlying math. ### Alternatives Alternative solution? Getting used to the fact that people are using EDEN without optimal scaling under a new name, five years after the original publication. ### Additional context [DRIVE: One-bit Distributed Mean Estimation](https://proceedings.neurips.cc/paper/2021/hash/0397758f8990c1b41b81b43ac389ab9f-Abstract.html) (2021), NeurIPS 2021 [EDEN: Communication-Efficient and Robust Distributed Mean Estimation for Federated Learning](https://proceedings.mlr.press/v162/vargaftik22a.html) (2022), ICML 2022. [A Note on TurboQuant and t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Please see the following article for an overview: https://towardsdatascience.com/how-a-2021-quantization-algorithm-quietly-outperforms-its-2026-successor/ . Disclaimer: I am the author of the linked article and a co-aut...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Implement EDEN over TurboQuant (better performance and more accurate attribution) feature request ### 🚀 The feature, motivation and pitch You're already working towards a TurboQuant implementation. I think yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 55. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: er TurboQuant (better performance and more accurate attribution) feature request ### 🚀 The feature, motivation and pitch You're already working towards a TurboQuant implementation. I think you'll find EDEN (NeurIPS 2021...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
