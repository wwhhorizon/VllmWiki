# vllm-project/vllm#1393: Error when use multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#1393](https://github.com/vllm-project/vllm/issues/1393) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error when use multiple GPUs

### Issue 正文摘录

Hi team, I am working on inference with codellama/CodeLlama-7b-Instruct-hf on vllm. I am using 2 T4 GPU for this. At the first place, I was trying with `engine_args.tensor_parallel_size = 1`. And it shows OOM. So after that, I tried `engine_args.tensor_parallel_size = 2`. But new error pop up. FYI, when I tried with 1 A100, the result looks good as the memory is enough. Could you help check on this? Thanks! **GPU** ``` (base) [root@ac4da495a32a vllm]# nvidia-smi Tue Oct 17 10:00:36 2023 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 525.125.06 Driver Version: 525.125.06 CUDA Version: 12.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 Tesla T4 Off | 00000000:00:04.0 Off | 0 | | N/A 48C P8 10W / 70W | 2MiB / 15360MiB | 0% Default | | | | N/A | +-------------------------------+----------------------+----------------------+ | 1 Tesla T4 Off | 00000000:00:05.0 Off | 0 | | N/A 4...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: --------------------------------------+ | NVIDIA-SMI 525.125.06 Driver Version: 525.125.06 CUDA Version: 12.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Error when use multiple GPUs Hi team, I am working on inference with codellama/CodeLlama-7b-Instruct-hf on vllm. I am using 2 T4 GPU for this. At the first place, I was trying with `engine_args.tensor_parallel_size = 1`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rallel_size = 1 engine_args.tensor_parallel_size = 2 engine_args.dtype = 'float16' print(f"engine_args: {engine_args}") """ AsyncEngineArgs(model='facebook/opt-13b', tokenizer='facebook/opt-13b', tokenizer_mode='auto',...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or_parallel_size = 2`. But new error pop up. FYI, when I tried with 1 A100, the result looks good as the memory is enough. Could you help check on this? Thanks! **GPU** ``` (base) [root@ac4da495a32a vllm]# nvidia-smi Tu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: , I was trying with `engine_args.tensor_parallel_size = 1`. And it shows OOM. So after that, I tried `engine_args.tensor_parallel_size = 2`. But new error pop up. FYI, when I tried with 1 A100, the result looks good as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
