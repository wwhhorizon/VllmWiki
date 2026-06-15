# vllm-project/vllm#12274: [Performance]: why vllm-0.6.1.post2 faster than latest vllm=0.6.6.post1?

| 字段 | 值 |
| --- | --- |
| Issue | [#12274](https://github.com/vllm-project/vllm/issues/12274) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: why vllm-0.6.1.post2 faster than latest vllm=0.6.6.post1?

### Issue 正文摘录

### Your current environment old: vllm-0.6.1.post2 new: vllm=0.6.6.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the previous version of vllm-0.6.1.post2 and I did benchmark to get the max TTFT and then I upgrade to the latest vllm=0.6.6.post1, but when I did the benchmark again I see a huge difference in the performance regarding the TTFT! benchmarking llama3.1-70b-awq model, with 20 1k request on 4gpus, the max TTFT was 10 seconds for the previous vllm but with the latest vllm it increased to be 37 seconds!! Any thoughts why this huge difference in TTFT here? Do I miss any configs or args to be set to make it faster? Thanks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment old: vllm-0.6.1.post2 new: vllm=0.6.6.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the previous version of vllm-0.6.1.post2 and I did benchmark to get the max TTFT and then...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: why vllm-0.6.1.post2 faster than latest vllm=0.6.6.post1? performance;stale ### Your current environment old: vllm-0.6.1.post2 new: vllm=0.6.6.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: why vllm-0.6.1.post2 faster than latest vllm=0.6.6.post1? performance;stale ### Your current environment old: vllm-0.6.1.post2 new: vllm=0.6.6.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Input Dumps _No response_ ### 🐛 Describe the bug I used the previous version of vllm-0.6.1.post2 and I did benchmark to get the max TTFT and then I upgrade to the latest vllm=0.6.6.post1, but when I did the benchmark ag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
