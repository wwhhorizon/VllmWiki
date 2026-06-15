# vllm-project/vllm#19359: [Doc]: Backwards compability with PyTorch

| 字段 | 值 |
| --- | --- |
| Issue | [#19359](https://github.com/vllm-project/vllm/issues/19359) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Backwards compability with PyTorch

### Issue 正文摘录

### 📚 The doc issue vLLM has become a very important component of the OSS ecosystem and is tightly integrated with [`torch`](https://github.com/pytorch/pytorch) and [`triton-lang`](https://github.com/triton-lang/triton/tree/main) From looking at the requirements it looks like the philosophy is to only ensure full compatibility with the newest PyTorch version (currently 2.7.0) [here](https://github.com/vllm-project/vllm/blob/59abbd84f90e5930c37e205de8849ac4fa8a96c7/requirements/cuda.txt#L9) which then also somewhat automatically pins the required triton version. While torch tries to stay backward compatible with earlier torch versions, this is not always ensured for libraries depending on torch & triton. VLLM for example uses custom triton code here: https://github.com/vllm-project/vllm/blob/59abbd84f90e5930c37e205de8849ac4fa8a96c7/vllm/attention/ops/prefix_prefill.py#L134 (and many other places) that is not always compatible with earlier triton versions. E.g. triton=3.1.0 doesn't have a `loop_unroll_factor` in its `tl.range` (see [here](https://github.com/triton-lang/triton/blob/cf34004b8a67d290a962da166f5aa2fc66751326/python/triton/language/core.py#L2473)). Hence vllm can't use P...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: PyTorch documentation;stale ### 📚 The doc issue vLLM has become a very important component of the OSS ecosystem and is tightly integrated with [`torch`](https://github.com/pytorch/pytorch) and [`triton-lang`](https://gi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -project/vllm/blob/59abbd84f90e5930c37e205de8849ac4fa8a96c7/requirements/cuda.txt#L9) which then also somewhat automatically pins the required triton version. While torch tries to stay backward compatible with earlier t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Doc]: Backwards compability with PyTorch documentation;stale ### 📚 The doc issue vLLM has become a very important component of the OSS ecosystem and is tightly integrated with [`torch`](https://github.com/pytorch/pytor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: htly integrated with [`torch`](https://github.com/pytorch/pytorch) and [`triton-lang`](https://github.com/triton-lang/triton/tree/main) From looking at the requirements it looks like the philosophy is to only ensure ful...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
