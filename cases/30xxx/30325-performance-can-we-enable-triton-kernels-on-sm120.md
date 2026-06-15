# vllm-project/vllm#30325: [Performance]: Can we enable triton_kernels on sm120

| 字段 | 值 |
| --- | --- |
| Issue | [#30325](https://github.com/vllm-project/vllm/issues/30325) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Can we enable triton_kernels on sm120

### Issue 正文摘录

### Proposal to improve performance Since PR (https://github.com/triton-lang/triton/pull/8498) had been merged, we may enable triton_kernels on sm120. https://github.com/vllm-project/vllm/blob/67475a6e81abea915857f82e6f10d80b03b842c9/vllm/model_executor/layers/quantization/mxfp4.py#L153-L160 Although I haven't looked at the relevant code in detail yet, I think it should be sufficient to complete the unit tests(or vllm had already had, just skip on sm120, delete one line is enough) for all the kernels involved when triton_kernels is enabled and run them on sm120. @zyongye Does this idea make sense? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: blob/67475a6e81abea915857f82e6f10d80b03b842c9/vllm/model_executor/layers/quantization/mxfp4.py#L153-L160 Although I haven't looked at the relevant code in detail yet, I think it should be sufficient to complete the unit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Can we enable triton_kernels on sm120 performance;stale ### Proposal to improve performance Since PR (https://github.com/triton-lang/triton/pull/8498) had been merged, we may enable triton_kernels on sm12...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: code in detail yet, I think it should be sufficient to complete the unit tests(or vllm had already had, just skip on sm120, delete one line is enough) for all the kernels involved when triton_kernels is enabled and run...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Performance]: Can we enable triton_kernels on sm120 performance;stale ### Proposal to improve performance Since PR (https://github.com/triton-lang/triton/pull/8498) had been merged, we may enable triton_kernels on sm12...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n't looked at the relevant code in detail yet, I think it should be sufficient to complete the unit tests(or vllm had already had, just skip on sm120, delete one line is enough) for all the kernels involved when triton_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
