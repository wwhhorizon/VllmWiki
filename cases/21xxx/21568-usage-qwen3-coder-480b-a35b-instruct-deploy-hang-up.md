# vllm-project/vllm#21568: [Usage]: Qwen3-Coder-480B-A35B-Instruct deploy hang up

| 字段 | 值 |
| --- | --- |
| Issue | [#21568](https://github.com/vllm-project/vllm/issues/21568) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe |
| 子分类 |  |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen3-Coder-480B-A35B-Instruct deploy hang up

### Issue 正文摘录

### Your current environment The deployment of Qwen3-Coder-480B-A35B-Instruct has been stuck and it has always been "Waiting for" ``` (pid=246, ip=10.1.30.2) DEBUG 07-24 07:04:46 [__init__.py:35] Checking if TPU platform is available. [repeated 7x across cluster] (pid=246, ip=10.1.30.2) DEBUG 07-24 07:04:46 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' [repeated 7x across cluster] (pid=246, ip=10.1.30.2) DEBUG 07-24 07:04:46 [__init__.py:52] Checking if CUDA platform is available. [repeated 13x across cluster] (pid=487) DEBUG 07-24 07:04:41 [__init__.py:72] Confirmed CUDA platform is available. [repeated 12x across cluster] (pid=497) DEBUG 07-24 07:04:41 [__init__.py:100] Checking if ROCm platform is available. [repeated 6x across cluster] (pid=497) DEBUG 07-24 07:04:41 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' [repeated 6x across cluster] (pid=497) DEBUG 07-24 07:04:41 [__init__.py:121] Checking if HPU platform is available. [repeated 6x across cluster] (pid=497) DEBUG 07-24 07:04:41 [__init__.py:128] HPU platform is not available because habana_frameworks is not found. [repeated 6x across cluster] (pid=4...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: pid=246, ip=10.1.30.2) DEBUG 07-24 07:04:46 [__init__.py:52] Checking if CUDA platform is available. [repeated 13x across cluster] (pid=487) DEBUG 07-24 07:04:41 [__init__.py:72] Confirmed CUDA platform is available. [r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: # How would you like to use vllm Deploy using the following command ``` docker run --privileged=true -itd --gpus all --network host --ipc host -e VLLM_LOGGING_LEVEL=DEBUG -e GLOO_SOCKET_IFNAME=bond0 --env NCCL_SOCKET_IF...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Qwen3-Coder-480B-A35B-Instruct deploy hang up usage;stale ### Your current environment The deployment of Qwen3-Coder-480B-A35B-Instruct has been stuck and it has always been "Waiting for" ``` (pid=246, ip=10.1....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: er --port 18080 --model /models --served-model-name qwen3-coder --enable-expert-parallel --tensor-parallel-size 8 --pipeline_parallel_size 2 --trust-remote-code --max-model-len 131072 --gpu-memory-util 0.9 --enable-auto...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Qwen3-Coder-480B-A35B-Instruct deploy hang up usage;stale ### Your current environment The deployment of Qwen3-Coder-480B-A35B-Instruct has been stuck and it has always been "Waiting for" ``` (pid=246, ip=10.1....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
