# vllm-project/vllm#15592: [Bug]:ModuleNotFoundError: No module named 'vllm._C' 

| 字段 | 值 |
| --- | --- |
| Issue | [#15592](https://github.com/vllm-project/vllm/issues/15592) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:ModuleNotFoundError: No module named 'vllm._C' 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I tried to run the collect_env.py file, I encountered the error: ModuleNotFoundError: No module named 'vllm._C' Additionally, I downloaded a .whl file to install the environment using the command: pip install vllm-0.8.3.dev166%2Bg29930428e.cu128-cp312-cp312-linux_x86_64.whl The installation completed without any errors, but when I attempted to deploy a local model, the following command: python -m vllm.entrypoints.openai.api_server --model /mnt/qy-test/pvc-cd37befa-daf6-42c1-80f5-70b54cbbf302/qwen-QwQ --trust-remote-code --host 0.0.0.0 --port 8080 resulted in an error： INFO 03-27 10:47:18 [__init__.py:239] Automatically detected platform cuda. Traceback (most recent call last): File " ", line 189, in _run_module_as_main File " ", line 112, in _get_module_details File "/mnt/qy-test/envs/conda/envs/vllm3/lib/python3.12/site-packages/vllm/__init__.py", line 11, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/mnt/qy-test/envs/conda/envs/vllm3/lib/python3.12/site-packages/vllm/engine/arg_utils.py", line 22, in from vllm.executor.executor_base import ExecutorBase File "/mnt/qy-test/envs/conda/envs/vllm3/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]:ModuleNotFoundError: No module named 'vllm._C' bug;torch.compile ### Your current environment ### 🐛 Describe the bug When I tried to run the collect_env.py file, I encountered the error: ModuleNotFoundError: No mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ： INFO 03-27 10:47:18 [__init__.py:239] Automatically detected platform cuda. Traceback (most recent call last): File " ", line 189, in _run_module_as_main File " ", line 112, in _get_module_details File "/mnt/qy-test/e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ion completed without any errors, but when I attempted to deploy a local model, the following command: python -m vllm.entrypoints.openai.api_server --model /mnt/qy-test/pvc-cd37befa-daf6-42c1-80f5-70b54cbbf302/qwen-QwQ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vllm/model_executor/layers/sampler.py", line 23, in from vllm.spec_decode.metrics import SpecDecodeWorkerMetrics File "/mnt/qy-test/envs/conda/envs/vllm3/lib/python3.12/site-packages/vllm/spec_decode/metrics.py", line 9...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: g command: python -m vllm.entrypoints.openai.api_server --model /mnt/qy-test/pvc-cd37befa-daf6-42c1-80f5-70b54cbbf302/qwen-QwQ --trust-remote-code --host 0.0.0.0 --port 8080 resulted in an error： INFO 03-27 10:47:18 [__...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
