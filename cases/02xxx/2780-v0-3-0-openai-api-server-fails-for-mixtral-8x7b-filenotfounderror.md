# vllm-project/vllm#2780: v0.3.0 openai.api_server fails for Mixtral-8x7B: FileNotFoundError

| 字段 | 值 |
| --- | --- |
| Issue | [#2780](https://github.com/vllm-project/vllm/issues/2780) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> v0.3.0 openai.api_server fails for Mixtral-8x7B: FileNotFoundError

### Issue 正文摘录

## v0.3.0 openai.api_server fails for Mixtral-8x7B: FileNotFoundError ### Description * vLLM v0.3.0 openai.api_server fails for Mixtral-8x7B: FileNotFoundError * vLLM v0.2.7 openai.api_server works fine (exact same command line, only different vLLM venv for 0.2.7) * `export PATH=$PATH:/sbin/ldconfig` does not help. * `/home/ob/models/huggingface/Mixtral-8x7B-Instruct-v0.1/2024-01-17` is downloaded from [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1). * GPUs: H100 PCIe (80GB) * Installation (in newly created venv): `pip install vllm` * Also tried latest source installation `f0d4e14` with `pip install -e .`, but gave same issue. ### Command line to reproduce ``` CUDA_VISIBLE_DEVICES=0,1 /home/ob/venvs/vllm-venv-v0.3.0/bin/python -m vllm.entrypoints.openai.api_server --host localhost --port 8206 --model '/home/ob/models/huggingface/Mixtral-8x7B-Instruct-v0.1/2024-01-17' --served-model-name "Mixtral-8x7B-Instruct-v0.1" --tensor-parallel-size 2 --gpu-memory-utilization 0.9 ``` ### Error Message ``` (vllm-venv-v0.3.0)ob@pascal:vllm-inst$ CUDA_VISIBLE_DEVICES=0,1 /home/ob/venvs/vllm-venv-v0.3.0/bin/python -m vllm.entrypoints.openai.api_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ps://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1). * GPUs: H100 PCIe (80GB) * Installation (in newly created venv): `pip install vllm` * Also tried latest source installation `f0d4e14` with `pip install -e .`, b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_load...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: d line, only different vLLM venv for 0.2.7) * `export PATH=$PATH:/sbin/ldconfig` does not help. * `/home/ob/models/huggingface/Mixtral-8x7B-Instruct-v0.1/2024-01-17` is downloaded from [mistralai/Mixtral-8x7B-Instruct-v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: v0.3.0 openai.api_server fails for Mixtral-8x7B: FileNotFoundError stale ## v0.3.0 openai.api_server fails for Mixtral-8x7B: FileNotFoundError ### Description * vLLM v0.3.0 openai.api_server fails for Mixtral-8x7B: File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1). * GPUs: H100 PCIe (80GB) * Installation (in newly created venv): `pip install vllm` * Also tried latest source installation `f0d4e14` with `pip install -e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
