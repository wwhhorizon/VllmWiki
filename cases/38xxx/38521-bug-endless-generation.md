# vllm-project/vllm#38521: [Bug]: Endless generation

| 字段 | 值 |
| --- | --- |
| Issue | [#38521](https://github.com/vllm-project/vllm/issues/38521) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Endless generation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading to vllm 0.18.0, we got an endless generation. When asking for a chat completions on the endpoint: /v1/chat/completions, vllm include in response inputs. When we authorize bigger prompt length, vllm never stop generating new tokens and start a solo conversation. We tried loading 2 different models as gguf files: - devstral small 2505 - tinyllama We got no special parameters but tried `--enable-prefix-caching` and `--enable-chunked-prefill` without any sucess. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ersation. We tried loading 2 different models as gguf files: - devstral small 2505 - tinyllama We got no special parameters but tried `--enable-prefix-caching` and `--enable-chunked-prefill` without any sucess. ### Befo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: new tokens and start a solo conversation. We tried loading 2 different models as gguf files: - devstral small 2505 - tinyllama We got no special parameters but tried `--enable-prefix-caching` and `--enable-chunked-prefi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nt models as gguf files: - devstral small 2505 - tinyllama We got no special parameters but tried `--enable-prefix-caching` and `--enable-chunked-prefill` without any sucess. ### Before submitting a new issue... - [x] M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ial parameters but tried `--enable-prefix-caching` and `--enable-chunked-prefill` without any sucess. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
