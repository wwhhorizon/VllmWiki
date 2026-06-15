# vllm-project/vllm#3504: [Bug]: Mistral generation degrades at long lengths

| 字段 | 值 |
| --- | --- |
| Issue | [#3504](https://github.com/vllm-project/vllm/issues/3504) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral generation degrades at long lengths

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ``` Collecting environment information... /scratch/gpfs/hyen/p-long-instruct/vllm_env/lib/python3.11/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Springdale Linux release 8.8 (Modena) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-18) Clang version: Could not collect CMake version: version 3.20.2 Libc version: glibc-2.28 Python version: 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-477.27.1.el8_8.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: L...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: d in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Springdale Linux release 8.8 (Modena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ead. warnings.warn( PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Springdale Linux release 8.8 (Modena) (x86_64) GCC version: (GCC) 8.5.0 2021051...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: The output of `python collect_env.py` ``` ``` Collecting environment information... /scratch/gpfs/hyen/p-long-instruct/vllm_env/lib/python3.11/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", torch_dtype=torch.bfloat16, device_map="auto", attn_implementation="flash_attention_2",) o = model.generate(**inputs.to(model.device), temperature=0, ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Mistral generation degrades at long lengths bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` Collecting environment information... /scratch/gpfs/hyen/p-long-instruct/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
