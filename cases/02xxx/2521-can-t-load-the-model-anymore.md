# vllm-project/vllm#2521: Can't load the model anymore

| 字段 | 值 |
| --- | --- |
| Issue | [#2521](https://github.com/vllm-project/vllm/issues/2521) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization |
| 症状 | build_error;mismatch;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Can't load the model anymore

### Issue 正文摘录

I can't load my model anymore, no matter what parameters I use for loading the model. ``` model_name_or_path = "TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ" tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=False, ) pp = pprint.PrettyPrinter(indent=2) pprint = pp.pprint llm = None def load_model(): global llm del llm if ray.is_initialized(): ray.shutdown() if 'AWQ' in model_name_or_path: quantization = "awq" dtype = "auto" if 'GPTQ' in model_name_or_path: quantization = "gptq" dtype = "float16" else: quantization = None dtype = "auto" llm = LLM(model=model_name_or_path, quantization=quantization, dtype=dtype, # tensor_parallel_size=1, tensor_parallel_size=2, # pipeline_parallel_size=1, # gpu_memory_utilization=0.5, # gpu_memory_utilization=0.6, # gpu_memory_utilization=0.8, # gpu_memory_utilization=0.9, gpu_memory_utilization=random.uniform(0.4, 1.0), # swap_space=10, # swap_space=20, # swap_space=40, swap_space=int(random.uniform(1, 50)), ) # input() print('Model loaded') load_model() ``` ``` nvidia-smi Sat Jan 20 19:55:40 2024 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 545.23.08 Driver Version...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ----------------------------+ | NVIDIA-SMI 545.23.08 Driver Version: 545.23.08 CUDA Version: 12.3 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ed(): ray.shutdown() if 'AWQ' in model_name_or_path: quantization = "awq" dtype = "auto" if 'GPTQ' in model_name_or_path: quantization = "gptq" dtype = "float16" else: quantization = None dtype = "auto" llm = LLM(mode
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # input() print('Model loaded') load_model() ``` ``` nvidia-smi Sat Jan 20 19:55:40 2024 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 545.23.08 Driver Version: 5...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | 2 N/A N/A 2367
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Can't load the model anymore I can't load my model anymore, no matter what parameters I use for loading the model. ``` model_name_or_path = "TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ" tokenizer = AutoTokenizer.from_p

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | local/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0x58 (0x7fc2184b7918 in /home/conic/.local/lib/python3.1… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x78 (0x7fc2184ce468 in /home/conic/.local/lib/python3.10/sit… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7fc25ccb0253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknown fu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
