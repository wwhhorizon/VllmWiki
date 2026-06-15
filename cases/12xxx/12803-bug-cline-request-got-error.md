# vllm-project/vllm#12803: [Bug]: cline request got error

| 字段 | 值 |
| --- | --- |
| Issue | [#12803](https://github.com/vllm-project/vllm/issues/12803) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cline request got error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use cline 3.2.0 request DeepSeek-R1-Distill-Qwen-32B which serverd by xinference 1.2.0 got error, and use continue for vs code works well and the process killed after request error log: ```text INFO 02-05 18:42:52 async_llm_engine.py:207] Added request 0fe578a6-e434-11ef-bd67-b4055d15d79f. ERROR 02-05 18:42:55 async_llm_engine.py:64] Engine background task failed ERROR 02-05 18:42:55 async_llm_engine.py:64] Traceback (most recent call last): ERROR 02-05 18:42:55 async_llm_engine.py:64] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 54, in _log_task_completion ERROR 02-05 18:42:55 async_llm_engine.py:64] return_value = task.result() ERROR 02-05 18:42:55 async_llm_engine.py:64] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 851, in run_engine_loop ERROR 02-05 18:42:55 async_llm_engine.py:64] result = task.result() ERROR 02-05 18:42:55 async_llm_engine.py:64] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 774, in engine_step ERROR 02-05 18:42:55 async_llm_engine.py:64] request_outputs = await self.engine.step_async(vir...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: el_input_tensors ERROR 02-05 18:42:55 async_llm_engine.py:64] return builder.build() # type: ignore ERROR 02-05 18:42:55 async_llm_engine.py:64] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner.py"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ne.py:64] File "/usr/local/lib/python3.10/dist-packages/vllm/attention/backends/utils.py", line 215, in build ERROR 02-05 18:42:55 async_llm_engine.py:64] input_block_tables[i, :len(block_table)] = block_table ERROR 02-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: line 867, in build ERROR 02-05 18:42:55 async_llm_engine.py:64] attn_metadata = self.attn_metadata_builder.build( ERROR 02-05 18:42:55 async_llm_engine.py:64] File "/usr/local/lib/python3.10/dist-packages/vllm/attention...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug I use cline 3.2.0 request DeepSeek-R1-Distill-Qwen-32B which serverd by xinference 1.2.0 got error, and use continue for vs code works well and the process killed after request error log: ```text...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: cline request got error bug ### Your current environment ### 🐛 Describe the bug I use cline 3.2.0 request DeepSeek-R1-Distill-Qwen-32B which serverd by xinference 1.2.0 got error, and use continue for vs code wor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
