# vllm-project/vllm#3354: [Neuron] RuntimeError: invalid argument to reset_peak_memory_stats

| 字段 | 值 |
| --- | --- |
| Issue | [#3354](https://github.com/vllm-project/vllm/issues/3354) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Neuron] RuntimeError: invalid argument to reset_peak_memory_stats

### Issue 正文摘录

I'm unable to run `python examples/offline_inference_neuron.py` Running on AWS on: Instance type: inf2.48xlarge AMI name: Deep Learning AMI Neuron (Ubuntu 22.04) 20240304 Following step (1), 2 and 3 of https://docs.vllm.ai/en/latest/getting_started/neuron-installation.html And installing `pip install mpmath==1.3.0` [see](https://github.com/vllm-project/vllm/issues/3353) When running `python examples/offline_inference_neuron.py` I get the following error: ``` python examples/offline_inference_neuron.py WARNING 03-12 14:03:55 ray_utils.py:62] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For distributed inference, please install Ray with `pip install ray`. config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 506/506 [00:00 . This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `lega...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ep (1), 2 and 3 of https://docs.vllm.ai/en/latest/getting_started/neuron-installation.html And installing `pip install mpmath==1.3.0` [see](https://github.com/vllm-project/vllm/issues/3353) When running `python examples...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ). For distributed inference, please install Ray with `pip install ray`. config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ut? performance ci_build;distributed_parallel;frontend_api;model_support;quantization cuda;quantization crash;import_error dtype;env_dependency I'm unable to run `python examples/offline_inference_neuron.py`
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es/vllm/worker/model_runner.py", line 88, in load_model with measure_cuda_memory() as m: File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/vllm/utils.py", line 327, in __enter__ self.initial_memory...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughl y read the reason why this was added as explained in https://github.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
