# vllm-project/vllm#8068: [Bug]: ValueError: could not broadcast input array from shape (513,) into shape (512,)

| 字段 | 值 |
| --- | --- |
| Issue | [#8068](https://github.com/vllm-project/vllm/issues/8068) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: could not broadcast input array from shape (513,) into shape (512,)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` ERROR 08-31 23:19:40 async_llm_engine.py:65] Engine background task failed ERROR 08-31 23:19:40 async_llm_engine.py:65] Traceback (most recent call last): ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 55, in _log_task_completion ERROR 08-31 23:19:40 async_llm_engine.py:65] return_value = task.result() ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 930, in run_engine_loop ERROR 08-31 23:19:40 async_llm_engine.py:65] result = task.result() ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 873, in engine_step ERROR 08-31 23:19:40 async_llm_engine.py:65] request_outputs = await self.engine.step_async(virtual_engine) ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 337, in step_async ERROR 08-31 23:19:40 async_llm_engine.py:65] output = await self.model_executor.execute_model_async( ERROR 08-31 23:19:40 async...

## 现有链接修复摘要

#43184 [V1][SpecDecode] Resume relaxed acceptance for thinking-mode tokens (port of #22238)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ync ERROR 08-31 23:19:40 async_llm_engine.py:65] output = await self.model_executor.execute_model_async( ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/executor/distribut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ine 873, in engine_step ERROR 08-31 23:19:40 async_llm_engine.py:65] request_outputs = await self.engine.step_async(virtual_engine) ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: el_input_tensors ERROR 08-31 23:19:40 async_llm_engine.py:65] return builder.build() # type: ignore ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner.py"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: line 707, in build ERROR 08-31 23:19:40 async_llm_engine.py:65] attn_metadata = self.attn_metadata_builder.build( ERROR 08-31 23:19:40 async_llm_engine.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/attention...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ne.py:65] File "/usr/local/lib/python3.10/dist-packages/vllm/attention/backends/flash_attn.py", line 467, in build ERROR 08-31 23:19:40 async_llm_engine.py:65] input_block_tables[i, :len(block_table)] = block_table ERRO...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43184](https://github.com/vllm-project/vllm/pull/43184) | mentioned | 0.6 | [V1][SpecDecode] Resume relaxed acceptance for thinking-mode tokens (port of #22238) | uction knob. SGLang's parallel effort (sgl-project/sglang#7702 and #8068) is still open; if there's interest, the two stacks could share a config schema. Searched on 2026-05-19 for |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
