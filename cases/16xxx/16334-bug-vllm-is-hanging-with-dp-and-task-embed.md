# vllm-project/vllm#16334: [Bug]: vLLM is hanging with DP and --task embed

| 字段 | 值 |
| --- | --- |
| Issue | [#16334](https://github.com/vllm-project/vllm/issues/16334) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM is hanging with DP and --task embed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM is hanging when DP is used with --task embed. ```bash python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model Snowflake/snowflake-arctic-embed-l-v2.0 \ --dtype float16 \ --task embed \ --port 7998 \ --seed 123 \ --max-model-len 8192 \ --gpu-memory-utilization 0.80 \ --tensor-parallel-size 1 \ --data-parallel-size 4 \ --served-model-name embed \ --override-pooler-config '{"pooling_type": "CLS", "normalize": false}' \ --use-v2-block-manager \ --max-log-len 20 \ --max-num-seqs 1024 ``` ``` ERROR 04-09 10:54:45 [engine.py:448] Timed out after 601 seconds waiting for clients. 1/4 clients joined. ERROR 04-09 10:54:45 [engine.py:448] Traceback (most recent call last): ERROR 04-09 10:54:45 [engine.py:448] File "/opt/anaconda/envs/vllm/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine ERROR 04-09 10:54:45 [engine.py:448] engine = MQLLMEngine.from_vllm_config( ERROR 04-09 10:54:45 [engine.py:448] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-09 10:54:45 [engine.py:448] File "/opt/anaconda/envs/vllm/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 128, i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vLLM is hanging with DP and --task embed bug;stale ### Your current environment ### 🐛 Describe the bug vLLM is hanging when DP is used with --task embed. ```bash python -u -m vllm.entrypoints.openai.api_server \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/opt/anaconda/envs/vllm/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ Fi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: --override-pooler-config '{"pooling_type": "CLS", "normalize": false}' \ --use-v2-block-manager \ --max-log-len 20 \ --max-num-seqs 1024 ``` ``` ERROR 04-09 10:54:45 [engine.py:448] Timed out after 601 seconds waiting f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: .0.0 \ --model Snowflake/snowflake-arctic-embed-l-v2.0 \ --dtype float16 \ --task embed \ --port 7998 \ --seed 123 \ --max-model-len 8192 \ --gpu-memory-utilization 0.80 \ --tensor-parallel-size 1 \ --data-parallel-size...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
