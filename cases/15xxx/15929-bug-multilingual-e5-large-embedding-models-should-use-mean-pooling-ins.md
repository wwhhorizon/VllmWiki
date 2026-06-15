# vllm-project/vllm#15929: [Bug]: multilingual-e5-large embedding models should use mean pooling instead of the last

| 字段 | 值 |
| --- | --- |
| Issue | [#15929](https://github.com/vllm-project/vllm/issues/15929) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: multilingual-e5-large embedding models should use mean pooling instead of the last

### Issue 正文摘录

### Your current environment I am using docker env for vLLM: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug I launched openai-compatible inference server on k8s cluster serving `intfloat/multilingual-e5-large-instruct` model. This is XLMRobertaModel type which is supposed to be using mean pooling instead of last pooling. But I confirmed that the result I get from vllm server matches the one that I can get normalizing the last hidden state. I think this must have been addressed from https://github.com/vllm-project/vllm/pull/9387, but apparently it's not. The command I used to launch is "python -m vllm.entrypoints.openai.api_server --model /mnt/models/e5-large ..." and the directory under `/mnt/models/e5-large` looks like this: ``` ❯ ls -laRX . drwxr-xr-x - jisoo 1 Apr 15:00 . drwxr-xr-x - jisoo 1 Apr 13:45 .. drwxr-xr-x - jisoo 1 Apr 15:00 1_Pooling lrw-r--r-- 690 jisoo 1 Apr 13:45 config.json lrw-r--r-- 1.1G jisoo 1 Apr 13:45 model.safetensors lrw-r--r-- 349 jisoo 1 Apr 15:00 modules.json lrw-r--r-- 53 jisoo 1 Apr 15:00 sentence_xlm-roberta_config.json lrw-r--r-- 5.1M jisoo 1 Apr 13:45 sentencepiece.bpe.model lrw-r--r-- 964 jisoo 1 Apr 13:45 special_tokens_map.json lrw-r--r-- 17M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: instead of the last bug;stale ### Your current environment I am using docker env for vLLM: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug I launched openai-compatible inference server on k8s cluster serving `intfloat/mu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: multilingual-e5-large embedding models should use mean pooling instead of the last bug;stale ### Your current environment I am using docker env for vLLM: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug I launched...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ``` { "word_embedding_dimension": 1024, "pooling_mode_cls_token": false, "pooling_mode_mean_tokens": true, "pooling_mode_max_tokens": false, "pooling_mode_mean_sqrt_len_tokens": false, "pooling_mode_weightedmean_tokens"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 5-large embedding models should use mean pooling instead of the last bug;stale ### Your current environment I am using docker env for vLLM: vllm/vllm-openai:v0.7.1 ### 🐛 Describe the bug I launched openai-compatible inf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
