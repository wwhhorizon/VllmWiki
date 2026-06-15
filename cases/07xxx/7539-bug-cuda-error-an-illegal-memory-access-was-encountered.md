# vllm-project/vllm#7539: [Bug]: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#7539](https://github.com/vllm-project/vllm/issues/7539) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The code cannot be shown due to corporate confidentiality reasons, and the problem is: for qwen2-72b-gptq-int4 as model and qwen2-7b-gptq-int8 as draft model, when spleculative decoding, a crash occurred after a short run in high concurrency. And the weird thing is, sometimes it crashes, sometimes it doesn't, it's random. server： current_dir=`pwd` cd /usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/quantization/utils if [ ! -f marlin_utils.py_bak ];then mv marlin_utils.py marlin_utils.py_bak fi sed 's/GPTQ_MARLIN_MIN_THREAD_K = 128/GPTQ_MARLIN_MIN_THREAD_K = 64/g' marlin_utils.py_bak | tee marlin_utils.py > /dev/null cd $current_dir python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8080 \ --served-model-name Qwen2-72B \ --model model \ --disable-log-requests \ --tensor-parallel-size 2 \ --kv-cache-dtype auto \ --gpu-memory-utilization 0.95 \ --enable-prefix-caching \ --use-v2-block-manager \ --speculative-model speculative_model \ --num-speculative-tokens 5 \ --max-model-len 20000 \ the log is : INFO: 127.0.0.1:41774 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:41818 - "POS...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug The code cannot be shown due to corporate confidentiality reasons, and the problem is: for qwen2-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: orporate confidentiality reasons, and the problem is: for qwen2-72b-gptq-int4 as model and qwen2-7b-gptq-int8 as draft model, when spleculative decoding, a crash occurred after a short run in high concurrency. And the w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tions HTTP/1.1" 500 Internal Server Error performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: --disable-log-requests \ --tensor-parallel-size 2 \ --kv-cache-dtype auto \ --gpu-memory-utilization 0.95 \ --enable-prefix-caching \ --use-v2-block-manager \ --speculative-model speculative_model \ --num-speculative-to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ry-utilization 0.95 \ --enable-prefix-caching \ --use-v2-block-manager \ --speculative-model speculative_model \ --num-speculative-tokens 5 \ --max-model-len 20000 \ the log is : INFO: 127.0.0.1:41774 - "POST /v1/chat/c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
