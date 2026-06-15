# vllm-project/vllm#9731: [Bug]: tensor parallelism multinode

| 字段 | 值 |
| --- | --- |
| Issue | [#9731](https://github.com/vllm-project/vllm/issues/9731) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tensor parallelism multinode

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With vllm==0.5.4 I used to be able to run llama 3.1 405B with tensor_parallelism=16 on 4 nodes, now this seems to be impossible with newer versions and I am trying to do this in the offline version, so pipeline_parallelism is not an option. Was this functionality removed on purpose? Thank you in advance. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: tensor parallelism multinode bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With vllm==0.5.4 I used to be able to run llama 3.1 405B with tensor_parallelism=16 on 4 no...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ]: tensor parallelism multinode bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With vllm==0.5.4 I used to be able to run llama 3.1 405B with tensor_parallelism=16 on 4 nodes,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or_parallelism=16 on 4 nodes, now this seems to be impossible with newer versions and I am trying to do this in the offline version, so pipeline_parallelism is not an option. Was this functionality removed on purpose? T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
