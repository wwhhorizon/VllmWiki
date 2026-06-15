# vllm-project/vllm#7986: [Bug]: vllm0.5.5 Ignores VLLM_USE_MODELSCOPE=True and Accesses huggingface.co

| 字段 | 值 |
| --- | --- |
| Issue | [#7986](https://github.com/vllm-project/vllm/issues/7986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.5.5 Ignores VLLM_USE_MODELSCOPE=True and Accesses huggingface.co

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After running ```bash docker run --runtime nvidia --gpus all -v cache/modelscope:/root/.cache/modelscope --env "VLLM_USE_MODELSCOPE=True" -p 8000:8000 --ipc host -d --name vllm vllm/vllm-openai:v0.5.5 --model LLM-Research/Meta-Llama-3.1-8B-Instruct --trust-remote-code -tp 4 ``` the container exits quickly. Upon checking the logs, it was found that ``` Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_errors.py", line 304, in hf_raise_for_status response.raise_for_status() File "/usr/local/lib/python3.10/dist-packages/requests/models.py", line 1024, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://huggingface.co/LLM-Research/Meta-Llama-3.1-8B-Instruct/resolve/main/preprocessor_config.json The above exception was the direct cause of the following exception: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/transformers/utils/hub.py", line 402, in cached_file resolved_file = hf_hub_download( File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/u...

## 现有链接修复摘要

#8037 [Bugfix] Fix ModelScope models in v0.5.5

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ur current environment ### 🐛 Describe the bug After running ```bash docker run --runtime nvidia --gpus all -v cache/modelscope:/root/.cache/modelscope --env "VLLM_USE_MODELSCOPE=True" -p 8000:8000 --ipc host -d --name v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm0.5.5 Ignores VLLM_USE_MODELSCOPE=True and Accesses huggingface.co bug ### Your current environment ### 🐛 Describe the bug After running ```bash docker run --runtime nvidia --gpus all -v cache/modelscope:/roo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0:8000 --ipc host -d --name vllm vllm/vllm-openai:v0.5.5 --model LLM-Research/Meta-Llama-3.1-8B-Instruct --trust-remote-code -tp 4 ``` the container exits quickly. Upon checking the logs, it was found that ``` Traceback...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ponse.raise_for_status() File "/usr/local/lib/python3.10/dist-packages/requests/models.py", line 1024, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 401 Client Error:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency #8037 [Bugfix] Fix ModelScope models in v0.5.5 Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8037](https://github.com/vllm-project/vllm/pull/8037) | closes_keyword | 0.95 | [Bugfix] Fix ModelScope models in v0.5.5 | FIX #7986 This recent PR https://github.com/vllm-project/vllm/pull/7710/ introduced support for some huggingface-specific code which needs to be handled differently when the mod |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
