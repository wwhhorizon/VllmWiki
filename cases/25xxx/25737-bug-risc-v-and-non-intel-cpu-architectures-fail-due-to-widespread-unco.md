# vllm-project/vllm#25737: [Bug]: RISC-V and non-Intel CPU architectures fail due to widespread unconditional IPEX dependencies

| 字段 | 值 |
| --- | --- |
| Issue | [#25737](https://github.com/vllm-project/vllm/issues/25737) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RISC-V and non-Intel CPU architectures fail due to widespread unconditional IPEX dependencies

### Issue 正文摘录

### Your current environment - Hardware: sg2044 - OS: LEulixOS 3.0 - Python: 3.11 - PyTorch: 2.8.0 - GCC: 15.1 - vLLM: commit 13dd93c6 ### 🐛 Describe the bug vLLM fails to run on RISC-V architecture due to multiple unconditional imports of Intel Extension for PyTorch throughout the CPU backend, even though IPEX is Intel x86-specific and not available on RISC-V architectures. ```bash export VLLM_ENABLE_V1_MULTIPROCESSING=0 VLLM_COMPILATION_LEVEL=0 vllm bench throughput \ --model Qwen/Qwen1.5-0.5B \ --input-len 128 \ --output-len 128 \ --enforce-eager --dtype float16 --max_model_len 4096 --max_num_batched_tokens 4096 Error message: ``` [rank0]: File "/AI/hebo/vllm/vllm/v1/attention/backends/cpu_attn.py", line 595, in forward [rank0]: import intel_extension_for_pytorch.llm.modules as ipex_modules [rank0]: ModuleNotFoundError: No module named 'intel_extension_for_pytorch' ``` Root cause analysis: 1. Architecture detection works correctly: The RISC-V architecture is now properly detected after recent additions to CpuArchEnum.RISCV. 2. IPEX availability check exists but is inconsistently applied: The code correctly checks IPEX availability at module level cpu_attn.py and sets _use_ipex...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: en/Qwen1.5-0.5B \ --input-len 128 \ --output-len 128 \ --enforce-eager --dtype float16 --max_model_len 4096 --max_num_batched_tokens 4096 Error message: ``` [rank0]: File "/AI/hebo/vllm/vllm/v1/attention/backends/cpu_at...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _V1_MULTIPROCESSING=0 VLLM_COMPILATION_LEVEL=0 vllm bench throughput \ --model Qwen/Qwen1.5-0.5B \ --input-len 128 \ --output-len 128 \ --enforce-eager --dtype float16 --max_model_len 4096 --max_num_batched_tokens 4096...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: unconditional imports of Intel Extension for PyTorch throughout the CPU backend, even though IPEX is Intel x86-specific and not available on RISC-V architectures. ```bash export VLLM_ENABLE_V1_MULTIPROCESSING=0 VLLM_COM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ntel CPU architectures fail due to widespread unconditional IPEX dependencies bug ### Your current environment - Hardware: sg2044 - OS: LEulixOS 3.0 - Python: 3.11 - PyTorch: 2.8.0 - GCC: 15.1 - vLLM: commit 13dd93c6 ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: RISC-V and non-Intel CPU architectures fail due to widespread unconditional IPEX dependencies bug ### Your current environment - Hardware: sg2044 - OS: LEulixOS 3.0 - Python: 3.11 - PyTorch: 2.8.0 - GCC: 15.1 - v...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
