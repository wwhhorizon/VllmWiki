# vllm-project/vllm#27504: [Usage]: `add_vision_id` ignored for Qwen 2.5-VL-32B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#27504](https://github.com/vllm-project/vllm/issues/27504) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: `add_vision_id` ignored for Qwen 2.5-VL-32B-Instruct

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-85-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 Nvidia driver version : 570.124.06 cuDNN version : Probably one of the following: /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn.so.9.8.0 /usr/local/cuda-12.0/targets/x86_64-linux/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: `add_vision_id` ignored for Qwen 2.5-VL-32B-Instruct usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) G...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ve Qwen/Qwen2.5-VL-32B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --dtype bfloat16 \ --limit-mm-per-prompt '{"image":2}' \ --mm-processor-kwargs '{"add_vision_id": true}' \ --max-model-len 8192 \ --tensor-parallel-size 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: `add_vision_id` ignored for Qwen 2.5-VL-32B-Instruct usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) G...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
