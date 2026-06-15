# vllm-project/vllm#8679: [Doc]: How to Specify System CUTLASS/CUTE Path?

| 字段 | 值 |
| --- | --- |
| Issue | [#8679](https://github.com/vllm-project/vllm/issues/8679) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: How to Specify System CUTLASS/CUTE Path?

### Issue 正文摘录

### 📚 The doc issue Currently, the installation process forces you to git clone CUTLASS, while I already have CUTLASS compiled on my system under `/usr/local/cutlass` for DeepSpeed, which allowed you to specify a `CUTLASS_PATH` envvar. Is there a way we could force this during installation from source? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Doc]: How to Specify System CUTLASS/CUTE Path? documentation ### 📚 The doc issue Currently, the installation process forces you to git clone CUTLASS, while I already have CUTLASS compiled on my system under `/usr/local...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Doc]: How to Specify System CUTLASS/CUTE Path? documentation ### 📚 The doc issue Currently, the installation process forces you to git clone CUTLASS, while I already have CUTLASS compiled on my system under `/usr/local...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
