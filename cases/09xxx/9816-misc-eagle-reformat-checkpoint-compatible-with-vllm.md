# vllm-project/vllm#9816: [Misc]: Eagle reformat checkpoint compatible with Vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#9816](https://github.com/vllm-project/vllm/issues/9816) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Eagle reformat checkpoint compatible with Vllm

### Issue 正文摘录

### Anything you want to discuss about vllm. As per the current eagle implementation in Vllm, the checkpoint must strictly adhere to the vllm format which wont work directly with common HF checkpoints for eagle like - https://huggingface.co/yuhuili There is a comment in the code to use a script to convert the HF checkpoint to vllm compatible format. ``` # This implementation is incompitable with https://huggingface.co/yuhuili/EAGLE-LLaMA3-Instruct-8B # due to missing lm_head weights and its config being that of a # Llama model. Here's a compatible version with the same weights: # https://huggingface.co/abhigoyal/EAGLE-LLaMA3-Instruct-8B-vllm # Also, here's an example script for converting trained EAGLE # checkpoint to vLLM compatible version: https://gist.github.com/abhigoyal1997/1e7a4109ccb7704fbc67f625e86b2d6d ``` Ref - https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/eagle.py#L127 Is this incompatibility of HF checkpoints and vllm format here to stay or would this be changed? Do we expect users to always provide a path with the vllm format of the checkpoint? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Misc]: Eagle reformat checkpoint compatible with Vllm stale ### Anything you want to discuss about vllm. As per the current eagle implementation in Vllm, the checkpoint must strictly adhere to the vllm format which won...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hts and its config being that of a # Llama model. Here's a compatible version with the same weights: # https://huggingface.co/abhigoyal/EAGLE-LLaMA3-Instruct-8B-vllm # Also, here's an example script for converting train...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Eagle reformat checkpoint compatible with Vllm stale ### Anything you want to discuss about vllm. As per the current eagle implementation in Vllm, the checkpoint must strictly adhere to the vllm format which won...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
