# vllm-project/vllm#2119: H100 multi-GPU vllm_worker startup error

| 字段 | 值 |
| --- | --- |
| Issue | [#2119](https://github.com/vllm-project/vllm/issues/2119) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> H100 multi-GPU vllm_worker startup error

### Issue 正文摘录

Hello, when I use multiple GPUs to start inference servers on the H100 machine, an error will be reported. This is normal when using one H100 GPU. Please help me find out what the problem is. Thank you. 2 H100 failed 1 H100 success 2 A100 success 1 A100 success Below is my environment information： NVIDIA-SMI 525.147.05 Driver Version: 525.147.05 CUDA Version: 12.1 Python 3.10.6 torch 2.1.1 transformers 4.36.1 torch 2.1.1 vllm 0.2.5 fschat 0.2.34 The following is the error message: `INFO 12-15 00:44:33 llm_engine.py:72] Initializing an LLM engine with config: model='/meta/', tokenizer='/meta/', tokenizer_mode=slow, revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=16000, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) WARNING 12-15 00:44:33 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. 2023-12-15 00:46:02 | ERROR | stderr | Traceback (most recent call last): 2023-12-15 00:46:02 | ERROR | stderr | File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main 2023-12-15 00:46:02 | ERROR | stderr | return _run_code(code, main_globals, Non...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: r='/meta/', tokenizer_mode=slow, revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=16000, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) WARNING 12-15 00:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: H100 multi-GPU vllm_worker startup error Hello, when I use multiple GPUs to start inference servers on the H100 machine, an error will be reported. This is normal when using one H100 GPU. Please help me find out what the
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 1 H100 success 2 A100 success 1 A100 success Below is my environment information： NVIDIA-SMI 525.147.05 Driver Version: 525.147.05 CUDA Version: 12.1 Python 3.10.6 torch 2.1.1 transformers 4.36.1 torch 2.1.1 vllm 0.2.5...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: enizer='/meta/', tokenizer_mode=slow, revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=16000, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) WARNING 12-1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ess Below is my environment information： NVIDIA-SMI 525.147.05 Driver Version: 525.147.05 CUDA Version: 12.1 Python 3.10.6 torch 2.1.1 transformers 4.36.1 torch 2.1.1 vllm 0.2.5 fschat 0.2.34 The following is the error...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
