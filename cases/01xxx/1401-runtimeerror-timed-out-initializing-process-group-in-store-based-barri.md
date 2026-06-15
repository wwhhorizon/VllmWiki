# vllm-project/vllm#1401: RuntimeError: Timed out initializing process group in store based barrier on rank: 1, for key: store_based_barrier_key:1 (world_size=2, worker_count=1, timeout=0:30:00)

| 字段 | 值 |
| --- | --- |
| Issue | [#1401](https://github.com/vllm-project/vllm/issues/1401) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: Timed out initializing process group in store based barrier on rank: 1, for key: store_based_barrier_key:1 (world_size=2, worker_count=1, timeout=0:30:00)

### Issue 正文摘录

Hi, I'm trying to deploy vLLM across 2 machine, each with a single NVIDIA L4 GPU using Ray. I follow the instruction here: https://vllm.readthedocs.io/en/latest/serving/distributed_serving.html. I got the setup ready on both host, they seems to form a proper Ray cluster, confirmed network access between them is fine: ```console $ ray status ======== Autoscaler status: 2023-10-17 17:43:04.622244 ======== Node status --------------------------------------------------------------- Healthy: 1 node_4667fabf1342992ec6673c78f445709bc8e1605ca4b80ef2614efa2b 1 node_b0853d9489e8e9090787aa24049fd311852147efec87cedaadd4b038 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/16.0 CPU 0.0/2.0 GPU 0B/37.70GiB memory 0B/17.31GiB object_store_memory Demands: (no resource demands) ``` But when I tried to run vllm server with `--tensor-parallel-size 2` like this: ```bash python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --tensor-parallel-size 2 --port 23119 --host 0.0.0.0 --tokenizer hf-internal-testing/llama-tokenizer ``` It failed with this tracestack ```console 2023-10-17...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ize 2` like this: ```bash python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --tensor-parallel-size 2 --port 23119 --host 0.0.0.0 --tokenizer hf-internal-testing/llama-tokenizer ``` It fa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: etwork access between them is fine: ```console $ ray status ======== Autoscaler status: 2023-10-17 17:43:04.622244 ======== Node status --------------------------------------------------------------- Healthy: 1 node_466...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 66, in _init_workers_ray init_torch_dist_process_group(self.workers, backend="nccl") File "/home/lamhoangtung.vz/miniforge3/envs/vllm/lib/python3.8/site-packages/ray/air/util/torch_dist.py", line 164, in init_torch_dist...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lel;frontend_api;model_support;quantization quantization crash dtype;env_dependency Hi, I'm trying to deploy vLLM across 2 machine, each with a single NVIDIA L4 GPU using Ray. I follow the instruction here: https://vllm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lama-tokenizer', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, seed=0) Traceback (mos...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
