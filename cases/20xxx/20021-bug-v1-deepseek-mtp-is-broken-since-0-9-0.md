# vllm-project/vllm#20021: [Bug]: [V1] DeepSeek MTP is broken since 0.9.0

| 字段 | 值 |
| --- | --- |
| Issue | [#20021](https://github.com/vllm-project/vllm/issues/20021) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [V1] DeepSeek MTP is broken since 0.9.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug DeepSeek MTP speculative decoder, which is available on V1 since #18435, is broken on current main branch. I haven't bisect thoroughly, but it was broken at least since v0.9.0. Launch options: ```bash vllm serve /app/model/DEEPSEEK-R1/ \ --served-model-name deepseek-ai/deepseek-r1 \ --gpu-memory-utilization 0.95 \ --tensor-parallel-size 16 \ --max-model-len 65536 \ --max-num-batched-tokens 8192 \ --reasoning-parser deepseek_r1 \ --speculative-config '{"method":"deepseek_mtp","num_speculative_tokeens":1}' ``` On current main(0.9.2.dev223+gee5ad8d2c), the following error is raised: ```log ... Loading safetensors checkpoint shards: 94% Completed | 154/163 [00:25 ) ERROR 06-24 14:22:13 [core.py:519] File "/app/.venv/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 623, in execute_method ERROR 06-24 14:22:13 [core.py:519] raise e ERROR 06-24 14:22:13 [core.py:519] File "/app/.venv/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 614, in execute_method ERROR 06-24 14:22:13 [core.py:519] return run_method(self, method, args, kwargs) ERROR 06-24 14:22:13 [core.py:519] File "/app/.venv/lib/python3.10/site-packa...

## 现有链接修复摘要

#18435 [V1] Support Deepseek MTP | #20022 [V1][Speculative Decoding] Fix DeepSeek MTP

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ug ### Your current environment ### 🐛 Describe the bug DeepSeek MTP speculative decoder, which is available on V1 since #18435, is broken on current main branch. I haven't bisect thoroughly, but it was broken at least s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: o 300 INFO 06-24 15:14:37 [ray_distributed_executor.py:571] VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE = auto INFO 06-24 15:14:37 [ray_distributed_executor.py:573] VLLM_USE_RAY_COMPILED_DAG_OVERLAP_COMM = False ERROR 06-24...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=16, pipeline_parallel_size=1, disable_custom_a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: object has no attribute 'embed_tokens' ``` On v0.9.0 where the multi KV cache group was yet to be introduced, the server frontend becomes ready, but it raises the following error if a request is consumed: ```log ... INF...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend='deepseek_r1'), observ...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18435](https://github.com/vllm-project/vllm/pull/18435) | mentioned | 0.45 | [V1] Support Deepseek MTP | bug deepseek mtp speculative decoder, which is available on v1 since #18435, is broken on current main branch. i haven't bisect thoroughly, but it was broken at least since v0.9.0… |
| [#20022](https://github.com/vllm-project/vllm/pull/20022) | closes_keyword | 0.95 | [V1][Speculative Decoding] Fix DeepSeek MTP | Fix #20021. I need better understanding on multiple KV cache group scenario, so leave it as a future work. ## Test Plan Launch options: ```bash vllm serve /app/model/DEEPSEEK-R |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
