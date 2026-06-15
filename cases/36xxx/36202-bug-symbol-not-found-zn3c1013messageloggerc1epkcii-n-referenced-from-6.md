# vllm-project/vllm#36202: [Bug]: Symbol not found: __ZN3c1013MessageLoggerC1EPKcii\n  Referenced from: <6A12389C-7A10-3CA4-BEDF-893991822933> /opt/anaconda3/envs/vllm-inference/lib/python3.11/site-packages/vllm/_C.abi3.so\n

| 字段 | 值 |
| --- | --- |
| Issue | [#36202](https://github.com/vllm-project/vllm/issues/36202) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Symbol not found: __ZN3c1013MessageLoggerC1EPKcii\n  Referenced from: <6A12389C-7A10-3CA4-BEDF-893991822933> /opt/anaconda3/envs/vllm-inference/lib/python3.11/site-packages/vllm/_C.abi3.so\n

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (vllm-inference) wendell@Wendell-Mac Qwen3-VL-2B-Instruct-New % python3 -m vllm.entrypoints.openai.api_server \ --model . \ --served-model-name Qwen3-VL-2B-Instruct \ --dtype auto \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 \ --max-model-len 16384 \ --max-num-batched-tokens 16384 \ --enforce-eager \ --allowed-local-media-path /Users/wendell/dataset \ --mm-processor-kwargs '{"max_image_size": [512, 512]}' INFO 03-06 10:56:42 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:287] (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:287] █ █ █▄ ▄█ (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.0 (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:287] █▄█▀ █ █ █ █ model . (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:287] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:287] (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:223] non-default args: {'host': '0.0.0.0', 'model': '.', 'trust_remote_code': True, 'allowed_local_media_path': '/Users/we...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Symbol not found: __ZN3c1013MessageLoggerC1EPKcii\n Referenced from: <6A12389C-7A10-3CA4-BEDF-893991822933> /opt/anaconda3/envs/vllm-inference/lib/python3.11/site-packages/vllm/_C.abi3.so\n bug ### Your current e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _server \ --model . \ --served-model-name Qwen3-VL-2B-Instruct \ --dtype auto \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 \ --max-model-len 16384 \ --max-num-batched-tokens 16384 \ --enforce-eager \ --allowed-l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ronment ### 🐛 Describe the bug (vllm-inference) wendell@Wendell-Mac Qwen3-VL-2B-Instruct-New % python3 -m vllm.entrypoints.openai.api_server \ --model . \ --served-model-name Qwen3-VL-2B-Instruct \ --dtype auto \ --trus...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: '{"max_image_size": [512, 512]}' INFO 03-06 10:56:42 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. (APIServer pid=82653) INFO 03-06 10:56:46 [utils.py:287...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: reduce=True, quantization=None, enforce_eager=True, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cpu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, d...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
