# vllm-project/vllm#20173: [Usage]: Even when using vllm version 0.91, it still doesn't support sm_100, making inference impossible.

| 字段 | 值 |
| --- | --- |
| Issue | [#20173](https://github.com/vllm-project/vllm/issues/20173) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Even when using vllm version 0.91, it still doesn't support sm_100, making inference impossible.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` INFO 06-27 16:37:35 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... /root/miniconda3/envs/jlp_vllm/lib/python3.12/site-packages/torch/cuda/__init__.py:287: UserWarning: NVIDIA B200 with CUDA capability sm_100 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. If you want to use the NVIDIA B200 GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/ warnings.warn( ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: Even when using vllm version 0.91, it still doesn't support sm_100, making inference impossible. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` INFO 06-27 16:37:35 [_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Usage]: Even when using vllm version 0.91, it still doesn't support sm_100, making inference impossible. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` INFO 06-27 16:37:35 [_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:244] Automatically detected platform cuda. Collecting environment information... /root/miniconda3/envs/jlp_vllm/lib/python3.12/site-packages/torch/cuda/__init__.py:287: UserWarning: NVIDIA B200 with CUDA capability...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: .91, it still doesn't support sm_100, making inference impossible. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` INFO 06-27 16:37:35 [__init__.py:244] Automatically detected...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: idia-nvshmem-cu12==3.2.5 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pytorch-triton==3.3.1+gitc8757738 [pip3] pyzmq==27.0.0 [pip3] torch==2.7.0 [pip3] torchaudio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.53.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
