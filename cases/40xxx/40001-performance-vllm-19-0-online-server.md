# vllm-project/vllm#40001: [Performance]: vllm 19.0 online server测试波动偏大

| 字段 | 值 |
| --- | --- |
| Issue | [#40001](https://github.com/vllm-project/vllm/issues/40001) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vllm 19.0 online server测试波动偏大

### Issue 正文摘录

### Proposal to improve performance 将模型部署成server做测测试，命令如下： ``` export CUBLAS_WORKSPACE_CONFIG=:4096:8 export PYTHONHASHSEED=0 OMP_NUM_THREADS=1 \ CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m vllm.entrypoints.openai.api_server --model /models/Qwen3-VL-8B-Instruct --served-model-name Qwen3-VL-8B-Instruct --port=8007 --limit-mm-per-prompt.image=15 --seed 42 --gpu-memory-utilization 0.90 --trust-remote-code True --tensor-parallel-size 8 --attention-backend FLASH_ATTN ``` 在batch size 为32，temperature 0 seed 42下请求调用，一批116的数据测试acc波动很大 ``` accuracy: 0.7155172413793104 precision: 0.7916666666666666 recall: 0.6551724137931034 f1: 0.7169811320754716 tp: 38 fp: 10 fn: 20 tn: 45 accuracy: 0.7844827586206896 precision: 0.7692307692307693 recall: 0.8333333333333334 f1: 0.8 tp: 50 fp: 15 fn: 10 tn: 41 "accuracy": 0.7241379310344828, "precision": 0.7959183673469388, "recall": 0.6724137931034483, "f1": 0.7289719626168225, "tp": 39, "fp": 10, "fn": 19, "tn": 45, ``` ACC最大靠近7个点 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before subm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: improve performance 将模型部署成server做测测试，命令如下： ``` export CUBLAS_WORKSPACE_CONFIG=:4096:8 export PYTHONHASHSEED=0 OMP_NUM_THREADS=1 \ CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m vllm.entrypoints.openai.api_server --model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ``` 在batch size 为32，temperature 0 seed 42下请求调用，一批116的数据测试acc波动很大 ``` accuracy: 0.7155172413793104 precision: 0.7916666666666666 recall: 0.6551724137931034 f1: 0.7169811320754716 tp: 38 fp: 10 fn: 20 tn: 45 accuracy: 0.7...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ``` 在batch size 为32，temperature 0 seed 42下请求调用，一批116的数据测试acc波动很大 ``` accuracy: 0.7155172413793104 precision: 0.7916666666666666 recall: 0.6551724137931034 f1: 0.7169811320754716 tp: 38 fp: 10 fn: 20 tn: 45 accuracy: 0.7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LAS_WORKSPACE_CONFIG=:4096:8 export PYTHONHASHSEED=0 OMP_NUM_THREADS=1 \ CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m vllm.entrypoints.openai.api_server --model /models/Qwen3-VL-8B-Instruct --served-model-name Qwen3-V...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ation 0.90 --trust-remote-code True --tensor-parallel-size 8 --attention-backend FLASH_ATTN ``` 在batch size 为32，temperature 0 seed 42下请求调用，一批116的数据测试acc波动很大 ``` accuracy: 0.7155172413793104 precision: 0.7916666666666666...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
