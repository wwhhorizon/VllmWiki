# vllm-project/vllm#31439: [Bug]: aot_compile disables inductor graph partition

| 字段 | 值 |
| --- | --- |
| Issue | [#31439](https://github.com/vllm-project/vllm/issues/31439) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: aot_compile disables inductor graph partition

### Issue 正文摘录

### Your current environment Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B200 GPU 7: NVIDIA B200 Nvidia driver version : 580.82.07 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-cu12==12.8.93 [pip3] nvidia-cuda-runtime-cu12==12.8.90 [pip3] nvidia-cudnn-cu12==9.10.2.21 [pip3] nvidia-cudnn-frontend==1.16.0 [pip3] nvidia-cufft-cu12==11.3.3.83 [pip3] nvidia-cufile-cu12==1.13.1.3 [pip3] nvidia-curand-cu12==10.3.9.90 [pip3] nvidia-cusolver-cu12==11.7.3.90 [pip3] nvidia-cusparse-cu12==12.5.8.93 [pip3] nvidia-cusparselt-cu12==0.7.1 [pip3] nvidia-cutlass-dsl==4.2.1 [pip3] nvidia-ml-py==13.580.82 [pip3] nvidia-nccl-cu12==2.27.5 [pip3] nvidia-nvjitlink-cu12==12.8.93 [pip3] nvidia-nvshmem-cu12==3.3.20 [pip3] nvidia-nvtx-cu12==12.8.90 [pip3] pyzmq==27.1.0 [pip3] torch==2.9.1 [pip...

## 现有链接修复摘要

#31536 fix(compile): apply partition wrapper when loading AOT cached functions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: aot_compile disables inductor graph partition bug ### Your current environment Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: runtime version : N/A Is XNNPACK available : True [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-cu12==12.8.93 [pi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: e disables inductor graph partition bug ### Your current environment Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ommand `vllm bench latency --model nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --attention-con fig.backend=TRITON_ATTN -cc.use_inductor_graph_partition=True -cc.cudagraph_mode=PIECEWISE --kv-cache-dtype=fp8 -cc.pass_confi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: DA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B2...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31536](https://github.com/vllm-project/vllm/pull/31536) | closes_keyword | 0.95 | fix(compile): apply partition wrapper when loading AOT cached functions | Fixes #31439 where VLLM_USE_AOT_COMPILE=1 causes 2x latency regression when use_inductor_graph_partition=True and cudagraph_mode=PIECEWISE. ## Root Cause The bug is in vllm/c |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
