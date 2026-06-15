# vllm-project/vllm#31296: [Bug]: Streaming output issue in vLLM v0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#31296](https://github.com/vllm-project/vllm/issues/31296) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Streaming output issue in vLLM v0.10.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying the Qwen3-Coder-480B-A35B-Instruct-FP8 model using vLLM v0.10.2 with the command below, I encountered an issue where the streaming output is inconsistent. Specifically, when using the streaming API, the returned content does not match the token count, and there is a noticeable loss of output during transmission. python3 -m vllm.entrypoints.openai.api_server --model /data/model/shared/Qwen3-Coder-480B-A35B-Instruct-FP8--49a7790-C7/LFS --served-model-name default --gpu-memory-utilization 0.9 --enable-chunked-prefill --enable-auto-tool-choice --tool-call-parser qwen3_coder --max-num-batched-tokens 100000 --max-model-len 131072 --tensor-parallel-size 8 --enable-expert-parallel --host 0.0.0.0 --port 48000 --enable-prefix-caching --trust-remote-code --max-num-seqs 128 >> $log_path 2>&1 & ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tch the token count, and there is a noticeable loss of output during transmission. python3 -m vllm.entrypoints.openai.api_server --model /data/model/shared/Qwen3-Coder-480B-A35B-Instruct-FP8--49a7790-C7/LFS --served-mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment ### 🐛 Describe the bug When deploying the Qwen3-Coder-480B-A35B-Instruct-FP8 model using vLLM v0.10.2 with the command below, I encountered an issue where the streaming output is inconsistent. S...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Streaming output issue in vLLM v0.10.2 bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the Qwen3-Coder-480B-A35B-Instruct-FP8 model using vLLM v0.10.2 with the command below, I encoun...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: w, I encountered an issue where the streaming output is inconsistent. Specifically, when using the streaming API, the returned content does not match the token count, and there is a noticeable loss of output during tran...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ## 🐛 Describe the bug When deploying the Qwen3-Coder-480B-A35B-Instruct-FP8 model using vLLM v0.10.2 with the command below, I encountered an issue where the streaming output is inconsistent. Specifically, when using th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
