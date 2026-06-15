# vllm-project/vllm#15976: [Bug]: vllm==0.8.2, when using the "bad_words" argument of SamplingParams, there is CUDA out of memory issue at ParallelSampleSequenceGroup's deepcopy

| 字段 | 值 |
| --- | --- |
| Issue | [#15976](https://github.com/vllm-project/vllm/issues/15976) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm==0.8.2, when using the "bad_words" argument of SamplingParams, there is CUDA out of memory issue at ParallelSampleSequenceGroup's deepcopy

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - I tried to add a list of bad_words to Qwen2-VL because sometimes it might output special tokens (which I don't want). - The list only contains five special tokens, which is not long. (below is how I added it) ``` sampling_kwargs = {"max_tokens": config.response_length, "detokenize": False, "bad_words": [" ", " ", " ", " ", " "]} ``` - However, during the handling of the sampling params, it seems that some deepcopy is needed. It only needs 2MB of CUDA memory, but that caused OOM. - I already set the gpu_memory_utilization to 0.4, which is quite low. It still doesn't help. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: add a list of bad_words to Qwen2-VL because sometimes it might output special tokens (which I don't want). - The list only contains five special tokens, which is not long. (below is how I added it) ``` sampling_kwargs =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ==0.8.2, when using the "bad_words" argument of SamplingParams, there is CUDA out of memory issue at ParallelSampleSequenceGroup's deepcopy bug;stale ### Your current environment ### 🐛 Describe the bug - I tried to add...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ment ### 🐛 Describe the bug - I tried to add a list of bad_words to Qwen2-VL because sometimes it might output special tokens (which I don't want). - The list only contains five special tokens, which is not long. (below...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s CUDA out of memory issue at ParallelSampleSequenceGroup's deepcopy bug;stale ### Your current environment ### 🐛 Describe the bug - I tried to add a list of bad_words to Qwen2-VL because sometimes it might output speci...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: me deepcopy is needed. It only needs 2MB of CUDA memory, but that caused OOM. - I already set the gpu_memory_utilization to 0.4, which is quite low. It still doesn't help. ### Before submitting a new issue... - [x] Make...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
