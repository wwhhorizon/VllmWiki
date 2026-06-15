# vllm-project/vllm#31387: [Feature]: Use Kimi to support to deploy fp8 model in 8xA100-PCIE-40GB GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#31387](https://github.com/vllm-project/vllm/issues/31387) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Use Kimi to support to deploy fp8 model in 8xA100-PCIE-40GB GPU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch You will get the next error info if you deploy a fp8 model like `mistralai/Devstral-2-123B-Instruct-2512` or deploy a llm (like `ZhipuAI/GLM-4.5-Air` and `Qwen/Qwen3-Next-80B-A3B-Instruct` ) with `--quantization fp8` param: ``` **Your GPU does not have native support for FP8 computation but FP8 quantization is being used. Weight-only FP8 compression will be used leveraging the Marlin kernel.** This may degrade performance for compute-heavy workloads. WorkerProc failed to start. Traceback (most recent call last): File "/home/ubisec/miniconda3/envs/swh-vllmn/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 722, in worker_main worker = WorkerProc(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ubisec/miniconda3/envs/swh-vllmn/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 562, in __init__ self.worker.load_model() File "/home/ubisec/miniconda3/envs/swh-vllmn/lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 289, in load_model self.model_runner.load_model(eep_scale_up=eep_scale_up) File "/home/ubisec/miniconda3/envs/swh-vllmn/lib/python3.11/site-packages/vllm/v1/worker/...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: Use Kimi to support to deploy fp8 model in 8xA100-PCIE-40GB GPU feature request;stale ### 🚀 The feature, motivation and pitch You will get the next error info if you deploy a fp8 model like `mistralai/Devstra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Use Kimi to support to deploy fp8 model in 8xA100-PCIE-40GB GPU feature request;stale ### 🚀 The feature, motivation and pitch You will get the next error info if you deploy a fp8 model like `mistralai/Devstra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Use Kimi to support to deploy fp8 model in 8xA100-PCIE-40GB GPU feature request;stale ### 🚀 The feature, motivation and pitch You will get the next error info if you deploy a fp8 model like `mistralai/Devstra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Use Kimi to support to deploy fp8 model in 8xA100-PCIE-40GB GPU feature request;stale ### 🚀 The feature, motivation and pitch You will get the next error info if you deploy a fp8 model like `mistralai/Devstra...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: er_partition part_size_k = layer.input_size_per_partition weight_block_size = getattr(layer, "weight_block_size", None) if size_k_first: assert layer.weight.shape == (part_size_k, part_size_n) else: assert layer.weight....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
