# vllm-project/vllm#31641: [Bug]: enable_chunked_prefill=True causes hang in AsyncLLM which is affected by disable_log_stats=True

| 字段 | 值 |
| --- | --- |
| Issue | [#31641](https://github.com/vllm-project/vllm/issues/31641) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enable_chunked_prefill=True causes hang in AsyncLLM which is affected by disable_log_stats=True

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am observing a hang when using `enable_chunked_prefill=True`. Here is a minimal reproducer which you can run like this; the strange thing is removing `disable_log_stats=True` will avoid the hang. ```bash chmod a+x reproducer.py ./reproducer.py ``` using this container `nvcr.io/nvidia/nemo-rl:v0.4.0.nemotron_3_nano`. `reproducer.py` below ```python #!/usr/bin/env -S uv run --script -q # /// script # dependencies = [ # "vllm==0.11.2", # "ray[default]==2.49.2" # ] # /// import asyncio import uuid from vllm.engine.arg_utils import AsyncEngineArgs from vllm.v1.engine.async_llm import AsyncLLM from vllm import SamplingParams # ============================================================================= # CONFIGURATION # ============================================================================= MODEL_NAME = "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16" MAX_NEW_TOKENS = 1 MAX_MODEL_LEN = 100000 PREFILL_LENGTHS = [ 8192, 8193, ] async def test(): engine_args = AsyncEngineArgs( model=MODEL_NAME, load_format="dummy", skip_tokenizer_init=False, enable_expert_parallel=False, enable_prefix_caching=False, max_model_len=MAX_MODEL_LEN, trust...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ow ```python #!/usr/bin/env -S uv run --script -q # /// script # dependencies = [ # "vllm==0.11.2", # "ray[default]==2.49.2" # ] # /// import asyncio import uuid from vllm.engine.arg_utils import AsyncEngineArgs from vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: enable_chunked_prefill=True causes hang in AsyncLLM which is affected by disable_log_stats=True bug;stale ### Your current environment ### 🐛 Describe the bug I am observing a hang when using `enable_chunked_prefi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ====================================================================== # CONFIGURATION # ============================================================================= MODEL_NAME = "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: logprobs_mode="processed_logprobs", distributed_executor_backend="ray", enable_chunked_prefill=True, max_num_batched_tokens=1024, tensor_parallel_size=2, ) print("DEBUG: Creating AsyncLLM engine...") llm = AsyncLLM.from...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ==================== MODEL_NAME = "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16" MAX_NEW_TOKENS = 1 MAX_MODEL_LEN = 100000 PREFILL_LENGTHS = [ 8192, 8193, ] async def test(): engine_args = AsyncEngineArgs( model=MODEL_NAM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
