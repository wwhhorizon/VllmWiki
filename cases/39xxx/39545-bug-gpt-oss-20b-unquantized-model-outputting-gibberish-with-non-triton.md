# vllm-project/vllm#39545: [Bug]: gpt-oss-20b unquantized model outputting gibberish with non-triton backends (built from main)

| 字段 | 值 |
| --- | --- |
| Issue | [#39545](https://github.com/vllm-project/vllm/issues/39545) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-20b unquantized model outputting gibberish with non-triton backends (built from main)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Output is gibberish when running unquantized gpt-oss-20b with non-triton backends (FlashInfer CUTLASS) on latest vLLM built from main. These backends were not previously available. Forcing the `triton` backend, the previous default behavior, doesn't cause this issue. ```python #!/usr/bin/env python3 """Minimal vLLM-only repro for gpt-oss generation issues.""" import os import platform import subprocess import sys import time MODEL = os.environ.get("MODEL", "unsloth/gpt-oss-20b-BF16") MOE_BACKEND = os.environ.get("MOE_BACKEND", "auto") DTYPE = os.environ.get("DTYPE", "auto") TEMPERATURE = float(os.environ.get("TEMPERATURE", "0.8")) TOP_P = float(os.environ.get("TOP_P", "0.95")) MAX_TOKENS = int(os.environ.get("MAX_TOKENS", "64")) MAX_MODEL_LEN = int(os.environ.get("MAX_MODEL_LEN", "1024")) TENSOR_PARALLEL_SIZE = int(os.environ.get("TENSOR_PARALLEL_SIZE", "1")) GPU_MEMORY_UTILIZATION = float(os.environ.get("GPU_MEMORY_UTILIZATION", "0.85")) SEED = int(os.environ.get("SEED", "0")) TRUST_REMOTE_CODE = os.environ.get("TRUST_REMOTE_CODE", "1") != "0" ENFORCE_EAGER = os.environ.get("ENFORCE_EAGER", "0") == "1" PROMPTS = [ "Hello, my nam...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: t vLLM built from main. These backends were not previously available. Forcing the `triton` backend, the previous default behavior, doesn't cause this issue. ```python #!/usr/bin/env python3 """Minimal vLLM-only repro fo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: gpt-oss-20b unquantized model outputting gibberish with non-triton backends (built from main) bug ### Your current environment ### 🐛 Describe the bug Output is gibberish when running unquantized gpt-oss-20b with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: gpt-oss-20b unquantized model outputting gibberish with non-triton backends (built from main) bug ### Your current environment ### 🐛 Describe the bug Output is gibberish when running unquantized gpt-oss-20b with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .split()[0]}") print(f"Platform: {platform.platform()}") print(f"CUDA_VISIBLE_DEVICES: {os.environ.get('CUDA_VISIBLE_DEVICES', ' ')}") try: import torch print(f"torch: {torch.__version__}") print(f"torch.cuda.is_availab...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rt subprocess import sys import time MODEL = os.environ.get("MODEL", "unsloth/gpt-oss-20b-BF16") MOE_BACKEND = os.environ.get("MOE_BACKEND", "auto") DTYPE = os.environ.get("DTYPE", "auto") TEMPERATURE = float(os.environ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
