# vllm-project/vllm#38744: [RFC][vLLM IR]: Automatically compile native impl for IR ops

| 字段 | 值 |
| --- | --- |
| Issue | [#38744](https://github.com/vllm-project/vllm/issues/38744) |
| 状态 | open |
| 标签 | RFC;vllm-ir |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][vLLM IR]: Automatically compile native impl for IR ops

### Issue 正文摘录

### Motivation. Sometimes we need to call an IR op inside another opaque torch custom op. That means the IR op will be invisible to model-level compilation, and dispatching to the raw native implementation will hurt performance. This problem is not unique to vLLM IR; it happens for `CustomOp` instances as well, and we currently circumvent it by wrapping `forward_native` with `torch.compile`. Prime examples of this are `SiluAndMul` and `QuantFP8` inside `fused_moe`. The same mechanism is utilized by the `_DecodeConcatQuantFP8` inside the MLA custom op. ### Proposed Change. We wrap the native implementation (or multiple implementations) with a torch.compile decorator. We can do that by setting `IrOpImpl.impl_fn = torch.compile(IrOpImpl.impl_fn, ...)` (including dynamic shape annotations). The big question is lifetime: ideally we can set this with the `set_priority` context and restore it after, but will that persist the compiled code, or will it recompile every time? I guess if torch doesn't cache this, we could cache it manually? We can optionally guard this with `torch.compiler.is_compiling()` although I think torch.compile already does that for us? Draft implementation in #38775....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC][vLLM IR]: Automatically compile native impl for IR ops RFC;vllm-ir ### Motivation. Sometimes we need to call an IR op inside another opaque torch custom op. That means the IR op will be invisible to model-level co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ive` with `torch.compile`. Prime examples of this are `SiluAndMul` and `QuantFP8` inside `fused_moe`. The same mechanism is utilized by the `_DecodeConcatQuantFP8` inside the MLA custom op. ### Proposed Change. We wrap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: this are `SiluAndMul` and `QuantFP8` inside `fused_moe`. The same mechanism is utilized by the `_DecodeConcatQuantFP8` inside the MLA custom op. ### Proposed Change. We wrap the native implementation (or multiple implem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nother opaque torch custom op. That means the IR op will be invisible to model-level compilation, and dispatching to the raw native implementation will hurt performance. This problem is not unique to vLLM IR; it happens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: d `QuantFP8` inside `fused_moe`. The same mechanism is utilized by the `_DecodeConcatQuantFP8` inside the MLA custom op. ### Proposed Change. We wrap the native implementation (or multiple implementations) with a torch....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
