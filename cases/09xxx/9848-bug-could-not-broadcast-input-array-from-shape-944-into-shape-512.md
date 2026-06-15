# vllm-project/vllm#9848: [Bug]:  could not broadcast input array from shape (944,) into shape (512,)

| 字段 | 值 |
| --- | --- |
| Issue | [#9848](https://github.com/vllm-project/vllm/issues/9848) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  could not broadcast input array from shape (944,) into shape (512,)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve "meta-llama/Meta-Llama-3.1-70B-Instruct" --port 7000 --max-num-seqs 64 --tensor-parallel-size=8 --max_model_len=32768 --distributed-executor-backend=mp --dtype=half Log: ERROR 10-30 11:32:21 engine.py:158] ValueError('could not broadcast input array from shape (944,) into shape (512,)') ERROR 10-30 11:32:21 engine.py:158] Traceback (most recent call last): ERROR 10-30 11:32:21 engine.py:158] File "/home/user/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 156, in start ERROR 10-30 11:32:21 engine.py:158] self.run_engine_loop() ERROR 10-30 11:32:21 engine.py:158] File "/home/user/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 219, in run_engine_loop ERROR 10-30 11:32:21 engine.py:158] request_outputs = self.engine_step() ERROR 10-30 11:32:21 engine.py:158] File "/home/user/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 237, in engine_step ERROR 10-30 11:32:21 engine.py:158] raise e ERROR 10-30 11:32:21 engine.py:158] File "/home/user/anaconda3/env...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: epare_model_input_tensors ERROR 10-30 11:32:21 engine.py:158] return builder.build() # type: ignore ERROR 10-30 11:32:21 engine.py:158] File "/home/user/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/worker/model...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 4 --tensor-parallel-size=8 --max_model_len=32768 --distributed-executor-backend=mp --dtype=half Log: ERROR 10-30 11:32:21 engine.py:158] ValueError('could not broadcast input array from shape (944,) into shape (512,)')...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ess ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ner.py", line 867, in build ERROR 10-30 11:32:21 engine.py:158] attn_metadata = self.attn_metadata_builder.build( ERROR 10-30 11:32:21 engine.py:158] File "/home/user/anaconda3/envs/vllm/lib/python3.10/site-packages/vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: (944,) into shape (512,) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm serve "meta-llama/Meta-Llama-3.1-70B-Instruct" --port 7000 --max-num-seqs 64 --tensor-paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
