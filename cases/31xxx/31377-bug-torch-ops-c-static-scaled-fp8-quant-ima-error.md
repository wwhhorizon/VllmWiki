# vllm-project/vllm#31377: [Bug]: torch.ops._C.static_scaled_fp8_quant IMA error

| 字段 | 值 |
| --- | --- |
| Issue | [#31377](https://github.com/vllm-project/vllm/issues/31377) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.ops._C.static_scaled_fp8_quant IMA error

### Issue 正文摘录

### Your current environment [pip3] flashinfer-python==0.5.3 [pip3] mypy==1.16.0 [pip3] mypy_extensions==1.1.0 [pip3] numpy==1.26.2 [pip3] nvidia-cudnn-frontend==1.17.0 [pip3] nvidia-cutlass-dsl==4.3.4 [pip3] nvidia-ml-py==13.590.44 [pip3] onnx==1.20.0 [pip3] onnx-ir==0.1.12 [pip3] onnxscript==0.5.4 [pip3] optree==0.13.0 [pip3] pyzmq==27.1.0 [pip3] torch==2.11.0a0+gita50d65a [pip3] torchvision==0.25.0a0+aa35ca1 [pip3] transformers==4.57.3 [pip3] triton==3.6.0+git9844da95 [conda] flashinfer-python 0.5.3 pypi_0 pypi [conda] magma-cuda126 2.6.1 1 pytorch [conda] mkl-include 2025.3.0 pypi_0 pypi [conda] mkl-static 2025.3.0 pypi_0 pypi [conda] numpy 1.26.2 pypi_0 pypi [conda] nvidia-cudnn-frontend 1.17.0 pypi_0 pypi [conda] nvidia-cutlass-dsl 4.3.4 pypi_0 pypi [conda] nvidia-ml-py 13.590.44 pypi_0 pypi [conda] onemkl-license 2025.3.0 pypi_0 pypi [conda] optree 0.13.0 pypi_0 pypi [conda] pyzmq 27.1.0 pypi_0 pypi [conda] torch 2.11.0a0+gita50d65a pypi_0 pypi [conda] torchvision 0.25.0a0+aa35ca1 pypi_0 pypi [conda] transformers 4.57.3 pypi_0 pypi [conda] triton 3.6.0+git9844da95 pypi_0 pypi vLLM Info ROCM Version : Could not collect vLLM Version : 0.1.dev12449+gc02a2705f.d20251226 (git sh...

## 现有链接修复摘要

#31395 [BugFix] register quant scale tensors as buffer

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: torch.ops._C.static_scaled_fp8_quant IMA error bug ### Your current environment [pip3] flashinfer-python==0.5.3 [pip3] mypy==1.16.0 [pip3] mypy_extensions==1.1.0 [pip3] numpy==1.26.2 [pip3] nvidia-cudnn-frontend=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 3.6.0+git9844da95 pypi_0 pypi vLLM Info ROCM Version : Could not collect vLLM Version : 0.1.dev12449+gc02a2705f.d20251226 (git sha: c02a2705f, date: 20251226) ### 🐛 Describe the bug `pytest -s tests/compile/test_fusion_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: atic_scaled_fp8_quant IMA error bug ### Your current environment [pip3] flashinfer-python==0.5.3 [pip3] mypy==1.16.0 [pip3] mypy_extensions==1.1.0 [pip3] numpy==1.26.2 [pip3] nvidia-cudnn-frontend==1.17.0 [pip3] nvidia-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fer-python 0.5.3 pypi_0 pypi [conda] magma-cuda126 2.6.1 1 pytorch [conda] mkl-include 2025.3.0 pypi_0 pypi [conda] mkl-static 2025.3.0 pypi_0 pypi [conda] n
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-Scout-17B-16E-Instruct-FP8-TestAttentionFp8StaticQuantPatternModel-+quant_fp8-dtype0-7-128-64-8]` gives IMA error. A bit investigation sho...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31395](https://github.com/vllm-project/vllm/pull/31395) | closes_keyword | 0.95 | [BugFix] register quant scale tensors as buffer | Close: #31377 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
