# vllm-project/vllm#12827: [Bug]: Runtime error occurs when running deepseek v3

| 字段 | 值 |
| --- | --- |
| Issue | [#12827](https://github.com/vllm-project/vllm/issues/12827) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Runtime error occurs when running deepseek v3

### Issue 正文摘录

### Your current environment When I use the following command： python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9111 --model /deepseek_v3 --max-num-batched-tokens 16384 --gpu-memory-utilization 0.97 --tensor-parallel-size 8 --disable-log-requests --trust-remote-code --enable-chunked-prefill it shows runtimeerror: nccl error 1:unhandled cuda error (run with nccl_debug=info for details) model: deepseek v3 vllm : v0.7.1--->pip3 install vllm how can i do? ![Image](https://github.com/user-attachments/assets/38427d33-1fb5-435c-a537-95a2b736250b) ![Image](https://github.com/user-attachments/assets/b18f8b9f-b58a-48cd-bba2-3d3bec2dc664) ### 🐛 Describe the bug When I use the following command： python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9111 --model /deepseek_v3 --max-num-batched-tokens 16384 --gpu-memory-utilization 0.97 --tensor-parallel-size 8 --disable-log-requests --trust-remote-code --enable-chunked-prefill it shows runtimeerror: nccl error 1:unhandled cuda error (run with nccl_debug=info for details) model: deepseek v3 vllm : v0.7.1--->pip3 install vllm how can i do? ### Before submitting a new issue... - [x] Make sure you already searched f...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Runtime error occurs when running deepseek v3 bug;stale ### Your current environment When I use the following command： python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9111 --model /deepseek_v3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --enable-chunked-prefill it shows runtimeerror: nccl error 1:unhandled cuda error (run with nccl_debug=info for details) model: deepseek v3 vllm : v0.7.1--->pip3 install vllm how can i do? ![Image](https://github.com/us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: h nccl_debug=info for details) model: deepseek v3 vllm : v0.7.1--->pip3 install vllm how can i do? ![Image](https://github.com/user-attachments/assets/38427d33-1fb5-435c-a537-95a2b736250b) ![Image](https://github.com/us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: thon3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9111 --model /deepseek_v3 --max-num-batched-tokens 16384 --gpu-memory-utilization 0.97 --tensor-parallel-size 8 --disable-log-requests --trust-remote-cod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;model_support cuda Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
