# vllm-project/vllm#12988: [Bug]: Qwen2.5-VL-72B-Instruct-AWQ error with TP=2 and low throughput (~2 tokens/s) on VLLM_USE_V1=1

| 字段 | 值 |
| --- | --- |
| Issue | [#12988](https://github.com/vllm-project/vllm/issues/12988) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;gemm_linear;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | gemm;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL-72B-Instruct-AWQ error with TP=2 and low throughput (~2 tokens/s) on VLLM_USE_V1=1

### Issue 正文摘录

### Your current environment My hardware is 2xA100 (80GB). **The AWQ model works on TP=1 with 1 A100, but the performance is very bad and slow (~2 token/s) while using V1.** I have uploaded the Qwen2.5-VL-72B-InstructAWQ model here: https://huggingface.co/PointerHQ/Qwen2.5-VL-72B-Instruct-Pointer-AWQ Would really appreciate any help on TP or the slow performance!! Feb 09 22:48:15.741 | (VllmWorkerProcess pid=60) ERROR 02-09 14:48:15 multiproc_worker_utils.py:242] ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. -- | -- Feb 09 22:48:15.792 | ERROR 02-09 14:48:15 engine.py:389] ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. Feb 09 22:48:15.898 | Process SpawnProcess-1: Feb 09 22:48:15.898 | ERROR 02-09 14:48:15 multiproc_worker_utils.py:124] Worker VllmWorkerProcess pid 60 died, exit code: -15 Feb 09 22:48:15.903 | Traceback (most recent call last): File "/usr/local/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/local/lib/python3.11/multiprocessing/process.py", line 108, in run sel...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2.5-VL-72B-Instruct-AWQ error with TP=2 and low throughput (~2 tokens/s) on VLLM_USE_V1=1 bug ### Your current environment My hardware is 2xA100 (80GB). **The AWQ model works on TP=1 with 1 A100, but the perf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _worker_utils.py:242] ValueError: The input size is not aligned with the quantized weight shape. This can be caused by too large tensor parallel size. -- | -- Feb 09 22:48:15.792 | ERROR 02-09 14:48:15 engine.py:389] Va...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: face.co/PointerHQ/Qwen2.5-VL-72B-Instruct-Pointer-AWQ Would really appreciate any help on TP or the slow performance!! Feb 09 22:48:15.741 | (VllmWorkerProcess pid=60) ERROR 02-09 14:48:15 multiproc_worker_utils.py:242]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s/s) on VLLM_USE_V1=1 bug ### Your current environment My hardware is 2xA100 (80GB). **The AWQ model works on TP=1 with 1 A100, but the performance is very bad and slow (~2 token/s) while using V1.** I have uploaded the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Qwen2.5-VL-72B-Instruct-AWQ error with TP=2 and low throughput (~2 tokens/s) on VLLM_USE_V1=1 bug ### Your current environment My hardware is 2xA100 (80GB). **The AWQ model works on TP=1 with 1 A100, but the perf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
