# vllm-project/vllm#20716: [Bug]: LLM.classify() fails on second call with ModernBERT due to missing torch.SymInt shape symbols

| 字段 | 值 |
| --- | --- |
| Issue | [#20716](https://github.com/vllm-project/vllm/issues/20716) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLM.classify() fails on second call with ModernBERT due to missing torch.SymInt shape symbols

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM import time llm = LLM(model="NousResearch/Minos-v1", max_model_len=8192, task="classify", compilation_config={"level": 3}) start = time.time() result = llm.classify(["Hello, how are you?"], use_tqdm=False) print(result[0].outputs.probs) print(f"First inference took: {time.time() - start:.2f}s") # Second call fails llm.classify(["Hello, how are you?"], use_tqdm=False) ``` I'm encountering an issue when using `vLLM==0.9.1` with a custom model (`ModernBERTForSequenceClassification`). The first call to `LLM.classify()` works as expected. However, a second call to `classify()` on the same instance crashes with an error originating from `vllm/compilation/backends.py`, specifically due to this code: ```python sym_shape_indices = [i for i, x in enumerate(args) if isinstance(x, torch.SymInt)] ``` The list ends up empty because the input shape arguments are plain integers (e.g., `7`) instead of symbolic shapes like `s0`, which is expected by the compiler backend. **Error Message:** ```python File ~/llmenv/lib/python3.12/site-packages/vllm/compilation/cuda_piecewise_backend.py:112, in CUDAPiecewiseBackend.__ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM import time llm = LLM(model="NousResearch/Minos-v1", max_model_len=8192, task="classify", compilation_config={"level": 3}) start = time.time...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug ```python from vllm import LLM import time llm = LLM(model="NousResearch/Minos-v1", max_model_len=8192, task="classify", compilation_config={"level": 3}) start = time.time() result = llm.classify(["Hell...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e same instance crashes with an error originating from `vllm/compilation/backends.py`, specifically due to this code: ```python sym_shape_indices = [i for i, x in enumerate(args) if isinstance(x, torch.SymInt)] ``` The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug ```python from vllm import LLM import time llm = LLM(model="NousResearch/Minos-v1", max_model_len=8192, task="classify", compilation_config={"level": 3}) start = time.time() result = llm.classify(["Hello, how are you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: econd call with ModernBERT due to missing torch.SymInt shape symbols bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM import time llm = LLM(model="NousResearch/Minos-v1", max_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
