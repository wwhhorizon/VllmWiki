# vllm-project/vllm#9134: Issue Running Inference on a Model with Multi Nodes and Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#9134](https://github.com/vllm-project/vllm/issues/9134) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Issue Running Inference on a Model with Multi Nodes and Inference

### Issue 正文摘录

### Your current environment ``` I'm attempting to run a multi-node, multi-GPU inference setup using vLLM with pipeline parallelism. However, I'm encountering an error related to the number of available GPUs. (llama_env) kogans@vinaka-vaka-levu:~$ nvidia-smi Mon Oct 7 13:19:31 2024 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.183.06 Driver Version: 535.183.06 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA GeForce RTX 2060 ... On | 00000000:01:00.0 Off | N/A | | N/A 36C P8 2W / 65W | 8MiB / 6144MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ +---------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=================================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ----------------------------+ | NVIDIA-SMI 535.183.06 Driver Version: 535.183.06 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Issue Running Inference on a Model with Multi Nodes and Inference usage;stale ### Your current environment ``` I'm attempting to run a multi-node, multi-GPU inference setup using vLLM with pipeline parallelism. However,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: multi-node, multi-GPU inference setup using vLLM with pipeline parallelism. However, I'm encountering an error related to the number of available GPUs. (llama_env) kogans@vinaka-vaka-levu:~$ nvidia-smi Mon Oct 7 13:19:3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ize 2 Error Log: INFO 10-04 16:11:19 config.py:1652] Downcasting torch.float32 to torch.float16. INFO 10-04 16:11:19 config.py:899] Defaulting to use ray for distributed inference WARNING 10-04 16:11:19 config.py:370] A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.12/site-packages/vllm/scripts.py", line 165, in main args.dispatch_function(args) File "/home/kogans/llama_project/llama_env/lib/python3.12/site-packages/vllm/scripts.py", line 37, in serve uvloop.run(run_ser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
