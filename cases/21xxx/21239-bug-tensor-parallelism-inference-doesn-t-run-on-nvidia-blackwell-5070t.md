# vllm-project/vllm#21239: [Bug]: tensor parallelism inference doesn't run on Nvidia Blackwell 5070ti

| 字段 | 值 |
| --- | --- |
| Issue | [#21239](https://github.com/vllm-project/vllm/issues/21239) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tensor parallelism inference doesn't run on Nvidia Blackwell 5070ti

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Setting tensor-parallel-size to 2 gives the error: (full error with traceback: https://gist.github.com/QuditWolf/da3763e79e282e6dac4c0191ef7c212d) ``` (VllmWorker rank=1 pid=3897542) ERROR 07-19 20:22:09 [multiproc_executor.py:546] RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)` ``` I have two Nvidia Blackwell 5070ti cards with 16GB memory each. I am trying to run deepseek-r1 models distributed on both GPUs. Sizes: 1.5B ~3GB, 8B ~16GB, 14B ~28GB, 30B, 70B **Could run Qwen 1.5B on a single gpu.** **Coudn't run Qwen-1.5B or Llama-8B distributed on both GPUs with tensor_parallel_size=2.** Would it help in debugging, to try to run Llama-8B on single gpu with tensor-parallel-size=1 by getting it to fit within 16GB? (how should I do that? disabling kv caching, batching etc?) Following Works: ```vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --port xxxx --tensor-parallel-size 1``` Doesn't work: ```vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --port xxxx --tensor-parallel-size 2``` Doesn't work: ```vllm serve deepseek-ai/DeepSeek-R1-Distill-Llama-8B --port xxxx --tensor-parallel-size...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: tensor parallelism inference doesn't run on Nvidia Blackwell 5070ti bug;stale ### Your current environment ### 🐛 Describe the bug Setting tensor-parallel-size to 2 gives the error: (full error with traceback: htt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ell 5070ti cards with 16GB memory each. I am trying to run deepseek-r1 models distributed on both GPUs. Sizes: 1.5B ~3GB, 8B ~16GB, 14B ~28GB, 30B, 70B **Could run Qwen 1.5B on a single gpu.** **Coudn't run Qwen-1.5B or...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tensor parallelism inference doesn't run on Nvidia Blackwell 5070ti bug;stale ### Your current environment ### 🐛 Describe the bug Setting tensor-parallel-size to 2 gives the error: (full error with traceback: https://gi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
