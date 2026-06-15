# vllm-project/vllm#24890: [Usage]: How do I load the local model when running the Docker image?

| 字段 | 值 |
| --- | --- |
| Issue | [#24890](https://github.com/vllm-project/vllm/issues/24890) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How do I load the local model when running the Docker image?

### Issue 正文摘录

### Your current environment ```text Traceback (most recent call last): File "//collect_env.py", line 19, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' ``` ### How would you like to use vllm I want to run embedding of a Qwen3-Embedding-8B. I also downloaded the model in local /Qwen3-Embedding-8B directory. I used the download link indicated in the URL below to pull the Intel/AMD x86 pre-built Docker image. https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#intelamd-x86_3 ``` docker pull public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.10.2 ``` However, the Docker image reports new error logs saying that it wants to download the model from Huggingface. Could you tell me how to let the Docker image to read the local model? Thank you so much! ``` #export HF_HUB_OFFLINE=1 # docker run --name q3-embedding \ -p 8080:8000 \ public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.10.2 \ --allowed-local-media-path /Qwen3-Embedding-8B \ --model Qwen3-Embedding-8B \ --task embedding \ --served-model-name Qwen3-Embedding-8B INFO 09-15 04:01:56 [__init__.py:216] Automatically detected platform cpu. WARNING 09-15 04:01:58 [__init__.py:1766...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Usage]: How do I load the local model when running the Docker image? usage ### Your current environment ```text Traceback (most recent call last): File "//collect_env.py", line 19, in from vllm.envs import environment_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How do I load the local model when running the Docker image? usage ### Your current environment ```text Traceback (most recent call last): File "//collect_env.py", line 19, in from vllm.envs import environment_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 3.12/site-packages/huggingface_hub/file_download.py", line 1546, in _get_metadata_or_catch_error (APIServer pid=1) metadata = get_hf_file_metadata( (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) File "/opt/ve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ol.py", line 787, in urlopen (APIServer pid=1) response = self._make_request( (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) File "/opt/venv/lib/python3.12/site-packages/urllib3/connectionpool.py", line 488, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
