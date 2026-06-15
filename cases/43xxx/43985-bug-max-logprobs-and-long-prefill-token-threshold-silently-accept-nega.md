# vllm-project/vllm#43985: [Bug]: --max-logprobs and --long-prefill-token-threshold silently accept negative values (config-validation gap)

| 字段 | 值 |
| --- | --- |
| Issue | [#43985](https://github.com/vllm-project/vllm/issues/43985) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --max-logprobs and --long-prefill-token-threshold silently accept negative values (config-validation gap)

### Issue 正文摘录

### Your current environment - OS: macOS 26.5 (arm64) - Python: 3.12.11 - PyTorch: 2.11.0 - vLLM: 0.1.dev1+g4438b6e7d - Transformers: 5.9.0 Built from source via `VLLM_TARGET_DEVICE=empty pip install -e .` at commit `4438b6e7d`. ### 🐛 Describe the bug Two CLI-settable integer parameters accept **negative** values that no validator rejects. Neither causes a crash or silent corruption, so this is **low severity** — but in both cases the malformed flag is silently ineffective (or surfaces a confusing error), with no signal to the user. Both are the same field-level admission shape as the batch tightened in #43794 (#43496 / #43521 / #43532): a CLI int field with no `Field(gt=0)` / `ge=` constraint whose downstream logic only special-cases specific values. **1. `--max-logprobs `** — `ModelConfig.max_logprobs` is declared `int = 20` (`vllm/config/model.py:234`) with no constraint. In `_validate_logprobs` (`vllm/sampling_params.py:680`) the sentinel rewrite only handles `== -1` (auto = vocab size); every other negative survives unchanged: - *logprob-requesting traffic*: the request is rejected, but the error message exposes the malformed cap to the user — `"Requested sample logprobs of 3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ansformers: 5.9.0 Built from source via `VLLM_TARGET_DEVICE=empty pip install -e .` at commit `4438b6e7d`. ### 🐛 Describe the bug Two CLI-settable integer parameters accept **negative** values that no validator rejects....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: --max-logprobs and --long-prefill-token-threshold silently accept negative values (config-validation gap) bug ### Your current environment - OS: macOS 26.5 (arm64) - Python: 3.12.11 - PyTorch: 2.11.0 - vLLM: 0.1....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `gt=` constraint cannot express "non-negative **or** exactly `-1`", so a small `field_validator` is the natural fix. ## Proposed fix Mirror the `field_validator` pattern landed in #43794: ```python # vllm/config/model.p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: lasses.fields(ModelConfig) if f.name == "max_logprobs") assert dict(ml.metadata) == {} # no constraint lp = next(f for f in dataclasses.fields(SchedulerConfig) if f.name == "long_prefill_token_threshold") assert dict(lp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: robs and --long-prefill-token-threshold silently accept negative values (config-validation gap) bug ### Your current environment - OS: macOS 26.5 (arm64) - Python: 3.12.11 - PyTorch: 2.11.0 - vLLM: 0.1.dev1+g4438b6e7d -...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
