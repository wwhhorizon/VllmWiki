# vllm-project/vllm#36207: [Bug]: kimi-2.5 reasoning_parser error.

| 字段 | 值 |
| --- | --- |
| Issue | [#36207](https://github.com/vllm-project/vllm/issues/36207) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kimi-2.5 reasoning_parser error.

### Issue 正文摘录

### Your current environment vllm_0.15.0 ### 🐛 Describe the bug launch_args: --tensor-parallel-size 8 --gpu-memory-utilization 0.75 --host xxxxx --port xxxxx --served-model-name xxxxx --trust-remote-code --enable-expert-parallel --mm-encoder-tp-mode data --data-parallel-size 4 --data-parallel-size-local 1 --data-parallel-address xxxxx --data-parallel-rpc-port xxxx --enable-auto-tool-choice --tool-call-parser kimi_k2 the answer: `"message":{"content":" The user said \"hello\" - this is a greeting. I should respond with a friendly, professional greeting while being concise and helpful. Hello! How can I help you today?","role":"assistant"},` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . I should respond with a friendly, professional greeting while being concise and helpful. Hello! How can I help you today?","role":"assistant"},` ### Before submitting a new issue... - [x] Make sure you already searche...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: },` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: u-memory-utilization 0.75 --host xxxxx --port xxxxx --served-model-name xxxxx --trust-remote-code --enable-expert-parallel --mm-encoder-tp-mode data --data-parallel-size 4 --data-parallel-size-local 1 --data-parallel-ad...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: -port xxxxx --served-model-name xxxxx --trust-remote-code --enable-expert-parallel --mm-encoder-tp-mode data --data-parallel-size 4 --data-parallel-size-local 1 --data-parallel-address xxxxx --data-parallel-rpc-port xxx...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
