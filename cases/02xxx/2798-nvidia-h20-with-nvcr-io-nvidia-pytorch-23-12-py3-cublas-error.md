# vllm-project/vllm#2798: Nvidia-H20 with nvcr.io/nvidia/pytorch:23.12-py3，CUBLAS Error！

| 字段 | 值 |
| --- | --- |
| Issue | [#2798](https://github.com/vllm-project/vllm/issues/2798) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;gemm;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Nvidia-H20 with nvcr.io/nvidia/pytorch:23.12-py3，CUBLAS Error！

### Issue 正文摘录

INFO 02-07 11:14:13 llm_engine.py:70] Initializing an LLM engine with config: model='/root/local_model_root/model/llama-2-7b/modelscope/Llama-2-7b-chat-ms', tokenizer='/root/local_model_root/model/llama-2-7b/modelscope/Llama-2-7b-chat-ms', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=True, seed=0) INFO 02-07 11:14:18 llm_engine.py:275] # GPU blocks: 9200, # CPU blocks: 512 Wed, 07 Feb 2024 11:14:20 aiperf_inference.py[line:213] INFO LLM engine created Processed prompts: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▊| 999/1000 [02:20 () :0 16 0x00000000030493c8 at::native::(anonymous namespace)::addmm_out_cuda_impl() Blas.cpp:0 17 0x000000000304988a at::native::structured_mm_out_cuda::impl() ???:0 18 0x0000000002dcc2e0 at::(anonymous namespace)::wrapper_CUDA_mm() RegisterCUDA.cpp:0 19 0x0000000002dcc350 c10::impl::wrap_kernel_functor_unboxed_ , at::Tensor, c10::guts::type...

## 现有链接修复摘要

#38423 [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=True, seed=0)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r (at::Tensor const&, at::Tensor const&)>::call() RegisterCompositeImplicitAutograd.cpp:0 24 0x00000000028a4051 at::_ops::matmul::call() ???:0 25 0x0000000001b7fa33 at::native::linear() ???:0 26 0x0000000002d05753 c10::...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: le INFO 02-07 11:14:13 llm_engine.py:70] Initializing an LLM engine with config: model='/root/local_model_root/model/llama-2-7b/modelscope/Llama-2-7b-chat-ms', tokenizer='/root/local_model_root/model/llama-2-7b/modelsco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ) :0 16 0x00000000030493c8 at::native::(anonymous namespace)::addmm_out_cuda_impl() Blas.cpp:0 17 0x000000000304988a at::native::structured_mm_out_cuda::impl() ???:0 18 0x0000000002dcc2e0 at::(anonymous namespace)::wrap...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0 24 0x00000000028a4051 at::_ops::matmul::call() ???:0 25 0x0000000001b7fa33 at::native::linear() ???:0 26 0x0000000002d05753 c10::impl::wrap_kernel_functor_unboxed_ const&), &at::(anonymous namespace)::(anonymous names...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38423](https://github.com/vllm-project/vllm/pull/38423) | closes_keyword | 0.95 | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 | Fixed upstream in [flashinfer-ai/flashinfer#2798](https://github.com/flashinfer-ai/flashinfer/pull/2798). 3. **`cutlass_scaled_mm_supports_fp4()` reported false availability** — |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
