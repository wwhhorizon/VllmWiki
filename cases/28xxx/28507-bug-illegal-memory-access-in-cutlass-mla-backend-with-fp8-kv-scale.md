# vllm-project/vllm#28507: [Bug]: Illegal memory access in CUTLASS MLA backend with FP8 KV scale

| 字段 | 值 |
| --- | --- |
| Issue | [#28507](https://github.com/vllm-project/vllm/issues/28507) |
| 状态 | closed |
| 标签 | bug;stale;nvidia |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;fp8;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Illegal memory access in CUTLASS MLA backend with FP8 KV scale

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The CUTLASS MLA backend triggers an illegal memory access error when running DeepSeek-V2-Lite with FP8 quantization and FP8 KV cache. The FLASHINFER MLA backend works correctly with identical configuration, leading to suspect this is a CUTLASS-specific implementation bug. ```python #!/usr/bin/env python3 import os from vllm import LLM, SamplingParams from vllm.attention.backends.registry import AttentionBackendEnum from vllm.config import CompilationConfig, CUDAGraphMode def run(model: str): os.environ["VLLM_ATTENTION_BACKEND"] = AttentionBackendEnum.CUTLASS_MLA.name comp = CompilationConfig( mode=0, backend="inductor", custom_ops=["all"], compile_mm_encoder=True, inductor_compile_config={ "combo_kernels": True, "benchmark_combo_kernel": True, }, cudagraph_mode=CUDAGraphMode.NONE, use_cudagraph=False, cudagraph_num_of_warmups=1, compile_sizes=[], splitting_ops=None, pass_config={}, ) llm = LLM( model=model, dtype="bfloat16", compilation_config=comp, tensor_parallel_size=1, disable_custom_all_reduce=True, quantization="fp8", kv_cache_dtype="fp8_e4m3", max_model_len=512, ) prompts = [ "Hello, my name is", "The president of the Unit...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Illegal memory access in CUTLASS MLA backend with FP8 KV scale bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug The CUTLASS MLA backend triggers an illegal memory access error when running Dee...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ly with identical configuration, leading to suspect this is a CUTLASS-specific implementation bug. ```python #!/usr/bin/env python3 import os from vllm import LLM, SamplingParams from vllm.attention.backends.registry im...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Illegal memory access in CUTLASS MLA backend with FP8 KV scale bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug The CUTLASS MLA backend triggers an illegal memory access error when running Dee...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y import AttentionBackendEnum from vllm.config import CompilationConfig, CUDAGraphMode def run(model: str): os.environ["VLLM_ATTENTION_BACKEND"] = AttentionBackendEnum.CUTLASS_MLA.name comp = CompilationConfig( mode=0,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: FP8 KV cache. The FLASHINFER MLA backend works correctly with identical configuration, leading to suspect this is a CUTLASS-specific implementation bug. ```python #!/usr/bin/env python3 import os from vllm import LLM, S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
