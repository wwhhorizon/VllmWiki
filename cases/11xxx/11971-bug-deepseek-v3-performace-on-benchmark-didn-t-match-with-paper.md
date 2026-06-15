# vllm-project/vllm#11971: [Bug]: Deepseek-v3 performace on benchmark didn't match with paper

| 字段 | 值 |
| --- | --- |
| Issue | [#11971](https://github.com/vllm-project/vllm/issues/11971) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek-v3 performace on benchmark didn't match with paper

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi guys, I used vllm to serve deepseek-v3 while I found the benchmark didn't reproduce the result on paper. Specifically, in my case deepseek-v3 got 82 on CEval comparing to 90 on paper. Are there any details I missed? be willing to reveal any detail of my settings. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Deepseek-v3 performace on benchmark didn't match with paper bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi guys, I used vllm to serve deepseek-v3 while I found the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ys, I used vllm to serve deepseek-v3 while I found the benchmark didn't reproduce the result on paper. Specifically, in my case deepseek-v3 got 82 on CEval comparing to 90 on paper. Are there any details I missed? be wi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -v3 while I found the benchmark didn't reproduce the result on paper. Specifically, in my case deepseek-v3 got 82 on CEval comparing to 90 on paper. Are there any details I missed? be willing to reveal any detail of my...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nchmark didn't match with paper bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi guys, I used vllm to serve deepseek-v3 while I found the benchmark didn't reproduce the resu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
