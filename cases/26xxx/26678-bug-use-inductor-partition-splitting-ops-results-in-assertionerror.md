# vllm-project/vllm#26678: [Bug]: use_inductor_partition + splitting_ops results in AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#26678](https://github.com/vllm-project/vllm/issues/26678) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | debug |
| Operator 关键词 | cuda;fp8;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: use_inductor_partition + splitting_ops results in AssertionError

### Issue 正文摘录

### Your current environment vllm main, torch 2.9 RC, B200 ### 🐛 Describe the bug With https://github.com/vllm-project/vllm/pull/25845, we can now use `splitting_ops` to specify what things to split on if `use_inductor_partition=True`. However, the following repro runs into the following error: Repro: ```python import os from typing import Optional import torch import torch.nn as nn from torch._dynamo.test_case import TestCase, run_tests from torch._subclasses.fake_tensor import FakeTensorMode from vllm import LLM, SamplingParams from vllm.config import CompilationConfig, CompilationLevel, CUDAGraphMode from tests.compile.backend import TestBackend from vllm.config import CompilationConfig, PassConfig, VllmConfig, CompilationLevel os.environ["TORCHINDUCTOR_FORCE_DISABLE_CACHES"] = "1" os.environ["VLLM_DISABLE_COMPILE_CACHE"] = "1" os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "1" os.environ["VLLM_USE_V1"] = "1" os.environ["VLLM_LOGGING_LEVEL"] = "DEBUG" os.environ["VLLM_USE_STANDALONE_COMPILE"] = "1" config = CompilationConfig( level=CompilationLevel.PIECEWISE, cudagraph_mode=CUDAGraphMode.FULL, # splitting_ops=[], custom_ops=['+quant_fp8'], use_inductor_graph_partition=True, ) l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: b.com/vllm-project/vllm/pull/25845, we can now use `splitting_ops` to specify what things to split on if `use_inductor_partition=True`. However, the following repro runs into the following error: Repro: ```python import...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ssertionError bug ### Your current environment vllm main, torch 2.9 RC, B200 ### 🐛 Describe the bug With https://github.com/vllm-project/vllm/pull/25845, we can now use `splitting_ops` to specify what things to split on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: graph_mode=CUDAGraphMode.FULL, # splitting_ops=[], custom_ops=['+quant_fp8'], use_inductor_graph_partition=True, ) llm = LLM( model="RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8", gpu_memory_utilization=0.6, max_model_len=30...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: or import FakeTensorMode from vllm import LLM, SamplingParams from vllm.config import CompilationConfig, CompilationLevel, CUDAGraphMode from tests.compile.backend import TestBackend from vllm.config import CompilationC...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: g import Optional import torch import torch.nn as nn from torch._dynamo.test_case import TestCase, run_tests from torch._subclasses.fake_tensor import FakeTensorMode from vllm import LLM, SamplingParams from vllm.config...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
