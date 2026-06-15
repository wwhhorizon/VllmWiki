# vllm-project/vllm#6204: [Bug]: got RuntimeError: Triton Error [CUDA]: device kernel image is invalid  when running deepseek-v2

| 字段 | 值 |
| --- | --- |
| Issue | [#6204](https://github.com/vllm-project/vllm/issues/6204) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: got RuntimeError: Triton Error [CUDA]: device kernel image is invalid  when running deepseek-v2

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... WARNING 07-08 14:14:25 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.5.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.17 Python version: 3.9.16 | packaged by conda-forge | (main, Feb 1 2023, 21:39:03) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY ### 🐛 Describe the bug The code is ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_name = 'deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct' max_model_len, tp_size = 8192, 1 tokenizer = AutoTokenizer.from_pretrained(model_name) llm = LLM(model=model_name, tensor_parallel_size=tp_size, max_model_len=max_model_len, trust_remote_code=True,enforce_eager=True) sampling_params = S...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nment information... WARNING 07-08 14:14:25 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build Py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: got RuntimeError: Triton Error [CUDA]: device kernel image is invalid when running deepseek-v2 bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment infor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `text The output of `python collect_env.py` ``` Collecting environment information... WARNING 07-08 14:14:25 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: got RuntimeError: Triton Error [CUDA]: device kernel image is invalid when running deepseek-v2 bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment infor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: module named 'vllm._C'") PyTorch version: 2.3.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 10.5.0 Clang version: Co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
