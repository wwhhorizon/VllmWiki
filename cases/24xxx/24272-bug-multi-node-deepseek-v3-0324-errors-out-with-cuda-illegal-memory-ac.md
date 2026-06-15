# vllm-project/vllm#24272: [Bug]: Multi-node DeepSeek-V3-0324 errors out with CUDA Illegal Memory Access

| 字段 | 值 |
| --- | --- |
| Issue | [#24272](https://github.com/vllm-project/vllm/issues/24272) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-node DeepSeek-V3-0324 errors out with CUDA Illegal Memory Access

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug cc: @pbelevich I am trying to follow along the example listed [here](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html#single-node-deployment) and extend it to rack scale (GB200 NVL72, 72xB200s). I have a custom docker image that I'm building and using in my AWS env, listed [here](https://github.com/pbelevich/vllm-ep/blob/main/vllm-ep.Dockerfile). Running `nvidia-smi` on a single node, I get: ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.172.08 Driver Version: 570.172.08 CUDA Version: 12.8 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA GB200 On | 00000000:29:00.0 Off | 0 | | N/A 27C P0 174W / 1200W | 0MiB / 189471MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nt) and extend it to rack scale (GB200 NVL72, 72xB200s). I have a custom docker image that I'm building and using in my AWS env, listed [here](https://github.com/pbelevich/vllm-ep/blob/main/vllm-ep.Dockerfile). Running...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Multi-node DeepSeek-V3-0324 errors out with CUDA Illegal Memory Access bug;stale ### Your current environment ### 🐛 Describe the bug cc: @pbelevich I am trying to follow along the example listed [here](https://do...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: w along the example listed [here](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html#single-node-deployment) and extend it to rack scale (GB200 NVL72, 72xB200s). I have a custom docker image that I'm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lti-node DeepSeek-V3-0324 errors out with CUDA Illegal Memory Access bug;stale ### Your current environment ### 🐛 Describe the bug cc: @pbelevich I am trying to follow along the example listed [here](https://docs.vllm.a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ying to follow along the example listed [here](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment.html#single-node-deployment) and extend it to rack scale (GB200 NVL72, 72xB200s). I have a custom docker i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
