# vllm-project/vllm#42878: [Bug]: DeepSeek V4 DSML tool calls fake-stream arguments instead of incremental deltas

| 字段 | 值 |
| --- | --- |
| Issue | [#42878](https://github.com/vllm-project/vllm/issues/42878) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 DSML tool calls fake-stream arguments instead of incremental deltas

### Issue 正文摘录

### Your current environment Reproduced at parser level on upstream `main` commit `0fa888465e5a30b797bdf2cdcd0f57fc77541cef`. This does not require model weights or a GPU to reproduce because it is in the DeepSeek DSML tool parser streaming path. ### 🐛 Describe the bug DeepSeek V4 DSML tool-call streaming currently buffers the entire ` ... ` block and emits `function.arguments` only once the closing invoke tag is present. That means `stream=true` does not actually stream tool-call arguments incrementally. For long tool-call arguments, clients receive no argument deltas until the full invoke is complete, then receive one large `function.arguments` payload. The current code path is inherited from `DeepSeekV32ToolParser` and explicitly documents the behavior as a buffer-until-complete-invoke strategy. Expected behavior: 1. Emit the tool-call id/type/name once the invoke start tag is recognized. 2. Emit valid OpenAI-compatible `function.arguments` fragments incrementally as DSML parameter content arrives. 3. Reassembling all argument fragments should produce the same JSON object as non-streaming parsing. 4. Preserve the existing `string="true|false"` semantics from #41801. Actual beha...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: The current code path is inherited from `DeepSeekV32ToolParser` and explicitly documents the behavior as a buffer-until-complete-invoke strategy. Expected behavior: 1. Emit the tool-call id/type/name once the invoke sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: DeepSeek V4 DSML tool calls fake-stream arguments instead of incremental deltas ### Your current environment Reproduced at parser level on upstream `main` commit `0fa888465e5a30b797bdf2cdcd0f57fc77541cef`. This d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: eepSeek V4 DSML tool-call streaming currently buffers the entire ` ... ` block and emits `function.arguments` only once the closing invoke tag is present. That means `stream=true` does not actually stream tool-call argu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: am arguments instead of incremental deltas ### Your current environment Reproduced at parser level on upstream `main` commit `0fa888465e5a30b797bdf2cdcd0f57fc77541cef`. This does not require model weights or a GPU to re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ommit `0fa888465e5a30b797bdf2cdcd0f57fc77541cef`. This does not require model weights or a GPU to reproduce because it is in the DeepSeek DSML tool parser streaming path. ### 🐛 Describe the bug DeepSeek V4 DSML tool-cal...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
