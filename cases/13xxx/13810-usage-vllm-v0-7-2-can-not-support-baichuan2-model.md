# vllm-project/vllm#13810: [Usage]: vllm v0.7.2 can not support baichuan2 model

| 字段 | 值 |
| --- | --- |
| Issue | [#13810](https://github.com/vllm-project/vllm/issues/13810) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm v0.7.2 can not support baichuan2 model

### Issue 正文摘录

### Your current environment GPU: H20 CUDA: 12.2 NVIDIA driver: 535.161.08 vllm: v0.7.2 summary: Error occurred when using vllm v0.7.2 to deploy baichuan2 model. The ERROR LOG is: ERROR 02-24 23:19:35 engine.py:389] If cu_seqlens_k is passed in, then page table is not supported ERROR 02-24 23:19:35 engine.py:389] Traceback (most recent call last): ERROR 02-24 23:19:35 engine.py:389] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 380, in run_mp_engine ERROR 02-24 23:19:35 engine.py:389] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 02-24 23:19:35 engine.py:389] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-24 23:19:35 engine.py:389] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 123, in from_engine_args ERROR 02-24 23:19:35 engine.py:389] return cls(ipc_path=ipc_path, ERROR 02-24 23:19:35 engine.py:389] ^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-24 23:19:35 engine.py:389] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 75, in __init__ ERROR 02-24 23:19:35 engine.py:389] self.engine = LLMEngine(*args, **kwargs) ERROR 02-24 23...

## 现有链接修复摘要

#15231 [Bugfix] detect alibi and revert to FA2

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 23:19:35 engine.py:389] self.model_executor.determine_num_available_blocks()) ERROR 02-24 23:19:35 engine.py:389] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-24 23:19:35 engine.py:389] File "/usr/local...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e.py:389] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/flash_attn.py", line 770, in forward ERROR 02-24 23:19:35 engine.py:389] flash_attn_varlen_func( ERROR 02-24 23:19:35 engine.py:389] File "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: not support baichuan2 model usage ### Your current environment GPU: H20 CUDA: 12.2 NVIDIA driver: 535.161.08 vllm: v0.7.2 summary: Error occurred when using vllm v0.7.2 to deploy baichuan2 model. The ERROR LOG is: ERROR...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ailable_blocks ERROR 02-24 23:19:35 engine.py:389] self.model_runner.profile_run() ERROR 02-24 23:19:35 engine.py:389] File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_con...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15231](https://github.com/vllm-project/vllm/pull/15231) | closes_keyword | 0.95 | [Bugfix] detect alibi and revert to FA2 | FIX #13810 <!--- pyml disable-next-line no-emphasis-as-heading --> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
