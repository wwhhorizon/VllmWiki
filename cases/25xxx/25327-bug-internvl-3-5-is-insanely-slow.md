# vllm-project/vllm#25327: [Bug]: InternVL 3.5 is insanely slow

| 字段 | 值 |
| --- | --- |
| Issue | [#25327](https://github.com/vllm-project/vllm/issues/25327) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | gemm |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL 3.5 is insanely slow

### Issue 正文摘录

### Your current environment vllm==0.10.0 ### 🐛 Describe the bug When I run ``` vllm serve OpenGVLab/InternVL3_5-4B --uvicorn-log-level=info --host 0.0.0.0 --port 8000 --max-model-len 32768 --api-key APIKEY --trust-remote-code --limit-mm-per-prompt.image 1 --no-enforce-eager --tensor-parallel-size 1 ``` on a H100 node, inference speed is quite slow. Is it due to the model? (I need the long context abilities so that's why I set 32k) It's taking 10 seconds for 6k input tokens and <200 output tokens. Not sure what is wrong. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: InternVL 3.5 is insanely slow bug;stale ### Your current environment vllm==0.10.0 ### 🐛 Describe the bug When I run ``` vllm serve OpenGVLab/InternVL3_5-4B --uvicorn-log-level=info --host 0.0.0.0 --port 8000 --ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: per-prompt.image 1 --no-enforce-eager --tensor-parallel-size 1 ``` on a H100 node, inference speed is quite slow. Is it due to the model? (I need the long context abilities so that's why I set 32k) It's taking 10 second...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: rformance distributed_parallel;frontend_api;model_support;multimodal_vlm gemm slowdown Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: InternVL 3.5 is insanely slow bug;stale ### Your current environment vllm==0.10.0 ### 🐛 Describe the bug When I run ``` vllm serve OpenGVLab/InternVL3_5-4B --uvicorn-log-level=info --host 0.0.0.0 --port 8000 --ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;model_support;multimodal_vlm gemm slowd...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
