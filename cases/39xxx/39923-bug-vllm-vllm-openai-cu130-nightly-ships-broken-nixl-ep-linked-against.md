# vllm-project/vllm#39923: [Bug]: vllm/vllm-openai:cu130-nightly ships broken nixl_ep linked against libcudart.so.12 — server fails at import

| 字段 | 值 |
| --- | --- |
| Issue | [#39923](https://github.com/vllm-project/vllm/issues/39923) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;moe |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai:cu130-nightly ships broken nixl_ep linked against libcudart.so.12 — server fails at import

### Issue 正文摘录

### Your current environment Running the published Docker image `vllm/vllm-openai:cu130-nightly` — not a local pip install. - Image: `vllm/vllm-openai@sha256:9f815b8ce5679bc3bad061194ad658b8ce8bd48b5174e64f587553d16a702eb3` - Image tag: `vllm/vllm-openai:cu130-nightly` (pulled 2026-04-15) - vLLM version inside image: `0.19.1rc1.dev296+gbcc2306ce` - Host: RTX 5090 (SM 12.0), driver 580.x, Ubuntu 24.04, Docker + nvidia-container-toolkit ### 🐛 Describe the bug The image contains CUDA **13** end-to-end (`libcudart.so.13`, `/usr/local/cuda-13.0/...`, `nvidia/cu13/`) but also ships a `nixl_ep/` package whose compiled `.so` was built against CUDA **12** and needs `libcudart.so.12`, which is **not present anywhere in the image**. Because `vllm.lora.utils` → `vllm.model_executor.layers.fused_moe.all2all_utils` eagerly imports `nixl_ep_prepare_finalize`, and `has_nixl_ep()` only checks `importlib.util.find_spec("nixl_ep")` (returns True because the directory exists), every `vllm` CLI invocation fails at startup: ``` File ".../vllm/model_executor/layers/fused_moe/nixl_ep_prepare_finalize.py", line 5, in import nixl_ep File ".../nixl_ep/__init__.py", line 23, in from . import nixl_ep_cpp as _...

## 现有链接修复摘要

#41746 [Bugfix] find_loaded_library: skip stub libraries and continue iterating

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: vllm/vllm-openai:cu130-nightly ships broken nixl_ep linked against libcudart.so.12 — server fails at import ### Your current environment Running the published Docker image `vllm/vllm-openai:cu130-nightly` — not a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: vllm/vllm-openai:cu130-nightly ships broken nixl_ep linked against libcudart.so.12 — server fails at import ### Your current environment Running the published Docker image `vllm/vllm-openai:cu130-nightly` — not a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: *not present anywhere in the image**. Because `vllm.lora.utils` → `vllm.model_executor.layers.fused_moe.all2all_utils` eagerly imports `nixl_ep_prepare_finalize`, and `has_nixl_ep()` only checks `importlib.util.find_spe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: image**. Because `vllm.lora.utils` → `vllm.model_executor.layers.fused_moe.all2all_utils` eagerly imports `nixl_ep_prepare_finalize`, and `has_nixl_ep()` only checks `importlib.util.find_spec("nixl_ep")` (returns True b...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41746](https://github.com/vllm-project/vllm/pull/41746) | mentioned | 0.6 | [Bugfix] find_loaded_library: skip stub libraries and continue iterating | ch on ARM64 + CUDA 13.x — different failure mode but adjacent class), #39923 (broken nixl_ep linked against libcudart.so.12 — packaging-bug class). |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
