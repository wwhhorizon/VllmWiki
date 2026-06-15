# vllm-project/vllm#16997: [Bug]: Qwen2.5-VL-72B Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#16997](https://github.com/vllm-project/vllm/issues/16997) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL-72B Inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Which version of vLLM actually supports Qwen2.5-VL-72B inference, I've tried various versions since 0.8.2, including the latest commit tonight, and have had all sorts of problems with it, such as OUT OF MEMORY, etc. Also the offline version and the server version I've tried and have had all sorts of problems with both. So is there a normal usable version? Some bug: [1;36m(VllmWorker rank=3 pid=1863294)[0;0m ERROR 04-23 01:03:33 [multiproc_executor.py:470] WorkerProc hit an exception. [1;36m(VllmWorker rank=3 pid=1863294)[0;0m ERROR 04-23 01:03:33 [multiproc_executor.py:470] Traceback (most recent call last): [1;36m(VllmWorker rank=3 pid=1863294)[0;0m ERROR 04-23 01:03:33 [multiproc_executor.py:470] File "/jizhicfs/leoyizhang/anaconda3/envs/vllm_0.8.4_f344107/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 465, in worker_busy_loop [1;36m(VllmWorker rank=3 pid=1863294)[0;0m ERROR 04-23 01:03:33 [multiproc_executor.py:470] output = func(*args, **kwargs) [1;36m(VllmWorker rank=3 pid=1863294)[0;0m ERROR 04-23 01:03:33 [multiproc_executor.py:470] ^^^^^^^^^^^^^^^^^^^^^ [1;36m(VllmWorker rank=3 pid=18...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rence bug ### Your current environment ### 🐛 Describe the bug Which version of vLLM actually supports Qwen2.5-VL-72B inference, I've tried various versions since 0.8.2, including the latest commit tonight, and have had...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 3/envs/vllm_0.8.4_f344107/lib/python3.12/site-packages/vllm/v1/attention/backends/flash_attn.py", line 578, in forward [1;36m(VllmWorker rank=3 pid=1863294)[0;0m ERROR 04-23 01:03:33 [multiproc_executor.py:470] cascad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ROR 04-23 01:03:33 [multiproc_executor.py:470] prefix_output, prefix_lse = flash_attn_varlen_func( [1;36m(VllmWorker rank=3 pid=1863294)[0;0m ERROR 04-23 01:03:33 [multiproc_executor.py:470] ^^^^^^^^^^^^^^^^^^^^^^^ [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5-VL-72B Inference bug ### Your current environment ### 🐛 Describe the bug Which version of vLLM actually supports Qwen2.5-VL-72B inference, I've tried various versions since 0.8.2, including the latest com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
