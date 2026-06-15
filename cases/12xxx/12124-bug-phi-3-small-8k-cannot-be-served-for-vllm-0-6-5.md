# vllm-project/vllm#12124: [Bug]: Phi-3-small-8k cannot be served for vllm >= 0.6.5

| 字段 | 值 |
| --- | --- |
| Issue | [#12124](https://github.com/vllm-project/vllm/issues/12124) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-3-small-8k cannot be served for vllm >= 0.6.5

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running the following code encounters an exception during model build: `Error in model execution (input dumped to ...): too many values to unpack (expected 2)` ```console python -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --host 0.0.0.0 --port 8080 \ --model microsoft/Phi-3-small-8k-instruct \ --gpu-memory-utilization 0.90 \ --enforce-eager \ --disable-log-requests \ --disable-custom-all-reduce \ --trust-remote-code ``` Traceback: ``` ERROR 01-16 16:42:00 engine.py:366] Traceback (most recent call last): ERROR 01-16 16:42:00 engine.py:366] File ".../.venv/lib/python3.10/site-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper ERROR 01-16 16:42:00 engine.py:366] return func(*args, **kwargs) ERROR 01-16 16:42:00 engine.py:366] File ".../.venv/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1691, in execute_model ERROR 01-16 16:42:00 engine.py:366] hidden_or_intermediate_states = model_executable( ERROR 01-16 16:42:00 engine.py:366] File ".../.venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl ERROR 0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the bug Running the following code encounters an exception during model build: `Error in model execution (input dumped to ...): too many values to unpack (expected 2)` ```console python -m vllm.entrypoints.openai.api_se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Phi-3-small-8k cannot be served for vllm >= 0.6.5 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running the following code encounters an exception during model build:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ne.py:366] File ".../.venv/lib/python3.10/site-packages/vllm/attention/backends/blocksparse_attn.py", line 384, in forward ERROR 01-16 16:42:00 engine.py:366] num_tokens, hidden_size = query.shape ERROR 01-16 16:42:00 e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 42:00 engine.py:366] attn_output = self.attn(q, k, v, kv_cache, attn_metadata=attn_metadata) ERROR 01-16 16:42:00 engine.py:366] File ".../.venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ailable_blocks ERROR 01-16 16:42:00 engine.py:366] self.model_runner.profile_run() ERROR 01-16 16:42:00 engine.py:366] File ".../.venv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_cont...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
