# vllm-project/vllm#17187: [Installation]: deployment failure on Kuberentes with CPU device (testing).

| 字段 | 值 |
| --- | --- |
| Issue | [#17187](https://github.com/vllm-project/vllm/issues/17187) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: deployment failure on Kuberentes with CPU device (testing).

### Issue 正文摘录

### Your current environment ```text Amazon EKS with kubernetes 1.32 Image: vllm/vllm-openai:latest ``` ### How you are installing vllm I am using this [example from the documentation](https://docs.vllm.ai/en/stable/deployment/k8s.html#deployment-with-cpus) to setup vllm deployment on Kubernetes. It fails to detect the device: ```bash DEBUG 04-25 06:11:24 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 04-25 06:11:24 [__init__.py:34] Checking if TPU platform is available. DEBUG 04-25 06:11:24 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 04-25 06:11:24 [__init__.py:52] Checking if CUDA platform is available. DEBUG 04-25 06:11:24 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 04-25 06:11:24 [__init__.py:93] CUDA platform is not available because: NVML Shared Library Not Found DEBUG 04-25 06:11:24 [__init__.py:100] Checking if ROCm platform is available. DEBUG 04-25 06:11:24 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 04-25 06:11:24 [__init__.py:122] Checking if HPU platform is available. DEBUG 04-25 06:11:24 [__init__.py...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: O 04-25 06:11:27 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='meta-llama/Llama-3.2-1B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: deployment failure on Kuberentes with CPU device (testing). installation;stale ### Your current environment ```text Amazon EKS with kubernetes 1.32 Image: vllm/vllm-openai:latest ``` ### How you are installing vllm I am...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: deployment failure on Kuberentes with CPU device (testing). installation;stale ### Your current environment ```text Amazon EKS with kubernetes 1.32 Image: vllm/vllm-openai:latest ``` ### How you are ins
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 04-25 06:11:24 [__init__.py:52] Checking if CUDA platform is available. DEBUG 04-25 06:11:24 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distribu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
