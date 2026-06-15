# vllm-project/vllm#881: Loading Model through Multi-Node Ray Cluster Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#881](https://github.com/vllm-project/vllm/issues/881) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Loading Model through Multi-Node Ray Cluster Fails

### Issue 正文摘录

## Problem Description I'm trying to spin up the VLLM API server inside a docker container (that has vllm and all requirements installed) on the head node of a ray cluster (the cluster contains 4 nodes and has access to 4 T4 GPUs) with the following command in the container: `python3 -m vllm.entrypoints.api_server --host 0.0.0.0 --port 8000 --model /home/model --tensor-parallel-size 4 --swap-space 2 ` I get back the following error (NOTE: I x'd out the IP): ``` python3 -m vllm.entrypoints.api_server --host 0.0.0.0 --port 8000 --model /home/model --tensor-parallel-size 4 --swap-space^Me 2 ^[[?2004l^M2023-08-25 22:29:16,736 INFO worker.py:1313 -- Using address ray://xxx.xxx.xxx.xx:10001 set in the environment variable RAY_ADDRESS 2023-08-25 22:29:16,737 INFO client_builder.py:237 -- Passing the following kwargs to ray.init() on the server: ignore_reinit_error INFO 08-25 22:29:19 llm_engine.py:70] Initializing an LLM engine with config: model='/home/model', tokenizer='/home/model', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=4, seed=0) WARNING 08-25 22:29:19 config.py:191] Po...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Problem Description I'm trying to spin up the VLLM API server inside a docker container (that has vllm and all requirements installed) on the head node of a ray cluster (the cluster contains 4 nodes and has access to 4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Loading Model through Multi-Node Ray Cluster Fails ## Problem Description I'm trying to spin up the VLLM API server inside a docker container (that has vllm and all requirements installed) on the head node of a ray clus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: - Each g4dn.xlarge instance has 1 Nvidia T4 GPU with 16 GB RAM. The node architecure is x86_64 and the platform is ubuntu. - So, in total my multi-node deployment has 4 different nodes with 4 total T4 GPUS. - Nvidia dri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: , tokenizer='/home/model', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=4, seed=0) WARNING 08-25 22:29:19 conf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: directory COPY llama-2-13b-merged/ /home/model/ # Expose port for http requests EXPOSE 8000 9999 # Setup entrypoint ENTRYPOINT ["/bin/bash"] ``` The requirements.txt is ``` vllm pandas transformers peft datasets jupyter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
