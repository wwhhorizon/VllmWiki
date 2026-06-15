# vllm-project/vllm#7590: [Bug]: Phi-3-small-128k-instruct on 4 T4 GPUs - Memory error: Tried to allocate 1024.00 GiB

| 字段 | 值 |
| --- | --- |
| Issue | [#7590](https://github.com/vllm-project/vllm/issues/7590) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-3-small-128k-instruct on 4 T4 GPUs - Memory error: Tried to allocate 1024.00 GiB

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to deploy a Phi-3 model on vLLM. Phi-3-small-128k-instruct is ~15GB and 7B parameters, so it should easily fit on my 4 Tesla T4 GPUs, which have 16GB RAM each. However, I am getting a ran out of memory error as it tries to load the model that makes no sense. It says tried to allocate 1024 GB, which does not seem possible since the model itself is not nearly that big. My parameters for this deployment are --dtype float16, --tensor-parallel-size 4. And I had to add --trust-remote-code (even though other issues say this is no longer needed for Phi-3 models, my transformers package is up to date but was requiring this parameter). I know this looks like a standard out of memory error, but this model is ~15 GB, so why would it be trying to allocate 1024GB? Any guidance would be appreciated, thanks. ``` ERROR 08-16 15:18:01 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 1740 died, exit code: -15 INFO 08-16 15:18:01 multiproc_worker_utils.py:123] Killing local vLLM worker processes Traceback (most recent call last): File "/usr/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/u...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: l itself is not nearly that big. My parameters for this deployment are --dtype float16, --tensor-parallel-size 4. And I had to add --trust-remote-code (even though other issues say this is no longer needed for Phi-3 mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: odels/phi3_small.py", line 261, in __init__ self.self_attn = Phi3SmallSelfAttention(config, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/nonroot/.local/lib/python3.11/site-packages/vllm/model_executor/models/phi3_small.py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: so why would it be trying to allocate 1024GB? Any guidance would be appreciated, thanks. ``` ERROR 08-16 15:18:01 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 1740 died, exit code: -15 INFO 08-16 15:18:01...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nt environment ### 🐛 Describe the bug I am trying to deploy a Phi-3 model on vLLM. Phi-3-small-128k-instruct is ~15GB and 7B parameters, so it should easily fit on my 4 Tesla T4 GPUs, which have 16GB RAM each. However,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -instruct on 4 T4 GPUs - Memory error: Tried to allocate 1024.00 GiB bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to deploy a Phi-3 model on vLLM. Phi-3-small-128k-instruct is ~15GB and 7B p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
