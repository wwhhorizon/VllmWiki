# vllm-project/vllm#3036: Tokenization Issue for google/gemma-7b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#3036](https://github.com/vllm-project/vllm/issues/3036) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tokenization Issue for google/gemma-7b-it

### Issue 正文摘录

Hello All I am trying deploy Gemm-7b-it model using vllm but when the Engine tries to download the tokenizer I am getting an error: OSError: Can't load tokenizer for 'google/gemma-7b-it'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'google/gemma-7b-it' is the correct path to a directory containing all relevant files for a GemmaTokenizerFast tokenizer. I am also attaching a screenshot of the error. Any help would be appreciated. ![Screenshot 2024-02-26 at 13 39 25](https://github.com/vllm-project/vllm/assets/51020974/d2d94b93-de63-4f05-a27b-f03b7c42c9b4)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Tokenization Issue for google/gemma-7b-it Hello All I am trying deploy Gemm-7b-it model using vllm but when the Engine tries to download the tokenizer I am getting an error: OSError: Can't load tokenizer for 'google/gem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: I am also attaching a screenshot of the error. Any help would be appreciated. ![Screenshot 2024-02-26 at 13 39 25](https://github.com/vllm-project/vllm/assets/51020974/d2d94b93-de63-4f05-a27b-f03b7c42c9b4)
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Tokenization Issue for google/gemma-7b-it Hello All I am trying deploy Gemm-7b-it model using vllm but when the Engine tries to download the tokenizer I am getting an error: OSError: Can't load tokenizer for 'google/gem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
