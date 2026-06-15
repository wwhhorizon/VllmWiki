# vllm-project/vllm#10666: [RFC]: Create `VllmState` to save immutable args in `VllmConfig`

| 字段 | 值 |
| --- | --- |
| Issue | [#10666](https://github.com/vllm-project/vllm/issues/10666) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Create `VllmState` to save immutable args in `VllmConfig`

### Issue 正文摘录

### Motivation. The `VllmConfig` becomes huge as more and more features are added in vLLM. But some of that I think is immutable to users, thus not suitable to be as a configure, e.g. `worker_cls`, and other [private args](https://github.com/vllm-project/vllm/blob/main/vllm/config.py#L2211C32-L2211C43). Inspired by this [comment](https://github.com/vllm-project/vllm/pull/10555#issuecomment-2492713627) from Nick, I think creating a dataclass `VllmState` could help making `VllmConfig` lighter and safer for users to specify. ### Proposed Change. I think `VllmState` is similar to `VllmConfig`, composed by similar member vars as `VllmConfig`. ```python @dataclass class VllmState: model_state: ModelState cache_state: CacheState parallel_state: ParallelState scheduler_state: SchedulerState device_state: DeviceState load_state: LoadState lora_state: Optional[LoRAState] speculative_state: Optional[SpeculativeState] decoding_state: Optional[DecodingState] observability_state: Optional[ObservabilityState] prompt_adapter_state: Optional[PromptAdapterState] quant_state: Optional[QuantizationState] compilation_state: CompilationState ``` And the initial member of `VllmState` will absorb the **i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Create `VllmState` to save immutable args in `VllmConfig` RFC;stale ### Motivation. The `VllmConfig` becomes huge as more and more features are added in vLLM. But some of that I think is immutable to users, thus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Create `VllmState` to save immutable args in `VllmConfig` RFC;stale ### Motivation. The `VllmConfig` becomes huge as more and more features are added in vLLM. But some of that I think is immutable to users, thus...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mState` could help making `VllmConfig` lighter and safer for users to specify. ### Proposed Change. I think `VllmState` is similar to `VllmConfig`, composed by similar member vars as `VllmConfig`. ```python @dataclass c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: abilityState] prompt_adapter_state: Optional[PromptAdapterState] quant_state: Optional[QuantizationState] compilation_state: CompilationState ``` And the initial member of `VllmState` will absorb the **immutable args**...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
