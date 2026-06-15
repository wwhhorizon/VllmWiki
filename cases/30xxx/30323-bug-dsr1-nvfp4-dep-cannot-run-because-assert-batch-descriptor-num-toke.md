# vllm-project/vllm#30323: [Bug]: DSR1 NVFP4 DEP cannot run because assert batch_descriptor.num_tokens == num_tokens_padded

| 字段 | 值 |
| --- | --- |
| Issue | [#30323](https://github.com/vllm-project/vllm/issues/30323) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;moe |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 NVFP4 DEP cannot run because assert batch_descriptor.num_tokens == num_tokens_padded

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message: [0;36m(EngineCore_DP1 pid=333606)[0;0m [2025-12-06 07:52:08] ERROR _base.py:426: exception calling callback for [0;36m(EngineCore_DP1 pid=333606)[0;0m Traceback (most recent call last): [0;36m(EngineCore_DP1 pid=333606)[0;0m File "/usr/lib/python3.12/concurrent/futures/_base.py", line 424, in add_done_callback [0;36m(EngineCore_DP1 pid=333606)[0;0m fn(self) [0;36m(EngineCore_DP1 pid=333606)[0;0m File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 337, in callback [0;36m(EngineCore_DP1 pid=333606)[0;0m result = f.result() [0;36m(EngineCore_DP1 pid=333606)[0;0m ^^^^^^^^^^ [0;36m(EngineCore_DP1 pid=333606)[0;0m File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result [0;36m(EngineCore_DP1 pid=333606)[0;0m return self.__get_result() [0;36m(EngineCore_DP1 pid=333606)[0;0m ^^^^^^^^^^^^^^^^^^^ [0;36m(EngineCore_DP1 pid=333606)[0;0m File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result [0;36m(EngineCore_DP1 pid=333606)[0;0m raise self._exception [0;36m(EngineCore_DP1 pid=333606)[0;...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: DSR1 NVFP4 DEP cannot run because assert batch_descriptor.num_tokens == num_tokens_padded bug;stale ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: owing repo. git clone https://github.com/kimbochen/bench_serving.git pip install pandas datasets --break-system-packages ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: added bug;stale ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message: [0;36m(EngineCore_DP1 pid=333606)[0;0m [2025-12-06 07:52:08] ERROR _base.py:426: except...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: run because assert batch_descriptor.num_tokens == num_tokens_padded bug;stale ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message: [0;36m(EngineCore_DP1 pid=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: VLLM_ATTENTION_BACKEND=FLASHINFER_MLA export VLLM_FLASHINFER_MOE_BACKEND=latency export VLLM_USE_FLASHINFER_MOE_FP4=1 server-side: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model nvidia/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
