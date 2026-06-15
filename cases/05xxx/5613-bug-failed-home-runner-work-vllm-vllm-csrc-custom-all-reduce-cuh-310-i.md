# vllm-project/vllm#5613: [Bug]: Failed: /home/runner/work/vllm/vllm/csrc/custom_all_reduce.cuh:310 'invalid argument'

| 字段 | 值 |
| --- | --- |
| Issue | [#5613](https://github.com/vllm-project/vllm/issues/5613) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed: /home/runner/work/vllm/vllm/csrc/custom_all_reduce.cuh:310 'invalid argument'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (SP2) (x86_64) GCC version: (GCC) 8.2.0 Clang version: Could not collect CMake version: version 2.8.12.2 Libc version: glibc-2.17 Python version: 3.8.18 (default, Jun 13 2024, 08:22:35) [GCC 8.2.0] (64-bit runtime) Python platform: Linux-4.18.0-147.5.1.6.h1136.eulerosv2r9.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB Nvidia driver version: 470.57.02 cuDNN version: /usr/local/cuda-10.1/targets/x86_64-linux/lib/libcudnn.so.7.6.5 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 72 On-line CPU(s) list: 0-71 Thread(s) per core: 2 Core(s) per socket: 18 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU famil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: thon collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (SP2) (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ent information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (SP2) (x86_64) GCC version: (GCC) 8.2.0 Clang version: Could not col...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: EulerOS 2.0 (S...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uawei/dataset/data_dir/model/checkpoints/llms/Qwen_Qwen1.5-72B-Chat-GPTQ-Int4" --tensor-parallel-size=2 --max-model-len=4000 --port=5001 I am having the error below: INFO 06-18 06:28:40 model_runner.py:980] CUDA graphs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: f==0.7.2 [pip3] torch==2.2.1+cu118 [pip3] transformers==4.41.2 [pip3] triton==2.2.0 [pip3] vllm_nccl_cu11==2.18.1.0.4.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
