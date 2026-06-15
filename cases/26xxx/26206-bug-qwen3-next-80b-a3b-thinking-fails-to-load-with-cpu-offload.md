# vllm-project/vllm#26206: [Bug]: Qwen3-Next-80B-A3B-Thinking fails to load with CPU offload

| 字段 | 值 |
| --- | --- |
| Issue | [#26206](https://github.com/vllm-project/vllm/issues/26206) |
| 状态 | open |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Thinking fails to load with CPU offload

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am attempting to load Qwen3-Next-80B-A3B-Thinking on a system with 120 GB VRAM + 512 GB RAM. No workee ```bash #!/bin/bash export HF_HUB_CACHE="/srv/huggingface" export CUDA_DEVICE_ORDER=PCI_BUS_ID export CUDA_VISIBLE_DEVICES=0,1,2,3,4 export OMP_NUM_THREADS=60 source ~/.virtualenvs/vllm/bin/activate export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4:$LD_PRELOAD # prepend the library to LD_PRELOAD vllm serve Qwen/Qwen3-Next-80B-A3B-Thinking \ --dtype auto \ --pipeline-parallel-size 5 \ -tp 1 \ --cpu-offload-gb 50 \ --max-model-len 10K \ --max-num-seqs 16 \ --no-enable-chunked-prefill \ --enforce-eager \ --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' ``` Error logs: ```text INFO 10-03 20:29:55 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=10323) INFO 10-03 20:29:58 [api_server.py:1839] vLLM API server version 0.11.0rc2.dev98+g96ebcaa3a (APIServer pid=10323) INFO 10-03 20:29:58 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen3-Next-80B-A3B-Thinking', 'host': '192.168.90.109', 'port': 8080, 'model': 'Qwen/Qwen3-Next-80B-A3B-Thinking', 'max_model_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: --max-model-len 10K \ --max-num-seqs 16 \ --no-enable-chunked-prefill \ --enforce-eager \ --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' ``` Error logs: ```text INFO 10-03 20:29:55 [__i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3-Next-80B-A3B-Thinking fails to load with CPU offload bug ### Your current environment ### 🐛 Describe the bug I am attempting to load Qwen3-Next-80B-A3B-Thinking on a system with 120 GB VRAM + 512 GB RAM. No...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: in/bash export HF_HUB_CACHE="/srv/huggingface" export CUDA_DEVICE_ORDER=PCI_BUS_ID export CUDA_VISIBLE_DEVICES=0,1,2,3,4 export OMP_NUM_THREADS=60 source ~/.virtualenvs/vllm/bin/activate export LD_PRELOAD=/usr/lib/x86_6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: brary to LD_PRELOAD vllm serve Qwen/Qwen3-Next-80B-A3B-Thinking \ --dtype auto \ --pipeline-parallel-size 5 \ -tp 1 \ --cpu-offload-gb 50 \ --max-model-len 10K \ --max-num-seqs 16 \ --no-enable-chunked-prefill \ --enfor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
