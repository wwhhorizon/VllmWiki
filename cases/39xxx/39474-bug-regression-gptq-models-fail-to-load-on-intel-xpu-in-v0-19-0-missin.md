# vllm-project/vllm#39474: [Bug] Regression: GPTQ models fail to load on Intel XPU in v0.19.0 (missing XPU branches in gptq.py)

| 字段 | 值 |
| --- | --- |
| Issue | [#39474](https://github.com/vllm-project/vllm/issues/39474) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;import_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Regression: GPTQ models fail to load on Intel XPU in v0.19.0 (missing XPU branches in gptq.py)

### Issue 正文摘录

## Your current environment ``` vLLM 0.19.0 (built from v0.19.0 tag via docker/Dockerfile.xpu) PyTorch 2.10.0+xpu triton-xpu 3.6.0 vllm-xpu-kernels 0.1.5 Intel Arc Pro B70 (Battlemage G31, 32GB VRAM, PCI 8086:e223) Ubuntu 25.10 host, container based on intel/deep-learning-essentials:2025.3.2-0-devel-ubuntu24.04 ``` ## 🐛 Describe the bug Starting any GPTQ-quantized model on Intel XPU with vLLM 0.19.0 fails during engine initialization with: ``` AttributeError: '_OpNamespace' '_C' object has no attribute 'gptq_shuffle' ``` This is a **regression from v0.17.x**, which handled GPTQ on XPU correctly. v0.17 had explicit `if current_platform.is_xpu():` branches in `vllm/model_executor/layers/quantization/gptq.py` that used `vllm_xpu_kernels` APIs. These branches were removed in v0.19, causing fallthrough to the CUDA-only `vllm._C` ops. The XPU build doesn't ship `vllm._C` at all (`WARNING [interface.py:229] Failed to import from vllm._C: ModuleNotFoundError`). Additionally, the XPU kernels shared library at `vllm_xpu_kernels/_xpu_C.abi3.so` is not auto-loaded by v0.19, so `torch.ops._xpu_C.int4_gemm_w4a16` is not registered when `gptq.py`'s `apply()` method would need it. ## Reproduction...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ## Your current environment ``` vLLM 0.19.0 (built from v0.19.0 tag via docker/Dockerfile.xpu) PyTorch 2.10.0+xpu triton-xpu 3.6.0 vllm-xpu-kernels 0.1.5 Intel Arc Pro B70 (Battlemage G31, 32GB VRAM, PCI 8086:e223) Ubun...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 25.3.2-0-devel-ubuntu24.04 ``` ## 🐛 Describe the bug Starting any GPTQ-quantized model on Intel XPU with vLLM 0.19.0 fails during engine initialization with: ``` AttributeError: '_OpNamespace' '_C' object has no attribu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] Regression: GPTQ models fail to load on Intel XPU in v0.19.0 (missing XPU branches in gptq.py) ## Your current environment ``` vLLM 0.19.0 (built from v0.19.0 tag via docker/Dockerfile.xpu) PyTorch 2.10.0+xpu trit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ` APIs. These branches were removed in v0.19, causing fallthrough to the CUDA-only `vllm._C` ops. The XPU build doesn't ship `vllm._C` at all (`WARNING [interface.py:229] Failed to import from vllm._C: ModuleNotFoundErr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .0 (built from v0.19.0 tag via docker/Dockerfile.xpu) PyTorch 2.10.0+xpu triton-xpu 3.6.0 vllm-xpu-kernels 0.1.5 Intel Arc Pro B70 (Battlemage G31, 32GB VRAM, PCI 8086:e223) Ubuntu 25.10 host, container based on intel/d...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
