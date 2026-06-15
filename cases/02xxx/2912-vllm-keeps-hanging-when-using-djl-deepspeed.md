# vllm-project/vllm#2912: vllm keeps hanging when using djl-deepspeed

| 字段 | 值 |
| --- | --- |
| Issue | [#2912](https://github.com/vllm-project/vllm/issues/2912) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vllm keeps hanging when using djl-deepspeed

### Issue 正文摘录

I am trying to deploy a Mistral 7B Instruct v0.2 model with `vllm` to an async Sagemaker endpoint with an A10 (g5.2xlarge) machine but I keep seeing ``` [INFO ] PyProcess - W-309-model-stdout: INFO 02-18 18:45:24 llm_engine.py:706] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.6%, CPU KV cache usage: 0.0% ``` The logs happen to show a successful deployment ``` 2024-02-15T17:06:15.629-05:00 | [INFO ] ModelInfo - Available GPU memory: 22481 MB, required: 0 MB, reserved: 500 MB | 2024-02-15T17:06:15.879-05:00 | [INFO ] ModelInfo - Loading model model on gpu(0) | 2024-02-15T17:06:15.879-05:00 | [INFO ] WorkerPool - scaling up min workers by 1 (from 0 to 1) workers. Total range is min 1 to max 1 | 2024-02-15T17:06:15.879-05:00 | [INFO ] PyProcess - Start process: 19000 - retry: 0 | 2024-02-15T17:06:16.129-05:00 | [INFO ] Connection - Set CUDA_VISIBLE_DEVICES=0 | 2024-02-15T17:06:20.242-05:00 | [INFO ] PyProcess - W-332-model-stdout: 332 - djl_python_engine started with args: ['--sock-type', 'unix', '--sock-name', '/tmp/djl_sock.19000', '--model-dir', '/opt/ml/model', '--entry-point'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: unning out of memory, consider decreasing gpu_memory_utilization or enforcing eager mode. | 2024-02-15T17:06:51.962-05:00 | [INFO ] PyProcess - W-332-model-stdout: INFO 02-15 22:06:51 model_runner.py:547] Graph capturin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: W-332-model-stdout: WARNING 02-15 22:06:28 config.py:457] Casting torch.bfloat16 to torch.float16. | 2024-02-15T17:06:33.242-05:00 | [INFO ] PyProcess - W-332-model-stdout: INFO 02-15 22:06:28 llm_engine.py:70] Initiali...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing djl-deepspeed stale I am trying to deploy a Mistral 7B Instruct v0.2 model with `vllm` to an async Sagemaker endpoint with an A10 (g5.2xlarge) machine but I keep seeing ``` [INFO ] PyProcess - W-309-model-stdout: IN...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.6%, CPU KV cache usage: 0.0% ``` The logs happen to show a successful deployment ``` 2024-02-15T17:06:15.629-05:00 | [INFO ] Mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: _format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=False, seed=0) | 2024-02-15T17:06:46.930-05:00 | [INFO ] PyProcess - W-332-model-stdout: INFO 02-15 22:06:45 llm_engine.py:275] # GPU blocks: 2050,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
