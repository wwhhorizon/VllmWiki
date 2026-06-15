# vllm-project/vllm#26239: [Feature]: support reasoning-parser for Qwen3-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#26239](https://github.com/vllm-project/vllm/issues/26239) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support reasoning-parser for Qwen3-VL

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm running Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 vllm 0.11.0 Using OpenWebUI for front-end. Expected: - THINKING part of the response goes to THINKING element (hidden by default) Actual: - THINKING part of the response goes to ANSWER. I found that starting tag ` ` is part of `tokenizer_config.json`, - that's why it's returned as part of the response, so front-end doesn't display it correctly. I tried to use ``` - "--reasoning-parser" - "qwen3" ``` But nothing changed. ### Alternatives I found that this works: ``` - "--reasoning-parser" - "deepseek_r1" ``` in that case opening ` ` tag returned as expected.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: support reasoning-parser for Qwen3-VL feature request;stale ### 🚀 The feature, motivation and pitch I'm running Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 vllm 0.11.0 Using OpenWebUI for front-end. Expected: - THINKI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support reasoning-parser for Qwen3-VL feature request;stale ### 🚀 The feature, motivation and pitch I'm running Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 vllm 0.11.0 Using OpenWebUI for front-end. Expected: - THINKI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: eature, motivation and pitch I'm running Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 vllm 0.11.0 Using OpenWebUI for front-end. Expected: - THINKING part of the response goes to THINKING element (hidden by default) Actual: - THI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
