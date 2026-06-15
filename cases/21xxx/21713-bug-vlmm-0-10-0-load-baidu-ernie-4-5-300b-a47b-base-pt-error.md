# vllm-project/vllm#21713: [Bug]: vlmm 0.10.0 load  baidu/ERNIE-4.5-300B-A47B-Base-PT  error

| 字段 | 值 |
| --- | --- |
| Issue | [#21713](https://github.com/vllm-project/vllm/issues/21713) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vlmm 0.10.0 load  baidu/ERNIE-4.5-300B-A47B-Base-PT  error

### Issue 正文摘录

### Your current environment centos 8 python:3.9 transformer: 4.54.0 vllm: 0.10.0 cuda: 12.9 ### 🐛 Describe the bug launch cmd: vllm serve $local_model_path --host ***** --port 8081 --dtype bfloat16 --pipeline-parallel-size 1 --tensor-parallel-size 8 --trust-remote-code --enable-chunked-prefill --served-model-name /mnt/hdfs/zw04mlnn01/checkpoint/llm_platform/model/baidu/ERNIE-4.5-300B-A47B-Base-PT/main --max-model-len 131072 --max-num-batched-tokens 2048 --max-num-seqs 256 --gpu-memory-utilization 0.9 --disable-custom-all-reduce --enable-chunked-prefill throw miss some weight, but model itself does not have these weights : ` WorkerProc failed to start. �[1;36m(VllmWorker rank=3 pid=4867)�[0;0m ERROR 07-26 18:47:24 [multiproc_executor.py:511] Traceback (most recent call last): �[1;36m(VllmWorker rank=3 pid=4867)�[0;0m ERROR 07-26 18:47:24 [multiproc_executor.py:511] File "/usr/local/lib64/python3.9/site-packages/vllm/v1/executor/multiproc_executor.py", line 485, in worker_main �[1;36m(VllmWorker rank=3 pid=4867)�[0;0m ERROR 07-26 18:47:24 [multiproc_executor.py:511] worker = WorkerProc(*args, **kwargs) �[1;36m(VllmWorker rank=3 pid=4867)�[0;0m ERROR 07-26 18:47:24 [multiproc_execut...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lm serve $local_model_path --host ***** --port 8081 --dtype bfloat16 --pipeline-parallel-size 1 --tensor-parallel-size 8 --trust-remote-code --enable-chunked-prefill --served-model-name /mnt/hdfs/zw04mlnn01/checkpoint/l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vlmm 0.10.0 load baidu/ERNIE-4.5-300B-A47B-Base-PT error bug ### Your current environment centos 8 python:3.9 transformer: 4.54.0 vllm: 0.10.0 cuda: 12.9 ### 🐛 Describe the bug launch cmd: vllm serve $local_model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: urrent environment centos 8 python:3.9 transformer: 4.54.0 vllm: 0.10.0 cuda: 12.9 ### 🐛 Describe the bug launch cmd: vllm serve $local_model_path --host ***** --port 8081 --dtype bfloat16 --pipeline-parallel-size 1 --t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ons. performance distributed_parallel;model_support cuda crash dtype;env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ights were not initialized from checkpoint: {'model.layers.19.mlp.shared_experts.gate_up_proj.weight', 'model.layers.37.mlp.shared_experts.gate_up_proj.weight', 'model.layers.31.mlp.shared_experts.down_proj.weight', 'mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
