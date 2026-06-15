# vllm-project/vllm#9388: [Feature]: Support sentence-transformers configuration files

| 字段 | 值 |
| --- | --- |
| Issue | [#9388](https://github.com/vllm-project/vllm/issues/9388) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support sentence-transformers configuration files

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently support for sentence transformer models being added in PRs such as https://github.com/vllm-project/vllm/pull/9056. However, these models come with extra configuration files for settings such as the pooling method and whether normalization of embeddings has to be done. There is a `modules.json` file as such as [this one](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/blob/main/modules.json_ containing configuration of layers: ``` [ { "idx": 0, "name": "0", "path": "", "type": "sentence_transformers.models.Transformer" }, { "idx": 1, "name": "1", "path": "1_Pooling", "type": "sentence_transformers.models.Pooling" }, { "idx": 2, "name": "2", "path": "2_Normalize", "type": "sentence_transformers.models.Normalize" } ] ``` The path refers to a directory that can be empty or non-existent in the case of default parameters. For example, in the case of the model above, `1_Pooling` contains a `config.json` file with the following: ``` { "word_embedding_dimension": 384, "pooling_mode_cls_token": false, "pooling_mode_mean_tokens": true, "pooling_mode_max_tokens": false, "pooling_mode_mean_sqrt_len_tokens": false } ``` Currently t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support sentence-transformers configuration files feature request ### 🚀 The feature, motivation and pitch Currently support for sentence transformer models being added in PRs such as https://github.com/vllm-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : ``` { "word_embedding_dimension": 384, "pooling_mode_cls_token": false, "pooling_mode_mean_tokens": true, "pooling_mode_max_tokens": false, "pooling_mode_mean_sqrt_len_tokens": false } ``` Currently the implementation...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support sentence-transformers configuration files feature request ### 🚀 The feature, motivation and pitch Currently support for sentence transformer models being added in PRs such as https://github.com/vllm-p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
