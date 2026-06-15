# vllm-project/vllm#35718: [Bug]: Garbled / gibberish output after serving Kimi-K2.5 with vLLM on 8×H200 (INT4) for some time

| 字段 | 值 |
| --- | --- |
| Issue | [#35718](https://github.com/vllm-project/vllm/issues/35718) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Garbled / gibberish output after serving Kimi-K2.5 with vLLM on 8×H200 (INT4) for some time

### Issue 正文摘录

### Your current environment - GPUs: 8× NVIDIA H200 - Serving: vLLM OpenAI server - Container image: vllm-openai:nightly-8fae54faff485e446dc8d1a700417f07659ef89e - CUDA libs mounted via LD_LIBRARY_PATH=/usr/local/cuda - 12.9/compat:/usr/local/nvidia/lib64:/usr/local/cuda/lib64 - Model: moonshotai/Kimi-K2.5 (local volume mount) ### 🐛 Describe the bug I’m serving Kimi-K2.5 on a single machine with 8× NVIDIA H200 using vLLM (OpenAI-compatible server). The service runs normally at first, but after running for a while the model sometimes starts returning garbled / nonsensical text (looks like random multilingual fragments, broken tokens, and junk characters). This happens in the reasoning field (and the response becomes unreadable / meaningless). The deployment generally follows the Kimi-K2.5 recommended inference engines (vLLM is listed as recommended in the repo README). ￼ ``` version: "3.9" services: kimi_k25_int4: image: vllm-openai:nightly-8fae54faff485e446dc8d1a700417f07659ef89e container_name: kimi-k25 ipc: host ports: - "40000:8000" environment: - LD_LIBRARY_PATH=/usr/local/cuda-12.9/compat:/usr/local/nvidia/lib64:/usr/local/cuda/lib64 deploy: resources: reservations: devices:...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er image: vllm-openai:nightly-8fae54faff485e446dc8d1a700417f07659ef89e - CUDA libs mounted via LD_LIBRARY_PATH=/usr/local/cuda - 12.9/compat:/usr/local/nvidia/lib64:/usr/local/cuda/lib64 - Model: moonshotai/Kimi-K2.5 (l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: erence engines (vLLM is listed as recommended in the repo README). ￼ ``` version: "3.9" services: kimi_k25_int4: image: vllm-openai:nightly-8fae54faff485e446dc8d1a700417f07659ef89e container_name: kimi-k25 ipc: host por...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Garbled / gibberish output after serving Kimi-K2.5 with vLLM on 8×H200 (INT4) for some time bug ### Your current environment - GPUs: 8× NVIDIA H200 - Serving: vLLM OpenAI server - Container image: vllm-openai:nightly-8f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: local/cuda - 12.9/compat:/usr/local/nvidia/lib64:/usr/local/cuda/lib64 - Model: moonshotai/Kimi-K2.5 (local volume mount) ### 🐛 Describe the bug I’m serving Kimi-K2.5 on a single machine with 8× NVIDIA H200 using vLLM (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
