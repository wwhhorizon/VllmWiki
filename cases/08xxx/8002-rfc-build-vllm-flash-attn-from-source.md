# vllm-project/vllm#8002: [RFC]: Build `vllm-flash-attn` from source

| 字段 | 值 |
| --- | --- |
| Issue | [#8002](https://github.com/vllm-project/vllm/issues/8002) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Build `vllm-flash-attn` from source

### Issue 正文摘录

### Motivation. To use a custom version of PyTorch in vLLM, `vllm-flash-attn` needs to be built with the same version. The easiest way to achieve that is by building it from source during the vLLM build. ### Proposed Change. We propose 3 different ways of building `vllm-flash-attn` from source: absorbing the package completely, building it as a CMake dependency, or running a nested `pip install`. Currently, alternative 2 is preferred, but we'd like to get feedback on that. I will update this RFC once we decide on an approach. More details here: https://docs.google.com/document/d/1njmz8NPT3am5gNcjbjzZG1BN-v8wIxWq6vb5QoctuZ0/edit?usp=sharing ### Feedback Period. _No response_ ### CC List. @WoosukKwon @youkaichao @tlrmchlsmth @bnellnm ### Any Other Things. _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [RFC]: Build `vllm-flash-attn` from source RFC ### Motivation. To use a custom version of PyTorch in vLLM, `vllm-flash-attn` needs to be built with the same version. The easiest way to achieve that is by building it fro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ck Period. _No response_ ### CC List. @WoosukKwon @youkaichao @tlrmchlsmth @bnellnm ### Any Other Things. _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
