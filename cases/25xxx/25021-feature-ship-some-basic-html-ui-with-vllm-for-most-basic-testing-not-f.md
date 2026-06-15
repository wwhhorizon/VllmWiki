# vllm-project/vllm#25021: [Feature]: Ship some basic html UI with vllm for most basic testing (not for prod usage)

| 字段 | 值 |
| --- | --- |
| Issue | [#25021](https://github.com/vllm-project/vllm/issues/25021) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Ship some basic html UI with vllm for most basic testing (not for prod usage)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch E.g. a single index.html webpage which could connect to an existing local `vllm serve ... --cors` instance (or another command serving such index.html page) Or maybe even `https://vllm.ai/chat?url=http://localhost:8000` could work if `vllm serve` sends back CORS-enabled header (when explicitly opted-in). Currently third-party solutions (like gradio/streamlit/open-webui) / dependencies need to be installed even for basic testing... --- Maybe the only foolproofing/"security" feature could be: check for a single-password string (like JupyterLab checks it) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 00` could work if `vllm serve` sends back CORS-enabled header (when explicitly opted-in). Currently third-party solutions (like gradio/streamlit/open-webui) / dependencies need to be installed even for basic testing......
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Ship some basic html UI with vllm for most basic testing (not for prod usage) feature request;unstale ### 🚀 The feature, motivation and pitch E.g. a single index.html webpage which could connect to an existin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ic html UI with vllm for most basic testing (not for prod usage) feature request;unstale ### 🚀 The feature, motivation and pitch E.g. a single index.html webpage which could connect to an existing local `vllm serve ......
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Ship some basic html UI with vllm for most basic testing (not for prod usage) feature request;unstale ### 🚀 The feature, motivation and pitch E.g. a single index.html webpage which could connect to an existin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
