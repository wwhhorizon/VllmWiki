# vllm-project/vllm#10299: [Usage]: Unable to Use vllm with meta-llama/Llama-3.2-1B Due to Missing chat_template

| 字段 | 值 |
| --- | --- |
| Issue | [#10299](https://github.com/vllm-project/vllm/issues/10299) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Unable to Use vllm with meta-llama/Llama-3.2-1B Due to Missing chat_template

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am unable to use the vllm server with the meta-llama/Llama-3.2-1B model because the llama-3.2 version no longer includes a chat_template. Consequently, I cannot find a suitable template to provide to the vllm server using the --chat_template option. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Unable to Use vllm with meta-llama/Llama-3.2-1B Due to Missing chat_template usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am unable t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm server with the meta-llama/Llama-3.2-1B model because the llama-3.2 version no longer includes a chat_template. Consequently, I cannot find a suitable template to provide to the vllm server using the --chat_templat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
