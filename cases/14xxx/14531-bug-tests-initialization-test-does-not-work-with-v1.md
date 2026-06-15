# vllm-project/vllm#14531: [Bug]: [Tests] Initialization Test Does Not Work With V1

| 字段 | 值 |
| --- | --- |
| Issue | [#14531](https://github.com/vllm-project/vllm/issues/14531) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Tests] Initialization Test Does Not Work With V1

### Issue 正文摘录

### Your current environment - Converting over the tests to use V1, this is not working ### 🐛 Describe the bug - works ```bash VLLM_USE_V1=0 pytest -v -x models/test_initialization.py -k "not Cohere" ``` - fails on Grok 1 ```bash VLLM_USE_V1=1 pytest -v -x models/test_initialization.py -k "not Cohere" ``` - works! (this is wild) ```bash VLLM_USE_V1=1 pytest -v -x models/test_initialization.py -k "Grok" ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: king ### 🐛 Describe the bug - works ```bash VLLM_USE_V1=0 pytest -v -x models/test_initialization.py -k "not Cohere" ``` - fails on Grok 1 ```bash VLLM_USE_V1=1 pytest -v -x models/test_initialization.py -k "not Cohere"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: [Tests] Initialization Test Does Not Work With V1 bug ### Your current environment - Converting over the tests to use V1, this is not working ### 🐛 Describe the bug - works ```bash VLLM_USE_V1=0 pytest -v -x mode...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
