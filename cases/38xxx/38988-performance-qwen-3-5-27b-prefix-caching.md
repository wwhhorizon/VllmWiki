# vllm-project/vllm#38988: [Performance]: Qwen 3.5 27B Prefix Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#38988](https://github.com/vllm-project/vllm/issues/38988) |
| 状态 | open |
| 标签 | performance |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Qwen 3.5 27B Prefix Caching

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression There have been discussions if Qwen 3.5 (27B) supports prefix caching in vLLM. - https://www.reddit.com/r/LocalLLaMA/comments/1rplb3r/vllm_prefix_caching_cannot_be_used_with_qwen_35/ - #36010 I would appreciate information on this issue. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Qwen 3.5 27B Prefix Caching performance ### Proposal to improve performance _No response_ ### Report of performance regression There have been discussions if Qwen 3.5 (27B) supports prefix caching in vLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression There have been discussions if Qwen 3.5 (27B) supports prefix caching in vLLM. - https://www.reddit.com/r/LocalLLaMA/comments/1rplb3r/vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm_prefix_caching_cannot_be_used_with_qwen_35/ - #36010 I would appreciate information on this issue. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```tex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
