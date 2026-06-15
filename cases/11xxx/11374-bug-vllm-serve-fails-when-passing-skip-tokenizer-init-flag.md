# vllm-project/vllm#11374: [Bug]: `vllm serve` fails when passing `--skip-tokenizer-init` flag

| 字段 | 值 |
| --- | --- |
| Issue | [#11374](https://github.com/vllm-project/vllm/issues/11374) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `vllm serve` fails when passing `--skip-tokenizer-init` flag

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I try to spin up a vllm server and I pass `--skip-tokenizer-init` to avoid initializing the default tokenizer, I face this error: ```bash INFO 12-20 18:09:25 model_runner.py:1527] Graph capturing finished in 20 secs, took 0.90 GiB INFO 12-20 18:09:25 llm_engine.py:431] init engine (profile, create kv cache, warmup model) took 24.05 seconds ERROR 12-20 18:09:25 engine.py:366] [Errno 2] No such file or directory: '/tmp/tmpnofm47vw/gauge_mostrecent_20577.db' ERROR 12-20 18:09:25 engine.py:366] Traceback (most recent call last): ERROR 12-20 18:09:25 engine.py:366] File "/home/ishitamed/vllm/vllm/engine/multiprocessing/engine.py", line 357, in run_mp_engine ERROR 12-20 18:09:25 engine.py:366] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 12-20 18:09:25 engine.py:366] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 12-20 18:09:25 engine.py:366] File "/home/ishitamed/vllm/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args ERROR 12-20 18:09:25 engine.py:366] return cls(ipc_path=ipc_path, ERROR 12-20 18:09:25 engine.py:366] ^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: de. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: skip-tokenizer-init` flag bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I try to spin up a vllm server and I pass `--skip-tokenizer-init` to avoid initializing th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: `vllm serve` fails when passing `--skip-tokenizer-init` flag bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I try to spin up a vllm server and I pass `--ski...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: secs, took 0.90 GiB INFO 12-20 18:09:25 llm_engine.py:431] init engine (profile, create kv cache, warmup model) took 24.05 seconds ERROR 12-20 18:09:25 engine.py:366] [Errno 2] No such file or directory: '/tmp/tmpnofm47...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
