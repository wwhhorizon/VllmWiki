# vllm-project/vllm#15744: [Bug]: client socket has timed out while trying to connect to GPU node, when initializing DeepSeek R1 in ray vllm serving

| 字段 | 值 |
| --- | --- |
| Issue | [#15744](https://github.com/vllm-project/vllm/issues/15744) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: client socket has timed out while trying to connect to GPU node, when initializing DeepSeek R1 in ray vllm serving

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I construct a ray cluster and try to deploy several DeepSeek-R1 replicas. pipeline-parallel-size: 3 Often, the model initialization would fail (not every time, could turn succeed after several retries) I'm on ray[serve]==2.44.0, vllm==0.8.2. This issue starts ever since 0.7.0. I've verified that it works well on 0.6.6.post1, but every version after that would possible to trigger below error msg when initializing multi-node models, (in our case is R1) Error: ``` :job_id:02000000 :actor_name:ServeReplica:DS-R1:vllmDeployment INFO 2025-03-29 06:17:53,742 DS-R1_vllmDeployment a3e34qi7 -- Starting with engine args: AsyncEngineArgs(model='DeepSeek-R1', served_model_name=None, tokenizer='DeepSeek-R1', hf_config_path=None, task='auto', skip_tokenizer_init=False, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', seed=None, max_model_len=16384, distributed_executor_backend='ray', pipeline_parallel_size=3, tensor_parallel_size=8, enable_expert_parallel=False, max_parallel_loading_workers=None, block_size=None, enable_pref...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: t to GPU node, when initializing DeepSeek R1 in ray vllm serving bug;ray;stale ### Your current environment ### 🐛 Describe the bug I construct a ray cluster and try to deploy several DeepSeek-R1 replicas. pipeline-paral...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: r='DeepSeek-R1', hf_config_path=None, task='auto', skip_tokenizer_init=False, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format= , dtype='...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: eploy several DeepSeek-R1 replicas. pipeline-parallel-size: 3 Often, the model initialization would fail (not every time, could turn succeed after several retries) I'm on ray[serve]==2.44.0, vllm==0.8.2. This issue star...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', seed=None, max_model_len=16384, distributed_executor_backend='ray', pipeline_parallel_size=3, tensor_parallel...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: eReplica:DS-R1:vllmDeployment.initialize_and_get_metadata) frame #17: _PyEval_EvalFrameDefault + 0x56d2 (0x4f3802 in ray::ServeReplica:DS-R1:vllmDeployment.initialize_and_get_metadata) frame #18: _PyFunction_Vectorcall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
