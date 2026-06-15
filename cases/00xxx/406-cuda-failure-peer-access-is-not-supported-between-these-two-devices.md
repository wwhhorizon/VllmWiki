# vllm-project/vllm#406: Cuda failure 'peer access is not supported between these two devices'

| 字段 | 值 |
| --- | --- |
| Issue | [#406](https://github.com/vllm-project/vllm/issues/406) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Cuda failure 'peer access is not supported between these two devices'

### Issue 正文摘录

Usage stats collection is enabled. To disable this, run the following command: `ray disable-usage-stats` before starting Ray. See https://docs.ray.io/en/master/cluster/usage-stats.html for more details. 2023-07-08 23:11:34,236 INFO worker.py:1610 -- Started a local Ray instance. View the dashboard at 127.0.0.1:8265 INFO 07-08 23:11:35 llm_engine.py:60] Initializing an LLM engine with config: model='openlm-research/open_llama_13b', tokenizer='openlm-research/open_llama_13b', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=4, seed=0) INFO 07-08 23:11:35 tokenizer.py:28] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. (Worker pid=4225) Exception raised in creation task: The actor died because of an error raised in its creation task, ray::Worker.__init__() (pid=4225, ip=172.31.68.176, actor_id=5dc662848f950df8d330eb8a01000000, repr= ) (Worker pid=4225) File "/opt/conda/lib/python3.10/site-packages/vllm/worker/worker.py", line 40, in __init__ (Work...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1275, internal error, NCCL version 2.14.3 (Worker pid=4225) ncclInternalError: Internal check failed. (Worker pid=4225) Last error: (Worker pid=4225) Cuda failure 'peer acce...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 5 INFO 07-08 23:11:35 llm_engine.py:60] Initializing an LLM engine with config: model='openlm-research/open_llama_13b', tokenizer='openlm-research/open_llama_13b', tokenizer_mode=auto, dtype=torch.float16, use_dummy_wei...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: a_13b', tokenizer='openlm-research/open_llama_13b', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=4, seed=0) INFO 07-08 23:11:35 tokeniz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Cuda failure 'peer access is not supported between these two devices' bug Usage stats collection is enabled. To disable this, run the following command: `ray disable-usage-stats` before starting Ray. See https://docs.ray
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ult_pg.allreduce([tensor], opts) (Worker pid=4225) torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1275, internal error, NCCL version 2.14.3 (Worker pid=4225) ncclI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
