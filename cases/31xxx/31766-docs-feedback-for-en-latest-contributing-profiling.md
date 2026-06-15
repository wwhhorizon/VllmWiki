# vllm-project/vllm#31766: [Docs] Feedback for `/en/latest/contributing/profiling/`

| 字段 | 值 |
| --- | --- |
| Issue | [#31766](https://github.com/vllm-project/vllm/issues/31766) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Docs] Feedback for `/en/latest/contributing/profiling/`

### Issue 正文摘录

### 📚 The doc issue When I follow this doc and run OpenAI Server[¶](https://docs.vllm.ai/en/latest/contributing/profiling/#openai-server), I found > usage: vllm [-h] [-v] {chat,complete,serve,bench,collect-env,run-batch} ... > vllm: error: unrecognized arguments: --profiler-config {"profiler": "torch", "torch_profiler_dir": "/workspace/vllm_profile"} I want to know if this update in the newer version? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Docs] Feedback for `/en/latest/contributing/profiling/` documentation ### 📚 The doc issue When I follow this doc and run OpenAI Server[¶](https://docs.vllm.ai/en/latest/contributing/profiling/#openai-server), I found >...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "/workspace/vllm_profile"} I want to know if this update in the newer version? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ect-env,run-batch} ... > vllm: error: unrecognized arguments: --profiler-config {"profiler": "torch", "torch_profiler_dir": "/workspace/vllm_profile"} I want to know if this update in the newer version? ### Suggest a po...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
