# vllm-project/vllm#13980: [Bug]:ValueError: vllm serve Qwen/Qwen2.5-VL-72B-Instruct-AWQ   ERROR:The input size is not aligned with the quantized weight shape.

| 字段 | 值 |
| --- | --- |
| Issue | [#13980](https://github.com/vllm-project/vllm/issues/13980) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:ValueError: vllm serve Qwen/Qwen2.5-VL-72B-Instruct-AWQ   ERROR:The input size is not aligned with the quantized weight shape.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 下面的命令可以部署成功（python -m vllm.entrypoints.openai.api_server）： `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=3,4,5,6 python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-72B-Instruct-AWQ --quantization awq_marlin --tensor-parallel-size 4 --max-model-len 28672 --gpu-memory-utilization 0.99 --max-num-batched-tokens 28672 --max-num-seqs 64 --host 0.0.0.0 --port 8000 --disable-custom-all-reduce --block-size 16` 下面的命令报错（vllm serve ）： `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=3,4,5,6 vllm serve Qwen/Qwen2.5-VL-72B-Instruct-AWQ --quantization awq_marlin --tensor-parallel-size 4 --max-model-len 28672 --gpu-memory-utilization 0.99 --max-num-batched-tokens 28672 --max-num-seqs 64 --host 0.0.0.0 --port 8000 --block-size 16 --disable-custom-all-reduce` error: `(VllmWorkerProcess pid=1808916) INFO 02-28 01:21:50 config.py:3054] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64] is overridden by config [64, 32, 2, 1, 4, 40, 8, 48, 16, 56, 24] WARNING 02-28 01:21:50 awq_marlin.py:132] Layer 'language_model.model.layers.0.mlp.down_proj' is not suppo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cess pid=1808916) INFO 02-28 01:21:50 config.py:3054] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64] is overridden by config [64, 32, 2, 1, 4, 40, 8, 48, 16, 56, 24] WARNING 02-28 01:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]:ValueError: vllm serve Qwen/Qwen2.5-VL-72B-Instruct-AWQ ERROR:The input size is not aligned with the quantized weight shape. bug;stale ### Your current environment ### 🐛 Describe the bug 下面的命令可以部署成功（python -m vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ERROR:The input size is not aligned with the quantized weight shape. bug;stale ### Your current environment ### 🐛 Describe the bug 下面的命令可以部署成功（python -m vllm.entrypoints.openai.api_server）： `PYTORCH_CUDA_ALLOC_CONF=expa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 1/site-packages/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/home/anaconda3/envs/xinference/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd uvloop.run(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bug 下面的命令可以部署成功（python -m vllm.entrypoints.openai.api_server）： `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=3,4,5,6 python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-72B-Inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
