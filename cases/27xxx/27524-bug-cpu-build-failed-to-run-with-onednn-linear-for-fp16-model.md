# vllm-project/vllm#27524: [Bug]: CPU build failed to run with OneDNN linear for fp16 model

| 字段 | 值 |
| --- | --- |
| Issue | [#27524](https://github.com/vllm-project/vllm/issues/27524) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU build failed to run with OneDNN linear for fp16 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To reproduce, just run: ``` python examples/offline_inference/basic/basic.py ``` However, models with bf16/fp32 dtype can work with OneDNN linear, and `pytest -s -v tests/kernels/test_onednn.py` can pass with fp16 on same build as well. cc @bigPYJ1151 Any idea? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27526 [Bugfix][CPU] Fallback oneDNN linear to torch linear to fix half gemm support on legecy platforms

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: CPU build failed to run with OneDNN linear for fp16 model bug ### Your current environment ### 🐛 Describe the bug To reproduce, just run: ``` python examples/offline_inference/basic/basic.py ``` However, models w...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n examples/offline_inference/basic/basic.py ``` However, models with bf16/fp32 dtype can work with OneDNN linear, and `pytest -s -v tests/kernels/test_onednn.py` can pass with fp16 on same build as well. cc @bigPYJ1151...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ory;speculative_decoding cuda;gemm;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency #27526 [Bugfix][CPU] Fallback oneDNN linear to torch linear to fix half gemm support on lege...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ea? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;gemm;kernel;operator;quantiz...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27526](https://github.com/vllm-project/vllm/pull/27526) | closes_keyword | 0.95 | [Bugfix][CPU] Fallback oneDNN linear to torch linear to fix half gemm support on legecy platforms | Fix #27524 ## Test Plan CI tests ## Test Result pass --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [x] The purpose of the P |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
