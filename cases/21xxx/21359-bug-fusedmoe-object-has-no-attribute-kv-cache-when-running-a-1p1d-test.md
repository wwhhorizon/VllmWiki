# vllm-project/vllm#21359: [Bug]: 'FusedMoE' object has no attribute 'kv_cache'  when running a 1P1D test with PowerMoE-3b

| 字段 | 值 |
| --- | --- |
| Issue | [#21359](https://github.com/vllm-project/vllm/issues/21359) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'FusedMoE' object has no attribute 'kv_cache'  when running a 1P1D test with PowerMoE-3b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug FusedMoE' object has no attribute 'kv_cache' when running a 1P1D test with PowerMoE-3b Follow the example `/vllm/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_example_p2p_nccl_xpyd.sh` 1. start the proxy 2. start prefill Node 3. start decode Node 4. Execute the command ```bash curl http://127.0.0.1:10001/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "/models/PowerMoE-3b", "prompt": "San Francisco is a", "max_tokens": 8, "temperature": 0 }' ``` error: ``` ERROR 07-22 00:57:43 [core.py:588] EngineCore encountered a fatal error. ERROR 07-22 00:57:43 [core.py:588] Traceback (most recent call last): ERROR 07-22 00:57:43 [core.py:588] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 579, in run_engine_core ERROR 07-22 00:57:43 [core.py:588] engine_core.run_busy_loop() ERROR 07-22 00:57:43 [core.py:588] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 606, in run_busy_loop ERROR 07-22 00:57:43 [core.py:588] self._process_engine_step() ERROR 07-22 00:57:43 [core.py:588] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py",...

## 现有链接修复摘要

#21428 [BugFix] Fix shared storage connector load kv only load attention layer

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -d '{ "model": "/models/PowerMoE-3b", "prompt": "San Francisco is a", "max_tokens": 8, "temperature": 0 }' ``` error: ``` ERROR 07-22 00:57:43 [core.py:588] EngineCore encountered a fatal error. ERROR 07-22 00:57:43 [co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nccl_xpyd/disagg_example_p2p_nccl_xpyd.sh` 1. start the proxy 2. start prefill Node 3. start decode Node 4. Execute the command ```bash curl http://127.0.0.1:10001/v1/completions \ -H "Content-Type: application/json" \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mpletions \ -H "Content-Type: application/json" \ -d '{ "model": "/models/PowerMoE-3b", "prompt": "San Francisco is a", "max_tokens": 8, "temperature": 0 }' ``` error: ``` ERROR 07-22 00:57:43 [core.py:588] EngineCore e...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: 'FusedMoE' object has no attribute 'kv_cache' when running a 1P1D test with PowerMoE-3b bug ### Your current environment ### 🐛 Describe the bug FusedMoE' object has no attribute 'kv_cache' when running a 1P1D tes...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21428](https://github.com/vllm-project/vllm/pull/21428) | closes_keyword | 0.95 | [BugFix] Fix shared storage connector load kv only load attention layer | fix #21359 , The bug was introduced in #19717 (Use torch op for all kernels in FusedMoE forward. Add additional testing for cudagraphs) pr19717 add fusedmoe into vllm_config.compi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
