# vllm-project/vllm#32116: [Bug]: Wen vllm engine core ready timeout because deepgemm warmup, apiserver exit,but engine core keep running

| 字段 | 值 |
| --- | --- |
| Issue | [#32116](https://github.com/vllm-project/vllm/issues/32116) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cache;gemm;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Wen vllm engine core ready timeout because deepgemm warmup, apiserver exit,but engine core keep running

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When i use 4*8 H200 to running Deepseek v3.2, use `vllm serve DeepSeek-V3.2 -tp=2 -dp=16 ....` to start vllm, but in dp head node happing because engine core ready timeout apiserve exit, but engine core not exit. ``` (ApiServer_3 pid=39385) Process ApiServer_3: (ApiServer_3 pid=39385) Traceback (most recent call last): (ApiServer_3 pid=39385) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (ApiServer_3 pid=39385) self.run() (ApiServer_3 pid=39385) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (ApiServer_3 pid=39385) self._target(*self._args, **self._kwargs) (ApiServer_3 pid=39385) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 251, in run_api_server_worker_proc (ApiServer_3 pid=39385) uvloop.run( (ApiServer_3 pid=39385) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 96, in run (ApiServer_3 pid=39385) return __asyncio.run( (ApiServer_3 pid=39385) ^^^^^^^^^^^^^^ (ApiServer_3 pid=39385) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (ApiServer_3 pid=39385) return runner.run(main) (ApiServer_3 pid=393...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: p/__init__.py", line 96, in run (ApiServer_3 pid=39385) return __asyncio.run( (ApiServer_3 pid=39385) ^^^^^^^^^^^^^^ (ApiServer_3 pid=39385) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (ApiServer_3 p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -11 01:44:59 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: because deepgemm warmup, apiserver exit,but engine core keep running bug;stale ### Your current environment ### 🐛 Describe the bug When i use 4*8 H200 to running Deepseek v3.2, use `vllm serve DeepSeek-V3.2 -tp=2 -dp=16...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). DeepGEMM warmup: 100%|████████████████████████████████████████████████████████████████████████████████████████████| 8181/8181 [19:0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
