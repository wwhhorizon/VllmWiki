# vllm-project/vllm#10078: [Doc]: openai_chat_completion_client_for_multimodal.py error

| 字段 | 值 |
| --- | --- |
| Issue | [#10078](https://github.com/vllm-project/vllm/issues/10078) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: openai_chat_completion_client_for_multimodal.py error

### Issue 正文摘录

### 📚 The doc issue vllm serve microsoft/Phi-3.5-vision-instruct --dtype auto --trust-remote-code --max_model_len 8192 --limit-mm-per-prompt image=2 raise self._make_status_error_from_response(err.response) from None openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': "[{'type': 'extra_forbidden', 'loc': ('body', 'max_completion_tokens'), 'msg': 'Extra inputs are not permitted', 'input': 64}]", 'type': 'BadRequestError', 'param': None, 'code': 400} ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: openai_chat_completion_client_for_multimodal.py error documentation ### 📚 The doc issue vllm serve microsoft/Phi-3.5-vision-instruct --dtype auto --trust-remote-code --max_model_len 8192 --limit-mm-per-prompt ima...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: on ### 📚 The doc issue vllm serve microsoft/Phi-3.5-vision-instruct --dtype auto --trust-remote-code --max_model_len 8192 --limit-mm-per-prompt image=2 raise self._make_status_error_from_response(err.response) from None...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: self._make_status_error_from_response(err.response) from None openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': "[{'type': 'extra_forbidden', 'loc': ('body', 'max_completion_tokens'), 'msg': 'Extr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
