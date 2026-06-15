# vllm-project/vllm#171: Load from HF format models doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#171](https://github.com/vllm-project/vllm/issues/171) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Load from HF format models doesn't work

### Issue 正文摘录

Running it on HF transformers models on the hub seems to break on : else: for bin_file in hf_bin_files: state = torch.load(bin_file, map_location="cpu") for name, param in state.items(): yield name, param Probably because it needs to call model.load_state_dict(torch.load(bin_file, map_location="cpu")) from huggingface model. The exact error is: AttributeError: 'TrainingArguments' object has no attribute 'items' Is this an error on my end or does this apply to all HF-format models on the hub?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Load from HF format models doesn't work Running it on HF transformers models on the hub seems to break on : else: for bin_file in hf_bin_files: state = torch.load(bin_file, map_location="cpu")
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: unning it on HF transformers models on the hub seems to break on : else: for bin_file in hf_bin_files: state = torch.load(bin_file, map_location="cpu") for name, param in state.items(): yield name, param Probably becaus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
