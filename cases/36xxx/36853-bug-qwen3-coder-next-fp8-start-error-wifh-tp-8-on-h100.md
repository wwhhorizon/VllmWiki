# vllm-project/vllm#36853: [Bug]: Qwen3-Coder-Next-FP8 start error wifh tp=8 on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#36853](https://github.com/vllm-project/vllm/issues/36853) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Coder-Next-FP8 start error wifh tp=8 on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug hi, - command ``` nerdctl run --gpus all --name vllm-serve --shm-size 64g -v /mnt/data02/000000/model/Qwen3-Coder-Next-FP8:/data/model -p 8000:8000 -e VLLM_USE_DEEP_GEMM=0 --ipc=host vllm/vllm-openai:v0.17.0 /data/model --served-model-name hello-model --gpu-memory-utilization 0.93 --tensor-parallel-size 8 --enable-expert-parallel --enable-force-include-usag ``` - error ``` (Worker_TP2_EP2 pid=490) INFO 03-11 22:47:13 [multiproc_executor.py:730] Parent process exited, terminating worker (Worker_TP2_EP2 pid=490) ERROR 03-11 22:47:13 [multiproc_executor.py:772] WorkerProc failed to start. (Worker_TP2_EP2 pid=490) ERROR 03-11 22:47:13 [multiproc_executor.py:772] Traceback (most recent call last): (Worker_TP2_EP2 pid=490) ERROR 03-11 22:47:13 [multiproc_executor.py:772] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 743, in worker_main (Worker_TP2_EP2 pid=490) ERROR 03-11 22:47:13 [multiproc_executor.py:772] worker = WorkerProc(*args, **kwargs) (Worker_TP2_EP2 pid=490) ERROR 03-11 22:47:13 [multiproc_executor.py:772] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP2_EP2 pid=490) ERROR 03-11 22:47:13...

## 现有链接修复摘要

#41312 [Bugfix][DeepSeek V4] Enable cross-node TP=16 FP8 serving

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3-Coder-Next-FP8 start error wifh tp=8 on H100 bug ### Your current environment ### 🐛 Describe the bug hi, - command ``` nerdctl run --gpus all --name vllm-serve --shm-size 64g -v /mnt/data02/000000/model/Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Coder-Next-FP8 start error wifh tp=8 on H100 bug ### Your current environment ### 🐛 Describe the bug hi, - command ``` nerdctl run --gpus all --name vllm-serve --shm-size 64g -v /mnt/data02/000000/model/Qwe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 000/model/Qwen3-Coder-Next-FP8:/data/model -p 8000:8000 -e VLLM_USE_DEEP_GEMM=0 --ipc=host vllm/vllm-openai:v0.17.0 /data/model --served-model-name hello-model --gpu-memory-utilization 0.93 --tensor-parallel-size 8 --en...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: gemm_linear;model_support;moe;quantization fp8;moe;operator;quantization build_error;crash dtype;env_dependency #41312 [Bugfix][DeepSeek V4] Enable cross-node TP=16 FP8 serving Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Qwen3-Coder-Next-FP8 start error wifh tp=8 on H100 bug ### Your current environment ### 🐛 Describe the bug hi, - command ``` nerdctl run --gpus all --name vllm-serve --shm-size 64g -v /mnt/data02/000000/model/Qwe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41312](https://github.com/vllm-project/vllm/pull/41312) | closes_keyword | 0.95 | [Bugfix][DeepSeek V4] Enable cross-node TP=16 FP8 serving | Fix A, open) - #36853 — Qwen3-Coder-Next-FP8 TP=8 error (related class, open) - #36836 — RayExecutorV2 (merged, enables the 2-node topology) - #38164 — RayExecutorV2 + EEP (futu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
