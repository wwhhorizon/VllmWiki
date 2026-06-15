# vllm-project/vllm#9268: [RFC]: Make device agnostic for diverse hardware support

| 字段 | 值 |
| --- | --- |
| Issue | [#9268](https://github.com/vllm-project/vllm/issues/9268) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Make device agnostic for diverse hardware support

### Issue 正文摘录

### Motivation. `vLLM` has already been adapted to many hardware devices, such as `GPU`, `TPU`, and `XPU`. However, adapting these backends requires implementing separate `Worker/Executor/Model Runner` frameworks for each, which leads to code redundancy and maintenance difficulties. In fact, these hardware framework codes can be abstracted at the device layer, forming a unified framework. This way, only one set of code would need to be maintained, and different backends would only need to implement the device layer interfaces and any device-specific logic if necessary. I also found some new features are only updated on GPU-related codes. In fact, these codes are also applicable to other hardware, but it is difficult for other hardware to perceive and follow these updates. ### Proposed Change. This RFC is intended to establish a unified framework. Maybe there will be diffuculty for intergrating hardware framework to common framework, It makes sense to work towards this direction, the diagram below represents a proposed solution: ![图片1](https://github.com/user-attachments/assets/1216b0ac-5b9a-4630-984c-70ac978f5b54) Taking `Executor` as example, for third-party hardware devices base...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ted, so after abstracting the device-related hard coding, such as `torch.cuda`, `torch.xpu`, `GPU Executor` could be used as the `Common Executor` of all third-party devices. Following https://github.com/vllm-project/vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: adapting these backends requires implementing separate `Worker/Executor/Model Runner` frameworks for each, which leads to code redundancy and maintenance difficulties. In fact, these hardware framework codes can be abst...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: le` -> `current_platform.is_pin_memory_available` - [ ] `DeviceMemoryProfiler` -> `current_platform.memory_profiler` - [ ] `wrap_device` -> `current_platform.wrap_device` - [x] `current_platform.verify_quantization` - [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rdware devices, such as `GPU`, `TPU`, and `XPU`. However, adapting these backends requires implementing separate `Worker/Executor/Model Runner` frameworks for each, which leads to code redundancy and maintenance difficu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uld only need to implement the device layer interfaces and any device-specific logic if necessary. I also found some new features are only updated on GPU-related codes. In fact, these codes are also applicable to other...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
