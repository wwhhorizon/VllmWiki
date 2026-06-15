# vllm-project/vllm#15676: [Bug]:  vllm 0.8.2 serve Gemma3 error

| 字段 | 值 |
| --- | --- |
| Issue | [#15676](https://github.com/vllm-project/vllm/issues/15676) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  vllm 0.8.2 serve Gemma3 error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (VllmWorker rank=0 pid=7482) INFO 03-28 12:57:37 [loader.py:447] Loading weights took 4.77 seconds (VllmWorker rank=0 pid=7482) INFO 03-28 12:57:37 [gpu_model_runner.py:1186] Model loading took 13.1665 GB and 5.346817 seconds (VllmWorker rank=1 pid=7560) INFO 03-28 12:57:38 [loader.py:447] Loading weights took 5.62 seconds (VllmWorker rank=1 pid=7560) INFO 03-28 12:57:38 [gpu_model_runner.py:1186] Model loading took 13.1665 GB and 6.083788 seconds (VllmWorker rank=2 pid=7645) INFO 03-28 12:57:39 [loader.py:447] Loading weights took 5.55 seconds (VllmWorker rank=2 pid=7645) INFO 03-28 12:57:39 [gpu_model_runner.py:1186] Model loading took 13.1665 GB and 6.311147 seconds (VllmWorker rank=3 pid=7737) INFO 03-28 12:57:40 [loader.py:447] Loading weights took 6.46 seconds (VllmWorker rank=3 pid=7737) INFO 03-28 12:57:40 [gpu_model_runner.py:1186] Model loading took 13.1665 GB and 7.117844 seconds ERROR 03-28 12:57:52 [core.py:343] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-28 12:57:52 [core.py:343] File "/venv/main/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 335, in run_engine_core ERROR 03-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;gemm;operator;sampling;tri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: I still can't deploy the model. It seems like I need to set --kv-cache-dtype fp8 or a similar parameter to optimize memory usage. Someone can Help me?????? ### Before submitting a new issue... - [x] Make sure you alread...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm 0.8.2 serve Gemma3 error bug ### Your current environment ### 🐛 Describe the bug (VllmWorker rank=0 pid=7482) INFO 03-28 12:57:37 [loader.py:447] Loading weights took 4.77 seconds (VllmWorker rank=0 pid=7482...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ??? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 12:57:52 [core.py:343] raise ValueError("No available memory for the cache blocks. " ERROR 03-28 12:57:52 [core.py:343] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
