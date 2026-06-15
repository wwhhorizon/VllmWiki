# vllm-project/vllm#13648: [Bug]: [ROCM] _sdpa_attention() takes from 8 to 9 positional arguments but 10 were given

| 字段 | 值 |
| --- | --- |
| Issue | [#13648](https://github.com/vllm-project/vllm/issues/13648) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCM] _sdpa_attention() takes from 8 to 9 positional arguments but 10 were given

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Step to reproduce ``` python -m vllm.entrypoints.openai.api_server --model avoroshilov/DeepSeek-R1-Distill-Qwen-32B-GPTQ_4bit-128g --disable-log-requests --max-model-len 4096 --gpu-memory-utilization 0.95 --served-model-name deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --max-num-seqs 8 -tp 2 --enforce-eager --enable-chunked-prefill ``` ``` ERROR 02-21 03:07:52 engine.py:400] _sdpa_attention() takes from 8 to 9 positional arguments but 10 were given ERROR 02-21 03:07:52 engine.py:400] Traceback (most recent call last): ERROR 02-21 03:07:52 engine.py:400] File "/root/vllm/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine ERROR 02-21 03:07:52 engine.py:400] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 02-21 03:07:52 engine.py:400] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-21 03:07:52 engine.py:400] File "/root/vllm/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args ERROR 02-21 03:07:52 engine.py:400] return cls(ipc_path=ipc_path, ERROR 02-21 03:07:52 engine.py:400] ^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-21 03:07:52 engine.py:400] File "/root/vllm/vllm/engine/multi...

## 现有链接修复摘要

#13649 [ROCM] Fix native attention function call for navi

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [ROCM] _sdpa_attention() takes from 8 to 9 positional arguments but 10 were given bug ### Your current environment ### 🐛 Describe the bug Step to reproduce ``` python -m vllm.entrypoints.openai.api_server --model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: el avoroshilov/DeepSeek-R1-Distill-Qwen-32B-GPTQ_4bit-128g --disable-log-requests --max-model-len 4096 --gpu-memory-utilization 0.95 --served-model-name deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --max-num-seqs 8 -tp 2 --...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ^^ ERROR 02-21 03:07:52 engine.py:400] File "/root/vllm/vllm/attention/backends/rocm_flash_attn.py", line 711, in forward ERROR 02-21 03:07:52 engine.py:400] out = self.attn_func( ERROR 02-21 03:07:52 engine.py:400] ^^^...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 03:07:52 engine.py:400] self.model_executor.determine_num_available_blocks()) ERROR 02-21 03:07:52 engine.py:400] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 02-21 03:07:52 engine.py:400] File "/root/vllm...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#13649](https://github.com/vllm-project/vllm/pull/13649) | closes_keyword | 0.95 | [ROCM] Fix native attention function call for navi | FIX #13648 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
