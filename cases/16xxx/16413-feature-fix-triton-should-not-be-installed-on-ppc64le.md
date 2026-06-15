# vllm-project/vllm#16413: [Feature]: (FIX) `triton` should not be installed on `ppc64le`

| 字段 | 值 |
| --- | --- |
| Issue | [#16413](https://github.com/vllm-project/vllm/issues/16413) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: (FIX) `triton` should not be installed on `ppc64le`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `triton==3.2.0` was added to `requirements/cpu.txt` in https://github.com/vllm-project/vllm/pull/16384 Triton is a GPU specific requirement and should not be added to CPU specific requirements file. Request to move it to `requirements/cuda.txt` Refer: [[Triton](https://github.com/triton-lang/triton)] - language/compiler for specifying and compiling tile programs into efficient GPU code. https://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf ### Alternatives _No response_ ### Additional context This is breaking ppc64le cpu builds of vLLM ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: (FIX) `triton` should not be installed on `ppc64le` feature request ### 🚀 The feature, motivation and pitch `triton==3.2.0` was added to `requirements/cpu.txt` in https://github.com/vllm-project/vllm/pull/163...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d to CPU specific requirements file. Request to move it to `requirements/cuda.txt` Refer: [[Triton](https://github.com/triton-lang/triton)] - language/compiler for specifying and compiling tile programs into efficient G...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: (FIX) `triton` should not be installed on `ppc64le` feature request ### 🚀 The feature, motivation and pitch `triton==3.2.0` was added to `requirements/cpu.txt` in https://github.com/vllm-project/vllm/pull/163...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: (FIX) `triton` should not be installed on `ppc64le` feature request ### 🚀 The feature, motivation and pitch `triton==3.2.0` was added to `requirements/cpu.txt` in https://github.com/vllm-project/vllm/pull/163...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
