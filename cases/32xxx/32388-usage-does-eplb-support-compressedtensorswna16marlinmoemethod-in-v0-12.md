# vllm-project/vllm#32388: [Usage]: Does EPLB support CompressedTensorsWNA16MarlinMoEMethod in v0.12.0 or higher version?

| 字段 | 值 |
| --- | --- |
| Issue | [#32388](https://github.com/vllm-project/vllm/issues/32388) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does EPLB support CompressedTensorsWNA16MarlinMoEMethod in v0.12.0 or higher version?

### Issue 正文摘录

### Your current environment Now, I have test int4-model which use `CompressedTensorsWNA16MarlinMoEMethod` with `EBLP` in v0.11.0 and the output is wrong. As it can be seen in v0.12.0 or higher version, the code like ``` if enable_eplb: raise NotImplementedError( "EPLB not supported for `CompressedTensorsW4A4MoEMethod` yet." ) ``` was deleted in `CompressedTensorsWNA16MarlinMoEMethod.apply()`!! ### How would you like to use vllm Does it mean EPLB support int4 model now? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: EPLB support CompressedTensorsWNA16MarlinMoEMethod in v0.12.0 or higher version? usage;stale ### Your current environment Now, I have test int4-model which use `CompressedTensorsWNA16MarlinMoEMethod` with `EBLP` in v0.1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: gher version? usage;stale ### Your current environment Now, I have test int4-model which use `CompressedTensorsWNA16MarlinMoEMethod` with `EBLP` in v0.11.0 and the output is wrong. As it can be seen in v0.12.0 or higher...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ow? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: version? usage;stale ### Your current environment Now, I have test int4-model which use `CompressedTensorsWNA16MarlinMoEMethod` with `EBLP` in v0.11.0 and the output is wrong. As it can be seen in v0.12.0 or higher vers...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: Does EPLB support CompressedTensorsWNA16MarlinMoEMethod in v0.12.0 or higher version? usage;stale ### Your current environment Now, I have test int4-model which use `CompressedTensorsWNA16MarlinMoEMethod` with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
