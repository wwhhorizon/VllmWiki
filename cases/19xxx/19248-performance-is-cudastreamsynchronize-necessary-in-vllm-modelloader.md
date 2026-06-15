# vllm-project/vllm#19248: [Performance]: Is cudaStreamSynchronize necessary in vLLM ModelLoader?

| 字段 | 值 |
| --- | --- |
| Issue | [#19248](https://github.com/vllm-project/vllm/issues/19248) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Is cudaStreamSynchronize necessary in vLLM ModelLoader?

### Issue 正文摘录

### Proposal to improve performance In vLLM model loader, each tensor load from DefaultLoader, then copy to GPU. It calls cudaStreamSynchronize in API tensor.copy_(). Why not call tensor.copy_(..., non_blocking=True) and call cudaStreamSynchronize in each safetensor file. In my case, it can enhance performance in ModelLoader process. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Is cudaStreamSynchronize necessary in vLLM ModelLoader? performance;stale ### Proposal to improve performance In vLLM model loader, each tensor load from DefaultLoader, then copy to GPU. It calls cudaStre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n enhance performance in ModelLoader process. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: eamSynchronize in API tensor.copy_(). Why not call tensor.copy_(..., non_blocking=True) and call cudaStreamSynchronize in each safetensor file. In my case, it can enhance performance in ModelLoader process. ### Report o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Is cudaStreamSynchronize necessary in vLLM ModelLoader? performance;stale ### Proposal to improve performance In vLLM model loader, each tensor load from DefaultLoader, then copy to GPU. It calls cudaStre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ce]: Is cudaStreamSynchronize necessary in vLLM ModelLoader? performance;stale ### Proposal to improve performance In vLLM model loader, each tensor load from DefaultLoader, then copy to GPU. It calls cudaStreamSynchron...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
