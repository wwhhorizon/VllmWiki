# vllm-project/vllm#9799: [Misc]: typo: casual instead of causal language model

| 字段 | 值 |
| --- | --- |
| Issue | [#9799](https://github.com/vllm-project/vllm/issues/9799) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: typo: casual instead of causal language model

### Issue 正文摘录

### Anything you want to discuss about vllm. There is a typo in the class names `NeuronCasualLM` and `OpenVINOCasualLM` in files [vllm/model_executor/model_loader/neuron.py](https://github.com/vllm-project/vllm/blob/09500f7ddeb974730972fd9284bd93c08a557cf6/vllm/model_executor/model_loader/neuron.py#L40) and [vllm/model_executor/model_loader/openvino.py](https://github.com/vllm-project/vllm/blob/09500f7ddeb974730972fd9284bd93c08a557cf6/vllm/model_executor/model_loader/openvino.py#L98). They should read `NeuronCausalLM` and `OpenVINOCausalLM` (causal and not casual). I will address this in a PR shortly.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: typo: casual instead of causal language model ### Anything you want to discuss about vllm. There is a typo in the class names `NeuronCasualLM` and `OpenVINOCasualLM` in files [vllm/model_executor/model_loader/ne...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
