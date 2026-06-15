# vllm-project/vllm#9434: [Feature]: Support for quantized models for tensorized model weights

| 字段 | 值 |
| --- | --- |
| Issue | [#9434](https://github.com/vllm-project/vllm/issues/9434) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for quantized models for tensorized model weights

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When trying to tensorize and load fp8 model (Mistral-Large 2) in my case, i am met with a warning: (VllmWorkerProcess pid=7091) WARNING 10-16 18:43:42 tensorizer.py:98] Loading a model using Tensorizer with quantization on vLLM is unstable and may lead to errors. (VllmWorkerProcess pid=1577) (VllmWorkerProcess pid=1612) ERROR 10-16 21:32:03 multiproc_worker_utils.py:233] RuntimeError: Expected b.stride(0) == 1 to be true, but got false. (Could this error message be improved? If so, please report an enhancement request to PyTorch.) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Support for quantized models for tensorized model weights feature request;stale ### 🚀 The feature, motivation and pitch When trying to tensorize and load fp8 model (Mistral-Large 2) in my case, i am met with...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: R 10-16 21:32:03 multiproc_worker_utils.py:233] RuntimeError: Expected b.stride(0) == 1 to be true, but got false. (Could this error message be improved? If so, please report an enhancement request to PyTorch.) ### Alte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ture]: Support for quantized models for tensorized model weights feature request;stale ### 🚀 The feature, motivation and pitch When trying to tensorize and load fp8 model (Mistral-Large 2) in my case, i am met with a wa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support for quantized models for tensorized model weights feature request;stale ### 🚀 The feature, motivation and pitch When trying to tensorize and load fp8 model (Mistral-Large 2) in my case, i am met with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
