# vllm-project/vllm#4501: [Feature]: Load new LoRA adapters on request

| 字段 | 值 |
| --- | --- |
| Issue | [#4501](https://github.com/vllm-project/vllm/issues/4501) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Load new LoRA adapters on request

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When experimenting with model finetuning, one can train a lot of LoRAs. In order to test (or deploy into production) new lora weights we have to restart the image because we can load loras only on docker start and lora loading with a request is not supported now. There were the [same issue](https://github.com/vllm-project/vllm/issues/4234) and relevant [PR](https://github.com/vllm-project/vllm/pull/3850) , however issue is closed but PR is not merged and actually doesn't pass tests. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Load new LoRA adapters on request feature request;stale ### 🚀 The feature, motivation and pitch When experimenting with model finetuning, one can train a lot of LoRAs. In order to test (or deploy into product...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a weights we have to restart the image because we can load loras only on docker start and lora loading with a request is not supported now. There were the [same issue](https://github.com/vllm-project/vllm/issues/4234) a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t;stale ### 🚀 The feature, motivation and pitch When experimenting with model finetuning, one can train a lot of LoRAs. In order to test (or deploy into production) new lora weights we have to restart the image because...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: menting with model finetuning, one can train a lot of LoRAs. In order to test (or deploy into production) new lora weights we have to restart the image because we can load loras only on docker start and lora loading wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
