# vllm-project/vllm#43605: [Bug]: MiniMax M2.5 TP8EP8 gfx950 with AITER causes memory access fault

| 字段 | 值 |
| --- | --- |
| Issue | [#43605](https://github.com/vllm-project/vllm/issues/43605) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;moe |
| 子分类 |  |
| Operator 关键词 | kernel;moe |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniMax M2.5 TP8EP8 gfx950 with AITER causes memory access fault

### Issue 正文摘录

### Your current environment - vllm/vllm-openai-rocm:v0.21.0 - 8xMI355 node ### 🐛 Describe the bug Running MiniMax M2.5 on MI355X with TP8EP8 causes memory fault during startup: ``` docker run \ --device=/dev/kfd \ --device=/dev/dri \ --security-opt seccomp=unconfined \ --group-add video \ --privileged \ --ipc=host -p 8000:8000 \ -v /it-share/data/:/root/.cache/huggingface \ -e HF_HUB_OFFLINE=1 \ -e VLLM_ROCM_USE_AITER=1 \ -e VLLM_ROCM_SHUFFLE_KV_CACHE_LAYOUT=1 \ vllm/vllm-openai-rocm:latest \ MiniMaxAI/MiniMax-M2.5 \ --trust-remote-code \ --tensor-parallel-size 8 \ --enable-expert-parallel ``` I was able to "resolve" the issue by temporarily setting `--max-num-batched-tokens 4K`, so I suspect this is an issue with the M=8k shape in AITER fmoe kernel. Alternatively it could be resolved by VLLM_ROCM_USE_AITER_MOE=0. See error in comment below ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: niMax M2.5 on MI355X with TP8EP8 causes memory fault during startup: ``` docker run \ --device=/dev/kfd \ --device=/dev/dri \ --security-opt seccomp=unconfined \ --group-add video \ --privileged \ --ipc=host -p 8000:800...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g]: MiniMax M2.5 TP8EP8 gfx950 with AITER causes memory access fault bug;rocm ### Your current environment - vllm/vllm-openai-rocm:v0.21.0 - 8xMI355 node ### 🐛 Describe the bug Running MiniMax M2.5 on MI355X with TP8EP8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ileged \ --ipc=host -p 8000:8000 \ -v /it-share/data/:/root/.cache/huggingface \ -e HF_HUB_OFFLINE=1 \ -e VLLM_ROCM_USE_AITER=1 \ -e VLLM_ROCM_SHUFFLE_KV_CACHE_LAYOUT=1 \ vllm/vllm-openai-rocm:latest \ MiniMaxAI/MiniMax...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: x-M2.5 \ --trust-remote-code \ --tensor-parallel-size 8 \ --enable-expert-parallel ``` I was able to "resolve" the issue by temporarily setting `--max-num-batched-tokens 4K`, so I suspect this is an issue with the M=8k...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: MiniMax M2.5 TP8EP8 gfx950 with AITER causes memory access fault bug;rocm ### Your current environment - vllm/vllm-openai-rocm:v0.21.0 - 8xMI355 node ### 🐛 Describe the bug Running MiniMax M2.5 on MI355X with TP8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
