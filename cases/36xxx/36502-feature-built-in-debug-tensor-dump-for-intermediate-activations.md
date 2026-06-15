# vllm-project/vllm#36502: [Feature]: Built-in debug tensor dump for intermediate activations

| 字段 | 值 |
| --- | --- |
| Issue | [#36502](https://github.com/vllm-project/vllm/issues/36502) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Built-in debug tensor dump for intermediate activations

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Motivation When debugging model accuracy issues (e.g. comparing outputs across different frameworks like SGLang vs vLLM, or before/after quantization), it is extremely useful to dump intermediate activations from every layer. Currently there is no built-in way to do this in vLLM — users have to manually patch `gpu_model_runner.py` to inject forward hooks, which is fragile and breaks across versions. SGLang has a similar feature (`tensor_dump_forward_hook.py`) that has proven very useful in practice. I'd like to propose adding native support in vLLM. ## Proposed Design ### Environment Variables (opt-in, zero overhead when disabled) | Variable | Type | Default | Description | |---|---|---|---| | `VLLM_DEBUG_TENSOR_DUMP_OUTPUT_FOLDER` | `str` | (unset) | Output directory. Feature is disabled when unset. | | `VLLM_DEBUG_TENSOR_DUMP_LAYERS` | `str` | (unset) | Comma-separated layer indices to dump (e.g. `"0,1,31"`). All layers when unset. | | `VLLM_DEBUG_TENSOR_DUMP_SKIP_PASSES` | `int` | `0` | Number of initial forward passes to skip (useful for skipping warmup). | ### Usage ```bash VLLM_DEBUG_TENSOR_DUMP_OUTPUT_FOLDER=./dump \ python -m vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: runner.py` to inject forward hooks, which is fragile and breaks across versions. SGLang has a similar feature (`tensor_dump_forward_hook.py`) that has proven very useful in practice. I'd like to propose adding native su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model(), gated by the env var check. - When enabled, torch.compile and CUDAGraph are automatically disabled (they are incompatible with .cpu() / torch.save inside hooks). - The custom __call__ injected by @support_torch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: otivation When debugging model accuracy issues (e.g. comparing outputs across different frameworks like SGLang vs vLLM, or before/after quantization), it is extremely useful to dump intermediate activations from every l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: Built-in debug tensor dump for intermediate activations feature request ### 🚀 The feature, motivation and pitch ## Motivation When debugging model accuracy issues (e.g. comparing outputs across different framew...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ion When debugging model accuracy issues (e.g. comparing outputs across different frameworks like SGLang vs vLLM, or before/after quantization), it is extremely useful to dump intermediate activations from every layer....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
