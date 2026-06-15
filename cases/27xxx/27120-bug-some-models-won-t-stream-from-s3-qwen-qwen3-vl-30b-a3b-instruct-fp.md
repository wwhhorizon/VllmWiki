# vllm-project/vllm#27120: [Bug]: some models won't stream from s3: Qwen/Qwen3-VL-30B-A3B-Instruct-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#27120](https://github.com/vllm-project/vllm/issues/27120) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: some models won't stream from s3: Qwen/Qwen3-VL-30B-A3B-Instruct-FP8

### Issue 正文摘录

### Your current environment using docker image: `docker.io/vllm/vllm-openai:v0.11.0` ### 🐛 Describe the bug Some models fail to load if streaming from S3. command: ```sh python3 \ -m vllm.entrypoints.openai.api_server \ --model=s3://llm-models/Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 \ --served-model-name=qwen-qwen3-vl-30b-a3b-instruct-fp8-a100 \ --load-format=runai_streamer \ --enable-prefix-caching \ --mm-encoder-tp-mode=data \ --async-scheduling ``` logs: ``` INFO 10-17 11:05:30 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=1) INFO 10-17 11:05:34 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=1) INFO 10-17 11:05:34 [utils.py:233] non-default args: {'model': 's3://llm-models/Qwen/Qwen3-VL-30B-A3B-Instruct-FP8', 'served_model_name': ['qwen-qwen3-vl-30b-a3b-instruct-fp8-a100'], 'load_format': 'runai_streamer', 'enable_prefix_caching': True, 'mm_encoder_tp_mode': 'data', 'async_scheduling': True} (APIServer pid=1) Traceback (most recent call last): (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/transformers/utils/hub.py", line 479, in cached_files (APIServer pid=1) hf_hub_download( (APIServer pid=1) File "/usr/local/lib/pytho...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: some models won't stream from s3: Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 bug;stale ### Your current environment using docker image: `docker.io/vllm/vllm-openai:v0.11.0` ### 🐛 Describe the bug Some models fail to load...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: n3-VL-30B-A3B-Instruct-FP8 bug;stale ### Your current environment using docker image: `docker.io/vllm/vllm-openai:v0.11.0` ### 🐛 Describe the bug Some models fail to load if streaming from S3. command: ```sh python3 \ -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: some models won't stream from s3: Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 bug;stale ### Your current environment using docker image: `docker.io/vllm/vllm-openai:v0.11.0` ### 🐛 Describe the bug Some models fail to load...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: truct-FP8 \ --served-model-name=qwen-qwen3-vl-30b-a3b-instruct-fp8-a100 \ --load-format=runai_streamer \ --enable-prefix-caching \ --mm-encoder-tp-mode=data \ --async-scheduling ``` logs: ``` INFO 10-17 11:05:30 [__init...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: some models won't stream from s3: Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 bug;stale ### Your current environment using docker image: `docker.io/vllm/vllm-openai:v0.11.0` ### 🐛 Describe the bug Some models fail to load if str...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
