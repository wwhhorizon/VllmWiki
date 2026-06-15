# vllm-project/vllm#4760: [Performance]: Why the avg. througput generation is low?

| 字段 | 值 |
| --- | --- |
| Issue | [#4760](https://github.com/vllm-project/vllm/issues/4760) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Why the avg. througput generation is low?

### Issue 正文摘录

### Report of performance regression Hi I use this: ``` server_vllm.py \ --model "/data/models_temp/functionary-small-v2.4/" \ --served-model-name "functionary" \ --dtype=bfloat16 \ --max-model-len 2048 \ --host 0.0.0.0 \ --port 8000 \ --enforce-eager \ --gpu-memory-utilization 0.94 ``` on rtx 3090 24gb Why I've got low speed?: `Avg prompt throughput: 102.2 tokens/s, Avg generation throughput: 2.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.8%, CPU KV cache usage: 0.0%` This is my config: ``` | INFO 05-11 08:17:48 server_vllm.py:473] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name='functionary', grammar_sampling=False, model='/data/models_temp/functionary-small-v2.4/', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='bfloat16', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=2048, guided_decoding_backend='outlines', worker_use_ray=False, pipeline_parallel_size=1, tensor_par...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Performance]: Why the avg. througput generation is low? performance;stale ### Report of performance regression Hi I use this: ``` server_vllm.py \ --model "/data/models_temp/functionary-small-v2.4/" \ --served-model-na...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: emp/functionary-small-v2.4/" \ --served-model-name "functionary" \ --dtype=bfloat16 \ --max-model-len 2048 \ --host 0.0.0.0 \ --port 8000 \ --enforce-eager \ --gpu-memory-utilization 0.94 ``` on rtx 3090 24gb Why I've g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: use this: ``` server_vllm.py \ --model "/data/models_temp/functionary-small-v2.4/" \ --served-model-name "functionary" \ --dtype=bfloat16 \ --max-model-len 2048 \ --host 0.0.0.0 \ --port 8000 \ --enforce-eager \ --gpu-m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: m.py:473] args: Namespace(host='0.0.0.0', port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name='functionary', grammar_sampling=False, model='/data/mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eport of performance regression Hi I use this: ``` server_vllm.py \ --model "/data/models_temp/functionary-small-v2.4/" \ --served-model-name "functionary" \ --dtype=bfloat16 \ --max-model-len 2048 \ --host 0.0.0.0 \ --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
