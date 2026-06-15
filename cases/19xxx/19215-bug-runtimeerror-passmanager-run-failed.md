# vllm-project/vllm#19215: [Bug]: RuntimeError: PassManager::run failed

| 字段 | 值 |
| --- | --- |
| Issue | [#19215](https://github.com/vllm-project/vllm/issues/19215) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: PassManager::run failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Start serving wtih "vllm serve Qwen/Qwen3-8B" on v100 When access it with client = OpenAI( base_url=f"http://{DEFAULT_HOST_IP}:8000/v1", api_key="EMPTY", } completion = client.chat.completions.create( model="Qwen/Qwen3-8B", messages=[ { "role": "user", "content": prompt, } ], extra_body={"guided_json": json_schema, "guided_decoding_backend": "xgrammar:disable-any-whitespace"}, ) got the following error ERROR 06-05 14:26:00 [engine.py:164] File "/home/abc/myenv/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 300, in forward ERROR 06-05 14:26:00 [engine.py:164] hidden_states = self.model(input_ids, positions, intermediate_tensors, ERROR 06-05 14:26:00 [engine.py:164] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-05 14:26:00 [engine.py:164] File "/home/abc/myenv/lib/python3.12/site-packages/vllm/compilation/decorators.py", line 172, in __call__ ERROR 06-05 14:26:00 [engine.py:164] return self.forward(*args, **kwargs) ERROR 06-05 14:26:00 [engine.py:164] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-05 14:26:00 [engine.py:164] File "/home/abc/myenv/lib/python3.12/site-packages/vllm/model_executor/mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: line 569, in run ERROR 06-05 14:26:00 [engine.py:164] kernel = self.compile(src, target=target, options=options.__dict__) ERROR 06-05 14:26:00 [engine.py:164] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RuntimeError: PassManager::run failed bug;stale ### Your current environment ### 🐛 Describe the bug Start serving wtih "vllm serve Qwen/Qwen3-8B" on v100 When access it with client = OpenAI( base_url=f"http://{DE...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: RuntimeError: PassManager::run failed bug;stale ### Your current environment ### 🐛 Describe the bug Start serving wtih "vllm serve Qwen/Qwen3-8B" on v100 When access it with client = OpenAI( base_url=f"http://{DE...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: extra_body={"guided_json": json_schema, "guided_decoding_backend": "xgrammar:disable-any-whitespace"}, ) got the following error ERROR 06-05 14:26:00 [engine.py:164] File "/home/abc/myenv/lib/python3.12/site-packages/vl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: .py:164] return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) ERROR 06-05 14:26:00 [engine.py:164] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-05 14:26:00 [engine.py:164] Fil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
