# vllm-project/vllm#38976: [Bug]:TimeoutError: RPC call to sample_tokens timed out. when pp is on under xpu env

| 字段 | 值 |
| --- | --- |
| Issue | [#38976](https://github.com/vllm-project/vllm/issues/38976) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:TimeoutError: RPC call to sample_tokens timed out. when pp is on under xpu env

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve --model /data/models/gpt-oss-20b/ --enforce-eager --port 8000 --host 0.0.0.0 --trust-remote-code --disable-sliding-window --gpu-memory-util=0.87 --max-num-batched-tokens=8192 --max-model-len=8192 --block-size 64 -tp=2 -pp 2 --distributed-executor-backend=mp ``` ```bash WARNING 04-04 18:12:14 [argparse_utils.py:191] With `vllm serve`, you should provide the model as a positional argument or in a config file instead of via the `--model` option. The `--model` option will be removed in v0.13. (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:299] (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.19.1rc1.dev29+g93726b2a1 (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:299] █▄█▀ █ █ █ █ model /data/models/gpt-oss-20b/ (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:299] (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:233] non-default args: {'model_tag': '/data/models/gpt-oss-20b/', 'host': '0.0.0.0', 'model': '/data/model...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: 85] Using max model len 8192 (APIServer pid=335596) INFO 04-04 18:12:14 [scheduler.py:238] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=335596) INFO 04-04 18:12:14 [config.py:126] Overridi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d=335596) INFO 04-04 18:12:14 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.19.1rc1.dev29+g93726b2a1 (APIServer pid=335596) INFO 04-04 18:12:14 [utils.py:299] █▄█▀ █ █ █ █ model /data/models/gpt-oss-20b/ (APIServer pid=335...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: 6) INFO 04-04 18:12:14 [compilation.py:290] Enabled custom fusions: norm_quant, act_quant (EngineCore pid=336188) INFO 04-04 18:12:19 [core.py:105] Initializing a V1 LLM engine (v0.19.1rc1.dev29+g93726b2a1) with config:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: len=8192 --block-size 64 -tp=2 -pp 2 --distributed-executor-backend=mp ``` ```bash WARNING 04-04 18:12:14 [argparse_utils.py:191] With `vllm serve`, you should provide the model as a positional argument or in a config f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: .87 --max-num-batched-tokens=8192 --max-model-len=8192 --block-size 64 -tp=2 -pp 2 --distributed-executor-backend=mp ``` ```bash WARNING 04-04 18:12:14 [argparse_utils.py:191] With `vllm serve`, you should provide the m...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
