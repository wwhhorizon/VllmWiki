# vllm-project/vllm#18823: [Bug]: 0.8.x with vllm V1 fails on loading Qwen-vl-2.5 with UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 2218: ordinal not in range(128)

| 字段 | 值 |
| --- | --- |
| Issue | [#18823](https://github.com/vllm-project/vllm/issues/18823) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 0.8.x with vllm V1 fails on loading Qwen-vl-2.5 with UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 2218: ordinal not in range(128)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We attempted to load models from the Qwen2.5-VL series using the “vllm serve” command (7b/32b/72b models were all tested, all resulting in the same error), but all failed with "torch._dynamo.exc.BackendCompilerFailed: backend='' raised UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 2218: ordinal not in range(128)" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .x with vllm V1 fails on loading Qwen-vl-2.5 with UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 2218: ordinal not in range(128) bug;stale ### Your current environment ### 🐛 Describe the bug We att...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 0.8.x with vllm V1 fails on loading Qwen-vl-2.5 with UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 2218: ordinal not in range(128) bug;stale ### Your current environment ### 🐛 Describe the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 0.8.x with vllm V1 fails on loading Qwen-vl-2.5 with UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 2218: ordinal not in range(128) bug;stale ### Your current environment ### 🐛 Describe the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: all resulting in the same error), but all failed with "torch._dynamo.exc.BackendCompilerFailed: backend='' raised UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 2218: ordinal not in range(128)" ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 8)" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
