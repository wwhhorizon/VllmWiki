# vllm-project/vllm#798: Connection refused

| 字段 | 值 |
| --- | --- |
| Issue | [#798](https://github.com/vllm-project/vllm/issues/798) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Connection refused

### Issue 正文摘录

**### _(llama) xxx@work-3:~/workspace/LLaMA-Efficient-Tuning-main$ ORCH_CPP_LOG_LEVEL=INFO TORCH_DISTRIBUTED_DEBUG=INFO NCCL_DEBUG=INFO NCCL_SOCKET_IFNAME=eth1 python -m vllm.entrypoints.api_server --model model/llama-2-70B --tensor-parallel-size 16 --engine-use-ray --worker-use-ray_** 2023-08-19 03:54:17,196 INFO worker.py:1431 -- Connecting to existing Ray cluster at address: 10.58.226.18:6379... 2023-08-19 03:54:17,202 INFO worker.py:1621 -- Connected to Ray cluster. INFO: Started server process [1985409] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://localhost:8000 (Press CTRL+C to quit) (LLMEngine pid=2347640, ip=10.58.226.15) INFO 08-19 15:49:41 llm_engine.py:70] Initializing an LLM engine with config: model='model/llama-2-70B', tokenizer='model/llama-2-70B', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=16, seed=0) (LLMEngine pid=2347640, ip=10.58.226.15) INFO 08-19 15:49:41 tokenizer.py:29] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Connection refused **### _(llama) xxx@work-3:~/workspace/LLaMA-Efficient-Tuning-main$ ORCH_CPP_LOG_LEVEL=INFO TORCH_DISTRIBUTED_DEBUG=INFO NCCL_DEBUG=INFO NCCL_SOCKET_IFNAME=eth1 python -m vllm.entrypoints.api_server --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Connection refused **### _(llama) xxx@work-3:~/workspace/LLaMA-Efficient-Tuning-main$ ORCH_CPP_LOG_LEVEL=INFO TORCH_DISTRIBUTED_DEBUG=INFO NCCL_DEBUG=INFO NCCL_SOCKET_IFNAME=eth1 python -m vllm.entrypoints.api_server --...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nizer='model/llama-2-70B', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=16, seed=0) (LLMEngine pid=2347640, ip...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 347640, ip=10.58.226.15) torch.distributed.all_reduce(torch.zeros(1).cuda()) (LLMEngine pid=2347640, ip=10.58.226.15) File "/home/huawei/anaconda3/envs/llama/lib/python3.10/site-packages/torch/distributed/distributed_c1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: (LLMEngine pid=2347640, ip=10.58.226.15) ray.exceptions.RayTaskError(DistBackendError): ray::RayWorker.execute_method() (pid=1985578, ip=10.58.226.18, actor_id=4e1229cbba77c46f4862cf2e10000000, repr= ) (LLMEngine pid=23...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
