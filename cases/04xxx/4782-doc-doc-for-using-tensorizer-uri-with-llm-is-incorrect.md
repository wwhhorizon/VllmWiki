# vllm-project/vllm#4782: [Doc]: Doc for using tensorizer_uri with LLM is incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#4782](https://github.com/vllm-project/vllm/issues/4782) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Doc for using tensorizer_uri with LLM is incorrect

### Issue 正文摘录

### 📚 The doc issue This code snippiet doesn't work - tensorizer_uri doesn't exist as a parameter llm = LLM(model="facebook/opt-125m", load_format="tensorizer", tensorizer_uri=path_to_opt_tensors, num_readers=3, vllm_tensorized=True) https://github.com/vllm-project/vllm/blob/702bee461f448b0186eb9d673baad29fd923c884/examples/tensorize_vllm_model.py#L91 ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: et doesn't work - tensorizer_uri doesn't exist as a parameter llm = LLM(model="facebook/opt-125m", load_format="tensorizer", tensorizer_uri=path_to_opt_tensors, num_readers=3, vllm_tensorized=True) https://github.com/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
