# vllm-project/vllm#11474: [Usage]: missing openai templates

| 字段 | 值 |
| --- | --- |
| Issue | [#11474](https://github.com/vllm-project/vllm/issues/11474) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: missing openai templates

### Issue 正文摘录

### Your current environment Is there a way to fix this errorr? All guides start with a line with the llm serve command, but it doesn’t work for me (even with tokenizer option) + I prefer a docker container? ![image](https://github.com/user-attachments/assets/66124ce1-7a75-4b45-bc21-ecc874493d1e) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd, but it doesn’t work for me (even with tokenizer option) + I prefer a docker container? ![image](https://github.com/user-attachments/assets/66124ce1-7a75-4b45-bc21-ecc874493d1e) ### How would you like to use vllm I w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
