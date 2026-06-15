# vllm-project/vllm#20965: [Bug]: vllm 1p1d test with v1 and nixl in one container, raise zmq.error.ZMQError: Address already in use (addr='tcp://localhost:5557')

| 字段 | 值 |
| --- | --- |
| Issue | [#20965](https://github.com/vllm-project/vllm/issues/20965) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 1p1d test with v1 and nixl in one container, raise zmq.error.ZMQError: Address already in use (addr='tcp://localhost:5557')

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. prefill: VLLM_USE_V1=1 \ CUDA_VISIBLE_DEVICES=0 \ python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8888 \ --model /stores/framework-test/models/llm/LLM-Research/Meta-Llama-3.1-8B-Instruct \ --gpu-memory-utilization 0.8 \ --trust-remote-code \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --max-model-len 2048 \ --max-num-seqs 256 \ --enforce-eager \ --kv-transfer-config '{"kv_connector": "NixlConnector", "kv_role": "kv_producer", "kv_rank": 0, "kv_parallel_size": 2}' 2. decode: VLLM_USE_V1=1 \ CUDA_VISIBLE_DEVICES=1 \ python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 9999 \ --model /stores/framework-test/models/llm/LLM-Research/Meta-Llama-3.1-8B-Instruct \ --gpu-memory-utilization 0.8 \ --trust-remote-code \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --max-model-len 2048 \ --max-num-seqs 256 \ --enforce-eager \ --kv-transfer-config '{"kv_connector": "NixlConnector", "kv_role": "kv_consumer", "kv_rank": 1, "kv_parallel_size": 2}' INFO 07-15 14:59:23 [nixl_connector.py:526] Registering KV_Caches: use_mla: False, num_blocks: 1434, b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash dtype;env_dependency Your...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 3.1-8B-Instruct \ --gpu-memory-utilization 0.8 \ --trust-remote-code \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --max-model-len 2048 \ --max-num-seqs 256 \ --enforce-eager \ --kv-transf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8888 \ --model /stores/framework-test/models/llm/LLM-Research/Meta-Llama-3.1-8B-Instruct \ --gpu-memory-utilization 0.8 \ --trust-remote-code \ --dtype bfl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t:5557') bug ### Your current environment ### 🐛 Describe the bug 1. prefill: VLLM_USE_V1=1 \ CUDA_VISIBLE_DEVICES=0 \ python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8888 \ --model /stores/framework...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: q/sugar/socket.py", line 320, in bind super().bind(addr) File "zmq/backend/cython/_zmq.py", line 998, in zmq.backend.cython._zmq.Socket.bind File "zmq/backend/cython/_zmq.py", line 187, in zmq.backend.cython._zmq._check...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
