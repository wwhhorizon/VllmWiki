# vllm-project/vllm#2022: Mixtral-8x7B-v0.1 TP 8 GPUS EDIT: TypeError: PaddedGatherOp.forward() takes 6 positional arguments but 7 were given

| 字段 | 值 |
| --- | --- |
| Issue | [#2022](https://github.com/vllm-project/vllm/issues/2022) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral-8x7B-v0.1 TP 8 GPUS EDIT: TypeError: PaddedGatherOp.forward() takes 6 positional arguments but 7 were given

### Issue 正文摘录

fixed Error: KeyError: 'model.layers.13.block_sparse_moe.experts.4.w2.weight' fixed with 'pt' as mentioned in https://github.com/vllm-project/vllm/issues/2020 the new error is TypeError: PaddedGatherOp.forward() takes 6 positional arguments but 7 were given model: https://huggingface.co/mistralai/Mixtral-8x7B-v0.1 python: 3.10 gpus: g5.48xlarge 8 x 24G A10 on AWS logs: ``` 023-12-11T17:25:22.531+02:00 | [WARN ] PyProcess - W-1511-model-stderr: llm = LLM(model=model_name, tensor_parallel_size=num_gpus, dtype=dtype, trust_remote_code=trust_remote_code, -- | -- | 2023-12-11T17:25:22.531+02:00 | [WARN ] PyProcess - W-1511-model-stderr: File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 93, in __init__ | 2023-12-11T17:25:22.531+02:00 | [WARN ] PyProcess - W-1511-model-stderr: self.llm_engine = LLMEngine.from_engine_args(engine_args) | 2023-12-11T17:25:22.531+02:00 | [WARN ] PyProcess - W-1511-model-stderr: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 246, in from_engine_args | 2023-12-11T17:25:22.531+02:00 | [WARN ] PyProcess - W-1511-model-stderr: engine = cls(*engine_configs, | 2023-12-11T17:25:22.531+02:00 | [WARN ] PyProce...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: () takes 6 positional arguments but 7 were given fixed Error: KeyError: 'model.layers.13.block_sparse_moe.experts.4.w2.weight' fixed with 'pt' as mentioned in https://github.com/vllm-project/vllm/issues/2020 the new err...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: e2c9c6dde7357dbac2ec0c2c57d8cd Note: with TP 4 I can't even run it (ofc OOM problems, the gpu memory for 4 gpus is not enough I guess)
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ts but 7 were given fixed Error: KeyError: 'model.layers.13.block_sparse_moe.experts.4.w2.weight' fixed with 'pt' as mentioned in https://github.com/vllm-project/vllm/issues/2020 the new error is TypeError: PaddedGather...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: - W-575-model-stderr: File "/usr/local/lib/python3.10/dist-packages/stk/backend/autocast.py", line 28, in decorate_fwd | 2023-12-11T18:13:26.782+02:00 | [WARN ] PyProcess - W-575-model-stderr: return fwd(*args, **kwargs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uirements.txt: langdetect fastapi uvicorn[standard] ninja # For faster builds. psutil ray==2.6.3 numpy huggingface-hub>=0.16.4 wrapt-timeout-decorator pydantic =0.12.3 transformers==4.36.0 accelerate>=0.24.1 peft>=0.6.2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
