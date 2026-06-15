# vllm-project/vllm#33147: [Bug]: vLLM 0.11 SSL Initialization Failure (ssl.SSLError: [CRYPTO] unknown error) on MicroOS 5.5 with FIPS Enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#33147](https://github.com/vllm-project/vllm/issues/33147) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.11 SSL Initialization Failure (ssl.SSLError: [CRYPTO] unknown error) on MicroOS 5.5 with FIPS Enabled

### Issue 正文摘录

### Your current environment - vLLM 0.11 - microOS 5.5 ```bash -bash-4.4$ cat /proc/sys/crypto/fips_enabled 1 ``` ### 🐛 Describe the bug ``` 2026-01-27 14:26:31 [INFO] Using standard model directory 2026-01-27 14:26:31 + '[' False = False ']' 2026-01-27 14:26:31 + PARAM_ENABLE_CHUNKED_PREFILL=--no-enable-chunked-prefill 2026-01-27 14:26:31 + python3 -m vllm.entrypoints.openai.api_server --port 8080 --served-model-name /mnt/models/Qwen2.5-0.5B-Instruct / --model /mnt/models/Qwen2.5-0.5B-Instruct --dtype half --gpu-memory-utilization 0.95 --tensor-parallel-size 1 --enforce-eager --no-enable-chunked-prefill 2026-01-27 14:26:32 /opt/venv/lib/python3.12/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. 2026-01-27 14:26:32 import pynvml # type: ignore[import] 2026-01-27 14:26:42 INFO 01-26 22:26:42 [__init__.py:216] Automatically detected platform cuda. 2026-01-27 14:26:47 Traceback (most recent call last): 2026-01-27 14:26:47 File " ", line 198, in _run_module_as_main 2026-01-27 14:26:47...

## 现有链接修复摘要

#40764 [CI/Build] Make opencv-python-headless an optional dependency

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ` ### 🐛 Describe the bug ``` 2026-01-27 14:26:31 [INFO] Using standard model directory 2026-01-27 14:26:31 + '[' False = False ']' 2026-01-27 14:26:31 + PARAM_ENABLE_CHUNKED_PREFILL=--no-enable-chunked-prefill 2026-01-2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: prefill 2026-01-27 14:26:32 /opt/venv/lib/python3.12/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: l.SSLError: [CRYPTO] unknown error) on MicroOS 5.5 with FIPS Enabled bug;stale ### Your current environment - vLLM 0.11 - microOS 5.5 ```bash -bash-4.4$ cat /proc/sys/crypto/fips_enabled 1 ``` ### 🐛 Describe the bug ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: dels/Qwen2.5-0.5B-Instruct / --model /mnt/models/Qwen2.5-0.5B-Instruct --dtype half --gpu-memory-utilization 0.95 --tensor-parallel-size 1 --enforce-eager --no-enable-chunked-prefill 2026-01-27 14:26:32 /opt/venv/lib/py...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40764](https://github.com/vllm-project/vllm/pull/40764) | closes_keyword | 0.95 | [CI/Build] Make opencv-python-headless an optional dependency | Fixes #40741 Related: #33147, #33756, #39986, #40276 CC @russellb @Isotr0py --- AI Assistance Disclosure: This PR was developed with AI assistance (Claude). All changes were rev |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
