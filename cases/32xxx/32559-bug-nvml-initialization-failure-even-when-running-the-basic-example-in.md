# vllm-project/vllm#32559: [Bug]: NVML initialization failure even when running the basic example in the WSL platform

| 字段 | 值 |
| --- | --- |
| Issue | [#32559](https://github.com/vllm-project/vllm/issues/32559) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVML initialization failure even when running the basic example in the WSL platform

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Even when running the very basic example [here](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/basic.py): ```bash (vllm) $ python examples/offline_inference/basic/basic.py ``` I got: I investigated this issue and here is the bare minimum script to reproduce this failure: based on what I found, the NVML initialization failure is related to the `fork` multiprocess method in the WSL platform: - This NVML initialization failure only happens in the child process, which can be seen from the reproduce script above - I printed the `mp_method` [here](https://github.com/vllm-project/vllm/blob/main/vllm/utils/system_utils.py#L156) and it's `fork`. If I hardcode the `mp_method` to be `spawn`, all above command (incl the example) can pass. This approves the issue is related to the `fork` method. - I also tried to run the same command in a plain Linux env and everything works fine (and it's using `fork` too). This approves the `nvml` + `fork` issue only happens on WSL Please let me know if the above RCA makes sense. I'll raise a PR to update the [`_maybe_force_spawn`](https://github.com/vllm-project/vllm/blob/m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory cuda;operator;quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ted_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory cuda;operator;quantization;triton build_error;crash;slowdown dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: orm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory cuda;operator;quantization;triton build_error;crash;slowdown dtype;env...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;moe;quantization;scheduler_memory cuda;operator;quantization;triton build_error;crash;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
