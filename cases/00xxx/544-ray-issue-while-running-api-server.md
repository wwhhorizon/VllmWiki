# vllm-project/vllm#544: Ray issue while running API server

| 字段 | 值 |
| --- | --- |
| Issue | [#544](https://github.com/vllm-project/vllm/issues/544) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Ray issue while running API server

### Issue 正文摘录

Hi All , I am trying to run `python3 -m vllm.entrypoints.api_server --model huggyllama/llama-13b --tensor-parallel-size 4` I am using local build of vllm. Hardware I am using . - A100 40GB - Python 3.10 - Cuda 12.0 ``` Traceback (most recent call last): File " suresh.bhusare/anaconda3/envs/vllm-test/lib/python3.10/runpy.py", line 187, in _run_module_as_main mod_name, mod_spec, code = _get_module_details(mod_name, _Error) File " suresh.bhusare/anaconda3/envs/vllm-test/lib/python3.10/runpy.py", line 110, in _get_module_details __import__(pkg_name) File " suresh.bhusare/inference-llm/vllm/vllm/__init__.py", line 4, in from vllm.engine.async_llm_engine import AsyncLLMEngine File " suresh.bhusare/inference-llm/vllm/vllm/engine/async_llm_engine.py", line 7, in from vllm.engine.llm_engine import LLMEngine File " suresh.bhusare/inference-llm/vllm/vllm/engine/llm_engine.py", line 9, in from vllm.engine.ray_utils import initialize_cluster, ray, RayWorker File " suresh.bhusare/inference-llm/vllm/vllm/engine/ray_utils.py", line 8, in from ray.air.util.torch_dist import TorchDistributedWorker File " suresh.bhusare/anaconda3/envs/vllm-test/lib/python3.10/site-packages/ray/air/__init__.py", line...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: del huggyllama/llama-13b --tensor-parallel-size 4` I am using local build of vllm. Hardware I am using . - A100 40GB - Python 3.10 - Cuda 12.0 ``` Traceback (most recent call last): File " suresh.bhusare/anaconda3/envs/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lel-size 4` I am using local build of vllm. Hardware I am using . - A100 40GB - Python 3.10 - Cuda 12.0 ``` Traceback (most recent call last): File " suresh.bhusare/anaconda3/envs/vllm-test/lib/python3.10/runpy.py", lin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: l , I am trying to run `python3 -m vllm.entrypoints.api_server --model huggyllama/llama-13b --tensor-parallel-size 4` I am using local build of vllm. Hardware I am using . - A100 40GB - Python 3.10 - Cuda 12.0 ``` Trace...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ack (most recent call last): File " suresh.bhusare/anaconda3/envs/vllm-test/lib/python3.10/runpy.py", line 187, in _run_module_as_main mod_name, mod_spec, code = _get_module_details(mod_name, _Error) File " suresh.bhusa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
