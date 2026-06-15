# vllm-project/vllm#18681: [Usage]: why max-num-batched-tokens can smaller than max-model-len

| 字段 | 值 |
| --- | --- |
| Issue | [#18681](https://github.com/vllm-project/vllm/issues/18681) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: why max-num-batched-tokens can smaller than max-model-len

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm using 16 H800 GPUs, vLLM version 0.7.2, and I'm deploying DeepSeek R1 671B. I can set max-model-len to 128K, but max-num-batched-tokens can only go up to 32K. As I understand it, max-num-batched-tokens refers to the maximum number of tokens allowed per batch, so a 128K sequence shouldn't fit. Is it split into chunks before being processed? What is the underlying technique here? 我使用16张h800，vllm version 0.7.2，部署deepseek r1 671b 但是我的max-model-len可以设置成128k，max-num-batched-tokens确只能有32k。 我理解的是max-num-batched-tokens表示每个批次只能放32k，128k放不下，难道是切块后放入的吗？这个是什么技术？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: why max-num-batched-tokens can smaller than max-model-len usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm using 16 H800 GPUs, vLLM ver...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y` ``` ### How would you like to use vllm I'm using 16 H800 GPUs, vLLM version 0.7.2, and I'm deploying DeepSeek R1 671B. I can set max-model-len to 128K, but max-num-batched-tokens can only go up to 32K. As I understan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: why max-num-batched-tokens can smaller than max-model-len usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm using 16 H800 GPUs, vLLM ver...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
