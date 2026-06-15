# vllm-project/vllm#696: Unexpected latency of StarCoder when enable tensor parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#696](https://github.com/vllm-project/vllm/issues/696) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 | latency_reg |
| Operator 关键词 | operator |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Unexpected latency of StarCoder when enable tensor parallel

### Issue 正文摘录

### Discussed in https://github.com/vllm-project/vllm/discussions/666 Originally posted by **zhaoyang-star** August 3, 2023 The latency of StarCoder running on 2 A100 40GB is higher than that running on 1 A100. While, the latency of LLaMA-13B running on 2 A100 40GB is lower than that running on 1 A100 as expected. So does MultiQueryAttenion impl in vLLM cause this? ![image](https://github.com/vllm-project/vllm/assets/24290792/ea66ad84-d8f3-4793-9970-ca70b07c13b0) ![image](https://github.com/vllm-project/vllm/assets/24290792/37a8c774-1b5a-4891-86db-ec464e79f58f) Note: Prompt token length and output token length both are set to 1k.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: **zhaoyang-star** August 3, 2023 The latency of StarCoder running on 2 A100 40GB is higher than that running on 1 A100. While, the latency of LLaMA-13B running on 2 A100 40GB is lower than that running on 1 A100 as expe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: A100 40GB is higher than that running on 1 A100. While, the latency of LLaMA-13B running on 2 A100 40GB is lower than that running on 1 A100 as expected. So does MultiQueryAttenion impl in vLLM cause this? ![image](http...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Unexpected latency of StarCoder when enable tensor parallel bug ### Discussed in https://github.com/vllm-project/vllm/discussions/666 Originally posted by **zhaoyang-star** August 3, 2023 The latency of StarCoder runnin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
