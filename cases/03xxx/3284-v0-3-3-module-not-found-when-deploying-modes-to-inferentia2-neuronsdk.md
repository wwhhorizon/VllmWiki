# vllm-project/vllm#3284: v0.3.3 - Module not found when deploying modes to Inferentia2/NeuronSDK

| 字段 | 值 |
| --- | --- |
| Issue | [#3284](https://github.com/vllm-project/vllm/issues/3284) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> v0.3.3 - Module not found when deploying modes to Inferentia2/NeuronSDK

### Issue 正文摘录

Error when running sample **python3 examples/offline_inference_neuron.py**, after installing v0.3.3 (from cloned source or from pip install git+...). ### Cause: directory **vllm/model_executor/models/neuron/** is not copied to expected path: **/opt/conda/lib/python3.10/site-packages/vllm/model_executor/models/neuron/** during package instalation. ``` module = importlib.import_module( File "/opt/conda/lib/python3.10/importlib/__init__.py", line 126, in import_module return _bootstrap._gcd_import(name[level:], package, level) File " ", line 1050, in _gcd_import File " ", line 1027, in _find_and_load File " ", line 992, in _find_and_load_unlocked File " ", line 241, in _call_with_frames_removed File " ", line 1050, in _gcd_import File " ", line 1027, in _find_and_load File " ", line 1004, in _find_and_load_unlocked ModuleNotFoundError: No module named 'vllm.model_executor.models.neuron' ``` ### Workaround: Manually copy the file **vllm/model_executor/models/neuron/llama.py** to **/opt/conda/lib/python3.10/site-packages/vllm/model_executor/models/neuron/llama.py** after pip installing vllm. After that, everything works fine. Could you fix that in the package installation, please? ###...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n running sample **python3 examples/offline_inference_neuron.py**, after installing v0.3.3 (from cloned source or from pip install git+...). ### Cause: directory **vllm/model_executor/models/neuron/** is not copied to e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oned source or from pip install git+...). ### Cause: directory **vllm/model_executor/models/neuron/** is not copied to expected path: **/opt/conda/lib/python3.10/site-packages/vllm/model_executor/models/neuron/** during...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0.3.2+neuron212 torch 2.1.2 torch-model-archiver 0.9.0 torch-xla 2.1.1 torchserve 0.9.0 torchvision 0.16.2 aws-neuronx-runtime-discovery 2.9 libneuronxla 2.0.755 neuronx-cc
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: v0.3.3 - Module not found when deploying modes to Inferentia2/NeuronSDK stale Error when running sample **python3 examples/offline_inference_neuron.py**, after installing v0.3.3 (from cloned source or from pip install g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
