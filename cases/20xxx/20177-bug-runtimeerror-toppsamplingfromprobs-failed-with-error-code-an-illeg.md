# vllm-project/vllm#20177: [Bug]: RuntimeError: TopPSamplingFromProbs failed with error code an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#20177](https://github.com/vllm-project/vllm/issues/20177) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: TopPSamplingFromProbs failed with error code an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running inference with Qwen2.5-72B-Instruct-AWQ, the model works fine on a single A100 GPU. However, when I scale to two A100 GPUs, I encounter the following error: `RuntimeError: TopPSamplingFromProbs failed with error code an illegal memory access was encountered.` Start command: ```bash #!/bin/bash # 设置环境变量 export CUDA_VISIBLE_DEVICES=0,1 # 激活虚拟环境 source /home/lucas/envs/nlp-vllm/bin/activate # 计算GPU数量 GPU_COUNT=$(echo $CUDA_VISIBLE_DEVICES | tr ',' '\n' | grep -c [0-9]) # MODEL=/data/modelscope/Qwen3-32B-AWQ MODEL=/data/modelscope/Qwen2.5-72B-Instruct-AWQ # 启动 vLLM serve 服务 vllm serve \ ${MODEL} \ --port 18101 \ --served-model-name vllm-text \ --max-model-len 8192 \ --tensor-parallel-size ${GPU_COUNT} \ --gpu-memory-utilization 0.9 ``` The error message: """ 2025-06-27 17:14:23: (VllmWorker rank=0 pid=776293) ERROR 06-27 17:14:23 [multiproc_executor.py:522] WorkerProc hit an exception. 2025-06-27 17:14:23: (VllmWorker rank=0 pid=776293) ERROR 06-27 17:14:23 [multiproc_executor.py:522] Traceback (most recent call last): 2025-06-27 17:14:23: (VllmWorker rank=0 pid=776293) ERROR 06-27 17:14:23 [multiproc_executor.py:522] Fi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nference with Qwen2.5-72B-Instruct-AWQ, the model works fine on a single A100 GPU. However, when I scale to two A100 GPUs, I encounter the following error: `RuntimeError: TopPSamplingFromProbs failed with error code an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: robs failed with error code an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug When running inference with Qwen2.5-72B-Instruct-AWQ, the model works fine on a single A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pid=776293) ERROR 06-27 17:14:23 [multiproc_executor.py:522] return flashinfer_sample(logits, k, p, generators) 2025-06-27 17:14:23: (VllmWorker rank=0 pid=776293) ERROR 06-27 17:14:23 [multiproc_executor.py:522] ^^^^^^...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Instruct-AWQ, the model works fine on a single A100 GPU. However, when I scale to two A100 GPUs, I encounter the following error: `RuntimeError: TopPSamplingFromProbs failed with error code an illegal memory access was...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
