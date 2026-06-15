# vllm-project/vllm#13656: [Bug]: v0.7.3 can't work on wsl-ubuntu mirrored network

| 字段 | 值 |
| --- | --- |
| Issue | [#13656](https://github.com/vllm-project/vllm/issues/13656) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.7.3 can't work on wsl-ubuntu mirrored network

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While using vllm to start a inference service, it worked fine on v0.7.2, but after ugrade to v0.7.3, the api endpoint is not accessable, the network to 8000 is not working. Here is the start command ```shell. vllm serve Qwen/Qwen2.5-VL-7B-Instruct --trust-remote-code --served-model-name gpt-4 --gpu-memory-utilization 0.98 --tensor-parallel-size 4 --port 8000 --api-key sk-123456 --max-model-len 65536 ``` I can see changes of console log, on v0.7.2, “Uvicorn running on" is shown at last, on v0.7.3, “Starting vLLM API server" is shown before "Available routes are". Maybe this change caused the problem. ![Image](https://github.com/user-attachments/assets/2f92e01d-bc5c-4f27-9375-3d393babb4fa) ![Image](https://github.com/user-attachments/assets/d0d2659d-cae1-451b-a1df-ccfe554c19c7) What's more, I'm using wsl ubuntu, using mirrored network. (If I change to bridged network, then v0.7.3 can work. v0.7.2 can work on both mirrored network and bridged network) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rk) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to 8000 is not working. Here is the start command ```shell. vllm serve Qwen/Qwen2.5-VL-7B-Instruct --trust-remote-code --served-model-name gpt-4 --gpu-memory-utilization 0.98 --tensor-parallel-size 4 --port 8000 --api-k...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: v0.7.3 can't work on wsl-ubuntu mirrored network bug;stale ### Your current environment ### 🐛 Describe the bug While using vllm to start a inference service, it worked fine on v0.7.2, but after ugrade to v0.7.3,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
