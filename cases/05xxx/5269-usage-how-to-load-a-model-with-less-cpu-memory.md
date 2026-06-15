# vllm-project/vllm#5269: [Usage]: How to load a model with less CPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#5269](https://github.com/vllm-project/vllm/issues/5269) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to load a model with less CPU memory

### Issue 正文摘录

### Your current environment none ### How would you like to use vllm When I load qwen1.5 32b bf16 with 32GB CPU memory, it is always insufficient, while 64GB can handle it. But 32GB works with hf from_pretrained. How can I run vllm with less CPU memory? Thanks~~~

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to load a model with less CPU memory usage ### Your current environment none ### How would you like to use vllm When I load qwen1.5 32b bf16 with 32GB CPU memory, it is always insufficient, while 64GB can h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: When I load qwen1.5 32b bf16 with 32GB CPU memory, it is always insufficient, while 64GB can handle it. But 32GB works with hf from_pretrained. How can I run vllm with less CPU memory? Thanks~~~
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nment none ### How would you like to use vllm When I load qwen1.5 32b bf16 with 32GB CPU memory, it is always insufficient, while 64GB can handle it. But 32GB works with hf from_pretrained. How can I run vllm with less...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
