# vllm-project/vllm#7992: [Bug]: Jamba-1.5-mini doesn't run on A100 with 70GB available memory

| 字段 | 值 |
| --- | --- |
| Issue | [#7992](https://github.com/vllm-project/vllm/issues/7992) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Jamba-1.5-mini doesn't run on A100 with 70GB available memory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running Jamba-1.5-mini with experts_int8 quantization crashes on A100(80GB) GPU with any max_model_len. I've tried with 8k/12k/16k. Output of NVIDIA-SMI: ``` (model) azureuser@votum-vm-new:~/vllm$ nvidia-smi Thu Aug 29 10:30:40 2024 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA A100 80GB PCIe Off | 00000001:00:00.0 Off | 0 | | N/A 35C P0 66W / 300W | 11766MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ ``` ```shell (model) azureuser@votum-vm-new:~/vllm$ vllm serve ai21labs/AI21-Jamba-1.5-Mini --max-model-len 16384 --quantization experts_int8 --kv-cache-dtype fp8 WARNING 08-29 09:57:06 cud...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: fp8', quantization_param_path=None, max_model_len=16384, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ----------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ent ### 🐛 Describe the bug Running Jamba-1.5-mini with experts_int8 quantization crashes on A100(80GB) GPU with any max_model_len. I've tried with 8k/12k/16k. Output of NVIDIA-SMI: ``` (model) azureuser@votum-vm-new:~/v...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: /AI21-Jamba-1.5-Mini --max-model-len 16384 --quantization experts_int8 --kv-cache-dtype fp8 WARNING 08-29 09:57:06 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ni with experts_int8 quantization crashes on A100(80GB) GPU with any max_model_len. I've tried with 8k/12k/16k. Output of NVIDIA-SMI: ``` (model) azureuser@votum-vm-new:~/vllm$ nvidia-smi Thu Aug 29 10:30:40 2024 +-----...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
