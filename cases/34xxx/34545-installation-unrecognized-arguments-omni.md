# vllm-project/vllm#34545: [Installation]: unrecognized arguments: --omni

| 字段 | 值 |
| --- | --- |
| Issue | [#34545](https://github.com/vllm-project/vllm/issues/34545) |
| 状态 | open |
| 标签 | installation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: unrecognized arguments: --omni

### Issue 正文摘录

### Your current environment pip show: ```shell root@xxxxxxx~# pip list | grep vllm vllm 0.15.0 vllm-omni 0.14.0 ``` I run server command : ```shell vllm serve /root/Qwen-Image-Edit-2509 --omni --port 8092 --max-num-seqs 10 --served-model-name Qwen-Image-Edit-2509 --tensor-parallel-size 2 ``` But with error: ```shell usage: vllm [-h] [-v] {chat,complete,serve,bench,collect-env,run-batch} ... vllm: error: unrecognized arguments: --omni ``` And then: ```text root@crd25:~# python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.7 | packaged by Anaconda, Inc. | (main, Oct 4 2024, 13:27:36) [GCC 11.2.0] (64-bit runtime) Python platform : Lin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: unrecognized arguments: --omni installation;stale ### Your current environment pip show: ```shell root@xxxxxxx~# pip list | grep vllm vllm 0.15.0 vllm-omni
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.7 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 0.14.0 ``` I run server command : ```shell vllm serve /root/Qwen-Image-Edit-2509 --omni --port 8092 --max-num-seqs 10 --served-model-name Qwen-Image-Edit-2509 --tensor-parallel-size 2 ``` But with error: ```shell usage:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.1 [pip3] numpy==2.1.2 [pip3] nvidia-cublas-cu11==11.11.3.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Installation]: unrecognized arguments: --omni installation;stale ### Your current environment pip show: ```shell root@xxxxxxx~# pip list | grep vllm vllm 0.15.0 vllm-omni 0.14.0 ``` I run server command : ```shell vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
