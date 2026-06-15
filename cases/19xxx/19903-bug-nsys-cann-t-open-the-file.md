# vllm-project/vllm#19903: [Bug]: nsys cann't open the file

| 字段 | 值 |
| --- | --- |
| Issue | [#19903](https://github.com/vllm-project/vllm/issues/19903) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nsys cann't open the file

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when I use NCCL_IB_HCA="mlx5_0,mlx5_1" NCCL_SOCKET_IFNAME=bond0 NCCL_DEBUG=INFO VLLM_LOGGING_LEVEL=DEBUG GLOO_SOCKET_IFNAME=bond0 nsys launch --cuda-graph-trace=node --session-new test --trace-fork-before-exec=true vllm serve /home/models/DeepSeek-V2-Lite --trust-remote-code --tensor-parallel-size 8 --max-model-len 65536 --disable-log-requests --enable-expert-parallel --disable-custom_all-reduce nsys start --session test --output report nsys stop --session test No matter the size of the file, it always consumes up to 40GB of memory during the opening process, and it crashes with an error when there is no more memory available. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_erro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: nsys cann't open the file bug;stale ### Your current environment ### 🐛 Describe the bug when I use NCCL_IB_HCA="mlx5_0,mlx5_1" NCCL_SOCKET_IFNAME=bond0 NCCL_DEBUG=INFO VLLM_LOGGING_LEVEL=DEBUG GLOO_SOCKET_IFNAME=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: BUG=INFO VLLM_LOGGING_LEVEL=DEBUG GLOO_SOCKET_IFNAME=bond0 nsys launch --cuda-graph-trace=node --session-new test --trace-fork-before-exec=true vllm serve /home/models/DeepSeek-V2-Lite --trust-remote-code --tensor-paral...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: or-parallel-size 8 --max-model-len 65536 --disable-log-requests --enable-expert-parallel --disable-custom_all-reduce nsys start --session test --output report nsys stop --session test No matter the size of the file, it...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
