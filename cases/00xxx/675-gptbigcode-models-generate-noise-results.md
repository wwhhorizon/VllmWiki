# vllm-project/vllm#675: GPTBigCode models generate noise results

| 字段 | 值 |
| --- | --- |
| Issue | [#675](https://github.com/vllm-project/vllm/issues/675) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPTBigCode models generate noise results

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/aa84c92ef636e689b506b9842c712e5c615cc73a/vllm/config.py#L101 Adding conditions for falcon models seems break inference for GPTBigCode models. It worked well on commit df5dd3c68ec7007e4b3a27907f4d954f1c7d511d, but broke on commit aa84c92ef636e689b506b9842c712e5c615cc73a. I have tried WizardCoder 15B, if I change the condition ```python if (getattr(self.hf_config, "multi_query", False) and (self.hf_config.model_type == "falcon" and not getattr(self.hf_config, "new_decoder_architecture", False))): ``` into ```python if getattr(self.hf_config, "multi_query", False): ``` , it works well. I'm not sure whether this is a bug, or I just need some extra configuration?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: GPTBigCode models generate noise results https://github.com/vllm-project/vllm/blob/aa84c92ef636e689b506b9842c712e5c615cc73a/vllm/config.py#L101 Adding conditions for falcon models seems break inference for GPTBigCode mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pe == "falcon" and not getattr(self.hf_config, "new_decoder_architecture", False))): ``` into ```python if getattr(self.hf_config, "multi_query", False): ``` , it works well. I'm not sure whether this is a bug, or I jus...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nge the condition ```python if (getattr(self.hf_config, "multi_query", False) and (self.hf_config.model_type == "falcon" and not getattr(self.hf_config, "new_decoder_architecture", False))): ``` into ```python if getatt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model_type == "falcon" and not getattr(self.hf_config, "new_decoder_architecture", False))): ``` into ```python if getattr(self.hf_config, "multi_query", False): ``` , it works well. I'm not sure whether this is a bug,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
