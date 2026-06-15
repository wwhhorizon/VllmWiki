# vllm-project/vllm#4124: [Feature]: Support HuggingFaceM4/idefics2-8b as vision model

| 字段 | 值 |
| --- | --- |
| Issue | [#4124](https://github.com/vllm-project/vllm/issues/4124) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support HuggingFaceM4/idefics2-8b as vision model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I know even llava 1.6 isn't in, but benchmarks for this model are much better. https://huggingface.co/HuggingFaceM4/idefics2-8b https://huggingface.co/blog/idefics2 ![image](https://github.com/vllm-project/vllm/assets/2249614/539c9454-2933-481c-9765-a82b14bc182a) TGI support coming according to model card discussion, but no PR in TGI yet for 2, but seems idefics is there. ### Alternatives llava1.6, but maybe obsolete by now. ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support HuggingFaceM4/idefics2-8b as vision model feature request;stale ### 🚀 The feature, motivation and pitch I know even llava 1.6 isn't in, but benchmarks for this model are much better. https://huggingfa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support HuggingFaceM4/idefics2-8b as vision model feature request;stale ### 🚀 The feature, motivation and pitch I know even llava 1.6 isn't in, but benchmarks for this model are much better. https://huggingfa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 🚀 The feature, motivation and pitch I know even llava 1.6 isn't in, but benchmarks for this model are much better. https://huggingface.co/HuggingFaceM4/idefics2-8b https://huggingface.co/blog/idefics2 ![image](https://g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
