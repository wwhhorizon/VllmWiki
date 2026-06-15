# vllm-project/vllm#38811: [Usage]: Qwen3-VL inference on video complains of lack of metadata

| 字段 | 值 |
| --- | --- |
| Issue | [#38811](https://github.com/vllm-project/vllm/issues/38811) |
| 状态 | open |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen3-VL inference on video complains of lack of metadata

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 3.27.6 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 | packaged by Anaconda, Inc. | (main, Mar 19 2026, 20:20:58) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-6.8.0-107-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.1.66 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3080 Laptop GPU Nvidia driver version : 580.126.09 cuDNN version : Probably one of the following: /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn.so.8.2.1 /usr/local/cuda-10.2/targets/x86_6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 3.27.6 Libc version : glibc-2.39 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Qwen3-VL inference on video complains of lack of metadata usage ### Your current environment ```text The output of `python collect_env.py` ============================== System Info ============================
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: tils import process_vision_info model_path = "Qwen/Qwen3-VL-2B-Instruct-FP8" video_path = "https://content.pexels.com/videos/free-videos.mp4" llm = LLM( model=model_path, gpu_memory_utilization=0.9, max_model_len=40000,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
