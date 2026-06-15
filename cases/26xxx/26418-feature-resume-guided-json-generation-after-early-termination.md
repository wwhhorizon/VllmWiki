# vllm-project/vllm#26418: [Feature]: Resume guided/JSON generation after early termination

| 字段 | 值 |
| --- | --- |
| Issue | [#26418](https://github.com/vllm-project/vllm/issues/26418) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Resume guided/JSON generation after early termination

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary Add support for continuing constrained (guided / JSON-schema) generation from a partial output after an abort (e.g., when stopping an “infinite list” mid-stream). This would let users truncate and resume without restarting decoding from scratch. ## Problem When streaming structured JSON with guided decoding, the model can enter an infinite or repetitive list loop. After aborting, we can fix the partial output (e.g. close brackets), but there’s no way to resume generation while maintaining grammar constraints. Previously, with Outlines + vLLM, we could continue generation using the same FSM/logits processor state. Now, aborting means losing all progress and schema consistency. The model should continue valid generation under the same schema. ## Why It Matters - Enables recovery from infinite or partial outputs. - Saves compute by reusing valid work. - Restores feature parity with Outlines’ GuideLogitsProcessor. - Improves robustness for streaming JSON use cases. ### Alternatives One option is to simply re-prompt the model with the partial JSON as input and ask it to “complete” the object but this loses the internal grammar state, s...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: usly, with Outlines + vLLM, we could continue generation using the same FSM/logits processor state. Now, aborting means losing all progress and schema consistency. The model should continue valid generation under the sa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Resume guided/JSON generation after early termination feature request;stale ### 🚀 The feature, motivation and pitch ## Summary Add support for continuing constrained (guided / JSON-schema) generation from a p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h. ## Problem When streaming structured JSON with guided decoding, the model can enter an infinite or repetitive list loop. After aborting, we can fix the partial output (e.g. close brackets), but there’s no way to resu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
