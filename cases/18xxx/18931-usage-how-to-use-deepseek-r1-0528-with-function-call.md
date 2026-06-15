# vllm-project/vllm#18931: [Usage]: How to use Deepseek-R1-0528 with function call

| 字段 | 值 |
| --- | --- |
| Issue | [#18931](https://github.com/vllm-project/vllm/issues/18931) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use Deepseek-R1-0528 with function call

### Issue 正文摘录

### Your current environment https://hf-mirror.com/deepseek-ai/DeepSeek-R1-0528 ### How would you like to use vllm 你好，现在官方api已经支持function call还有JsonOutput https://api-docs.deepseek.com/zh-cn/news/news250528， 开放权重也支持fuction call https://hf-mirror.com/deepseek-ai/DeepSeek-R1-0528/blob/main/tokenizer_config.json 请问vllm目前有没有更新支持 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: k-R1-0528 with function call usage ### Your current environment https://hf-mirror.com/deepseek-ai/DeepSeek-R1-0528 ### How would you like to use vllm 你好，现在官方api已经支持function call还有JsonOutput https://api-docs.deepseek.com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 新支持 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
