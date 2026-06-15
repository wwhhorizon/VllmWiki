# vllm-project/vllm#19014: [Bug]: Qwen-2.5 VL inference speed very low

| 字段 | 值 |
| --- | --- |
| Issue | [#19014](https://github.com/vllm-project/vllm/issues/19014) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | gemm;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen-2.5 VL inference speed very low

### Issue 正文摘录

### Your current environment We conducted local inference tests on each version of VLLM and found that Qwen-2.5-VL is slower than vllm==0.7.3, while the accuracy is quite similar. Please investigate and assist us in resolving this issue. ##our command docker run --rm --runtime nvidia --gpus='"device=2,3"' --mount type=bind,source=/home/uhong_lin/llm,target=/llm -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 -p 7412:8000 --ipc=host vllm/vllm-openai:v0.9.0 --model /llm/Qwen2.5-VL-32B-Instruct-AWQ --served-model-name Qwen2.5-VL-32B-Instruct-AWQ --disable-log-requests --gpu-memory-utilization 0.95 --max-model-len 32768 --tensor-parallel-size 2 --quantization awq --max-num-seqs 16 --limit-mm-per-prompt image=2 --dtype auto MODEL | VLLM VERSION | Time to first token | Average token / s -- | -- | -- | -- QWEN-2.5-VL-32B-AWQ | 0.7.3 | 2.78 sec | 312 QWEN-2.5-VL-32B-AWQ | 0.8.5(速度異常) | 5.47 sec | 50 QWEN-2.5-VL-32B-AWQ | 0.9.0(速度異常) | 4.8sec | 42 ### 🐛 Describe the bug We conducted local inference tests on each version of VLLM and found that Qwen-2.5-VL is slower than vllm==0.7.3, while the accuracy is quite similar. Please investigate and assist us in resolving this issue. ##our command docker run --...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Your current environment We conducted local inference tests on each version of VLLM and found that Qwen-2.5-VL is slower than vllm==0.7.3, while the accuracy is quite similar. Please investigate and assist us in res...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: memory-utilization 0.95 --max-model-len 32768 --tensor-parallel-size 2 --quantization awq --max-num-seqs 16 --limit-mm-per-prompt image=2 --dtype auto MODEL | VLLM VERSION | Time to first token | Average token / s -- |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen-2.5 VL inference speed very low bug;stale ### Your current environment We conducted local inference tests on each version of VLLM and found that Qwen-2.5-VL is slower than vllm==0.7.3, while the accuracy is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen-2.5 VL inference speed very low bug;stale ### Your current environment We conducted local inference tests on each version of VLLM and found that Qwen-2.5-VL is slower than vllm==0.7.3, while the accuracy is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: low bug;stale ### Your current environment We conducted local inference tests on each version of VLLM and found that Qwen-2.5-VL is slower than vllm==0.7.3, while the accuracy is quite similar. Please investigate and as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
