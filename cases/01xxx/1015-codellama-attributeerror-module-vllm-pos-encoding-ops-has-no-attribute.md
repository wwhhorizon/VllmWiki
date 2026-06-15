# vllm-project/vllm#1015: codellama AttributeError: module 'vllm.pos_encoding_ops' has no attribute 'rotary_embedding'

| 字段 | 值 |
| --- | --- |
| Issue | [#1015](https://github.com/vllm-project/vllm/issues/1015) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> codellama AttributeError: module 'vllm.pos_encoding_ops' has no attribute 'rotary_embedding'

### Issue 正文摘录

vllm version: 90eb3f43ca5228647c834243d98881d53c7745d0 model: https://huggingface.co/codellama/CodeLlama-7b-Python-hf error: ![image](https://github.com/vllm-project/vllm/assets/138603914/35c042d2-b452-430f-acc1-11ef643366ca) Only error in codellama, it's good when i use another model

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: codellama AttributeError: module 'vllm.pos_encoding_ops' has no attribute 'rotary_embedding' vllm version: 90eb3f43ca5228647c834243d98881d53c7745d0 model: https://huggingface.co/codellama/CodeLlama-7b-Python-hf error: !...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: module 'vllm.pos_encoding_ops' has no attribute 'rotary_embedding' vllm version: 90eb3f43ca5228647c834243d98881d53c7745d0 model: https://huggingface.co/codellama/CodeLlama-7b-Python-hf error: ![image](https://github.com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
