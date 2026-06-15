# vllm-project/vllm#5085: [Feature]: Adopt Colossal Inference Features (55% speedup over vLLM)

| 字段 | 值 |
| --- | --- |
| Issue | [#5085](https://github.com/vllm-project/vllm/issues/5085) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adopt Colossal Inference Features (55% speedup over vLLM)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ColossalAI has been able to demonstrate an impressive speedup over vLLM in multi-GPU inference. With TP=2, batch size 64, input len 512, output len 256 - a 55% speedup can be observed. I believe vLLM could see a speedup if it was to adopt a more performant batched prefilling. ![image](https://github.com/vllm-project/vllm/assets/27340033/ad30d755-8683-4ecb-b1b7-52ee6216b6bd) For reference, here is the continuous batching feature: ![image](https://github.com/vllm-project/vllm/assets/27340033/a5026956-d087-4a5e-b0aa-d7a4c19f73d9) ### Alternatives _No response_ ### Additional context Blog post: https://hpc-ai.com/blog/colossal-inference Source code: https://github.com/hpcaitech/ColossalAI/tree/main/colossalai/inference

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ture]: Adopt Colossal Inference Features (55% speedup over vLLM) feature request;stale ### 🚀 The feature, motivation and pitch ColossalAI has been able to demonstrate an impressive speedup over vLLM in multi-GPU inferen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
