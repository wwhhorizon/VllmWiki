# vllm-project/vllm#31086: [Bug][ROCm]: Triton backend broken

| 字段 | 值 |
| --- | --- |
| Issue | [#31086](https://github.com/vllm-project/vllm/issues/31086) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: Triton backend broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am reviewing the failure of test `pytest -s -v tests/models/multimodal/generation/test_pixtral.py::test_chat[bfloat16-8192-mistralai/Pixtral-12B-2409]` on ROCm. After playing with the attention backends, I can report the following: 1. sdpa for vit with triton fails with float16 and bfloat16 2. flash attention for vit with triton fails with float16 and bfloat16 3. sdpa for vit with triton passes with float32 4. aiter flash attention for vit with triton backend fails with float16 and bloat16 5. aiter flash attention for vit with aiter flash attention backend passes with both float16 and bfloat16 6. flash attention for vit with aiter flash attention backend passes (I only tested bfloat16) 7. sdpa for vit with aiter flash attention backend passes (I only tested bfloat16) I changed the original code of pixtral (`vllm/vllm/model_executor/models/pixtral.py`) to: By making this change I was able to set the backends that I wanted to. After that, I only had to hard set the backends that I wanted using `vllm/vllm/platforms/rocm.py` and functions `get_vit_attn_backend` and `get_attn_backend_cls`. TL;DR: Something is going on with the Trito...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: test -s -v tests/models/multimodal/generation/test_pixtral.py::test_chat[bfloat16-8192-mistralai/Pixtral-12B-2409]` on ROCm. After playing with the attention backends, I can report the following: 1. sdpa for vit with tr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug][ROCm]: Triton backend broken bug;rocm ### Your current environment ### 🐛 Describe the bug I am reviewing the failure of test `pytest -s -v tests/models/multimodal/generation/test_pixtral.py::test_chat[bfloat16-819...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_deco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][ROCm]: Triton backend broken bug;rocm ### Your current environment ### 🐛 Describe the bug I am reviewing the failure of test `pytest -s -v tests/models/multimodal/generation/test_pixtral.py::test_chat[bfloat16-819...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug I am reviewing the failure of test `pytest -s -v tests/models/multimodal/generation/test_pixtral.py::test_chat[bfloat16-8192-mistralai/Pixtral-12B-2409]` on ROCm. After playing with the attention backen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
